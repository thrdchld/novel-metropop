#!/usr/bin/env python3
"""
Test sederhana untuk pemeriksa Rujukan Mundur di scripts/audit-continuity.py.
Menggunakan folder contoh sementara sehingga tidak mengubah folder story/.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AUDIT_SCRIPT = Path(__file__).resolve().parent / "audit-continuity.py"


class TestAuditContinuityRujukanMundur(unittest.TestCase):
    def _buat_cerita_sementara(
        self,
        root: Path,
        chapters: dict[int, str],
        rujukan_section: str = "",
    ) -> Path:
        story_dir = root / "Contoh Cerita"
        chap_dir = story_dir / "chapters"
        chap_dir.mkdir(parents=True, exist_ok=True)
        (story_dir / "canon.md").write_text("# Canon\n", encoding="utf-8")
        (story_dir / "state.md").write_text("# State\n", encoding="utf-8")
        ledger_body = "# Ledger\n\n## A. Timeline Master\n\n| Bab | Hari/jam |\n|---|---|\n| 1 | Senin |\n"
        if rujukan_section:
            ledger_body += f"\n{rujukan_section}\n"
        (story_dir / "ledger.md").write_text(ledger_body, encoding="utf-8")
        for num, text in chapters.items():
            (chap_dir / f"bab-{num:02d}.md").write_text(text, encoding="utf-8")
        return story_dir

    def _run_audit(self, story_dir: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(AUDIT_SCRIPT), str(story_dir)],
            capture_output=True,
            text=True,
        )

    def test_tanpa_tabel_rujukan_mundur_hanya_peringatan(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            story_dir = self._buat_cerita_sementara(
                Path(tmp),
                {1: "## **Bab 1: Awal**\n\nAku menaruh kunci di laci.\n"},
            )
            res = self._run_audit(story_dir)
            self.assertEqual(res.returncode, 0, res.stdout)
            self.assertIn("tabel tidak ada", res.stdout.lower())

    def test_rujukan_mundur_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rujukan = (
                "## Rujukan Mundur\n\n"
                "| Fakta | Dipakai di bab | Ditanam di bab | Kutipan penanda |\n"
                "|---|---|---|---|\n"
                "| Kunci laci meja | 3 | 1 | menaruh kunci di laci |\n"
            )
            story_dir = self._buat_cerita_sementara(
                Path(tmp),
                {
                    1: "## **Bab 1: Awal**\n\nAku menaruh kunci di laci sebelum pergi.\n",
                    3: "## **Bab 3: Temuan**\n\nKunci itu masih ada di sana.\n",
                },
                rujukan_section=rujukan,
            )
            res = self._run_audit(story_dir)
            self.assertEqual(res.returncode, 0, res.stdout)
            self.assertIn("[OK] Rujukan 'Kunci laci meja'", res.stdout)

    def test_bab_penanaman_lebih_besar_atau_sama_dengan_pemakaian(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rujukan = (
                "## Rujukan Mundur\n\n"
                "| Fakta | Dipakai di bab | Ditanam di bab | Kutipan penanda |\n"
                "|---|---|---|---|\n"
                "| Nota belanja | 2 | 2 | nota terselip di tas |\n"
                "| Payung biru | 1 | 3 | payung biru di sudut pintu |\n"
            )
            story_dir = self._buat_cerita_sementara(
                Path(tmp),
                {
                    1: "## **Bab 1: Awal**\n\nTeks bab satu.\n",
                    2: "## **Bab 2: Tengah**\n\nAda nota terselip di tas.\n",
                    3: "## **Bab 3: Akhir**\n\nAda payung biru di sudut pintu.\n",
                },
                rujukan_section=rujukan,
            )
            res = self._run_audit(story_dir)
            self.assertEqual(res.returncode, 1, res.stdout)
            self.assertIn("bab penanaman (2) >= bab pemakaian (2)", res.stdout)
            self.assertIn("bab penanaman (3) >= bab pemakaian (1)", res.stdout)

    def test_file_bab_tidak_ada(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rujukan = (
                "## Rujukan Mundur\n\n"
                "| Fakta | Dipakai di bab | Ditanam di bab | Kutipan penanda |\n"
                "|---|---|---|---|\n"
                "| Struk parkir | 3 | 2 | struk parkir basah |\n"
            )
            story_dir = self._buat_cerita_sementara(
                Path(tmp),
                {
                    1: "## **Bab 1: Awal**\n\nTeks bab satu.\n",
                    3: "## **Bab 3: Akhir**\n\nTeks bab tiga.\n",
                },
                rujukan_section=rujukan,
            )
            res = self._run_audit(story_dir)
            self.assertEqual(res.returncode, 1, res.stdout)
            self.assertIn("file bab penanaman (bab-02.md) tidak ada", res.stdout)

    def test_kutipan_penanda_tidak_ditemukan(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rujukan = (
                "## Rujukan Mundur\n\n"
                "| Fakta | Dipakai di bab | Ditanam di bab | Kutipan penanda |\n"
                "|---|---|---|---|\n"
                "| Botol minum penyok | 3 | 1 | botol penyok warna merah |\n"
            )
            story_dir = self._buat_cerita_sementara(
                Path(tmp),
                {
                    1: "## **Bab 1: Awal**\n\nDia memegang botol minum hitam polos.\n",
                    3: "## **Bab 3: Akhir**\n\nTeks bab tiga.\n",
                },
                rujukan_section=rujukan,
            )
            res = self._run_audit(story_dir)
            self.assertEqual(res.returncode, 1, res.stdout)
            self.assertIn("kutipan penanda 'botol penyok warna merah' tidak ditemukan di Bab 01", res.stdout)


if __name__ == "__main__":
    unittest.main()

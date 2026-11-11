#!/usr/bin/env python3
"""
Master Gatekeeper & Stress Test Terpadu — Novel MetroPop Indonesia (v1.0)
Menjalankan 15 Pemeriksaan Wajib Repo (engine/03 s.d. engine/11) sekaligus dalam satu perintah.
Jika ada 1 saja pelanggaran di bab mana pun, skrip ini keluar dengan kode GAGAL (exit 1).

Cara pakai:
  python3 scripts/stress-test.py "story/Ada Kamu di Jadwalku"
  python3 scripts/stress-test.py "story/Ada Kamu di Jadwalku/chapters/bab-01.md"
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from analyze_prose_core import inspect_chapter_rules

PASS_ICON = "[LULUS]"
FAIL_ICON = "[GAGAL]"


def check_story_pillars(story_dir: Path) -> list[str]:
    errors: list[str] = []
    for req in ("canon.md", "outline.md", "state.md", "ledger.md"):
        p = story_dir / req
        if not p.is_file():
            errors.append(f"Dokumen pilar tidak ditemukan: {req}")
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        if req == "outline.md" and "TERKUNCI" not in txt:
            errors.append("outline.md belum berstatus TERKUNCI")
        if req == "canon.md" and "Profil Karakter" not in txt and "Character Sheet" not in txt:
            errors.append("canon.md belum memuat Profil Karakter Lengkap (Character Sheet)")
    return errors


def extract_character_names(story_dir: Path) -> set[str]:
    """Ambil nama panggilan tokoh dari canon.md untuk mencegah nama tokoh masuk ke judul bab (Bab 7+)."""
    names: set[str] = {"hana", "bima", "nino", "fajar", "meli", "maya", "hendra", "ratih"}
    canon = story_dir / "canon.md"
    if canon.is_file():
        txt = canon.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"^###\s+\d+\.\s+([A-Za-z]+)", txt, flags=re.M):
            names.add(m.group(1).lower())
    return names


def main() -> int:
    parser = argparse.ArgumentParser(description="Stress Test Terpadu 15 Aturan Repo Novel MetroPop.")
    parser.add_argument("target", help="Folder story/<Judul> atau file bab-*.md")
    args = parser.parse_args()

    target = Path(args.target)
    if target.is_file():
        story_dir = target.parent.parent
        files = [target]
    else:
        story_dir = target
        chapters_dir = target / "chapters" if (target / "chapters").is_dir() else target
        files = sorted(chapters_dir.glob("bab-*.md"))

    if not files:
        print(f"{FAIL_ICON} Tidak ditemukan file bab-*.md di {target}", file=sys.stderr)
        return 1

    print("=" * 78)
    print(f"  STRESS TEST TERPADU (15 ATURAN REPO): {story_dir.name}")
    print("=" * 78)

    total_errors: list[str] = []

    # 1. Cek Dokumen Pilar (jika target adalah folder story)
    if target.is_dir() and (story_dir / "canon.md").exists():
        pillar_errs = check_story_pillars(story_dir)
        if pillar_errs:
            for e in pillar_errs:
                total_errors.append(f"[Pilar] {e}")
            print(f"  1. Dokumen Pilar & Character Sheet : {FAIL_ICON} ({len(pillar_errs)} isu)")
        else:
            print(f"  1. Dokumen Pilar & Character Sheet : {PASS_ICON}")

    char_names = extract_character_names(story_dir)

    # 2-14. Cek Seluruh Bab terhadap 13 Kategori Prosa, Struktur, Pembuka, & Dialog
    cat_counts = {
        "word_range": 0,
        "plain_text": 0,
        "title_rule": 0,
        "in_medias_res": 0,
        "long_quote": 0,
        "aykb_quote": 0,
        "mixed_negation": 0,
        "filter_words": 0,
        "stock_tells": 0,
        "ai_syntax": 0,
        "bookish_tags": 0,
        "slop_clinical": 0,
        "sensory_cap": 0,
        "discourse_rhythm": 0,
    }

    for f in files:
        res = inspect_chapter_rules(f, char_names=char_names)
        for cat, errs in res["errors"].items():
            if errs:
                cat_counts[cat] += len(errs)
                for e in errs:
                    total_errors.append(f"[{f.name}] {e}")

    labels = [
        ("word_range", "2. Rentang Kata Bab (600-900 kata)"),
        ("plain_text", "3. Teks Polos 100% (0 Em Dash, 0 Markup *, 0 Quote Atas)"),
        ("title_rule", "4. Aturan Judul Bab (Clue Singkat & Bebas Nama Tokoh)"),
        ("in_medias_res", "5. Pembuka Bab In Medias Res & Ruang Aksi"),
        ("long_quote", "6. Batas Napas Kalimat Dialog (<=20 Kata per Kutipan)"),
        ("aykb_quote", "7. Anti-Eksposisi 'As You Know, Bob' di Dialog"),
        ("mixed_negation", "8. Konsistensi Register Lisan di Dialog (Anti Belang nggak/tidak)"),
        ("filter_words", "9. Bebas Kata Filter Persepsi (terasa/tampak/terlihat/menyadari)"),
        ("stock_tells", "10. Bebas Gerakan Klise / Stock Tells (menghela napas/gigit bibir)"),
        ("ai_syntax", "11. Bebas Sintaksis AI ('Sambil...', ', membuat', Pembungkus Abstrak)"),
        ("bookish_tags", "12. Bebas Tag Dialog Buku Pelajaran (ujarnya/tuturnya/tukasnya)"),
        ("slop_clinical", "13. Bebas AI Slop & Jargon Psikologi Klinis"),
        ("sensory_cap", "14. Batas Anatomi Tubuh (<=2) & Penciuman (<=2) per Bab"),
        ("discourse_rhythm", "15. Variasi Posisi Dialog (EndQ <=75%) & Kalimat (0 Deret Mono)"),
    ]

    for key, title in labels:
        cnt = cat_counts[key]
        status = PASS_ICON if cnt == 0 else f"{FAIL_ICON} ({cnt} pelanggaran)"
        print(f"  {title:<62}: {status}")

    # 15. Jalankan audit-continuity.py jika target adalah folder story
    if target.is_dir() and (story_dir / "ledger.md").exists():
        script_dir = Path(__file__).resolve().parent
        audit_cmd = [sys.executable, str(script_dir / "audit-continuity.py"), str(story_dir)]
        proc = subprocess.run(audit_cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            total_errors.append("[Kontinuitas] audit-continuity.py mendeteksi isu kontinuitas.")
            print(f"  {'16. Audit Kontinuitas Berlapis (Hari/Waktu/Uang/Pengetahuan)':<62}: {FAIL_ICON}")
        else:
            print(f"  {'16. Audit Kontinuitas Berlapis (Hari/Waktu/Uang/Pengetahuan)':<62}: {PASS_ICON}")

    print("-" * 78)
    if total_errors:
        print(f"  HASIL AKHIR: {FAIL_ICON} Ditemukan {len(total_errors)} pelanggaran yang WAJIB diperbaiki:")
        for err in total_errors[:40]:
            print(f"   - {err}")
        if len(total_errors) > 40:
            print(f"   ... dan {len(total_errors) - 40} pelanggaran lainnya.")
        print("=" * 78)
        return 1

    print(f"  HASIL AKHIR: {PASS_ICON} Seluruh {len(files)} bab LULUS 100% tanpa pelanggaran (0 isu).")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Master Gatekeeper & Stress Test Terpadu (22 Pemeriksaan) — Novel MetroPop Indonesia.
Memeriksa 8 Sinkronisasi Aset & Dokumen + 14 Aturan Prosa, Gaya, & Dialog sekaligus.

Satu-satunya sumber kebenaran aturan: scripts/rules.json.

Cara pakai:
  python3 scripts/stress-test.py "story/Ada Kamu di Jadwalku"
  python3 scripts/stress-test.py --fix "story/Ada Kamu di Jadwalku"
  python3 scripts/stress-test.py "story/Ada Kamu di Jadwalku/chapters/bab-01.md"
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from analyze_prose_core import inspect_chapter_rules

PASS_ICON = "[LULUS]"
FAIL_ICON = "[GAGAL]"
FIXED_ICON = "[DIPERBAIKI]"


def load_rules(repo_root: Path) -> dict:
    rules_path = repo_root / "scripts" / "rules.json"
    return json.loads(rules_path.read_text(encoding="utf-8"))


def generate_rules_doc(repo_root: Path) -> str:
    """Membuat konten engine/12-stress-rules.md otomatis dari scripts/rules.json."""
    rules_data = load_rules(repo_root)
    params = rules_data["params"]
    prose_rules = rules_data["rules"]
    sync_checks = rules_data["sync_checks"]
    patterns = rules_data["patterns"]

    doc: list[str] = [
        "# Aturan Gatekeeper & Stress Test Terpadu (22 Pemeriksaan)",
        "",
        "> **PENTING: DOKUMEN INI DIGENERATE SECARA OTOMATIS DARI `scripts/rules.json`. JANGAN DIEDIT MANUAL.**",
        "> Untuk mengubah aturan, batasan, atau daftar kata terlarang, ubah file `scripts/rules.json` lalu jalankan:",
        "> ```bash",
        '> python3 scripts/stress-test.py --fix "story/<Judul Novel>"',
        "> ```",
        "",
        "---",
        "",
        "## 1. Filosofi Gatekeeper Tunggal & Zero-Manual Checking",
        "",
        "Repositori ini menerapkan prinsip **Single Source of Truth** (`scripts/rules.json`) dan **Zero-Manual Checking**.",
        "Penulis atau AI dilarang keras mengklaim naskah/revisi selesai atau melakukan `git commit` sebelum perintah gatekeeper berikut mengembalikan hasil **100% LULUS**:",
        "",
        "```bash",
        'python3 scripts/stress-test.py "story/<Judul Novel>"',
        "```",
        "",
        "Jika terdapat ketidaksinkronan pada file turunan (`manuscript.md`, `reader.html`, `universe-registry.md`, atau `engine/12-stress-rules.md`), gunakan flag `--fix` untuk perbaikan otomatis:",
        "",
        "```bash",
        'python3 scripts/stress-test.py --fix "story/<Judul Novel>"',
        "```",
        "",
        "---",
        "",
        "## 2. Parameter Kuantitatif Utama (`params`)",
        "",
        "| Parameter | Nilai Batas | Keterangan |",
        "|---|---|---|",
        f"| `word_min` | {params['word_min']} kata | Batas minimum kata per bab (AGENTS.md 4.2) |",
        f"| `word_max` | {params['word_max']} kata | Batas maksimum kata per bab (AGENTS.md 4.2) |",
        f"| `max_quote_words` | {params['max_quote_words']} kata | Batas panjang maksimum satu kutipan dialog lisan (engine/05-style.md 6) |",
        f"| `title_max_words` | {params['title_max_words']} kata | Batas kata judul bab tanpa nama tokoh (engine/05-style.md 4) |",
        f"| `endq_max_pct` | {params['endq_max_pct']}% | Batas toleransi paragraf dialog berakhir kutipan (engine/05-style.md 5E) |",
        f"| `endq_min_dialogue_paras` | {params['endq_min_dialogue_paras']} | Minimal paragraf dialog agar EndQ dicek |",
        f"| `embodied_max` | {params['embodied_max']}x | Batas maksimum sebutan reaksi anatomi tubuh per bab (engine/05-style.md 5C) |",
        f"| `smell_max` | {params['smell_max']}x | Batas maksimum kata penciuman/bau/aroma per bab (engine/05-style.md 5C) |",
        f"| `mono_min_run` | {params['mono_min_run']} kalimat | Batas deret kalimat berpanjang seragam (engine/05-style.md 5E) |",
        f"| `mono_tolerance` | {params['mono_tolerance']} kata | Toleransi selisih panjang kalimat seragam |",
        f"| `mono_min_words` | {params['mono_min_words']} kata | Panjang kalimat minimum untuk perhitungan deret seragam |",
        "",
        "---",
        "",
        "## 3. Rincian 8 Pemeriksaan Sinkronisasi Aset & Dokumen",
        "",
        "| No | Kunci | Pemeriksaan | Aturan & Mekanisme Validasi |",
        "|---|---|---|---|",
    ]

    for idx, sc in enumerate(sync_checks, 1):
        doc.append(f"| {idx} | `{sc['key']}` | {sc['title']} | {sc['rule']} |")

    doc.extend([
        "",
        "---",
        "",
        "## 4. Rincian 14 Aturan Prosa, Struktur, & Dialog",
        "",
        "| No | Kunci | Aturan | Definisi Validasi | Rujukan Engine |",
        "|---|---|---|---|---|",
    ])

    for idx, r in enumerate(prose_rules, 9):
        desc = r["rule"].format(**params)
        doc.append(f"| {idx} | `{r['key']}` | {r['title']} | {desc} | {r['doc']} |")

    doc.extend([
        "",
        "---",
        "",
        "## 5. Bank Pola Regex & Kata Terlarang (`patterns`)",
        "",
    ])

    for pkey, plist in patterns.items():
        doc.append(f"### Pola `{pkey}` ({len(plist)} pola)")
        doc.append("```")
        doc.append(", ".join(plist))
        doc.append("```")
        doc.append("")

    return "\n".join(doc) + "\n"


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


def check_numbering_and_outline(story_dir: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    outline_path = story_dir / "outline.md"
    outline_titles: dict[int, str] = {}

    if outline_path.is_file():
        outline_txt = outline_path.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"^###\s+Bab\s+(\d+):\s*(.+)$", outline_txt, re.M):
            outline_titles[int(m.group(1))] = m.group(2).strip()

    for idx, f in enumerate(files, 1):
        m_num = re.search(r"bab-(\d+)", f.name)
        if not m_num:
            errors.append(f"Format nama file tidak sesuai: {f.name} (harus bab-NN.md)")
            continue
        chap_num = int(m_num.group(1))
        if chap_num != idx:
            errors.append(f"Nomor file bab lompat/tidak urut: {f.name} berada di urutan ke-{idx}")

        # Cek kesesuaian judul dengan outline
        txt = f.read_text(encoding="utf-8", errors="ignore")
        title_m = re.search(r"^##\s+(\*\*)?Bab\s+\d+:\s*(.+?)(\*\*)?$", txt, re.M)
        if not title_m:
            errors.append(f"Header judul bab '## **Bab N: Judul**' tidak ditemukan di {f.name}")
        else:
            raw_title = title_m.group(2).strip()
            chap_title = re.sub(r"^\*+|\*+$", "", raw_title).strip()
            if chap_num in outline_titles:
                exp_title = re.sub(r"^\*+|\*+$", "", outline_titles[chap_num]).strip()
                if chap_title.lower() != exp_title.lower():
                    errors.append(f"Judul {f.name} ('{chap_title}') berbeda dengan outline ('{exp_title}')")

    return errors


def check_ledger_and_state(story_dir: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    total_chaps = len(files)

    ledger_path = story_dir / "ledger.md"
    if ledger_path.is_file():
        ledger_txt = ledger_path.read_text(encoding="utf-8", errors="ignore")
        rows = [int(m.group(1)) for m in re.finditer(r"^\|\s*(\d+)\s*\|", ledger_txt, re.M)]
        missing = set(range(1, total_chaps + 1)) - set(rows)
        if missing:
            errors.append(f"ledger.md belum mencakup bab: {sorted(missing)}")
        if len(rows) < total_chaps:
            errors.append(f"ledger.md baru mencatat {len(rows)} dari {total_chaps} bab")

    state_path = story_dir / "state.md"
    if state_path.is_file():
        state_txt = state_path.read_text(encoding="utf-8", errors="ignore")
        expected_token = f"Bab {total_chaps}"
        if expected_token not in state_txt:
            errors.append(f"state.md belum menyebut frontier bab terakhir '{expected_token}'")

    return errors


def build_manuscript_text(story_dir: Path, files: list[Path]) -> str:
    pieces: list[str] = [f"# {story_dir.name}\n\n"]
    for ch in files:
        pieces.append(ch.read_text(encoding="utf-8", errors="ignore").strip())
        pieces.append("\n\n---\n\n")
    return "".join(pieces)


def check_and_sync_manuscript(story_dir: Path, files: list[Path], fix: bool = False) -> tuple[bool, str]:
    manuscript_path = story_dir / "manuscript.md"
    expected = build_manuscript_text(story_dir, files)

    if not manuscript_path.is_file():
        if fix:
            manuscript_path.write_text(expected, encoding="utf-8")
            return True, f"manuscript.md berhasil dibuat ({len(files)} bab)"
        return False, "manuscript.md belum ada di folder cerita"

    actual = manuscript_path.read_text(encoding="utf-8", errors="ignore")
    if actual.splitlines() == expected.splitlines():
        return True, "manuscript.md identik dengan seluruh bab"

    if fix:
        manuscript_path.write_text(expected, encoding="utf-8")
        return True, f"manuscript.md berhasil disinkronkan ({len(files)} bab)"
    return False, "manuscript.md tidak sinkron dengan bab terkini (jalankan dengan --fix)"


def check_and_sync_reader(repo_root: Path, files: list[Path], fix: bool = False) -> tuple[bool, str]:
    reader_path = repo_root / "reader.html"
    index_path = repo_root / "index.html"
    builder_script = repo_root / "scripts" / "build-reader.py"

    if not reader_path.is_file() or not index_path.is_file():
        if fix and builder_script.is_file():
            proc = subprocess.run([sys.executable, str(builder_script)], capture_output=True, text=True)
            if proc.returncode == 0:
                return True, "reader.html dan index.html (GitHub Pages) berhasil dibuat ulang"
            return False, f"Gagal membuat reader.html: {proc.stderr}"
        return False, "reader.html / index.html belum dibuat di root repositori"

    reader_mtime = min(reader_path.stat().st_mtime, index_path.stat().st_mtime)
    newest_chap = max((f.stat().st_mtime for f in files), default=0)

    if reader_mtime < newest_chap:
        if fix and builder_script.is_file():
            proc = subprocess.run([sys.executable, str(builder_script)], capture_output=True, text=True)
            if proc.returncode == 0:
                return True, "reader.html dan index.html berhasil diperbarui dengan bab terbaru"
            return False, f"Gagal memperbarui reader.html: {proc.stderr}"
        return False, "reader.html / index.html lebih lama dari file bab terkini (perlu di-build ulang)"

    # Validasi integritas JSON & JS di reader.html dan index.html
    for html_file in [reader_path, index_path]:
        html_txt = html_file.read_text(encoding="utf-8", errors="ignore")
        scripts = re.findall(r"<script(?:\s+[^>]*)?>(.*?)</script>", html_txt, re.DOTALL)
        if len(scripts) < 2:
            return False, f"{html_file.name} kehilangan script engine"
        try:
            json.loads(scripts[0])
        except Exception as e:
            return False, f"JSON data di {html_file.name} rusak: {e}"
        if shutil.which("node"):
            tmp_val = repo_root / f".tmp_val_{html_file.stem}.js"
            try:
                tmp_val.write_text(scripts[1], encoding="utf-8")
                res = subprocess.run(["node", "-c", str(tmp_val)], capture_output=True, text=True)
                if res.returncode != 0:
                    return False, f"Sintaks JavaScript di {html_file.name} error: {res.stderr.strip()}"
            finally:
                if tmp_val.exists():
                    tmp_val.unlink()

    return True, "reader.html dan index.html (GitHub Pages) mutakhir & valid"


def check_and_sync_registry(repo_root: Path, story_dir: Path, files: list[Path], fix: bool = False) -> tuple[bool, str]:
    reg_path = repo_root / "story" / "universe-registry.md"
    if not reg_path.is_file():
        return False, "story/universe-registry.md tidak ditemukan"

    content = reg_path.read_text(encoding="utf-8", errors="ignore")
    story_name = story_dir.name
    total_chaps = len(files)
    total_words = sum(len(f.read_text(encoding="utf-8", errors="ignore").split()) for f in files)
    total_words_fmt = f"{total_words:,}".replace(",", ".")

    pat = re.compile(
        r"^(\|\s*`?[A-Z0-9-]+`?\s*\|\s*`?[A-Z0-9-]+`?\s*\|\s*"
        + re.escape(story_name)
        + r"\s*\|\s*`?[A-Z]+`?\s*\|\s*)(\d+)(\s*\|\s*)([\d.]+)(\s*\|.*)$",
        re.M,
    )
    m = pat.search(content)
    if not m:
        return False, f"Judul '{story_name}' belum terdaftar di Tabel 1 universe-registry.md"

    reg_chaps = int(m.group(2))
    reg_words = m.group(4)

    if reg_chaps == total_chaps and reg_words == total_words_fmt:
        return True, f"Metrik cocok ({total_chaps} bab, {total_words_fmt} kata)"

    if fix:
        new_row = f"{m.group(1)}{total_chaps}{m.group(3)}{total_words_fmt}{m.group(5)}"
        new_content = pat.sub(lambda _: new_row, content, count=1)
        reg_path.write_text(new_content, encoding="utf-8")
        return True, f"universe-registry.md diperbarui ({total_chaps} bab, {total_words_fmt} kata)"

    return False, f"Metrik registry ({reg_chaps} bab, {reg_words} kata) != aktual ({total_chaps} bab, {total_words_fmt} kata)"


def check_and_sync_rules_doc(repo_root: Path, fix: bool = False) -> tuple[bool, str]:
    doc_path = repo_root / "engine" / "12-stress-rules.md"
    expected = generate_rules_doc(repo_root)

    if not doc_path.is_file():
        if fix:
            doc_path.write_text(expected, encoding="utf-8")
            return True, "engine/12-stress-rules.md berhasil digenerate dari rules.json"
        return False, "engine/12-stress-rules.md belum ada (jalankan dengan --fix)"

    actual = doc_path.read_text(encoding="utf-8", errors="ignore")
    if actual == expected:
        return True, "engine/12-stress-rules.md identik dengan rules.json"

    if fix:
        doc_path.write_text(expected, encoding="utf-8")
        return True, "engine/12-stress-rules.md berhasil disinkronkan dari rules.json"
    return False, "engine/12-stress-rules.md tidak sinkron dengan rules.json (jalankan dengan --fix)"


def extract_character_names(story_dir: Path) -> set[str]:
    names: set[str] = {"hana", "bima", "nino", "fajar", "meli", "maya", "hendra", "ratih"}
    canon = story_dir / "canon.md"
    if canon.is_file():
        txt = canon.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"^###\s+\d+\.\s+([A-Za-z]+)", txt, flags=re.M):
            names.add(m.group(1).lower())
    return names


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Master Gatekeeper & Stress Test Terpadu (22 Pemeriksaan) Novel MetroPop."
    )
    parser.add_argument("target", help="Folder story/<Judul> atau file bab-*.md")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Sinkronkan otomatis aset turunan (manuscript.md, reader.html, universe-registry.md, engine/12-stress-rules.md)",
    )
    args = parser.parse_args()

    target = Path(args.target).resolve()
    repo_root = Path(__file__).resolve().parent.parent

    is_single_chapter = target.is_file()
    if is_single_chapter:
        story_dir = target.parent.parent
        files = [target]
    else:
        story_dir = target
        chapters_dir = target / "chapters" if (target / "chapters").is_dir() else target
        files = sorted(chapters_dir.glob("bab-*.md"))

    if not files:
        print(f"{FAIL_ICON} Tidak ditemukan file bab-*.md di {target}", file=sys.stderr)
        return 1

    print("=" * 82)
    print(f"  MASTER GATEKEEPER & STRESS TEST TERPADU (22 PEMERIKSAAN)")
    print(f"  Target: {story_dir.name}{' (bab tunggal)' if is_single_chapter else f' ({len(files)} bab)'}")
    print("=" * 82)

    total_errors: list[str] = []

    # =========================================================================
    # [A] 8 PEMERIKSAAN SINKRONISASI ASET & DOKUMEN
    # =========================================================================
    print("  [A] SINKRONISASI ASET & DOKUMEN (8 PEMERIKSAAN):")

    if is_single_chapter:
        print("  (Lewati pemeriksaan sinkronisasi untuk pengetesan bab tunggal)\n")
    else:
        # 1. Dokumen Pilar
        pillar_errs = check_story_pillars(story_dir)
        if pillar_errs:
            for e in pillar_errs:
                total_errors.append(f"[Pilar] {e}")
            print(f"  1. Dokumen Pilar & Character Sheet             : {FAIL_ICON} ({len(pillar_errs)} isu)")
        else:
            print(f"  1. Dokumen Pilar & Character Sheet             : {PASS_ICON}")

        # 2. Penomoran & Outline Title Sync
        num_errs = check_numbering_and_outline(story_dir, files)
        if num_errs:
            for e in num_errs:
                total_errors.append(f"[Nomor/Judul] {e}")
            print(f"  2. Penomoran Bab & Judul Sinkron Outline       : {FAIL_ICON} ({len(num_errs)} isu)")
        else:
            print(f"  2. Penomoran Bab & Judul Sinkron Outline       : {PASS_ICON}")

        # 3. Ledger & State Frontier Sync
        ls_errs = check_ledger_and_state(story_dir, files)
        if ls_errs:
            for e in ls_errs:
                total_errors.append(f"[Ledger/State] {e}")
            print(f"  3. Baris ledger.md & Garis Depan state.md      : {FAIL_ICON} ({len(ls_errs)} isu)")
        else:
            print(f"  3. Baris ledger.md & Garis Depan state.md      : {PASS_ICON}")

        # 4. manuscript.md Sync
        manu_ok, manu_msg = check_and_sync_manuscript(story_dir, files, fix=args.fix)
        if manu_ok:
            icon = FIXED_ICON if (args.fix and "berhasil" in manu_msg) else PASS_ICON
            print(f"  4. Naskah Gabungan manuscript.md               : {icon}")
        else:
            total_errors.append(f"[manuscript.md] {manu_msg}")
            print(f"  4. Naskah Gabungan manuscript.md               : {FAIL_ICON} ({manu_msg})")

        # 5. reader.html & index.html Sync
        reader_ok, reader_msg = check_and_sync_reader(repo_root, files, fix=args.fix)
        if reader_ok:
            icon = FIXED_ICON if (args.fix and "berhasil" in reader_msg) else PASS_ICON
            print(f"  5. Ebook Web Reader (reader & index.html)      : {icon}")
        else:
            total_errors.append(f"[reader.html] {reader_msg}")
            print(f"  5. Ebook Web Reader (reader & index.html)      : {FAIL_ICON} ({reader_msg})")

        # 6. universe-registry.md Sync
        reg_ok, reg_msg = check_and_sync_registry(repo_root, story_dir, files, fix=args.fix)
        if reg_ok:
            icon = FIXED_ICON if (args.fix and "diperbarui" in reg_msg) else PASS_ICON
            print(f"  6. Metrik Semesta di universe-registry.md      : {icon}")
        else:
            total_errors.append(f"[universe-registry.md] {reg_msg}")
            print(f"  6. Metrik Semesta di universe-registry.md      : {FAIL_ICON} ({reg_msg})")

        # 7. engine/12-stress-rules.md Sync
        rules_ok, rules_msg = check_and_sync_rules_doc(repo_root, fix=args.fix)
        if rules_ok:
            icon = FIXED_ICON if (args.fix and "berhasil" in rules_msg) else PASS_ICON
            print(f"  7. Dokumen Aturan engine/12-stress-rules.md    : {icon}")
        else:
            total_errors.append(f"[12-stress-rules.md] {rules_msg}")
            print(f"  7. Dokumen Aturan engine/12-stress-rules.md    : {FAIL_ICON} ({rules_msg})")

        # 8. Audit Kontinuitas Berlapis (audit-continuity.py)
        audit_script = repo_root / "scripts" / "audit-continuity.py"
        if audit_script.is_file() and (story_dir / "ledger.md").exists():
            proc = subprocess.run([sys.executable, str(audit_script), str(story_dir)], capture_output=True, text=True)
            if proc.returncode != 0:
                total_errors.append("[Kontinuitas] audit-continuity.py menemukan isu kontinuitas.")
                print(f"  8. Audit Kontinuitas Berlapis                  : {FAIL_ICON}")
            else:
                print(f"  8. Audit Kontinuitas Berlapis                  : {PASS_ICON}")
        else:
            print(f"  8. Audit Kontinuitas Berlapis                  : {PASS_ICON} (dilewati, bukan folder story)")

        print()

    # =========================================================================
    # [B] 14 ATURAN KUALITAS PROSA, GAYA, & DIALOG
    # =========================================================================
    print(f"  [B] KUALITAS PROSA, GAYA, & DIALOG (14 ATURAN x {len(files)} BAB):")
    char_names = extract_character_names(story_dir)

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
        ("word_range", "9. Rentang Kata Bab (600-900 kata)"),
        ("plain_text", "10. Teks Polos 100% (0 Em Dash, 0 Markup *, 0 Quote Atas)"),
        ("title_rule", "11. Aturan Judul Bab (Clue Singkat & Bebas Nama Tokoh)"),
        ("in_medias_res", "12. Pembuka In Medias Res & Ruang Aksi"),
        ("long_quote", "13. Batas Napas Kalimat Dialog (<=20 Kata per Kutipan)"),
        ("aykb_quote", "14. Anti-Eksposisi 'As You Know, Bob' di Dialog"),
        ("mixed_negation", "15. Konsistensi Register Lisan di Dialog (Anti Belang)"),
        ("filter_words", "16. Bebas Kata Filter Persepsi"),
        ("stock_tells", "17. Bebas Gerakan Klise / Stock Tells"),
        ("ai_syntax", "18. Bebas Sintaksis AI & Pembungkus Abstrak"),
        ("bookish_tags", "19. Bebas Tag Dialog Buku Pelajaran"),
        ("slop_clinical", "20. Bebas AI Slop & Jargon Psikologi Klinis"),
        ("sensory_cap", "21. Batas Anatomi Tubuh (<=2) & Penciuman (<=2) per Bab"),
        ("discourse_rhythm", "22. Variasi Posisi Dialog (EndQ <=75%) & Ritme Kalimat"),
    ]

    for key, title in labels:
        cnt = cat_counts[key]
        status = PASS_ICON if cnt == 0 else f"{FAIL_ICON} ({cnt} pelanggaran)"
        print(f"  {title:<62}: {status}")

    print("-" * 82)
    if total_errors:
        print(f"  HASIL AKHIR: {FAIL_ICON} Ditemukan {len(total_errors)} pelanggaran yang WAJIB diperbaiki:")
        for err in total_errors[:30]:
            print(f"   - {err}")
        if len(total_errors) > 30:
            print(f"   ... dan {len(total_errors) - 30} pelanggaran lainnya.")
        print("=" * 82)
        return 1

    print(f"  HASIL AKHIR: {PASS_ICON} Seluruh 22 pemeriksaan LULUS 100% (0 pelanggaran).")
    print("=" * 82)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

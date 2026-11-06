#!/usr/bin/env python3
"""
Audit Kontinuitas Lintas Bab (Engine v2.3)

Script ini memvalidasi kontinuitas antarbab, keberadaan file state.md,
serta menguji konsistensi klaim waktu relatif, label status hubungan,
perkenalan tokoh, dan angka nominal uang.

Cara pakai:
  python3 scripts/audit-continuity.py "story/Narik Ojol Cinta Pun Nongol"
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

STATUS_TERMS = [
    "pacar", "calon istri", "calon suami", "calon cucu mantu", "tunangan",
    "istri", "suami", "pasangan", "kekasih", "pacar sewaan", "pacar pura-pura",
]
RELATIVE_TERMS = [
    "kemarin", "semalam", "tadi malam", "tadi pagi", "tadi siang", "tadi sore",
    "minggu lalu", "minggu depan", "besok", "lusa", "hari ini", "nanti malam",
    "senin lalu", "selasa lalu", "rabu lalu", "kamis lalu", "jumat lalu", "sabtu lalu",
    "dua hari lalu", "tiga hari lalu", "seminggu", "dua minggu", "sebulan",
]
INTRO_PATTERNS = [
    r"\bItu ([A-Z][a-z]+(?: [A-Z][a-z]+)?)\b",
    r"\bbernama ([A-Z][a-z]+(?: [A-Z][a-z]+)?)\b",
    r"\bNamanya baru kuketahui belakangan: ([A-Z][a-z]+)\b",
]
MONEY_RE = re.compile(r"(?:Rp\s?[\d.,]+(?:\s?(?:juta|ribu))?|\b(?:[a-z]+(?: [a-z]+)?) (?:juta|ribu) rupiah)", re.I)


def load(story: Path) -> list[tuple[int, list[str]]]:
    chapters = story / "chapters" if (story / "chapters").is_dir() else story
    out = []
    for f in sorted(chapters.glob("bab-*.md")):
        m = re.search(r"bab-(\d+)", f.name)
        if m:
            n = int(m.group(1))
            out.append((n, f.read_text(encoding="utf-8").splitlines()))
    return out


def audit_story(story_dir: Path) -> int:
    issues = 0
    print("=" * 70)
    print(f"AUDIT KONTINUITAS BERLAPIS: {story_dir.name}")
    print("=" * 70)

    # 0. Verifikasi Dokumen Pilar Kontinuitas & Universe Registry
    pilar_files = ["canon.md", "state.md", "ledger.md"]
    print("0. DOKUMEN PILAR KONTINUITAS & UNIVERSE REGISTRY:")
    univ_reg = story_dir.parent / "universe-registry.md"
    if univ_reg.is_file():
        print(f"   [OK] story/universe-registry.md ditemukan ({univ_reg.stat().st_size} bytes)")
    else:
        print("   [WARN] story/universe-registry.md tidak ditemukan di root story/!")

    for pf in pilar_files:
        p = story_dir / pf
        if p.is_file():
            print(f"   [OK] {pf} ditemukan ({p.stat().st_size} bytes)")
        else:
            print(f"   [FAIL] {pf} TIDAK DITEMUKAN!")
            issues += 1
    print()

    chapters = load(story_dir)
    if not chapters:
        print("   [FAIL] Tidak ada file bab ditemukan di folder chapters/.", file=sys.stderr)
        return 1

    # 1. Label Status Hubungan Per Bab
    print("=" * 70)
    print("1. LABEL STATUS HUBUNGAN PER BAB (cek konsisten dengan tahap hubungan)")
    print("=" * 70)
    for n, lines in chapters:
        hits = defaultdict(list)
        for i, line in enumerate(lines, 1):
            low = line.lower()
            for term in STATUS_TERMS:
                if re.search(rf"\b{re.escape(term)}\b", low):
                    hits[term].append(i)
        if hits:
            summary = ", ".join(f"{t} (L{','.join(map(str, v[:3]))})" for t, v in hits.items())
            print(f"Bab {n:02d}: {summary}")

    # 2. Klaim Waktu Relatif & Validasi Hari Otomatis terhadap Ledger
    print()
    print("=" * 70)
    print("2. KLAIM WAKTU RELATIF & VALIDASI HARI OTOMATIS (vs ledger.md)")
    print("=" * 70)
    days_order = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    ledger_days: dict[int, str] = {}
    ledger_path = story_dir / "ledger.md"
    if ledger_path.is_file():
        for line in ledger_path.read_text(encoding="utf-8").splitlines():
            m_row = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+)\|", line)
            if m_row:
                b_num = int(m_row.group(1))
                w_loc = m_row.group(2).lower()
                for d in days_order:
                    if re.search(rf"\b{d}\b", w_loc):
                        ledger_days[b_num] = d
                        break

    day_adj_re = re.compile(
        r"\b(senin|selasa|rabu|kamis|jumat|sabtu|minggu)(?:\s+(?:pagi|siang|sore|petang|malam))?\s+(besok|kemarin)\b",
        re.I,
    )

    for n, lines in chapters:
        active_day = ledger_days.get(n)
        for i, line in enumerate(lines, 1):
            low = line.lower()
            found = [t for t in RELATIVE_TERMS if re.search(rf"\b{re.escape(t)}\b", low)]
            if found:
                day_tag = f" [Hari Bab: {active_day.capitalize()}]" if active_day else ""
                print(f"Bab {n:02d} L{i:02d}{day_tag} [{', '.join(found)}]: {line.strip()[:110]}")
            if active_day:
                idx = days_order.index(active_day)
                expected_tomorrow = days_order[(idx + 1) % 7]
                expected_yesterday = days_order[(idx - 1) % 7]
                for m_d in day_adj_re.finditer(low):
                    mentioned_day = m_d.group(1).lower()
                    rel_word = m_d.group(2).lower()
                    if rel_word == "besok" and mentioned_day != expected_tomorrow:
                        print(
                            f"   [FAIL] Bab {n:02d} L{i:02d}: Bab berlangsung hari {active_day.capitalize()}, "
                            f"tetapi menyebut '{m_d.group(0)}' (besok seharusnya {expected_tomorrow.capitalize()})!"
                        )
                        issues += 1
                    elif rel_word == "kemarin" and mentioned_day != expected_yesterday:
                        print(
                            f"   [FAIL] Bab {n:02d} L{i:02d}: Bab berlangsung hari {active_day.capitalize()}, "
                            f"tetapi menyebut '{m_d.group(0)}' (kemarin seharusnya {expected_yesterday.capitalize()})!"
                        )
                        issues += 1

    # 3. Perkenalan Tokoh Ganda
    print()
    print("=" * 70)
    print("3. PERKENALAN TOKOH GANDA (tokoh 'diperkenalkan' lebih dari sekali)")
    print("=" * 70)
    intro = defaultdict(list)
    for n, lines in chapters:
        text = "\n".join(lines)
        for pat in INTRO_PATTERNS:
            for m in re.finditer(pat, text):
                intro[m.group(1)].append(n)
    dup_intro = False
    for name, bab in sorted(intro.items()):
        uniq = sorted(set(bab))
        if len(uniq) > 1:
            print(f"   [WARNING] {name}: diperkenalkan ganda di Bab {uniq}")
            dup_intro = True
            issues += 1
    if not dup_intro:
        print("   [OK] Tidak ada perkenalan tokoh ganda.")

    # 4. Nominal Uang Per Bab
    print()
    print("=" * 70)
    print("4. NOMINAL UANG PER BAB (cocokkan dengan Fakta Keras di state.md / ledger.md)")
    print("=" * 70)
    for n, lines in chapters:
        text = " ".join(lines)
        found = [m.group(0).strip() for m in MONEY_RE.finditer(text)]
        if found:
            print(f"Bab {n:02d}: {'; '.join(dict.fromkeys(found))[:230]}")

    # 5. Aturan Spesifik Kasus & Milestone Kontinuitas
    print()
    print("=" * 70)
    print("5. VERIFIKASI AMBANG BATAS & MILESTONE (Automated Rule Assertions)")
    print("=" * 70)
    # Check Bab 1-2 for premature "calon istri"
    for n, lines in chapters:
        if n in (1, 2):
            for i, line in enumerate(lines, 1):
                if re.search(r"\bcalon istri\b", line, re.I):
                    print(f"   [FAIL] Bab {n:02d} L{i}: Deteksi 'calon istri' sebelum waktunya!")
                    issues += 1
    # Check Bab 1: "Damar" must not be named in Bab 1
    for n, lines in chapters:
        if n == 1:
            for i, line in enumerate(lines, 1):
                if re.search(r"\bDamar\b", line):
                    print(f"   [FAIL] Bab 01 L{i}: Nama 'Damar' muncul prematur sebelum Bab 12!")
                    issues += 1
    # Check Bab 2: Rian must not recite plate B 4892 TBT in his dialogue
    for n, lines in chapters:
        if n == 2:
            for i, line in enumerate(lines, 1):
                low = line.lower()
                if ("b 4892 tbt" in low) and ("ujar rian" in low or "kata rian" in low or "rian sambil" in low):
                    print(f"   [FAIL] Bab 02 L{i}: Rian secara ajaib mengetahui nomor pelat B 4892 TBT!")
                    issues += 1
    # Check that Rian does not meet Ibu in Bab 20
    for n, lines in chapters:
        if n == 20:
            text = "\n".join(lines).lower()
            if "cium tangan ibu" in text or "rian mencium tangan ibu" in text or "rian duduk di ruang tengah" in text:
                print(f"   [FAIL] Bab 20: Pelanggaran milestone Rian bertemu Ibu sebelum Bab 23!")
                issues += 1

    if issues == 0:
        print("   [PASS] Seluruh pengecekan kontinuitas otomatis BERSIH (0 isu).")
    else:
        print(f"   [ALERT] Terdeteksi {issues} potensi isu kontinuitas.")

    return 0 if issues == 0 else 1


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    target = Path(sys.argv[1])
    if not target.exists():
        print(f"Path tidak ditemukan: {target}", file=sys.stderr)
        return 1
    return audit_story(target)


if __name__ == "__main__":
    raise SystemExit(main())

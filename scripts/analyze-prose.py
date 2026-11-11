#!/usr/bin/env python3
"""
Analisis Mekanis Prosa Bahasa Indonesia — Novel MetroPop (v2.2)
Menggabungkan pemeriksaan kaidah MetroPop Indonesia + metrik haowjy & Nanako0129/sepia:
  1. Rentang kata bab (600-900 standar; 901-1200 darurat) & 0 Em Dash (—)
  2. Deteksi Frasa AI Slop & Terjemahan Harfiah
  3. Rasio Paragraf Dialog & Kebiasaan Kutipan di Akhir Paragraf (Quote at Paragraph End >75%)
  4. Uji Kelisanan Dialog (Batas Maksimal 20 Kata per Kutipan "..." & Anti-"As You Know, Bob" di Dialog)
  5. Distribusi Panjang Kalimat & Deteksi Deretan >=3 Kalimat Berurutan Panjang Seragam
  6. Pola Sintaksis AI (Klausa "Sambil...", ", membuat...", & Rotasi Tag Buku Pelajaran "ujarnya/tuturnya/tukasnya")
  7. Batas Sensasi Anatomi Tubuh (Over-Embodied <=2) & Indera Penciuman (Smell <=2)
  8. Register Kausal Manusia Indonesia (soalnya/gara-gara/makanya/masalahnya/habisnya)
  9. Jejak Kata Ganti POV 1 vs POV 3 & Pengulangan Kata (Window 5 Paragraf)

Cara pakai:
  python3 scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol/chapters/bab-01.md"
  python3 scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol"
"""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)?")
SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])(?:[”"\']*)\s+')
QUOTE_RE = re.compile(r'[“"]([^”"]+)[”"]')
PARA_END_QUOTE_RE = re.compile(r'[”"]\s*$')
MAX_QUOTE_WORDS = 20

# Pola eksposisi waktu/backstory "As You Know, Bob" yang tidak wajar diucapkan di dalam dialog
AYKB_DIALOGUE_PATTERNS = [
    r"\b(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|beberapa)\s+(?:hari|minggu|bulan|tahun)\s+(?:yang\s+)?lalu\b",
    r"\b(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s+lalu\b",
    r"\bselama\s+(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan)\s+(?:hari|minggu|bulan|tahun)\b",
    r"\bsebagai\s+atasan\s+yang\s+sudah\b",
]

ID_STOPWORDS = {
    "yang", "untuk", "dengan", "tidak", "dalam", "bukan", "sudah",
    "karena", "kalau", "nggak", "enggak", "lebih", "masih", "harus",
    "bisa", "akan", "seperti", "ketika", "waktu", "sambil", "sampai",
    "depan", "belakang", "atas", "bawah", "antara", "sebuah", "seorang",
    "mereka", "kami", "kita", "kalian", "beliau", "diriku", "dirinya",
    "begitu", "sangat", "sekali", "paling", "hanya", "cuma", "mulai",
    "terus", "langsung", "kembali", "lagi", "tanpa", "lewat", "sejak",
    "selama", "sekitar", "setelah", "sebelum", "namun", "tetapi",
    "padahal", "meski", "walau", "bahwa", "apakah", "kenapa", "mengapa",
    "bagaimana", "dimana", "kemana", "darimana", "siapa", "kapan", "berapa",
}

AI_SLOP_PATTERNS = [
    r"arah jam sebelas",
    r"izin diberikan",
    r"kecilkan suaramu",
    r"papan tombol",
    r"sepeda kargo",
    r"penghangat kabin",
    r"menulis cek",
    r"atmosfer membeku",
    r"bak disambar petir",
    r"mengukir senyum",
    r"menyemburkan caci maki",
    r"janji suci",
    r"selempang cum laude melingkar",
]

BOOKISH_SPEECH_TAGS = (
    "ujarnya", "tuturnya", "timpalnya", "tukasnya", "cetusnya", "serunya", "imbuhnya", "tandasnya", "kilahnya"
)

EMBODIED_PATTERNS = [
    r"dada(?:ku)?\s+sesak",
    r"tenggorokan(?:ku)?\s+tercekat",
    r"keringat\s+dingin",
    r"jantung(?:ku)?\s+berdegup",
    r"jantung(?:ku)?\s+mencelos",
    r"napas(?:ku)?\s+memburu",
    r"perut(?:ku)?\s+melilit",
    r"lutut(?:ku)?\s+lemas",
]

SMELL_WORDS = ("aroma", "bau", "baunya", "wangi", "wanginya", "harum", "harumnya")
HUMAN_CAUSALS = ("soalnya", "gara-gara", "masalahnya", "makanya", "habisnya", "lagian")


def strip_markdown_headers(text: str) -> str:
    lines = [line for line in text.splitlines() if not line.strip().startswith("#")]
    return "\n".join(lines)


def get_words(text: str) -> list[str]:
    return [m.group(0).lower() for m in WORD_RE.finditer(text)]


def get_paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def get_sentences(text: str) -> list[str]:
    flat = " ".join(line.strip() for line in text.splitlines() if line.strip())
    return [s.strip() for s in SENTENCE_SPLIT_RE.split(flat) if s.strip()]


def detect_similar_length_runs(sent_lengths: list[int], tolerance: int = 2, min_run: int = 3, min_words: int = 10) -> list[tuple[int, int, list[int]]]:
    """Deteksi deretan >=3 kalimat menengah/panjang (>=10 kata) berurutan yang panjang katanya hampir sama."""
    runs: list[tuple[int, int, list[int]]] = []
    n = len(sent_lengths)
    i = 0
    while i < n:
        if sent_lengths[i] < min_words:
            i += 1
            continue
        j = i + 1
        while j < n and sent_lengths[j] >= min_words and abs(sent_lengths[j] - sent_lengths[i]) <= tolerance:
            j += 1
        if j - i >= min_run:
            runs.append((i + 1, j, sent_lengths[i:j]))
            i = j
        else:
            i += 1
    return runs


def analyze_chapter(path: Path, verbose: bool = True) -> dict:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    body = strip_markdown_headers(raw)
    all_words = get_words(body)
    word_count = len(all_words)

    paras = get_paragraphs(body)
    sents = get_sentences(body)
    sent_lengths = [len(get_words(s)) for s in sents if get_words(s)]

    # 1. Cek Em Dash & AI Slop
    em_dash_count = raw.count("—")
    slop_hits = []
    lower_raw = raw.lower()
    for pat in AI_SLOP_PATTERNS:
        if re.search(pat, lower_raw):
            slop_hits.append(pat)

    # 2. Rasio Dialog, Kutipan di Akhir Paragraf, Batas 20 Kata per Kutipan, & Anti-"As You Know, Bob"
    dialogue_paras_list = [p for p in paras if QUOTE_RE.search(p)]
    dialogue_paras = len(dialogue_paras_list)
    dialogue_pct = (dialogue_paras / len(paras) * 100) if paras else 0.0
    end_quote_paras = sum(1 for p in dialogue_paras_list if PARA_END_QUOTE_RE.search(p))
    end_quote_pct = (end_quote_paras / dialogue_paras * 100) if dialogue_paras else 0.0

    all_quotes = [m.group(1).strip() for p in paras for m in QUOTE_RE.finditer(p)]
    long_quotes: list[tuple[int, str]] = []
    aykb_quotes: list[tuple[str, str]] = []
    for q in all_quotes:
        q_words = get_words(q)
        if len(q_words) > MAX_QUOTE_WORDS:
            long_quotes.append((len(q_words), q))
        q_low = q.lower()
        for pat in AYKB_DIALOGUE_PATTERNS:
            m_aykb = re.search(pat, q_low)
            if m_aykb:
                aykb_quotes.append((m_aykb.group(0), q))
                break

    # 3. Deretan >=3 Kalimat Berurutan dengan Panjang Seragam (Sepia Style-Pass)
    mono_runs = detect_similar_length_runs(sent_lengths, tolerance=2, min_run=3)

    # 4. Pola Sintaksis AI & Tag Buku Pelajaran
    counts = Counter(all_words)
    leading_sambil = sum(1 for s in sents if s.lower().startswith("sambil "))
    making_clause = len(re.findall(r",\s*membuat\s+", lower_raw))
    bookish_tags = sum(counts[t] for t in BOOKISH_SPEECH_TAGS)

    # 5. Batas Sensasi Anatomi (Over-Embodied) & Penciuman (Smell) & Kausal Manusia
    embodied_count = sum(len(re.findall(pat, lower_raw)) for pat in EMBODIED_PATTERNS)
    smell_count = sum(counts[w] for w in SMELL_WORDS)
    human_causal_count = sum(counts[w] for w in HUMAN_CAUSALS)

    # 6. Distribusi Kata Ganti POV 1 vs POV 3
    pov1_direct = sum(counts[w] for w in ("aku", "saya", "gue", "gua", "ku"))
    pov1_clitic = sum(
        freq for w, freq in counts.items()
        if len(w) > 4 and w.endswith("ku") and w not in ("buku", "kuku", "suku", "dagu", "lagu", "kaku", "beku", "laku", "paku")
    )
    pov1_total = pov1_direct + pov1_clitic
    pov3_total = sum(counts[w] for w in ("dia", "ia", "mereka", "beliau"))

    # 7. Deteksi Pengulangan Kata (Window 5 Paragraf)
    window_size = 5
    repetitions: dict[str, tuple[int, int, int]] = {}
    for i in range(0, max(len(paras) - window_size + 1, 1)):
        win = paras[i : i + window_size]
        win_counts = Counter(
            w for p in win for w in get_words(p)
            if len(w) >= 5 and w not in ID_STOPWORDS
        )
        for w, c in win_counts.items():
            if c >= 4:
                prev = repetitions.get(w, (0, 0, 0))[0]
                if c > prev:
                    repetitions[w] = (c, i + 1, i + len(win))

    if verbose:
        print("=" * 68)
        print(f"  Analisis Mekanis Prosa (v2.2): {path.name}")
        print("=" * 68)
        status = "OK (Standar 600-900)"
        if word_count < 600:
            status = "PERINGATAN (<600 kata)"
        elif word_count > 1200:
            status = "PERINGATAN (>1200 kata)"
        elif word_count > 900:
            status = "OK (Darurat 901-1200)"
        print(f"  Jumlah Kata Prosa     : {word_count} kata [{status}]")
        print(f"  Em Dash (—)           : {em_dash_count} [{'LULUS' if em_dash_count == 0 else 'GAGAL!'}]")
        print(f"  Frasa AI Slop         : {len(slop_hits)} ditemukan {slop_hits if slop_hits else '[LULUS]'}")
        print(
            f"  Rasio Paragraf Dialog : {dialogue_paras}/{len(paras)} par ({dialogue_pct:.0f}%) | "
            f"Dialog di Akhir Par: {end_quote_paras}/{dialogue_paras} ({end_quote_pct:.0f}%)"
        )
        print(
            f"  Kelisanan Dialog      : Kutipan >{MAX_QUOTE_WORDS} kata = {len(long_quotes)} [{'LULUS' if not long_quotes else 'PERBAIKI!'}] | "
            f"Eksposisi Waktu ('As You Know, Bob') = {len(aykb_quotes)} [{'LULUS' if not aykb_quotes else 'PERBAIKI!'}]"
        )
        for qw, qt in long_quotes[:5]:
            print(f"    -> [>{MAX_QUOTE_WORDS}w: {qw} kata] \"{qt}\"")
        for trig, qt in aykb_quotes[:5]:
            print(f"    -> [AYKB: '{trig}'] \"{qt}\"")
        if sent_lengths:
            print(
                f"  Panjang Kalimat       : rata-rata {statistics.fmean(sent_lengths):.1f} kata "
                f"(min {min(sent_lengths)}, maks {max(sent_lengths)}, std {statistics.pstdev(sent_lengths) if len(sent_lengths) > 1 else 0:.1f})"
            )
        print(
            f"  Deret Kalimat Seragam : {len(mono_runs)} deret (>=3 kalimat selisih <=2 kata)"
        )
        print(
            f"  Pola Sintaksis AI     : Awalan 'Sambil' = {leading_sambil} | ', membuat' = {making_clause} | "
            f"Tag buku (ujarnya/tuturnya) = {bookish_tags}"
        )
        print(
            f"  Indera & Emosi (Sepia): Anatomi tubuh = {embodied_count} (batas <=2) | "
            f"Bau/Aroma = {smell_count} (batas <=2) | Kausal lisan = {human_causal_count}"
        )
        print(
            f"  Jejak Kata Ganti      : POV-1 (aku/-ku/gue) = {pov1_total} ({pov1_total/max(word_count,1)*100:.1f}%) | "
            f"POV-3 (dia/ia/mereka) = {pov3_total} ({pov3_total/max(word_count,1)*100:.1f}%)"
        )
        if repetitions:
            top_reps = sorted(repetitions.items(), key=lambda x: -x[1][0])[:8]
            rep_str = ", ".join(f'"{w}" ({c}x di par {s}-{e})' for w, (c, s, e) in top_reps)
            print(f"  Kata Sering Diulang   : {rep_str}")
        print()

    return {
        "name": path.name,
        "words": word_count,
        "em_dash": em_dash_count,
        "slop": slop_hits,
        "dialogue_pct": dialogue_pct,
        "end_quote_pct": end_quote_pct,
        "long_quotes": len(long_quotes),
        "aykb_quotes": len(aykb_quotes),
        "mean_sent": statistics.fmean(sent_lengths) if sent_lengths else 0.0,
        "mono_runs": len(mono_runs),
        "embodied": embodied_count,
        "smell": smell_count,
        "bookish": bookish_tags,
        "pov1_pct": pov1_total / max(word_count, 1) * 100,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analisis mekanis prosa Bahasa Indonesia (v2.2).")
    parser.add_argument("target", help="File bab .md atau folder story/<Judul>")
    args = parser.parse_args()

    target = Path(args.target)
    if target.is_file():
        analyze_chapter(target, verbose=True)
        return 0

    chapters_dir = target / "chapters" if (target / "chapters").is_dir() else target
    files = sorted(chapters_dir.glob("bab-*.md"))
    if not files:
        print(f"Tidak ditemukan file bab-*.md di {target}", file=sys.stderr)
        return 1

    print(
        f"{'Bab':<10} | {'Kata':<5} | {'Em':<2} | {'Dlg%':<5} | {'EndQ%':<6} | "
        f"{'Dlg>20':<6} | {'AYKB':<4} | {'Kal(Avg)':<8} | {'Mono':<4} | {'Tubuh':<5} | {'Bau':<3} | {'POV1%'}"
    )
    print("-" * 92)
    for f in files:
        res = analyze_chapter(f, verbose=False)
        print(
            f"{res['name']:<10} | {res['words']:<5} | {res['em_dash']:<2} | "
            f"{res['dialogue_pct']:>4.0f}% | {res['end_quote_pct']:>4.0f}%  | "
            f"{res['long_quotes']:>6} | {res['aykb_quotes']:>4} | "
            f"{res['mean_sent']:>8.1f} | {res['mono_runs']:>4} | "
            f"{res['embodied']:>5} | {res['smell']:>3} | {res['pov1_pct']:>4.1f}%"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

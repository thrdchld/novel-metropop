#!/usr/bin/env python3
"""
Modul Inti Pemeriksaan Kaidah Prosa, Dialog, Pembuka Bab, & Judul — Novel MetroPop Indonesia.
Dipakai bersama oleh scripts/analyze-prose.py dan scripts/stress-test.py.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)?")
SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])(?:[”"\']*)\s+')
QUOTE_RE = re.compile(r'[“"]([^”"]+)[”"]')
PARA_END_QUOTE_RE = re.compile(r'[”"]\s*$')
MAX_QUOTE_WORDS = 20

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

CLINICAL_PATTERNS = [
    r"\btrauma\b",
    r"mekanisme pertahanan",
    r"hyper-independence",
    r"\bfatherless\b",
    r"\btoxic\b",
    r"\binsecure\b",
    r"\bhealing\b",
]

FILTER_WORDS = ("terasa", "tampak", "terlihat", "seolah-olah", "menyadari", "menyaksikan")

STOCK_TELLS = (
    "menghela napas",
    "mengembuskan napas",
    "mengepalkan tangan",
    "rahang mengeras",
    "menggigit bibir",
)

WRAPPER_PATTERNS = (
    r"\bsebuah perasaan\b",
    r"\bada rasa\b",
    r"\bkeputusannya untuk\b",
    r"\bkesadaran itu\b",
    r"\bkehadirannya\b",
)

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

AYKB_DIALOGUE_PATTERNS = [
    r"\b(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|beberapa)\s+(?:hari|minggu|bulan|tahun)\s+(?:yang\s+)?lalu\b",
    r"\b(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s+lalu\b",
    r"\bselama\s+(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan)\s+(?:hari|minggu|bulan|tahun)\b",
    r"\bsebagai\s+atasan\s+yang\s+sudah\b",
]

# Pembuka bab pasif (laporan cuaca/suasana/waktu) yang melanggar In Medias Res & Action Space
PASSIVE_OPENING_PATTERNS = [
    r"^(?:pagi|siang|sore|malam)\s+itu\b",
    r"^hari\s+(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s+(?:pagi|siang|sore|malam)\s+itu\b",
    r"^(?:matahari|mentari|cahaya\s+lampu|sinar\s+matahari)\s+memantul\b",
    r"^suasana\s+di\s+dalam\b",
    r"^waktu\s+sudah\s+menunjukkan\b",
]


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


def detect_similar_length_runs(
    sent_lengths: list[int], tolerance: int = 2, min_run: int = 3, min_words: int = 10
) -> list[tuple[int, int, list[int]]]:
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


def inspect_chapter_rules(path: Path, char_names: set[str] | None = None) -> dict:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    body = strip_markdown_headers(raw)
    all_words = get_words(body)
    word_count = len(all_words)
    paras = get_paragraphs(body)
    sents = get_sentences(body)
    sent_lengths = [len(get_words(s)) for s in sents if get_words(s)]
    counts = Counter(all_words)
    lower_body = body.lower()

    errors: dict[str, list[str]] = {
        "word_range": [],
        "plain_text": [],
        "title_rule": [],
        "in_medias_res": [],
        "long_quote": [],
        "aykb_quote": [],
        "mixed_negation": [],
        "filter_words": [],
        "stock_tells": [],
        "ai_syntax": [],
        "bookish_tags": [],
        "slop_clinical": [],
        "sensory_cap": [],
        "discourse_rhythm": [],
    }

    # 1. Word range (600-900 standar)
    if word_count < 600 or word_count > 900:
        errors["word_range"].append(f"Jumlah kata {word_count} (wajib 600-900 kata)")

    # 2. Plain text: 0 em dash, 0 markup (*, **, ~~, `), 0 quote pembuka di atas judul
    if "—" in raw:
        errors["plain_text"].append(f"Ditemukan karakter em dash (—): {raw.count('—')}x")
    if any(ch in body for ch in ("*", "`", "~")):
        errors["plain_text"].append("Ditemukan simbol markup (*, `, ~) di dalam tubuh teks bab")
    if lines and not lines[0].startswith("## Bab "):
        errors["plain_text"].append("Baris pertama bab bukan header '## Bab N: Judul'")

    # 3. Title rule: ## Bab N: Judul (<=5 kata, tanpa nama tokoh)
    if lines and lines[0].startswith("## Bab "):
        m_title = re.match(r"^##\s+Bab\s+(\d+)\s*:\s*(.+)$", lines[0])
        if not m_title:
            errors["title_rule"].append(f"Format judul bab tidak sesuai: '{lines[0]}'")
        else:
            title_text = m_title.group(2).strip()
            title_words = get_words(title_text)
            if len(title_words) > 5:
                errors["title_rule"].append(f"Judul bab terlalu panjang ({len(title_words)} kata > 5): '{title_text}'")
            if char_names:
                hit_names = [w for w in title_words if w in char_names]
                if hit_names:
                    errors["title_rule"].append(f"Judul bab mengandung nama tokoh ({hit_names}): '{title_text}'")

    # 4. In Medias Res & Action Space opening
    if paras:
        first_para = paras[0]
        if first_para.startswith(">"):
            errors["in_medias_res"].append("Dilarang memasang quote/epigraph di awal bab")
        for pat in PASSIVE_OPENING_PATTERNS:
            if re.search(pat, first_para.lower()):
                errors["in_medias_res"].append(f"Kalimat pertama bab pasif (bukan In Medias Res): '{first_para[:70]}...'")

    # 5-7. Kelisanan Dialog (<=20 kata per kutipan, 0 AYKB, 0 belang nggak+tidak)
    all_quotes = [m.group(1).strip() for p in paras for m in QUOTE_RE.finditer(p)]
    for q in all_quotes:
        qw = get_words(q)
        if len(qw) > MAX_QUOTE_WORDS:
            errors["long_quote"].append(f"Kutipan {len(qw)} kata (>{MAX_QUOTE_WORDS}): \"{q}\"")
        q_low = q.lower()
        for pat in AYKB_DIALOGUE_PATTERNS:
            m_aykb = re.search(pat, q_low)
            if m_aykb:
                errors["aykb_quote"].append(f"Eksposisi waktu '{m_aykb.group(0)}' di dialog: \"{q}\"")
                break
        if ("nggak" in qw or "enggak" in qw) and "tidak" in qw:
            errors["mixed_negation"].append(f"Campuran 'nggak' dan 'tidak' dalam satu kutipan: \"{q}\"")

    # 8. Filter words
    for fw in FILTER_WORDS:
        if counts[fw] > 0:
            errors["filter_words"].append(f"Kata filter persepsi '{fw}' ditemukan {counts[fw]}x")

    # 9. Stock tells
    for st in STOCK_TELLS:
        c_st = len(re.findall(re.escape(st), lower_body))
        if c_st > 0:
            errors["stock_tells"].append(f"Gerakan klise (stock tell) '{st}' ditemukan {c_st}x")

    # 10. AI Syntax ('Sambil...', ', membuat', wrapper nouns)
    leading_sambil = sum(1 for s in sents if s.lower().startswith("sambil "))
    if leading_sambil > 0:
        errors["ai_syntax"].append(f"Kalimat berawalan 'Sambil ...' ditemukan {leading_sambil}x")
    making_clause = len(re.findall(r",\s*membuat\s+", lower_body))
    if making_clause > 0:
        errors["ai_syntax"].append(f"Klausa partisip ', membuat ...' ditemukan {making_clause}x")
    for wp in WRAPPER_PATTERNS:
        m_wp = re.search(wp, lower_body)
        if m_wp:
            errors["ai_syntax"].append(f"Pembungkus abstrak/nominalisasi '{m_wp.group(0)}' ditemukan")

    # 11. Bookish tags
    for bt in BOOKISH_SPEECH_TAGS:
        if counts[bt] > 0:
            errors["bookish_tags"].append(f"Tag dialog buku pelajaran '{bt}' ditemukan {counts[bt]}x")

    # 12. AI Slop & Clinical jargon
    for pat in AI_SLOP_PATTERNS:
        if re.search(pat, lower_body):
            errors["slop_clinical"].append(f"Frasa AI slop ditemukan: '{pat}'")
    for pat in CLINICAL_PATTERNS:
        m_cl = re.search(pat, lower_body)
        if m_cl:
            errors["slop_clinical"].append(f"Jargon klinis/psikologi ditemukan: '{m_cl.group(0)}'")

    # 13. Sensory caps (embodied <=2, smell <=2)
    embodied_count = sum(len(re.findall(pat, lower_body)) for pat in EMBODIED_PATTERNS)
    smell_count = sum(counts[w] for w in SMELL_WORDS)
    if embodied_count > 2:
        errors["sensory_cap"].append(f"Sensasi anatomi tubuh berlebihan: {embodied_count}x (batas <=2)")
    if smell_count > 2:
        errors["sensory_cap"].append(f"Deskripsi bau/aroma berlebihan: {smell_count}x (batas <=2)")

    # 14. Discourse rhythm (EndQ% <=75%, Mono == 0)
    dialogue_paras_list = [p for p in paras if QUOTE_RE.search(p)]
    dialogue_paras = len(dialogue_paras_list)
    end_quote_paras = sum(1 for p in dialogue_paras_list if PARA_END_QUOTE_RE.search(p))
    end_quote_pct = (end_quote_paras / dialogue_paras * 100) if dialogue_paras else 0.0
    if dialogue_paras >= 4 and end_quote_pct > 75.0:
        errors["discourse_rhythm"].append(f"Kutipan di akhir paragraf terlalu tinggi: {end_quote_pct:.0f}% (batas <=75%)")

    mono_runs = detect_similar_length_runs(sent_lengths, tolerance=2, min_run=3)
    if mono_runs:
        errors["discourse_rhythm"].append(f"Ditemukan {len(mono_runs)} deret >=3 kalimat panjang seragam: {mono_runs}")

    return {
        "name": path.name,
        "words": word_count,
        "errors": errors,
    }

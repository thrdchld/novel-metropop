#!/usr/bin/env python3
"""
Modul Inti Pemeriksaan Kaidah Prosa, Dialog, Pembuka Bab, & Judul — Novel MetroPop Indonesia.
Dipakai bersama oleh scripts/analyze-prose.py dan scripts/stress-test.py.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

RULES_PATH = Path(__file__).resolve().parent / "rules.json"
RULES = json.loads(RULES_PATH.read_text(encoding="utf-8"))
P = RULES["params"]
PAT = RULES["patterns"]

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)?")
SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])(?:[”"\']*)\s+')
QUOTE_RE = re.compile(r'[“"]([^”"]+)[”"]')
PARA_END_QUOTE_RE = re.compile(r'[”"]\s*$')

MAX_QUOTE_WORDS = P["max_quote_words"]
AI_SLOP_PATTERNS = PAT["ai_slop"]
CLINICAL_PATTERNS = PAT["clinical"]
FILTER_WORDS = tuple(PAT["filter_words"])
STOCK_TELLS = tuple(PAT["stock_tells"])
WRAPPER_PATTERNS = tuple(PAT["wrapper_nouns"])
BOOKISH_SPEECH_TAGS = tuple(PAT["bookish_tags"])
EMBODIED_PATTERNS = PAT["embodied"]
SMELL_WORDS = tuple(PAT["smell_words"])
HUMAN_CAUSALS = tuple(PAT["human_causals"])
AYKB_DIALOGUE_PATTERNS = PAT["aykb_dialogue"]
PASSIVE_OPENING_PATTERNS = PAT["passive_opening"]


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
    sent_lengths: list[int], tolerance: int = P["mono_tolerance"], min_run: int = P["mono_min_run"], min_words: int = P["mono_min_words"]
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

    # 1. Word range (600-900 standar, darurat <=1200)
    word_max_limit = P.get("word_max_emergency", P["word_max"])
    if word_count < P["word_min"] or word_count > word_max_limit:
        errors["word_range"].append(f"Jumlah kata {word_count} (wajib {P['word_min']}-{word_max_limit} kata)")

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
            if len(title_words) > P["title_max_words"]:
                errors["title_rule"].append(f"Judul bab terlalu panjang ({len(title_words)} kata > {P['title_max_words']}): '{title_text}'")
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
    if embodied_count > P["embodied_max"]:
        errors["sensory_cap"].append(f"Sensasi anatomi tubuh berlebihan: {embodied_count}x (batas <=2)")
    if smell_count > P["smell_max"]:
        errors["sensory_cap"].append(f"Deskripsi bau/aroma berlebihan: {smell_count}x (batas <=2)")

    # 14. Discourse rhythm (EndQ% <=75%, Mono == 0)
    dialogue_paras_list = [p for p in paras if QUOTE_RE.search(p)]
    dialogue_paras = len(dialogue_paras_list)
    end_quote_paras = sum(1 for p in dialogue_paras_list if PARA_END_QUOTE_RE.search(p))
    end_quote_pct = (end_quote_paras / dialogue_paras * 100) if dialogue_paras else 0.0
    if dialogue_paras >= P["endq_min_dialogue_paras"] and end_quote_pct > P["endq_max_pct"]:
        errors["discourse_rhythm"].append(f"Kutipan di akhir paragraf terlalu tinggi: {end_quote_pct:.0f}% (batas <={P['endq_max_pct']}%)")

    mono_runs = detect_similar_length_runs(sent_lengths)
    if mono_runs:
        errors["discourse_rhythm"].append(f"Ditemukan {len(mono_runs)} deret >=3 kalimat panjang seragam: {mono_runs}")

    return {
        "name": path.name,
        "words": word_count,
        "errors": errors,
    }

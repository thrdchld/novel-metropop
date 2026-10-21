"""Analyze a reference manuscript (chapter lengths, hooks, dialogue ratio)."""

from __future__ import annotations

import json
import re
import statistics
from pathlib import Path
from typing import Any

from .text import word_count

CHAPTER_RE = re.compile(r"^Bab\s+(\d+)\s*[:\-—]\s*(.+)$", re.MULTILINE | re.IGNORECASE)
DIALOGUE_LINE_RE = re.compile(r"^\s*[\w .]{2,30}:\s+\S")
MIN_CHAPTER_WORDS = 100


def _split_chapters(text: str) -> list[dict[str, Any]]:
    matches = list(CHAPTER_RE.finditer(text))
    drafts: dict[int, dict[str, Any]] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        title = match.group(2).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end]
        words = word_count(body)
        candidate = {"number": number, "title": title, "body": body, "words": words}
        # Blueprint files repeat chapter numbers (outline + manuscript);
        # keep the longest version, which is the actual prose.
        if number not in drafts or words > drafts[number]["words"]:
            drafts[number] = candidate
    return [
        drafts[number]
        for number in sorted(drafts)
        if drafts[number]["words"] >= MIN_CHAPTER_WORDS
    ]


def _dialogue_ratio(body: str) -> float:
    paragraphs = [line.strip() for line in body.splitlines() if line.strip()]
    if not paragraphs:
        return 0.0
    dialogue = [
        line for line in paragraphs
        if '"' in line or '“' in line or DIALOGUE_LINE_RE.match(line)
    ]
    return round(len(dialogue) / len(paragraphs) * 100, 1)


def _hook(body: str) -> str:
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    return lines[-1] if lines else ""


def analyze(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    chapters = _split_chapters(text)
    word_counts = [chapter["words"] for chapter in chapters]
    total = sum(word_counts)
    average = round(statistics.mean(word_counts)) if word_counts else 0
    median = round(statistics.median(word_counts)) if word_counts else 0
    in_range = sum(1 for count in word_counts if 600 <= count <= 900)
    prose = "\n\n".join(chapter["body"] for chapter in chapters)
    dialogue = _dialogue_ratio(prose)

    for chapter in chapters:
        chapter["dialogue_percent"] = _dialogue_ratio(chapter["body"])
        chapter["hook"] = _hook(chapter["body"])

    return {
        "file": str(path),
        "chapters": len(chapters),
        "total_words": total,
        "average": average,
        "median": median,
        "min": min(word_counts) if word_counts else 0,
        "max": max(word_counts) if word_counts else 0,
        "in_range": in_range,
        "dialogue_percent": dialogue,
        "chapter_data": chapters,
    }


def render_report(result: dict[str, Any]) -> str:
    lines = [
        f"# Analisis Referensi — {Path(result['file']).name}",
        "",
        f"- Bab terdeteksi: **{result['chapters']}**",
        f"- Total kata: **{result['total_words']:,}**",
        f"- Rata-rata: **{result['average']:,}** kata (median {result['median']:,})",
        f"- Rentang: {result['min']:,}–{result['max']:,} kata",
        f"- Bab dalam rentang 600–900 kata: **{result['in_range']}/{result['chapters']}**",
        f"- Estimasi porsi paragraf dialog: **{result['dialogue_percent']}%**",
        "",
        "## Per Bab",
        "",
        "| Bab | Judul | Kata | Dialog | Hook |",
        "|---|---|---|---|---|",
    ]
    for chapter in result["chapter_data"]:
        hook = chapter["hook"].replace("|", "\\|")
        if len(hook) > 90:
            hook = hook[:89] + "…"
        lines.append(
            f"| {chapter['number']} | {chapter['title']} | {chapter['words']} | "
            f"{chapter['dialogue_percent']}% | {hook} |"
        )
    lines.extend([
        "",
        "## Catatan",
        "",
        "- Angka ini dipakai untuk mengkalibrasi target bab dan panjang hook.",
        "- Entri di bawah 100 kata (judul, kerangka, atau catatan) diabaikan.",
        "- Referensi dengan 600–900 kata per bab cocok untuk MetroPop web novel.",
        "- Porsi dialog di bawah 20% biasanya terasa seperti ringkasan, bukan adegan.",
    ])
    return "\n".join(lines) + "\n"


def result_json(result: dict[str, Any]) -> str:
    cleaned = dict(result)
    cleaned["chapter_data"] = [
        {key: value for key, value in chapter.items() if key != "body"}
        for chapter in result["chapter_data"]
    ]
    cleaned["hook_preview"] = [chapter["hook"][:120] for chapter in result["chapter_data"]]
    return json.dumps(cleaned, ensure_ascii=False, indent=2)

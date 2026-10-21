"""Validate a story folder against MetroPop constraints."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .render import chapter_filename, word_range
from .storage import chapter_path, load_story
from .text import split_frontmatter, word_count


def inspect_story(story_dir: Path) -> dict[str, Any]:
    story = load_story(story_dir)
    chapters = story.get("chapters", [])
    errors: list[str] = []
    warnings: list[str] = []
    rows: list[dict[str, Any]] = []
    seen_titles: dict[str, int] = {}

    if len(chapters) < 30:
        errors.append(f"Jumlah bab {len(chapters)}; MetroPop minimal 30 bab.")
    if len(chapters) != int(story.get("chapter_count", len(chapters))):
        errors.append("story.json: chapter_count tidak cocok dengan daftar chapters.")
    if not story.get("secret"):
        warnings.append("Rahasia utama kosong; konflik jangka panjang akan lemah.")
    if not story.get("glossary"):
        warnings.append("Glosarium kosong; istilah kerja akan sulit dijelaskan konsisten.")

    for chapter in chapters:
        number = int(chapter["number"])
        title = chapter.get("title", "")
        path = chapter_path(story_dir, number)
        row: dict[str, Any] = {
            "number": number,
            "title": title,
            "phase": chapter.get("phase", ""),
            "phase_label": chapter.get("phase_label", ""),
            "status": "missing",
            "words": 0,
            "target": int(chapter.get("target_words", story.get("target_words", 750))),
            "file": str(path.relative_to(story_dir)),
            "issues": [],
        }

        if title in seen_titles:
            errors.append(f"Judul bab duplikat: '{title}' (bab {seen_titles[title]} dan {number}).")
        seen_titles[title] = number

        if not chapter.get("hook"):
            errors.append(f"Bab {number}: hook kosong.")
        if not chapter.get("scene"):
            warnings.append(f"Bab {number}: adegan kosong.")

        if not path.exists():
            errors.append(f"Bab {number}: file {chapter_filename(number)} tidak ada.")
            rows.append(row)
            continue

        text = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        status = meta.get("status", "todo")
        words = word_count(body)
        row["status"] = status
        row["words"] = words

        if status not in {"todo", "draft", "done"}:
            warnings.append(f"Bab {number}: status tidak dikenal '{status}'.")
        if meta.get("judul") and meta["judul"].strip('"') != title:
            warnings.append(f"Bab {number}: judul di frontmatter berbeda dari outline.")
        if meta.get("target_kata") and str(meta["target_kata"]) != str(row["target"]):
            warnings.append(f"Bab {number}: target_kata di frontmatter berbeda dari outline.")

        if status == "todo":
            warnings.append(f"Bab {number}: belum ditulis.")
        elif status == "draft":
            if words == 0:
                warnings.append(f"Bab {number}: berstatus draft tetapi belum ada isi.")
            else:
                warnings.append(f"Bab {number}: masih draft ({words} kata).")
        elif status == "done":
            if words == 0:
                errors.append(f"Bab {number}: berstatus done tetapi kosong.")
            else:
                low, high = word_range(row["target"])
                if words < low:
                    warnings.append(f"Bab {number}: {words} kata, di bawah rentang {low}–{high}.")
                elif words > high:
                    warnings.append(f"Bab {number}: {words} kata, di atas rentang {low}–{high}.")

        rows.append(row)

    done = sum(1 for row in rows if row["status"] == "done")
    written = sum(1 for row in rows if row["status"] in {"draft", "done"})
    total_words = sum(row["words"] for row in rows)
    done_words = [row["words"] for row in rows if row["status"] == "done"]
    average = round(sum(done_words) / len(done_words)) if done_words else 0
    percent = round(done / len(rows) * 100) if rows else 0

    return {
        "story": story,
        "story_dir": story_dir,
        "rows": rows,
        "errors": errors,
        "warnings": warnings,
        "done": done,
        "written": written,
        "percent": percent,
        "total_words": total_words,
        "average": average,
    }

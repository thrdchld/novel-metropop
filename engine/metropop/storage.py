"""Filesystem layout for stories."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .render import chapter_filename, render_bible, render_chapter_skeleton, render_outline
from .text import folder_name

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_STORY_ROOT = REPO_ROOT / "story"
STORY_FILE = "story.json"


def story_folder(root: Path, title: str) -> Path:
    return root / folder_name(title)


def chapter_path(story_dir: Path, number: int) -> Path:
    return story_dir / "chapters" / chapter_filename(number)


def save_rendered(story: dict[str, Any], story_dir: Path) -> None:
    story_dir.mkdir(parents=True, exist_ok=True)
    (story_dir / "bible.md").write_text(render_bible(story), encoding="utf-8")
    (story_dir / "outline.md").write_text(render_outline(story), encoding="utf-8")


def save_story(story: dict[str, Any], story_dir: Path, skeleton: bool = True) -> None:
    story_dir.mkdir(parents=True, exist_ok=True)
    chapters_dir = story_dir / "chapters"
    chapters_dir.mkdir(exist_ok=True)

    (story_dir / STORY_FILE).write_text(
        json.dumps(story, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    save_rendered(story, story_dir)

    if skeleton:
        for chapter in story["chapters"]:
            path = chapter_path(story_dir, chapter["number"])
            if not path.exists():
                path.write_text(render_chapter_skeleton(story, chapter), encoding="utf-8")


def load_story(story_dir: Path) -> dict[str, Any]:
    path = story_dir / STORY_FILE if story_dir.is_dir() else story_dir
    return json.loads(path.read_text(encoding="utf-8"))


def iter_stories(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    found = [path for path in root.iterdir() if path.is_dir() and (path / STORY_FILE).is_file()]
    return sorted(found, key=lambda path: path.name.lower())


def resolve_story(path: str | Path | None, root: Path) -> Path:
    if path:
        candidate = Path(path).expanduser()
        if candidate.is_file() and candidate.name == STORY_FILE:
            candidate = candidate.parent
        if (candidate / STORY_FILE).is_file():
            return candidate.resolve()
        alternative = root / str(path)
        if (alternative / STORY_FILE).is_file():
            return alternative.resolve()
        raise FileNotFoundError(f"Cerita tidak ditemukan: {path}")

    cwd = Path.cwd()
    if (cwd / STORY_FILE).is_file():
        return cwd

    stories = iter_stories(root)
    if len(stories) == 1:
        return stories[0]
    if not stories:
        raise FileNotFoundError(f"Belum ada cerita di {root}. Buat dengan: metropop new \"Judul\"")
    names = ", ".join(story.name for story in stories)
    raise FileNotFoundError(f"Ada beberapa cerita ({names}). Tentukan dengan --story.")


def read_chapter(story_dir: Path, number: int) -> str:
    path = chapter_path(story_dir, number)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def previous_written_chapter(story_dir: Path, number: int) -> str:
    for candidate in range(number - 1, 0, -1):
        from .text import split_frontmatter, word_count

        text = read_chapter(story_dir, candidate)
        if not text:
            continue
        _, body = split_frontmatter(text)
        if word_count(body) > 0:
            return text
    return ""


def status_counts(story_dir: Path, story: dict[str, Any]) -> tuple[int, int]:
    from .text import split_frontmatter

    done = 0
    written = 0
    for chapter in story["chapters"]:
        text = read_chapter(story_dir, chapter["number"])
        meta, _ = split_frontmatter(text)
        if meta.get("status", "todo") == "done":
            done += 1
        if meta.get("status", "todo") != "todo":
            written += 1
    return done, written


def story_summaries(root: Path) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for story_dir in iter_stories(root):
        try:
            story = load_story(story_dir)
        except (json.JSONDecodeError, OSError):
            continue
        done, written = status_counts(story_dir, story)
        summaries.append({
            "dir": story_dir,
            "title": story.get("title", story_dir.name),
            "chapters": story.get("chapter_count", len(story.get("chapters", []))),
            "done": done,
            "written": written,
            "seed": story.get("seed", "-"),
            "engine": story.get("engine_label", story.get("engine", "-")),
        })
    return summaries

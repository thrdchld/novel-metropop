"""Text helpers: frontmatter, word counting, slugs."""

from __future__ import annotations

import re

FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*\n?", re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
HEADING_RE = re.compile(r"^[ \t]{0,3}#{1,6}[ \t]+.*$", re.MULTILINE)
RULE_RE = re.compile(r"^[ \t]*([-*_])(?:[ \t]*\1){2,}[ \t]*$", re.MULTILINE)
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
MARKUP_RE = re.compile(r"[*_`~>#|]+")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, text[match.end():]


def clean_prose(text: str) -> str:
    """Remove markdown scaffolding that should not count as prose."""
    text = COMMENT_RE.sub(" ", text)
    text = IMAGE_RE.sub(" ", text)
    text = LINK_RE.sub(r"\1", text)
    text = HEADING_RE.sub(" ", text)
    text = RULE_RE.sub(" ", text)
    text = MARKUP_RE.sub(" ", text)
    return text


def word_count(text: str) -> int:
    cleaned = clean_prose(text)
    return len([token for token in cleaned.split() if any(ch.isalnum() for ch in token)])


def slugify(text: str) -> str:
    lowered = text.lower().strip()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-") or "tanpa-judul"


def folder_name(title: str) -> str:
    """Keep the title readable, only remove characters that break paths."""
    name = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "-", title).strip()
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name or "Tanpa Judul"


def first_sentences(text: str, count: int = 1) -> str:
    cleaned = " ".join(clean_prose(text).split())
    if not cleaned:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", cleaned)
    return " ".join(parts[:count]).strip()


def tail_words(text: str, count: int = 120) -> str:
    cleaned = " ".join(clean_prose(text).split())
    words = cleaned.split()
    return " ".join(words[-count:])


def truncate(text: str, width: int = 90) -> str:
    text = " ".join(text.split())
    if len(text) <= width:
        return text
    return text[: max(0, width - 1)].rstrip() + "…"

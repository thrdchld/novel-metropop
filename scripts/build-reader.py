#!/usr/bin/env python3
"""
scripts/build-reader.py
Membangun web app pembaca novel mandiri (Single-File Offline Ebook Reader & Story Catalog)
ke file reader.html di root repositori.
"""

import os
import glob
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STORY_DIR = REPO_ROOT / "story"
OUTPUT_FILE = REPO_ROOT / "reader.html"


def parse_story(folder: Path) -> dict:
    canon_file = folder / "canon.md"
    title = folder.name
    blurb = ""
    logline = ""
    genre = "Web Novel MetroPop"
    target_audience = "13+"
    pov = "Orang Pertama (POV 1)"
    latar = "Jakarta"
    tema = ""
    pertanyaan = ""
    characters = []
    address_matrix = []

    if canon_file.is_file():
        c_text = canon_file.read_text(encoding="utf-8")

        def get_field(pat):
            m = re.search(pat, c_text, re.S)
            return m.group(1).strip() if m else ""

        blurb = get_field(r"-\s+\*\*?Blurb:\*\*?\s*(.*?)(?=\n-|\n##|$)")
        logline = get_field(r"-\s+\*\*?Logline:\*\*?\s*(.*?)(?=\n-|\n##|$)")
        genre = get_field(r"-\s+\*\*?Genre:\*\*?\s*(.*?)(?=\n-|\n##|$)") or genre
        pov = get_field(r"-\s+\*\*?POV:\*\*?\s*(.*?)(?=\n-|\n##|$)") or pov
        tema = get_field(r"-\s+\*\*?Tema:\*\*?\s*(.*?)(?=\n-|\n##|$)")
        latar = get_field(r"-\s+\*\*?Latar:\*\*?\s*(.*?)(?=\n-|\n##|$)") or latar
        pertanyaan = get_field(r"-\s+\*\*?Pertanyaan Dramatik:\*\*?\s*(.*?)(?=\n-|\n##|$)")

        cast_m = re.search(r"##\s+Cast\s*\n\s*\|.*?\n\|[-| :]+\n(.*?)(?=\n##|\Z)", c_text, re.S)
        if cast_m:
            rows = [r.strip() for r in cast_m.group(1).strip().splitlines() if r.strip().startswith("|")]
            for r in rows:
                cols = [c.strip() for c in r.strip("|").split("|")]
                if len(cols) >= 5:
                    characters.append({
                        "name": cols[0],
                        "role": cols[1],
                        "age": cols[2],
                        "job": cols[3],
                        "desc": cols[4],
                    })

        addr_m = re.search(r"##\s+Matriks Sapaan.*?\n\s*\|.*?\n\|[-| :]+\n(.*?)(?=\n##|\Z)", c_text, re.S)
        if addr_m:
            rows = [r.strip() for r in addr_m.group(1).strip().splitlines() if r.strip().startswith("|")]
            for r in rows:
                cols = [c.strip() for c in r.strip("|").split("|")]
                if len(cols) >= 5:
                    address_matrix.append({
                        "speakers": cols[0].replace("**", "").replace("*", ""),
                        "pov_call": cols[1].replace("`", ""),
                        "formal": cols[2].replace("`", ""),
                        "close": cols[3].replace("`", ""),
                        "conflict": cols[4].replace("`", ""),
                    })

    chapters_dir = folder / "chapters"
    chap_files = sorted(chapters_dir.glob("bab-*.md"))
    chapters = []
    total_words = 0
    for cf in chap_files:
        m = re.search(r"bab-(\d+)", cf.name)
        num = int(m.group(1)) if m else len(chapters) + 1
        raw = cf.read_text(encoding="utf-8")
        lines = raw.strip().splitlines()
        c_title = f"Bab {num}"
        body_lines = []
        for l in lines:
            if l.startswith("## Bab"):
                c_title = l.replace("##", "").strip()
            else:
                body_lines.append(l)
        body = "\n".join(body_lines).strip()
        words = len(re.findall(r"\w+", body))
        total_words += words
        chapters.append({
            "number": num,
            "title": c_title,
            "wordCount": words,
            "readTimeMin": max(1, round(words / 220)),
            "content": body,
        })

    return {
        "id": re.sub(r"[^a-z0-9]+", "-", folder.name.lower()).strip("-"),
        "title": title,
        "genre": genre,
        "status": f"Tamat ({len(chapters)} Bab)",
        "blurb": blurb,
        "logline": logline,
        "pov": pov,
        "tema": tema,
        "latar": latar,
        "pertanyaan": pertanyaan,
        "characters": characters,
        "addressMatrix": address_matrix,
        "totalWords": total_words,
        "totalReadTimeMin": max(1, round(total_words / 220)),
        "chapterCount": len(chapters),
        "chapters": chapters,
    }


def generate_html(stories: list) -> str:
    data_json = json.dumps(stories, ensure_ascii=False, indent=2)

    return f"""<!DOCTYPE html>
<html lang="id" data-theme="sepia" data-font="serif" data-size="19" data-width="normal" data-spacing="normal">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>MetroPop Reader - Katalog & Pembaca Novel</title>
  <meta name="description" content="Aplikasi web pembaca novel mandiri (offline-first) untuk katalog cerita MetroPop Indonesia.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>">
  <style>
    /* CSS Variables & Theme Palettes */
    :root {{
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --font-serif: Georgia, Cambria, "Times New Roman", Times, serif;
      --font-current: var(--font-serif);
      --font-size-base: 19px;
      --line-height-base: 1.8;
      --max-width-content: 740px;
      --transition-smooth: 0.2s ease;
    }}

    /* Light Theme */
    :root[data-theme="light"] {{
      --bg-canvas: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #ffffff;
      --bg-muted: #f1f5f9;
      --border-color: #e2e8f0;
      --border-subtle: #edf2f7;
      --text-main: #0f172a;
      --text-secondary: #475569;
      --text-muted: #64748b;
      --accent-color: #0284c7;
      --accent-hover: #0369a1;
      --accent-subtle: #e0f2fe;
      --accent-contrast: #ffffff;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 14px rgba(0,0,0,0.08);
      --shadow-lg: 0 10px 25px rgba(0,0,0,0.12);
      --chat-bubble-bg: #e2e8f0;
      --chat-bubble-text: #0f172a;
    }}

    /* Sepia Theme (Warm Paper, Easy on Eyes) */
    :root[data-theme="sepia"] {{
      --bg-canvas: #f6f1e5;
      --bg-surface: #fdfaf2;
      --bg-surface-elevated: #ffffff;
      --bg-muted: #ece3cf;
      --border-color: #e2d5be;
      --border-subtle: #eee6d6;
      --text-main: #2c241c;
      --text-secondary: #5c4d40;
      --text-muted: #827263;
      --accent-color: #a14e1a;
      --accent-hover: #7f3b11;
      --accent-subtle: #fbeee4;
      --accent-contrast: #ffffff;
      --shadow-sm: 0 1px 3px rgba(70,50,30,0.08);
      --shadow-md: 0 4px 14px rgba(70,50,30,0.1);
      --shadow-lg: 0 10px 25px rgba(70,50,30,0.15);
      --chat-bubble-bg: #ebdcc5;
      --chat-bubble-text: #2c241c;
    }}

    /* Dark Theme (OLED Friendly) */
    :root[data-theme="dark"] {{
      --bg-canvas: #0b0c0e;
      --bg-surface: #14161a;
      --bg-surface-elevated: #1e2228;
      --bg-muted: #242931;
      --border-color: #2b313b;
      --border-subtle: #1f232a;
      --text-main: #f1f5f9;
      --text-secondary: #cbd5e1;
      --text-muted: #94a3b8;
      --accent-color: #38bdf8;
      --accent-hover: #7dd3fc;
      --accent-subtle: #082f49;
      --accent-contrast: #0b0c0e;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.5);
      --shadow-md: 0 4px 14px rgba(0,0,0,0.6);
      --shadow-lg: 0 10px 25px rgba(0,0,0,0.8);
      --chat-bubble-bg: #272c35;
      --chat-bubble-text: #f1f5f9;
    }}

    /* Font Settings */
    :root[data-font="sans"] {{ --font-current: var(--font-sans); }}
    :root[data-font="serif"] {{ --font-current: var(--font-serif); }}

    :root[data-size="15"] {{ --font-size-base: 15px; }}
    :root[data-size="17"] {{ --font-size-base: 17px; }}
    :root[data-size="19"] {{ --font-size-base: 19px; }}
    :root[data-size="21"] {{ --font-size-base: 21px; }}
    :root[data-size="23"] {{ --font-size-base: 23px; }}
    :root[data-size="25"] {{ --font-size-base: 25px; }}

    :root[data-spacing="compact"] {{ --line-height-base: 1.6; }}
    :root[data-spacing="normal"] {{ --line-height-base: 1.8; }}
    :root[data-spacing="relaxed"] {{ --line-height-base: 2.05; }}

    :root[data-width="narrow"] {{ --max-width-content: 640px; }}
    :root[data-width="normal"] {{ --max-width-content: 740px; }}
    :root[data-width="wide"] {{ --max-width-content: 860px; }}

    /* Base Reset */
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.5;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
      transition: background-color var(--transition-smooth), color var(--transition-smooth);
    }}

    button, input, select {{
      font-family: inherit;
      color: inherit;
    }}

    /* Top Reading Progress Bar */
    #reading-progress-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: var(--accent-color);
      z-index: 1000;
      transition: width 0.1s ease-out;
    }}

    /* Header Nav */
    header.app-header {{
      position: sticky;
      top: 0;
      left: 0;
      right: 0;
      height: 60px;
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      z-index: 500;
      transition: transform 0.25s ease, background-color var(--transition-smooth);
    }}

    .zen-mode header.app-header {{
      transform: translateY(-100%);
    }}

    .header-left, .header-right {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .header-center {{
      flex: 1;
      text-align: center;
      padding: 0 8px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-main);
      cursor: pointer;
    }}

    .header-center small {{
      display: block;
      font-size: 0.75rem;
      font-weight: 400;
      color: var(--text-muted);
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .icon-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 8px;
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .icon-btn:hover {{
      background: var(--bg-muted);
      color: var(--text-main);
    }}

    .icon-btn:active {{
      transform: scale(0.95);
    }}

    .icon-btn svg {{
      width: 20px;
      height: 20px;
      fill: none;
      stroke: currentColor;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }}

    .btn-text {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-main);
    }}

    .btn-text:hover {{
      background: var(--bg-muted);
    }}

    .btn-primary {{
      background: var(--accent-color);
      color: var(--accent-contrast);
      border-color: var(--accent-color);
    }}

    .btn-primary:hover {{
      background: var(--accent-hover);
      border-color: var(--accent-hover);
    }}

    /* Main Container Views */
    main.app-main {{
      min-height: calc(100vh - 60px);
      padding: 24px 16px 80px;
    }}

    .view-hidden {{
      display: none !important;
    }}

    /* CATALOG VIEW */
    .catalog-container {{
      max-width: 900px;
      margin: 0 auto;
    }}

    .catalog-hero {{
      text-align: center;
      margin-bottom: 32px;
      padding: 24px 16px;
      border-bottom: 1px solid var(--border-color);
    }}

    .catalog-hero h1 {{
      font-size: 1.85rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
    }}

    .catalog-hero p {{
      color: var(--text-secondary);
      font-size: 1rem;
      max-width: 580px;
      margin: 0 auto;
    }}

    .story-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow var(--transition-smooth), transform var(--transition-smooth);
    }}

    .story-card:hover {{
      box-shadow: var(--shadow-md);
    }}

    .story-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }}

    .story-title {{
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .badge-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }}

    .badge {{
      display: inline-block;
      padding: 3px 9px;
      font-size: 0.75rem;
      font-weight: 600;
      border-radius: 6px;
      background: var(--bg-muted);
      color: var(--text-secondary);
      border: 1px solid var(--border-color);
    }}

    .badge-accent {{
      background: var(--accent-subtle);
      color: var(--accent-color);
      border-color: transparent;
    }}

    .story-blurb {{
      font-size: 0.95rem;
      color: var(--text-secondary);
      line-height: 1.65;
      margin: 14px 0 18px;
      background: var(--bg-muted);
      padding: 14px 18px;
      border-radius: 10px;
      border-left: 4px solid var(--accent-color);
    }}

    .progress-box {{
      margin: 16px 0;
      padding: 10px 14px;
      background: var(--bg-canvas);
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }}

    .progress-meta {{
      display: flex;
      justify-content: space-between;
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}

    .progress-bar-bg {{
      height: 6px;
      background: var(--border-color);
      border-radius: 3px;
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: var(--accent-color);
      border-radius: 3px;
      width: 0%;
      transition: width 0.3s ease;
    }}

    .story-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }}

    /* READER VIEW */
    .reader-container {{
      max-width: var(--max-width-content);
      margin: 0 auto;
      padding: 0 8px;
      font-family: var(--font-current);
      transition: max-width var(--transition-smooth);
    }}

    .chapter-heading-area {{
      text-align: center;
      margin-bottom: 36px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border-color);
    }}

    .chapter-novel-label {{
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 600;
      color: var(--accent-color);
      margin-bottom: 6px;
      font-family: var(--font-sans);
    }}

    .chapter-main-title {{
      font-size: 1.75rem;
      font-weight: 700;
      line-height: 1.35;
      color: var(--text-main);
      margin-bottom: 8px;
    }}

    .chapter-meta-line {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-family: var(--font-sans);
    }}

    .prose-body {{
      font-size: var(--font-size-base);
      line-height: var(--line-height-base);
      color: var(--text-main);
      word-break: break-word;
    }}

    .prose-body p {{
      margin-bottom: 1.35em;
      text-align: justify;
      hyphens: auto;
    }}

    @media (max-width: 640px) {{
      .prose-body p {{
        text-align: left;
      }}
    }}

    /* Chat bubble highlight */
    .chat-msg {{
      background: var(--chat-bubble-bg);
      color: var(--chat-bubble-text);
      padding: 10px 16px;
      border-radius: 10px;
      margin: 14px 0;
      font-family: var(--font-sans);
      font-size: calc(var(--font-size-base) * 0.92);
      line-height: 1.5;
      border-left: 3px solid var(--accent-color);
    }}

    .chat-sender {{
      font-weight: 700;
      color: var(--accent-color);
      margin-bottom: 2px;
      display: block;
    }}

    /* Search Highlights */
    mark.search-hit {{
      background-color: #fef08a;
      color: #713f12;
      padding: 0 2px;
      border-radius: 2px;
    }}

    :root[data-theme="dark"] mark.search-hit {{
      background-color: #854d0e;
      color: #fef08a;
    }}

    /* Reader Bottom Navigation */
    .reader-footer {{
      margin-top: 48px;
      padding-top: 28px;
      border-top: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 16px;
      align-items: center;
      font-family: var(--font-sans);
    }}

    .nav-buttons-row {{
      display: flex;
      width: 100%;
      justify-content: space-between;
      gap: 10px;
    }}

    .nav-buttons-row button {{
      flex: 1;
      max-width: 220px;
    }}

    .reader-actions-row {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      justify-content: center;
    }}

    /* Floating Zen Action */
    .floating-zen-btn {{
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 50%;
      width: 48px;
      height: 48px;
      display: none;
      align-items: center;
      justify-content: center;
      box-shadow: var(--shadow-md);
      z-index: 600;
      cursor: pointer;
    }}

    .zen-mode .floating-zen-btn {{
      display: flex;
    }}

    /* Search Bar In-Reader */
    #search-toolbar {{
      position: sticky;
      top: 60px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 8px 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 450;
      box-shadow: var(--shadow-sm);
    }}

    #search-input {{
      flex: 1;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: var(--bg-muted);
      color: var(--text-main);
      font-size: 0.9rem;
    }}

    #search-input:focus {{
      outline: 2px solid var(--accent-color);
      background: var(--bg-surface);
    }}

    .search-counter {{
      font-size: 0.8rem;
      color: var(--text-muted);
      white-space: nowrap;
    }}

    /* MODAL & DRAWER STYLES */
    .modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(2px);
      z-index: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
    }}

    .modal-backdrop.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-box {{
      background: var(--bg-surface);
      border-radius: 14px;
      width: 100%;
      max-width: 580px;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      transform: scale(0.96);
      transition: transform 0.2s ease;
    }}

    .modal-backdrop.active .modal-box {{
      transform: scale(1);
    }}

    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-color);
    }}

    .modal-header h3 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .modal-body {{
      padding: 20px;
      overflow-y: auto;
    }}

    /* TOC Drawer Specific */
    .toc-drawer {{
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      width: 320px;
      max-width: 85vw;
      background: var(--bg-surface);
      border-right: 1px solid var(--border-color);
      z-index: 900;
      transform: translateX(-100%);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-lg);
    }}

    .toc-drawer.open {{
      transform: translateX(0);
    }}

    .toc-header {{
      padding: 16px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .toc-search-box {{
      padding: 10px 16px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .toc-search-box input {{
      width: 100%;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: var(--bg-muted);
      font-size: 0.85rem;
    }}

    .toc-list {{
      flex: 1;
      overflow-y: auto;
      padding: 8px 0;
      list-style: none;
    }}

    .toc-item {{
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      border-left: 3px solid transparent;
      transition: background 0.15s ease;
      font-size: 0.9rem;
    }}

    .toc-item:hover {{
      background: var(--bg-muted);
    }}

    .toc-item.active {{
      border-left-color: var(--accent-color);
      background: var(--accent-subtle);
      color: var(--accent-color);
      font-weight: 600;
    }}

    .toc-item-title {{
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      padding-right: 8px;
    }}

    .toc-item-words {{
      font-size: 0.75rem;
      color: var(--text-muted);
      white-space: nowrap;
    }}

    /* Appearance Settings Grid */
    .setting-section {{
      margin-bottom: 20px;
    }}

    .setting-section:last-child {{
      margin-bottom: 0;
    }}

    .setting-label {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-secondary);
      margin-bottom: 8px;
      display: block;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .setting-btn-group {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
      gap: 8px;
    }}

    .setting-btn {{
      padding: 8px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-muted);
      color: var(--text-main);
      font-size: 0.9rem;
      font-weight: 500;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s ease;
    }}

    .setting-btn.active {{
      border-color: var(--accent-color);
      background: var(--accent-subtle);
      color: var(--accent-color);
      font-weight: 600;
    }}

    .font-size-control {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-muted);
      border-radius: 8px;
      border: 1px solid var(--border-color);
      padding: 4px;
    }}

    .font-size-btn {{
      width: 44px;
      height: 38px;
      border: none;
      background: transparent;
      font-weight: 700;
      cursor: pointer;
      border-radius: 6px;
      color: var(--text-main);
    }}

    .font-size-btn:hover {{
      background: var(--bg-surface);
    }}

    .font-size-display {{
      font-weight: 600;
      font-size: 0.95rem;
    }}

    /* Info / Canon Tabs */
    .tabs-nav {{
      display: flex;
      border-bottom: 1px solid var(--border-color);
      gap: 4px;
      margin-bottom: 16px;
    }}

    .tab-btn {{
      padding: 8px 14px;
      border: none;
      background: transparent;
      border-bottom: 2px solid transparent;
      color: var(--text-secondary);
      font-size: 0.9rem;
      font-weight: 500;
      cursor: pointer;
    }}

    .tab-btn.active {{
      color: var(--accent-color);
      border-bottom-color: var(--accent-color);
      font-weight: 600;
    }}

    .tab-content {{
      display: none;
    }}

    .tab-content.active {{
      display: block;
    }}

    /* Table styles for Canon */
    .canon-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin-top: 10px;
    }}

    .canon-table th, .canon-table td {{
      padding: 8px 10px;
      border: 1px solid var(--border-color);
      text-align: left;
    }}

    .canon-table th {{
      background: var(--bg-muted);
      font-weight: 600;
    }}

    .canon-dl dt {{
      font-weight: 700;
      color: var(--accent-color);
      margin-top: 12px;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .canon-dl dd {{
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.6;
      margin-bottom: 8px;
    }}

    /* Toast Notification */
    #toast-msg {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: var(--text-main);
      color: var(--bg-canvas);
      padding: 10px 20px;
      border-radius: 30px;
      font-size: 0.9rem;
      font-weight: 500;
      box-shadow: var(--shadow-lg);
      z-index: 1000;
      opacity: 0;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }}

    #toast-msg.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>

  <!-- Top Scroll Progress Bar -->
  <div id="reading-progress-bar"></div>

  <!-- Main Navigation Header -->
  <header class="app-header" id="app-header">
    <div class="header-left">
      <button class="btn-text" id="btn-back-catalog" style="display: none;" onclick="showCatalogView()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg>
        <span>Katalog</span>
      </button>
      <div id="brand-area" style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.35rem;">📚</span>
        <strong style="font-size: 1.05rem; letter-spacing: -0.3px;">MetroPop Reader</strong>
      </div>
    </div>

    <div class="header-center" id="header-center-info" onclick="openTocDrawer()">
      <span id="header-novel-title">-</span>
      <small id="header-chapter-title">-</small>
    </div>

    <div class="header-right">
      <button class="icon-btn" id="btn-search-toggle" title="Cari di Bab Ini" onclick="toggleSearchBar()" style="display: none;">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      </button>
      <button class="icon-btn" id="btn-toc-toggle" title="Daftar Bab" onclick="openTocDrawer()" style="display: none;">
        <svg viewBox="0 0 24 24"><line x1="8" x2="21" y1="6" y2="6"/><line x1="8" x2="21" y1="12" y2="12"/><line x1="8" x2="21" y1="18" y2="18"/><line x1="3" x2="3.01" y1="6" y2="6"/><line x1="3" x2="3.01" y1="12" y2="12"/><line x1="3" x2="3.01" y1="18" y2="18"/></svg>
      </button>
      <button class="icon-btn" id="btn-settings-toggle" title="Pengaturan Tampilan" onclick="openSettingsModal()">
        <svg viewBox="0 0 24 24"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="3"/><path d="m4.9 4.9 14.2 14.2M19.1 4.9 4.9 19.1"/></svg>
      </button>
      <button class="icon-btn" id="btn-zen-toggle" title="Mode Zen / Layar Penuh" onclick="toggleZenMode()" style="display: none;">
        <svg viewBox="0 0 24 24"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
      </button>
    </div>
  </header>

  <!-- In-Reader Search Toolbar -->
  <div id="search-toolbar" style="display: none;">
    <input type="text" id="search-input" placeholder="Ketik kata yang dicari di bab ini..." oninput="handleSearch(this.value)">
    <span class="search-counter" id="search-count">0 hasil</span>
    <button class="icon-btn" title="Hasil Sebelumnya" onclick="navigateSearch(-1)">
      <svg viewBox="0 0 24 24"><path d="m18 15-6-6-6 6"/></svg>
    </button>
    <button class="icon-btn" title="Hasil Berikutnya" onclick="navigateSearch(1)">
      <svg viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>
    </button>
    <button class="icon-btn" title="Tutup Pencarian" onclick="closeSearchBar()">
      <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg>
    </button>
  </div>

  <!-- Main Viewports -->
  <main class="app-main">

    <!-- CATALOG VIEW -->
    <section id="catalog-view" class="catalog-container">
      <div class="catalog-hero">
        <h1>Katalog Novel MetroPop</h1>
        <p>Koleksi web novel perkotaan Indonesia: dialog santai membumi, struktur plot teruji, kontinuitas ketat, 0 em dash, dan teks polos bebas markup.</p>
      </div>

      <div id="stories-grid">
        <!-- Rendered via JS -->
      </div>
    </section>

    <!-- READER VIEW -->
    <section id="reader-view" class="reader-container view-hidden">
      <div class="chapter-heading-area">
        <div class="chapter-novel-label" id="reader-novel-title">-</div>
        <h2 class="chapter-main-title" id="reader-chapter-title">-</h2>
        <div class="chapter-meta-line" id="reader-chapter-meta">-</div>
      </div>

      <article class="prose-body" id="reader-content-body">
        <!-- Chapter text rendered here -->
      </article>

      <!-- Reader Footer Nav -->
      <footer class="reader-footer">
        <div class="nav-buttons-row">
          <button class="btn-text" id="btn-prev-chapter" onclick="stepChapter(-1)">
            ← Bab Sebelumnya
          </button>
          <button class="btn-text" id="btn-toc-footer" onclick="openTocDrawer()">
            Daftar Bab
          </button>
          <button class="btn-text btn-primary" id="btn-next-chapter" onclick="stepChapter(1)">
            Bab Selanjutnya →
          </button>
        </div>

        <div class="reader-actions-row">
          <button class="btn-text" onclick="copyCurrentChapter()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
            <span>Salin Teks Bab Ini</span>
          </button>
          <button class="btn-text" onclick="openCanonModal()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
            <span>Info Cerita & Karakter</span>
          </button>
        </div>
      </footer>
    </section>

  </main>

  <!-- Floating Zen Exit Button -->
  <button class="floating-zen-btn" title="Keluar Mode Zen" onclick="toggleZenMode()">
    <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" fill="none" stroke-width="2"><path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/></svg>
  </button>

  <!-- TABLE OF CONTENTS DRAWER -->
  <div class="modal-backdrop" id="toc-backdrop" onclick="closeTocDrawer()"></div>
  <aside class="toc-drawer" id="toc-drawer">
    <div class="toc-header">
      <h3 style="font-size: 1.1rem; font-weight: 700;">Daftar Bab</h3>
      <button class="icon-btn" onclick="closeTocDrawer()">
        <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg>
      </button>
    </div>
    <div class="toc-search-box">
      <input type="text" id="toc-search-input" placeholder="Cari judul bab..." oninput="filterToc(this.value)">
    </div>
    <ul class="toc-list" id="toc-list">
      <!-- Injected by JS -->
    </ul>
  </aside>

  <!-- SETTINGS MODAL -->
  <div class="modal-backdrop" id="settings-backdrop" onclick="closeSettingsModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3>Pengaturan Tampilan</h3>
        <button class="icon-btn" onclick="closeSettingsModal()">
          <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg>
        </button>
      </div>
      <div class="modal-body">
        <!-- Tema Warna -->
        <div class="setting-section">
          <label class="setting-label">Tema Warna</label>
          <div class="setting-btn-group">
            <button class="setting-btn" data-theme="sepia" onclick="setTheme('sepia')">Sepia (Kertas)</button>
            <button class="setting-btn" data-theme="light" onclick="setTheme('light')">Terang</button>
            <button class="setting-btn" data-theme="dark" onclick="setTheme('dark')">Gelap (OLED)</button>
          </div>
        </div>

        <!-- Pilihan Font -->
        <div class="setting-section">
          <label class="setting-label">Gaya Huruf</label>
          <div class="setting-btn-group">
            <button class="setting-btn" data-font="serif" onclick="setFont('serif')" style="font-family: var(--font-serif);">Serif (Buku)</button>
            <button class="setting-btn" data-font="sans" onclick="setFont('sans')" style="font-family: var(--font-sans);">Sans (Modern)</button>
          </div>
        </div>

        <!-- Ukuran Huruf -->
        <div class="setting-section">
          <label class="setting-label">Ukuran Teks</label>
          <div class="font-size-control">
            <button class="font-size-btn" onclick="changeFontSize(-2)">A-</button>
            <span class="font-size-display" id="font-size-label">19px</span>
            <button class="font-size-btn" onclick="changeFontSize(2)">A+</button>
          </div>
        </div>

        <!-- Lebar Kolom -->
        <div class="setting-section">
          <label class="setting-label">Lebar Baca (Desktop/Tablet)</label>
          <div class="setting-btn-group">
            <button class="setting-btn" data-width="narrow" onclick="setWidth('narrow')">Ramping</button>
            <button class="setting-btn" data-width="normal" onclick="setWidth('normal')">Standar</button>
            <button class="setting-btn" data-width="wide" onclick="setWidth('wide')">Lebar</button>
          </div>
        </div>

        <!-- Spasi Baris -->
        <div class="setting-section">
          <label class="setting-label">Spasi Baris</label>
          <div class="setting-btn-group">
            <button class="setting-btn" data-spacing="compact" onclick="setSpacing('compact')">Rapat</button>
            <button class="setting-btn" data-spacing="normal" onclick="setSpacing('normal')">Standar</button>
            <button class="setting-btn" data-spacing="relaxed" onclick="setSpacing('relaxed')">Lebar</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- CANON & INFO MODAL -->
  <div class="modal-backdrop" id="canon-backdrop" onclick="closeCanonModal(event)">
    <div class="modal-box" style="max-width: 680px;" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="canon-modal-title">Info Cerita & Panduan Canon</h3>
        <button class="icon-btn" onclick="closeCanonModal()">
          <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg>
        </button>
      </div>
      <div class="modal-body">
        <div class="tabs-nav">
          <button class="tab-btn active" onclick="switchCanonTab('tab-premise')">Premis & Blurb</button>
          <button class="tab-btn" onclick="switchCanonTab('tab-cast')">Daftar Tokoh (Cast)</button>
          <button class="tab-btn" onclick="switchCanonTab('tab-matrix')">Matriks Sapaan</button>
        </div>

        <!-- Tab 1: Premis -->
        <div class="tab-content active" id="tab-premise">
          <dl class="canon-dl">
            <dt>Logline</dt>
            <dd id="info-logline">-</dd>
            <dt>Blurb Resmi</dt>
            <dd id="info-blurb">-</dd>
            <dt>Tema Utama</dt>
            <dd id="info-tema">-</dd>
            <dt>Latar & Suasana</dt>
            <dd id="info-latar">-</dd>
            <dt>Pertanyaan Dramatik</dt>
            <dd id="info-pertanyaan">-</dd>
          </dl>
        </div>

        <!-- Tab 2: Cast -->
        <div class="tab-content" id="tab-cast">
          <div id="info-cast-list" style="overflow-x: auto;">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Tab 3: Sapaan -->
        <div class="tab-content" id="tab-matrix">
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 10px;">
            Aturan panggilan tokoh di narasi batin POV 1 vs sapaan formal, akrab, dan saat konflik.
          </p>
          <div id="info-matrix-list" style="overflow-x: auto;">
            <!-- Rendered via JS -->
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast-msg">Notifikasi</div>

  <!-- EMBEDDED STORY DATA (JSON) -->
  <script id="story-data" type="application/json">
{data_json}
  </script>

  <!-- APPLICATION LOGIC -->
  <script>
    // State Management
    let STORIES = [];
    let currentStory = null;
    let currentChapterIndex = 0;
    let searchMatches = [];
    let currentSearchMatchIndex = -1;

    const STORAGE_KEY = "metropop_reader_state_v1";

    function getStorage() {{
      try {{
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : {{}};
      }} catch (e) {{
        return {{}};
      }}
    }}

    function saveStorage(key, val) {{
      try {{
        const s = getStorage();
        s[key] = val;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(s));
      }} catch (e) {{}}
    }}

    function saveStoryProgress(storyId, chapterNum) {{
      const s = getStorage();
      if (!s.progress) s.progress = {{}};
      s.progress[storyId] = chapterNum;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(s));
    }}

    function getStoryProgress(storyId) {{
      const s = getStorage();
      return (s.progress && s.progress[storyId]) ? s.progress[storyId] : 1;
    }}

    // App Initialization
    document.addEventListener("DOMContentLoaded", () => {{
      try {{
        const el = document.getElementById("story-data");
        STORIES = JSON.parse(el.textContent);
      }} catch (e) {{
        console.error("Gagal membaca data cerita:", e);
      }}

      // Restore user preferences
      const st = getStorage();
      if (st.theme) setTheme(st.theme);
      if (st.font) setFont(st.font);
      if (st.size) setFontSize(st.size);
      if (st.width) setWidth(st.width);
      if (st.spacing) setSpacing(st.spacing);

      // Render Catalog
      renderCatalog();

      // Check URL parameters for direct deep-linking (e.g. ?story=...&bab=...)
      const urlParams = new URLSearchParams(window.location.search);
      const storyParam = urlParams.get("story");
      const babParam = parseInt(urlParams.get("bab"), 10);

      if (storyParam) {{
        const target = STORIES.find(s => s.id === storyParam);
        if (target) {{
          openReader(target.id, babParam || getStoryProgress(target.id));
          return;
        }}
      }}

      showCatalogView();

      // Scroll listener for reading progress bar
      window.addEventListener("scroll", updateScrollProgress, {{ passive: true }});
    }});

    function updateScrollProgress() {{
      const reader = document.getElementById("reader-view");
      if (reader.classList.contains("view-hidden")) return;

      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const bar = document.getElementById("reading-progress-bar");
      if (docHeight > 0) {{
        const pct = Math.min(100, Math.max(0, (scrollTop / docHeight) * 100));
        bar.style.width = pct + "%";
      }} else {{
        bar.style.width = "0%";
      }}
    }}

    // Views Toggle
    function showCatalogView() {{
      document.getElementById("catalog-view").classList.remove("view-hidden");
      document.getElementById("reader-view").classList.add("view-hidden");
      document.getElementById("btn-back-catalog").style.display = "none";
      document.getElementById("brand-area").style.display = "flex";
      document.getElementById("btn-search-toggle").style.display = "none";
      document.getElementById("btn-toc-toggle").style.display = "none";
      document.getElementById("btn-zen-toggle").style.display = "none";
      document.getElementById("header-novel-title").textContent = "-";
      document.getElementById("header-chapter-title").textContent = "-";
      document.getElementById("reading-progress-bar").style.width = "0%";
      closeSearchBar();
      renderCatalog();
      window.scrollTo(0, 0);
    }}

    function renderCatalog() {{
      const grid = document.getElementById("stories-grid");
      grid.innerHTML = "";

      if (!STORIES || STORIES.length === 0) {{
        grid.innerHTML = `<p style="text-align: center; color: var(--text-muted); padding: 40px 0;">Belum ada cerita yang terdaftar di repositori.</p>`;
        return;
      }}

      STORIES.forEach(story => {{
        const lastRead = getStoryProgress(story.id);
        const progressPct = Math.round((lastRead / story.chapterCount) * 100);

        const card = document.createElement("div");
        card.className = "story-card";
        card.innerHTML = `
          <div class="story-header">
            <div>
              <h2 class="story-title">${{escapeHtml(story.title)}}</h2>
              <div class="badge-group">
                <span class="badge badge-accent">${{escapeHtml(story.genre)}}</span>
                <span class="badge">${{escapeHtml(story.status)}}</span>
                <span class="badge">${{story.totalWords.toLocaleString()}} kata</span>
                <span class="badge">~${{story.totalReadTimeMin}} menit baca</span>
              </div>
            </div>
          </div>

          <div class="story-blurb">
            ${{escapeHtml(story.blurb || story.logline)}}
          </div>

          <div class="progress-box">
            <div class="progress-meta">
              <span>Progres Baca: Bab ${{lastRead}} dari ${{story.chapterCount}}</span>
              <span>${{progressPct}}%</span>
            </div>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" style="width: ${{progressPct}}%;"></div>
            </div>
          </div>

          <div class="story-actions">
            <button class="btn-text btn-primary" onclick="openReader('${{story.id}}', ${{lastRead}})">
              <span>${{lastRead > 1 ? 'Lanjut Baca (Bab ' + lastRead + ')' : 'Mulai Baca Bab 1'}}</span>
            </button>
            <button class="btn-text" onclick="openTocForStory('${{story.id}}')">
              <span>Daftar Bab (${{story.chapterCount}})</span>
            </button>
            <button class="btn-text" onclick="openCanonModalForStory('${{story.id}}')">
              <span>Info Cerita & Tokoh</span>
            </button>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    // Reader Functionality
    function openReader(storyId, chapterNum) {{
      const story = STORIES.find(s => s.id === storyId);
      if (!story) return;
      currentStory = story;

      let idx = story.chapters.findIndex(c => c.number === chapterNum);
      if (idx === -1) idx = 0;
      currentChapterIndex = idx;

      document.getElementById("catalog-view").classList.add("view-hidden");
      document.getElementById("reader-view").classList.remove("view-hidden");
      document.getElementById("btn-back-catalog").style.display = "inline-flex";
      document.getElementById("brand-area").style.display = "none";
      document.getElementById("btn-search-toggle").style.display = "inline-flex";
      document.getElementById("btn-toc-toggle").style.display = "inline-flex";
      document.getElementById("btn-zen-toggle").style.display = "inline-flex";

      renderCurrentChapter();
    }}

    function renderCurrentChapter() {{
      if (!currentStory || !currentStory.chapters[currentChapterIndex]) return;
      const ch = currentStory.chapters[currentChapterIndex];

      // Update Header info
      document.getElementById("header-novel-title").textContent = currentStory.title;
      document.getElementById("header-chapter-title").textContent = ch.title;

      // Update Reader info
      document.getElementById("reader-novel-title").textContent = `${{currentStory.title}} / Bab ${{ch.number}} dari ${{currentStory.chapterCount}}`;
      document.getElementById("reader-chapter-title").textContent = ch.title;
      document.getElementById("reader-chapter-meta").textContent = `${{ch.wordCount.toLocaleString()}} kata • ~${{ch.readTimeMin}} menit waktu baca`;

      // Format Body Content
      const bodyEl = document.getElementById("reader-content-body");
      bodyEl.innerHTML = formatChapterBody(ch.content);

      // Save progress
      saveStoryProgress(currentStory.id, ch.number);

      // Nav buttons state
      const btnPrev = document.getElementById("btn-prev-chapter");
      const btnNext = document.getElementById("btn-next-chapter");

      btnPrev.disabled = (currentChapterIndex === 0);
      btnPrev.style.opacity = (currentChapterIndex === 0) ? "0.4" : "1";

      const isLast = (currentChapterIndex === currentStory.chapters.length - 1);
      btnNext.disabled = isLast;
      btnNext.style.opacity = isLast ? "0.4" : "1";
      btnNext.textContent = isLast ? "Tamat" : "Bab Selanjutnya →";

      // Reset scroll & search
      window.scrollTo(0, 0);
      closeSearchBar();
      updateTocActive();
    }}

    function formatChapterBody(rawText) {{
      const lines = rawText.split(/\\n\\s*\\n/);
      let html = "";

      for (let p of lines) {{
        p = p.trim();
        if (!p) continue;

        // Check for Chat format: "Nama: Isi pesan"
        const chatMatch = p.match(/^([A-Za-z0-9\\s]{2,30}):\\s+(.+)$/s);
        if (chatMatch && !p.startsWith('"') && !p.startsWith('“')) {{
          html += `
            <div class="chat-msg">
              <span class="chat-sender">${{escapeHtml(chatMatch[1])}}</span>
              <div>${{escapeHtml(chatMatch[2])}}</div>
            </div>
          `;
        }} else {{
          html += `<p>${{escapeHtml(p)}}</p>`;
        }}
      }}
      return html;
    }}

    function stepChapter(delta) {{
      if (!currentStory) return;
      const nextIdx = currentChapterIndex + delta;
      if (nextIdx >= 0 && nextIdx < currentStory.chapters.length) {{
        currentChapterIndex = nextIdx;
        renderCurrentChapter();
      }}
    }}

    // TOC Management
    function openTocDrawer() {{
      if (!currentStory && STORIES.length > 0) {{
        currentStory = STORIES[0];
      }}
      if (!currentStory) return;

      renderTocList();
      document.getElementById("toc-drawer").classList.add("open");
      document.getElementById("toc-backdrop").classList.add("active");
    }}

    function openTocForStory(storyId) {{
      const s = STORIES.find(item => item.id === storyId);
      if (s) {{
        currentStory = s;
        openTocDrawer();
      }}
    }}

    function closeTocDrawer() {{
      document.getElementById("toc-drawer").classList.remove("open");
      document.getElementById("toc-backdrop").classList.remove("active");
    }}

    function renderTocList(filterQuery = "") {{
      const list = document.getElementById("toc-list");
      list.innerHTML = "";

      if (!currentStory) return;

      const q = filterQuery.toLowerCase();
      currentStory.chapters.forEach((ch, idx) => {{
        if (q && !ch.title.toLowerCase().includes(q) && !(`bab ${{ch.number}}`).includes(q)) {{
          return;
        }}

        const li = document.createElement("li");
        li.className = `toc-item ${{idx === currentChapterIndex ? 'active' : ''}}`;
        li.innerHTML = `
          <div class="toc-item-title">${{escapeHtml(ch.title)}}</div>
          <div class="toc-item-words">${{ch.wordCount}} kata</div>
        `;
        li.onclick = () => {{
          currentChapterIndex = idx;
          closeTocDrawer();
          if (document.getElementById("reader-view").classList.contains("view-hidden")) {{
            openReader(currentStory.id, ch.number);
          }} else {{
            renderCurrentChapter();
          }}
        }};
        list.appendChild(li);
      }});
    }}

    function filterToc(val) {{
      renderTocList(val);
    }}

    function updateTocActive() {{
      const items = document.querySelectorAll(".toc-item");
      items.forEach((item, idx) => {{
        if (idx === currentChapterIndex) {{
          item.classList.add("active");
        }} else {{
          item.classList.remove("active");
        }}
      }});
    }}

    // Settings Modal
    function openSettingsModal() {{
      document.getElementById("settings-backdrop").classList.add("active");
      updateSettingsUI();
    }}

    function closeSettingsModal() {{
      document.getElementById("settings-backdrop").classList.remove("active");
    }}

    function updateSettingsUI() {{
      const root = document.documentElement;
      const theme = root.getAttribute("data-theme") || "sepia";
      const font = root.getAttribute("data-font") || "serif";
      const width = root.getAttribute("data-width") || "normal";
      const spacing = root.getAttribute("data-spacing") || "normal";
      const size = root.getAttribute("data-size") || "19";

      document.querySelectorAll("[data-theme]").forEach(b => {{
        b.classList.toggle("active", b.getAttribute("data-theme") === theme);
      }});
      document.querySelectorAll("[data-font]").forEach(b => {{
        b.classList.toggle("active", b.getAttribute("data-font") === font);
      }});
      document.querySelectorAll("[data-width]").forEach(b => {{
        b.classList.toggle("active", b.getAttribute("data-width") === width);
      }});
      document.querySelectorAll("[data-spacing]").forEach(b => {{
        b.classList.toggle("active", b.getAttribute("data-spacing") === spacing);
      }});
      document.getElementById("font-size-label").textContent = size + "px";
    }}

    function setTheme(theme) {{
      document.documentElement.setAttribute("data-theme", theme);
      saveStorage("theme", theme);
      updateSettingsUI();
    }}

    function setFont(font) {{
      document.documentElement.setAttribute("data-font", font);
      saveStorage("font", font);
      updateSettingsUI();
    }}

    function setWidth(w) {{
      document.documentElement.setAttribute("data-width", w);
      saveStorage("width", w);
      updateSettingsUI();
    }}

    function setSpacing(s) {{
      document.documentElement.setAttribute("data-spacing", s);
      saveStorage("spacing", s);
      updateSettingsUI();
    }}

    function setFontSize(val) {{
      val = Math.max(15, Math.min(25, parseInt(val, 10)));
      document.documentElement.setAttribute("data-size", val);
      saveStorage("size", val);
      updateSettingsUI();
    }}

    function changeFontSize(delta) {{
      const current = parseInt(document.documentElement.getAttribute("data-size") || "19", 10);
      setFontSize(current + delta);
    }}

    // Zen Mode (Distraction-Free)
    function toggleZenMode() {{
      document.body.classList.toggle("zen-mode");
      const isZen = document.body.classList.contains("zen-mode");
      showToast(isZen ? "Mode Zen aktif (fokus penuh teks)" : "Mode Zen dinonaktifkan");
    }}

    // Copy Current Chapter
    function copyCurrentChapter() {{
      if (!currentStory || !currentStory.chapters[currentChapterIndex]) return;
      const ch = currentStory.chapters[currentChapterIndex];
      const textToCopy = `${{ch.title}}\\n\\n${{ch.content}}`;

      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(textToCopy).then(() => {{
          showToast("Teks Bab berhasil disalin ke clipboard!");
        }}).catch(() => {{
          fallbackCopyText(textToCopy);
        }});
      }} else {{
        fallbackCopyText(textToCopy);
      }}
    }}

    function fallbackCopyText(text) {{
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      try {{
        document.execCommand("copy");
        showToast("Teks Bab berhasil disalin!");
      }} catch (e) {{
        showToast("Gagal menyalin teks.");
      }}
      document.body.removeChild(ta);
    }}

    // In-Chapter Search
    function toggleSearchBar() {{
      const bar = document.getElementById("search-toolbar");
      if (bar.style.display === "none") {{
        bar.style.display = "flex";
        document.getElementById("search-input").focus();
      }} else {{
        closeSearchBar();
      }}
    }}

    function closeSearchBar() {{
      document.getElementById("search-toolbar").style.display = "none";
      document.getElementById("search-input").value = "";
      document.getElementById("search-count").textContent = "0 hasil";
      clearSearchHighlights();
    }}

    function clearSearchHighlights() {{
      if (!currentStory || !currentStory.chapters[currentChapterIndex]) return;
      const bodyEl = document.getElementById("reader-content-body");
      bodyEl.innerHTML = formatChapterBody(currentStory.chapters[currentChapterIndex].content);
      searchMatches = [];
      currentSearchMatchIndex = -1;
    }}

    function handleSearch(query) {{
      query = query.trim();
      clearSearchHighlights();
      if (!query || query.length < 2) {{
        document.getElementById("search-count").textContent = "0 hasil";
        return;
      }}

      const bodyEl = document.getElementById("reader-content-body");
      const regex = new RegExp(`(${{escapeRegex(query)}})`, "gi");

      let count = 0;
      bodyEl.querySelectorAll("p, .chat-msg div").forEach(el => {{
        const original = el.textContent;
        if (regex.test(original)) {{
          const replaced = original.replace(regex, '<mark class="search-hit">$1</mark>');
          el.innerHTML = replaced;
        }}
      }});

      searchMatches = bodyEl.querySelectorAll("mark.search-hit");
      document.getElementById("search-count").textContent = `${{searchMatches.length}} hasil`;
      if (searchMatches.length > 0) {{
        currentSearchMatchIndex = 0;
        highlightCurrentMatch();
      }}
    }}

    function navigateSearch(direction) {{
      if (searchMatches.length === 0) return;
      currentSearchMatchIndex += direction;
      if (currentSearchMatchIndex >= searchMatches.length) currentSearchMatchIndex = 0;
      if (currentSearchMatchIndex < 0) currentSearchMatchIndex = searchMatches.length - 1;
      highlightCurrentMatch();
    }}

    function highlightCurrentMatch() {{
      searchMatches.forEach((m, idx) => {{
        if (idx === currentSearchMatchIndex) {{
          m.style.outline = "2px solid var(--accent-color)";
          m.scrollIntoView({{ behavior: "smooth", block: "center" }});
        }} else {{
          m.style.outline = "none";
        }}
      }});
      document.getElementById("search-count").textContent = `${{currentSearchMatchIndex + 1}} dari ${{searchMatches.length}}`;
    }}

    // Canon & Info Modal
    function openCanonModal() {{
      if (!currentStory) return;
      openCanonModalForStory(currentStory.id);
    }}

    function openCanonModalForStory(storyId) {{
      const story = STORIES.find(s => s.id === storyId);
      if (!story) return;

      document.getElementById("canon-modal-title").textContent = `Info Cerita: ${{story.title}}`;
      document.getElementById("info-logline").textContent = story.logline || "-";
      document.getElementById("info-blurb").textContent = story.blurb || "-";
      document.getElementById("info-tema").textContent = story.tema || "-";
      document.getElementById("info-latar").textContent = story.latar || "-";
      document.getElementById("info-pertanyaan").textContent = story.pertanyaan || "-";

      // Render Cast
      const castContainer = document.getElementById("info-cast-list");
      if (story.characters && story.characters.length > 0) {{
        let tableHtml = `
          <table class="canon-table">
            <thead>
              <tr><th>Tokoh</th><th>Peran</th><th>Umur</th><th>Pekerjaan</th><th>Fungsi Dramatik</th></tr>
            </thead>
            <tbody>
        `;
        story.characters.forEach(c => {{
          tableHtml += `
            <tr>
              <td><strong>${{escapeHtml(c.name)}}</strong></td>
              <td>${{escapeHtml(c.role)}}</td>
              <td>${{escapeHtml(c.age)}}</td>
              <td>${{escapeHtml(c.job)}}</td>
              <td>${{escapeHtml(c.desc)}}</td>
            </tr>
          `;
        }});
        tableHtml += `</tbody></table>`;
        castContainer.innerHTML = tableHtml;
      }} else {{
        castContainer.innerHTML = `<p style="font-size: 0.9rem; color: var(--text-muted);">Belum ada data tokoh terdaftar di canon.</p>`;
      }}

      // Render Address Matrix
      const matrixContainer = document.getElementById("info-matrix-list");
      if (story.addressMatrix && story.addressMatrix.length > 0) {{
        let matrixHtml = `
          <table class="canon-table">
            <thead>
              <tr><th>Pembicara -> Lawan</th><th>Narasi Batin POV 1</th><th>Formal Awal</th><th>Saat Akrab</th><th>Saat Konflik</th></tr>
            </thead>
            <tbody>
        `;
        story.addressMatrix.forEach(m => {{
          matrixHtml += `
            <tr>
              <td><strong>${{escapeHtml(m.speakers)}}</strong></td>
              <td>${{escapeHtml(m.pov_call)}}</td>
              <td>${{escapeHtml(m.formal)}}</td>
              <td>${{escapeHtml(m.close)}}</td>
              <td>${{escapeHtml(m.conflict)}}</td>
            </tr>
          `;
        }});
        matrixHtml += `</tbody></table>`;
        matrixContainer.innerHTML = matrixHtml;
      }} else {{
        matrixContainer.innerHTML = `<p style="font-size: 0.9rem; color: var(--text-muted);">Belum ada data matriks sapaan terdaftar di canon.</p>`;
      }}

      switchCanonTab("tab-premise");
      document.getElementById("canon-backdrop").classList.add("active");
    }}

    function closeCanonModal() {{
      document.getElementById("canon-backdrop").classList.remove("active");
    }}

    function switchCanonTab(tabId) {{
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

      const targetBtn = document.querySelector(`.tab-btn[onclick*="${{tabId}}"]`);
      if (targetBtn) targetBtn.classList.add("active");

      const targetTab = document.getElementById(tabId);
      if (targetTab) targetTab.classList.add("active");
    }}

    // Utilities
    function showToast(msg) {{
      const toast = document.getElementById("toast-msg");
      toast.textContent = msg;
      toast.classList.add("show");
      setTimeout(() => {{
        toast.classList.remove("show");
      }}, 2400);
    }}

    function escapeHtml(str) {{
      if (!str) return "";
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    function escapeRegex(str) {{
      return str.replace(/[.*+?^${{}}()|[\\]\\\\]/g, "\\\\$&");
    }}
  </script>
</body>
</html>
"""


def main():
    print("Membaca data cerita dari folder story/...")
    story_dirs = [d for d in sorted(STORY_DIR.iterdir()) if d.is_dir() and (d / "chapters").is_dir()]
    stories = [parse_story(d) for d in story_dirs]

    print(f"Ditemukan {len(stories)} cerita:")
    for s in stories:
        print(f"  - {s['title']}: {s['chapterCount']} bab, {s['totalWords']} kata")

    print(f"Menulis file web app mandiri ke: {OUTPUT_FILE}...")
    html_content = generate_html(stories)
    OUTPUT_FILE.write_text(html_content, encoding="utf-8")
    print(f"Selesai! Ukuran file: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB.")


if __name__ == "__main__":
    main()

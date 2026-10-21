"""Command line interface for the MetroPop story engine."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__, corpus, data, planner, render
from .checker import inspect_story
from .storage import (
    DEFAULT_STORY_ROOT,
    STORY_FILE,
    iter_stories,
    load_story,
    previous_written_chapter,
    resolve_story,
    save_rendered,
    save_story,
    story_folder,
    story_summaries,
)


def _root(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


def _targets(path: str | None, root: Path) -> list[Path]:
    if path:
        return [resolve_story(path, root)]
    cwd = Path.cwd()
    if (cwd / STORY_FILE).is_file():
        return [cwd]
    stories = iter_stories(root)
    if not stories:
        raise FileNotFoundError(f"Belum ada cerita di {root}.")
    return stories


def cmd_new(args: argparse.Namespace) -> int:
    root = _root(args.root)
    story = planner.plan_story(
        title=args.title,
        engine_key=args.engine,
        seed=args.seed,
        chapters=args.chapters,
        target_words=args.target,
    )
    destination = story_folder(root, story["title"])
    if destination.exists():
        print(f"Folder sudah ada: {destination}", file=sys.stderr)
        print("Pilih judul lain atau hapus folder itu secara manual.", file=sys.stderr)
        return 2

    save_story(story, destination, skeleton=not args.no_skeleton)
    print(f"Cerita dibuat: {story['title']}")
    print(f"- Folder   : {destination}")
    print(f"- Mesin    : {story['engine_label']} ({story['engine']})")
    print(f"- Bab      : {story['chapter_count']} × ±{story['target_words']} kata")
    print(f"- Seed     : {story['seed']}")
    print(f"- Bible    : {destination / 'bible.md'}")
    print(f"- Outline  : {destination / 'outline.md'}")
    print()
    print("Langkah berikutnya:")
    print(f"  bash engine/bin/metropop brief 1 --story \"{destination}\"")
    print(f"  bash engine/bin/metropop check --story \"{destination}\"")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    root = _root(args.root)
    summaries = story_summaries(root)
    if not summaries:
        print(f"Belum ada cerita di {root}.")
        print('Buat dengan: metropop new "Judul Cerita"')
        return 0
    print(f"{'Judul':<28} {'Bab':>4} {'Selesai':>8} {'Seed':>10}  Folder")
    print("-" * 92)
    for summary in summaries:
        directory = summary["dir"].name
        print(
            f"{summary['title'][:27]:<28} {summary['chapters']:>4} "
            f"{summary['done']:>8} {str(summary['seed']):>10}  {directory}"
        )
    return 0


def cmd_brief(args: argparse.Namespace) -> int:
    root = _root(args.root)
    story_dir = resolve_story(args.story, root)
    story = load_story(story_dir)
    chapter = next((c for c in story["chapters"] if int(c["number"]) == args.chapter), None)
    if not chapter:
        raise ValueError(f"Bab {args.chapter} tidak ada di {story['title']}.")
    next_chapter = next(
        (c for c in story["chapters"] if int(c["number"]) == args.chapter + 1),
        None,
    )
    previous = previous_written_chapter(story_dir, args.chapter)
    text = render.render_brief(story, chapter, previous_text=previous, next_chapter=next_chapter)
    if args.out:
        output = Path(args.out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"Paket penulisan ditulis ke {output}")
    else:
        print(text)
    return 0


def _print_check(result: dict, verbose: bool = True) -> None:
    story = result["story"]
    print(f"Cerita : {story['title']}")
    print(f"Folder : {result['story_dir']}")
    print(f"Bab    : {len(result['rows'])} (minimum 30)")
    print(
        f"Target : ±{story.get('target_words', 750)} kata/bab, "
        f"total ±{sum(row['target'] for row in result['rows']):,} kata"
    )
    print()

    if verbose:
        print(f"{'No':>3}  {'Status':<8} {'Kata':>6} {'Target':>7}  Judul")
        print("-" * 78)
        for row in result["rows"]:
            print(
                f"{row['number']:>3}  {row['status']:<8} {row['words']:>6} "
                f"{row['target']:>7}  {row['title']}"
            )
        print()

    if result["errors"]:
        print(f"ERROR ({len(result['errors'])}):")
        for message in result["errors"]:
            print(f"  - {message}")
    if result["warnings"]:
        print(f"PERINGATAN ({len(result['warnings'])}):")
        for message in result["warnings"][:25]:
            print(f"  - {message}")
        if len(result["warnings"]) > 25:
            print(f"  - ... dan {len(result['warnings']) - 25} peringatan lain.")
    if not result["errors"] and not result["warnings"]:
        print("Tidak ada masalah.")

    print()
    print(
        f"Ringkasan: {result['done']}/{len(result['rows'])} selesai "
        f"({result['percent']}%) · {result['total_words']:,} kata tertulis · "
        f"{result['average']:,} kata rata-rata bab selesai · "
        f"{len(result['errors'])} error · {len(result['warnings'])} peringatan"
    )


def cmd_check(args: argparse.Namespace) -> int:
    root = _root(args.root)
    targets = _targets(args.story or args.path, root)
    failed = False
    multiple = len(targets) > 1
    total_errors = 0
    total_warnings = 0
    for index, story_dir in enumerate(targets):
        result = inspect_story(story_dir)
        if multiple:
            print(f"=== {result['story']['title']} ===")
        _print_check(result, verbose=not multiple)
        total_errors += len(result["errors"])
        total_warnings += len(result["warnings"])
        if result["errors"] or (args.strict and result["warnings"]):
            failed = True
        if multiple and index + 1 < len(targets):
            print()
    if multiple:
        print()
        print(
            f"Total: {len(targets)} cerita · {total_errors} error · "
            f"{total_warnings} peringatan"
        )
    return 1 if failed else 0


def cmd_stats(args: argparse.Namespace) -> int:
    root = _root(args.root)
    story_dir = resolve_story(args.story or args.path, root)
    result = inspect_story(story_dir)
    print(render.render_stats(result["story"], result["rows"]))
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    root = _root(args.root)
    story_dir = resolve_story(args.story or args.path, root)
    story = load_story(story_dir)
    save_rendered(story, story_dir)
    print(f"Bible dan outline diperbarui: {story_dir}")
    return 0


def cmd_analyze(args: argparse.Namespace) -> int:
    path = Path(args.file).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"File tidak ditemukan: {path}")
    result = corpus.analyze(path)
    if args.json:
        payload = corpus.result_json(result)
        if args.out:
            output = Path(args.out).expanduser()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(payload + "\n", encoding="utf-8")
            print(f"JSON ditulis ke {output}")
        else:
            print(payload)
        return 0
    report = corpus.render_report(result)
    if args.out:
        output = Path(args.out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
        print(f"Laporan ditulis ke {output}")
    else:
        print(report)
    return 0


def cmd_engines(args: argparse.Namespace) -> int:
    print("Mesin cerita MetroPop:")
    print()
    for engine in data.ENGINES:
        print(f"- {engine['key']:<17} {engine['label']}")
        print(f"  {engine['promise']}")
        print(f"  Contoh judul: {', '.join(engine['titles'][:4])}")
        print()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="metropop",
        description="Mesin cerita MetroPop: rencanakan, tulis, dan validasi web novel 30–50 bab.",
    )
    parser.add_argument("--version", action="version", version=f"metropop {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    new = sub.add_parser("new", help="Buat folder cerita baru beserta bible dan outline.")
    new.add_argument("title", nargs="?", help="Judul cerita. Jika kosong, dipilih dari mesin.")
    new.add_argument("--engine", choices=[engine["key"] for engine in data.ENGINES], help="Mesin premis.")
    new.add_argument("--seed", type=int, help="Benih acak untuk hasil yang bisa diulang.")
    new.add_argument("--chapters", type=int, default=40, help="Jumlah bab (minimal 30, default 40).")
    new.add_argument("--target", type=int, default=750, help="Target kata per bab (default 750).")
    new.add_argument("--root", default=str(DEFAULT_STORY_ROOT), help="Folder penyimpanan cerita.")
    new.add_argument("--no-skeleton", action="store_true", help="Jangan buat file bab kosong.")
    new.set_defaults(handler=cmd_new)

    listing = sub.add_parser("list", help="Daftar cerita yang sudah ada.")
    listing.add_argument("--root", default=str(DEFAULT_STORY_ROOT))
    listing.set_defaults(handler=cmd_list)

    brief = sub.add_parser("brief", help="Cetak paket penulisan untuk satu bab.")
    brief.add_argument("chapter", type=int, help="Nomor bab.")
    brief.add_argument("--story", help="Folder cerita (atau jalankan dari dalam folder cerita).")
    brief.add_argument("--root", default=str(DEFAULT_STORY_ROOT))
    brief.add_argument("--out", help="Simpan paket ke file markdown.")
    brief.set_defaults(handler=cmd_brief)

    check = sub.add_parser("check", help="Validasi jumlah bab, hitungan kata, dan status.")
    check.add_argument("path", nargs="?", help="Folder cerita. Kosong = semua cerita di root.")
    check.add_argument("--story", help="Folder cerita (alternatif dari path posisional).")
    check.add_argument("--root", default=str(DEFAULT_STORY_ROOT))
    check.add_argument("--strict", action="store_true", help="Peringatan juga dianggap gagal.")
    check.set_defaults(handler=cmd_check)

    stats = sub.add_parser("stats", help="Statistik kemajuan satu cerita.")
    stats.add_argument("path", nargs="?", help="Folder cerita.")
    stats.add_argument("--story", help="Folder cerita (alternatif dari path posisional).")
    stats.add_argument("--root", default=str(DEFAULT_STORY_ROOT))
    stats.set_defaults(handler=cmd_stats)

    refresh = sub.add_parser("render", help="Tulis ulang bible.md dan outline.md dari story.json.")
    refresh.add_argument("path", nargs="?", help="Folder cerita.")
    refresh.add_argument("--story", help="Folder cerita (alternatif dari path posisional).")
    refresh.add_argument("--root", default=str(DEFAULT_STORY_ROOT))
    refresh.set_defaults(handler=cmd_render)

    analyze = sub.add_parser("analyze", help="Analisis manuskrip referensi (panjang bab, hook, dialog).")
    analyze.add_argument("file", help="File teks/markdown referensi.")
    analyze.add_argument("--out", help="Simpan laporan ke file.")
    analyze.add_argument("--json", action="store_true", help="Keluarkan JSON, bukan markdown.")
    analyze.set_defaults(handler=cmd_analyze)

    engines = sub.add_parser("engines", help="Daftar mesin premis yang tersedia.")
    engines.set_defaults(handler=cmd_engines)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.handler(args) or 0)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

"""Markdown renderers for story bibles, outlines, chapters, and briefs."""

from __future__ import annotations

from typing import Any

from .text import truncate

CAST_ORDER = ["protagonis", "love", "antagonis", "sekutu", "mentor", "keluarga"]

CAST_LABELS = {
    "name": "Nama lengkap",
    "call": "Sebutan",
    "role": "Peran",
    "age": "Umur",
    "job": "Pekerjaan",
    "want": "Yang diinginkan",
    "need": "Yang sebenarnya dibutuhkan",
    "flaw": "Cacat karakter",
    "wound": "Luka lama",
    "arc": "Busur",
    "voice": "Suara",
    "family_pressure": "Tekanan keluarga",
    "charm": "Daya tarik",
    "boundary": "Batas pribadi",
    "secret": "Rahasia",
    "tactic": "Taktik",
    "vulnerability": "Titik lemah",
    "rationale": "Alasan ia merasa benar",
    "stake": "Taruhan pribadi",
    "condition": "Syarat bantuan",
    "pressure": "Tekanan keluarga",
    "function": "Fungsi dramatik",
}

TARGET_WORDS = 750

PHASE_DESCRIPTIONS = {
    "setup": "Dunia awal → komitmen",
    "escalation": "Konsekuensi → peringatan",
    "midpoint": "Pembalikan pemahaman",
    "fallout": "Retak → titik terendah",
    "act3": "Rencana → citra akhir",
}


def word_range(target: int) -> tuple[int, int]:
    return max(600, round(target * 0.8)), min(950, round(target * 1.2))


def chapter_filename(number: int) -> str:
    return f"bab-{number:02d}.md"


def total_target(story: dict[str, Any]) -> int:
    return sum(int(chapter.get("target_words", story.get("target_words", TARGET_WORDS))) for chapter in story["chapters"])


def _cast_table(story: dict[str, Any]) -> str:
    lines = [
        "| Tokoh | Peran | Umur | Pekerjaan | Fungsi dramatik |",
        "|---|---|---|---|---|",
    ]
    for key in CAST_ORDER:
        person = story["cast"].get(key)
        if not person:
            continue
        lines.append(
            "| {name} | {role} | {age} | {job} | {function} |".format(
                name=person.get("name", "-"),
                role=person.get("role", "-"),
                age=person.get("age", "-"),
                job=person.get("job") or "—",
                function=person.get("function") or "—",
            )
        )
    return "\n".join(lines)


def _cast_details(story: dict[str, Any]) -> str:
    blocks: list[str] = []
    for key in CAST_ORDER:
        person = story["cast"].get(key)
        if not person:
            continue
        heading = f"### {person.get('name', '-')} — {person.get('role', '-')}"
        detail_lines = [heading]
        for field in [
            "age", "job", "want", "need", "flaw", "wound", "family_pressure",
            "charm", "boundary", "secret", "tactic", "vulnerability",
            "rationale", "stake", "condition", "pressure", "function", "arc", "voice",
        ]:
            value = person.get(field)
            if value:
                detail_lines.append(f"- **{CAST_LABELS[field]}:** {value}")
        blocks.append("\n".join(detail_lines))
    return "\n\n".join(blocks)


def render_bible(story: dict[str, Any]) -> str:
    world = story["world"]
    cast = story["cast"]
    protagonist = cast["protagonis"]
    total = total_target(story)
    glossary = story.get("glossary", {})

    glossary_lines = ["| Istilah | Arti |", "|---|---|"]
    for term, meaning in sorted(glossary.items()):
        glossary_lines.append(f"| {term} | {meaning} |")

    return f"""# {story["title"]}

> {story["logline"]}

## Profil Cerita

- **Genre:** MetroPop — drama urban dengan romansa dan kritik sosial ringan
- **Panjang:** {story["chapter_count"]} bab × ±{story["target_words"]} kata (±{total:,} kata)
- **POV:** orang ketiga dekat; satu POV per bab; beberapa bab sampingan
- **Kota:** {world.get("city", "Jakarta")}
- **Mesin cerita:** {story["engine_label"]}
- **Benih acak:** `{story["seed"]}`

## Pertanyaan Dramatik

{story["dramatic_question"]}

## Tema

{story["theme"]}

## Janji ke Pembaca

{story["promise"]}

## Sinopsis

{story["premise"]}

Arah akhir: {story["ending_direction"]}

## Tokoh

{_cast_table(story)}

{_cast_details(story)}

## Dunia dan Aturan

- **{world.get("company", "-")}** — {world.get("sector", "-")}. {protagonist["call"]} bekerja sebagai {world.get("job", "-")}.
- **Proyek utama:** {world.get("project", "-")}.
- **Klien / pihak luar:** {world.get("client", "-")}.
- **Kanal komunikasi:** {world.get("channel", "-")}.
- **Tekanan keluarga:** {protagonist.get("family_pressure", "-")}.
- **Rahasia utama:** {story["secret"]}
- **Rahasia ini tidak boleh diungkap sebelum bab {story["midpoint_chapter"]}.**

## Aturan Kontinuitas

1. Satu bab = satu adegan utama, satu POV, satu perubahan status.
2. Informasi hanya diketahui oleh tokoh yang menyaksikannya sendiri.
3. Nama, umur, jabatan, dan hubungan tidak berubah tanpa alasan yang tertulis di bab.
4. Istilah kerja dijelaskan inline pada kemunculan pertama, lalu boleh dipakai bebas.
5. Hook bab sebelumnya tidak boleh diselesaikan di paragraf pertama bab berikutnya.
6. Bab sampingan hanya boleh menambah informasi, bukan mengulang adegan dari POV lain.
7. Klimaks terjadi di bab {story["climax_chapter"]}; setelah itu tidak ada konflik baru.
8. Uang, waktu, dan jarak harus konsisten dengan yang sudah disebutkan.

## Glosarium

{chr(10).join(glossary_lines)}

## Catatan Penulisan

- Target per bab: {story["target_words"]} kata. Bab titik balik boleh ±900 kata.
- Rentang yang diterima: 600–900 kata untuk bab biasa; 720–950 untuk bab titik balik.
- Dialog minimal 30% dari bab; sisanya narasi dan aksi.
- Setiap bab harus punya satu detail konkret: makanan, aplikasi, benda di meja, suara ruangan.
- Hook wajib menjadi kalimat terakhir bab.
"""


def render_outline(story: dict[str, Any]) -> str:
    lines = [
        f"# Outline — {story['title']}",
        "",
        f"{story['chapter_count']} bab × ±{story['target_words']} kata (±{total_target(story):,} kata).",
        "",
        f"**Pertanyaan dramatik:** {story['dramatic_question']}",
        "",
        f"**Rahasia utama:** {story['secret']} (jangan dibuka sebelum bab {story['midpoint_chapter']}).",
        "",
        "## Peta Babak",
        "",
        "| Babak | Bab | Jumlah | Fungsi |",
        "|---|---|---|---|",
    ]
    for phase in story["phases"]:
        span = str(phase["start"]) if phase["start"] == phase["end"] else f"{phase['start']}–{phase['end']}"
        lines.append(
            f"| {phase['label']} | {span} | {phase['count']} | {PHASE_DESCRIPTIONS.get(phase['key'], phase['key'])} |"
        )

    lines.extend(["", "## Bab", ""])
    for chapter in story["chapters"]:
        side = " · *bab sampingan*" if chapter.get("side_chapter") else ""
        lines.append(f"### Bab {chapter['number']} — {chapter['title']}")
        lines.append("")
        lines.append(f"- **Fase:** {chapter['phase_label']}{side}")
        lines.append(f"- **POV:** {chapter['pov']} · **Waktu:** {chapter['time']} · **Tempat:** {chapter['place']}")
        lines.append(f"- **Fungsi:** {chapter['function']}")
        lines.append(f"- **Adegan:** {chapter['scene']}")
        lines.append(f"- **Konflik:** {chapter['conflict']}")
        lines.append(f"- **Belokan:** {chapter['turn']}")
        lines.append(f"- **Hook:** {chapter['hook']}")
        lines.append(f"- **Target:** ±{chapter['target_words']} kata")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_chapter_skeleton(story: dict[str, Any], chapter: dict[str, Any]) -> str:
    side = "Bab sampingan. " if chapter.get("side_chapter") else ""
    return f"""---
bab: {chapter['number']}
judul: "{chapter['title']}"
status: todo
pov: "{chapter['pov']}"
target_kata: {chapter['target_words']}
waktu: "{chapter['time']}"
tempat: "{chapter['place']}"
---

# Bab {chapter['number']}: {chapter['title']}

<!-- BRIEF
Fase: {chapter['phase_label']}
POV: {chapter['pov']} — {side}tetap satu POV untuk seluruh bab.
Waktu/tempat: {chapter['time']}, {chapter['place']}
Fungsi: {chapter['function']}
Adegan: {chapter['scene']}
Konflik: {chapter['conflict']}
Belokan: {chapter['turn']}
Hook wajib (kalimat terakhir): {chapter['hook']}
Target: ±{chapter['target_words']} kata.
-->
"""


def render_brief(
    story: dict[str, Any],
    chapter: dict[str, Any],
    previous_text: str = "",
    next_chapter: dict[str, Any] | None = None,
) -> str:
    target = int(chapter.get("target_words", story["target_words"]))
    low, high = word_range(target)
    cast = story["cast"]
    protagonist = cast["protagonis"]
    love = cast["love"]
    antagonist = cast["antagonis"]
    ally = cast["sekutu"]

    previous_block = "(belum ada bab sebelumnya)"
    if previous_text.strip():
        previous_block = truncate(" ".join(previous_text.split()), 700)

    next_block = ""
    if next_chapter:
        next_block = (
            f"\n**Bab berikutnya ({next_chapter['number']}) akan dibuka dengan tekanan:** "
            f"{next_chapter['scene']}\n\nJangan selesaikan tekanan itu di bab ini.\n"
        )

    glossary_lines = [
        f"- **{term}:** {meaning}" for term, meaning in sorted(story.get("glossary", {}).items())
    ]

    return f"""# Paket Penulisan — {story['title']}, Bab {chapter['number']}

## Target

- **{low}–{high} kata** (titik tengah ±{target})
- Satu adegan utama, satu POV: **{chapter['pov']}**
- Waktu: {chapter['time']} · Tempat: {chapter['place']}
- Fase: {chapter['phase_label']} · Fungsi: {chapter['function']}

## Brief

- **Adegan:** {chapter['scene']}
- **Konflik:** {chapter['conflict']}
- **Belokan:** {chapter['turn']}
- **Hook (wajib jadi kalimat terakhir):** {chapter['hook']}
- **Target kata:** ±{target} (terima {low}–{high})

## Konteks Cerita

- **Logline:** {story['logline']}
- **Pertanyaan dramatik:** {story['dramatic_question']}
- **Tema:** {story['theme']}
- **Rahasia yang belum boleh dibuka:** {story['secret']}
- **Batas pengungkapan:** jangan ungkap sebelum bab {story['midpoint_chapter']}.
- **Arah akhir (jangan ditulis sekarang):** {story['ending_direction']}

**Akhir bab sebelumnya:**
> {previous_block}
{next_block}
## Tokoh yang Relevan

- **{protagonist['name']}** ({protagonist['call']}) — {protagonist['job']}. Ingin: {protagonist['want']}. Butuh: {protagonist['need']}. Cacat: {protagonist['flaw']}. Suara: {protagonist['voice']}.
- **{love['name']}** ({love['call']}) — {love['job']}. Daya tarik: {love['charm']}. Batas: {love['boundary']}. Rahasia: {love['secret']}.
- **{antagonist['name']}** ({antagonist['call']}) — {antagonist['role']}. Taktik: {antagonist['tactic']}. Titik lemah: {antagonist['vulnerability']}.
- **{ally['name']}** ({ally['call']}) — {ally['role']}. Taruhan: {ally['stake']}. Syarat bantuan: {ally['condition']}.

## Aturan Gaya

1. Bahasa Indonesia kasual urban. Boleh slang yang lazim, tetapi jangan sampai mengaburkan arti.
2. Orang ketiga dekat, kala lampau. Tidak ada head-hopping di tengah bab.
3. Satu bab = satu adegan utama. Boleh ada perpindahan tempat kecil, tetapi satu konflik.
4. Minimal 30% dialog. Dialog harus punya subteks; jangan menjelaskan semuanya.
5. Jelaskan istilah kerja sekali secara inline, lalu pakai bebas.
6. Sertakan satu detail konkret yang bisa dilihat, disentuh, atau didengar.
7. Jangan menutup bab dengan ringkasan. Tutup dengan {chapter['hook']!r} atau varian yang lebih kuat.
8. Jangan menyelesaikan hook bab sebelumnya di paragraf pertama.

## Glosarium

{chr(10).join(glossary_lines)}

## Setelah Menulis

- Simpan ke `chapters/{chapter_filename(chapter['number'])}`.
- Ubah `status: todo` menjadi `status: done`.
- Jalankan `metropop check` dari folder cerita.
- Pastikan hitungan kata berada di rentang {low}–{high}.
"""


def render_stats(story: dict[str, Any], chapter_stats: list[dict[str, Any]]) -> str:
    done = [item for item in chapter_stats if item["status"] == "done"]
    written = sum(item["words"] for item in chapter_stats)
    average = round(sum(item["words"] for item in done) / len(done)) if done else 0
    percent = round(len(done) / len(chapter_stats) * 100) if chapter_stats else 0
    lines = [
        f"# Statistik — {story['title']}",
        "",
        f"- Bab: {len(chapter_stats)}",
        f"- Selesai: {len(done)} ({percent}%)",
        f"- Kata tertulis: {written:,}",
        f"- Rata-rata bab selesai: {average:,} kata",
        f"- Target total: {total_target(story):,} kata",
        "",
        "| Fase | Bab | Selesai | Kata |",
        "|---|---|---|---|",
    ]
    for phase in story["phases"]:
        items = [c for c in chapter_stats if c["phase"] == phase["key"]]
        phase_done = [c for c in items if c["status"] == "done"]
        lines.append(
            f"| {phase['label']} | {len(items)} | {len(phase_done)} | {sum(c['words'] for c in items):,} |"
        )
    return "\n".join(lines) + "\n"

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
    "appearance": "Penampilan khas",
    "tells": "Tells fisik dan kebiasaan",
    "signature_object": "Benda khas",
    "emotional_tell": "Tell emosi",
    "lie": "Kebohongan yang diyakini",
    "never_do": "Tidak akan pernah",
    "motive": "Motif",
    "address": "Pola sapaan",
    "dialogue_sample": "Contoh dialog",
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
            "rationale", "stake", "condition", "pressure", "motive",
            "appearance", "tells", "signature_object", "emotional_tell",
            "lie", "never_do", "address", "function", "arc", "voice", "dialogue_sample",
        ]:
            value = person.get(field)
            if value:
                if isinstance(value, list):
                    separator = " · " if field == "dialogue_sample" else ", "
                    value = separator.join(str(item) for item in value)
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
- **Outline:** v{story.get("outline", {}).get("version", "0.1")} — {story.get("outline", {}).get("status", "draft")}
- **Rilis:** {story.get("release_plan", "3–5 bab per minggu")}
- **Benih acak:** `{story["seed"]}`

## Blurb

{story.get("blurb", story["logline"])}

## Pertanyaan Dramatik

{story["dramatic_question"]}

## Tema

{story["theme"]}

## Janji ke Pembaca

{story["promise"]}

## Struktur

- **Bab 1 wajib in medias res:** buka di detik kesalahan/pemicu, bukan pagi yang tenang.
- **Titik putar:** {", ".join("bab " + str(number) for number in story.get("turning_points", []))}.
- **Midpoint:** bab {story["midpoint_chapter"]}. **Klimaks:** bab {story["climax_chapter"]}.
- **Bab titik balik** boleh ±900 kata; bab biasa ±750 kata.
- **Tanpa deus ex machina:** masalah tidak selesai karena kebetulan yang menyelamatkan.

## Format Teks

- Judul bab: `## Bab N: Judul` — 2–5 kata, memancing rasa penasaran, tidak membocorkan twist.
- Chat: `**Nama:** *isi pesan*`.
- Email atau surat yang dibaca tokoh: ditulis miring.
- Tanpa emoji di narasi maupun chat.
- Satu bab = satu adegan/beat, 600–900 kata, selalu berakhir hook.

## Acuan

Dokumen utama: `Panduan Menulis Web Novel Metropop Indonesia.txt` di root repo.
Outline harus berstatus **TERKUNCI** sebelum bab ditulis. Stress test ada di
`stress-test.md`; kontinuitas ada di `ledger.md`.

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
2. Satu sumber kebenaran: `ledger.md`. Fakta hanya sah jika ada di Ledger atau teks bab yang disetujui.
3. Informasi hanya diketahui oleh tokoh yang menyaksikannya sendiri.
4. Nama, umur, jabatan, dan hubungan tidak berubah tanpa alasan yang tertulis di bab.
5. Istilah kerja dijelaskan inline pada kemunculan pertama, lalu boleh dipakai bebas.
6. Hook bab sebelumnya tidak boleh diselesaikan di paragraf pertama bab berikutnya.
7. Bab sampingan hanya boleh menambah informasi, bukan mengulang adegan dari POV lain.
8. Klimaks terjadi di bab {story["climax_chapter"]}; setelah itu tidak ada konflik baru.
9. Uang, waktu, dan jarak harus konsisten dengan yang sudah disebutkan.
10. Tidak ada tokoh baru tanpa setup; tidak ada kebetulan yang menyelamatkan protagonis.
11. Setelah setiap bab, perbarui `ledger.md`: timeline, pengetahuan, benda, setup/payoff.

## Motif

- **Refleks khas:** {protagonist.get("flaw", "-")}
- **Objek khas:** {protagonist.get("signature_object", "-")}
- **Aturan mekanisme:** {story.get("logic_rules", ["-"])[0]}
- **Tekanan keluarga:** {protagonist.get("family_pressure", "-")}

## Batasan Konten

- Nama tokoh, perusahaan, dan produk fiktif; hindari merek nyata dan tokoh publik.
- Tanpa konten eksplisit dan tanpa umpatan kasar.
- Tema berat (burnout, tekanan keluarga) ditangani dengan empati, bukan ditertawakan.

## Glosarium

{chr(10).join(glossary_lines)}

## Catatan Penulisan

- Target per bab: {story["target_words"]} kata. Bab titik balik boleh ±900 kata.
- Rentang yang diterima: 600–900 kata untuk bab biasa; 720–950 untuk bab titik balik.
- Dialog minimal 30% dari bab; sisanya narasi dan aksi.
- Setiap bab harus punya satu detail konkret: makanan, aplikasi, benda di meja, suara ruangan.
- Hook wajib menjadi kalimat terakhir bab.
- Tanpa emoji dan tanpa umpatan kasar.
- Bab 1 wajib in medias res; tiga kalimat pertama harus membuat pembaca bertanya "terus gimana?".
"""


def render_outline(story: dict[str, Any]) -> str:
    outline = story.get("outline", {})
    turning = ", ".join(f"bab {number}" for number in story.get("turning_points", []))
    lines = [
        f"# Outline — {story['title']}",
        "",
        f"{story['chapter_count']} bab × ±{story['target_words']} kata (±{total_target(story):,} kata).",
        "",
        f"**Status outline:** v{outline.get('version', '0.1')} — {outline.get('status', 'draft').upper()} "
        f"(jalankan `metropop lock` setelah stress test).",
        "",
        "**Format:** `## Bab N: Judul` · chat `**Nama:** *isi*` · email/surat miring · tanpa emoji.",
        "",
        f"**Blurb:** {story.get('blurb', story['logline'])}",
        "",
        f"**Pertanyaan dramatik:** {story['dramatic_question']}",
        "",
        f"**Rahasia utama:** {story['secret']} (jangan dibuka sebelum bab {story['midpoint_chapter']}).",
        "",
        f"**Titik putar:** {turning}. **Midpoint:** bab {story['midpoint_chapter']}. "
        f"**Klimaks:** bab {story['climax_chapter']}.",
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
        turning_note = " · **titik putar**" if chapter.get("turning_point") else ""
        beats = " ".join(
            f"{index}) {beat}" for index, beat in enumerate(chapter.get("beats", []), start=1)
        )
        lines.append(f"### Bab {chapter['number']} — {chapter['title']}{turning_note}")
        lines.append("")
        lines.append(f"- **Fase:** {chapter['phase_label']}{side}")
        lines.append(
            f"- **Hari/jam/tempat:** {chapter.get('day', '-')} · {chapter['time']} · {chapter['place']}"
        )
        lines.append(f"- **POV:** {chapter['pov']} · **Fungsi:** {chapter['function']}")
        lines.append(f"- **Tujuan adegan:** {chapter.get('goal', '-')}")
        lines.append(f"- **Adegan:** {chapter['scene']}")
        lines.append(f"- **Komplikasi:** {chapter['conflict']}")
        lines.append(f"- **Beat:** {beats}")
        lines.append(f"- **Perubahan:** {chapter.get('change', '-')}")
        lines.append(f"- **Siapa tahu apa:** {chapter.get('knowledge', '-')}")
        lines.append(f"- **Setup yang ditanam:** {chapter.get('setup', '—')}")
        lines.append(f"- **Payoff yang dibayar:** {chapter.get('payoff', '—')}")
        lines.append(f"- **Humor / awkward:** {chapter.get('humor_beat', '—')}")
        lines.append(f"- **Momen emosional:** {chapter.get('emotional_beat', '—')}")
        lines.append(f"- **Teknik naratif:** {chapter.get('technique', '-')}")
        lines.append(f"- **Hook:** {chapter['hook']} (*{chapter.get('hook_type', 'Pertanyaan')}*)")
        lines.append(f"- **Kenapa masuk akal:** {chapter.get('logic', '-')}")
        lines.append(f"- **Pertanyaan pembaca yang dijawab:** {chapter.get('reader_question', '-')}")
        lines.append(f"- **Yang TIDAK terjadi:** {chapter.get('not_happening', '-')}")
        lines.append(f"- **Target:** ±{chapter['target_words']} kata")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_chapter_skeleton(story: dict[str, Any], chapter: dict[str, Any]) -> str:
    side = "Bab sampingan. " if chapter.get("side_chapter") else ""
    beats = " ".join(
        f"{index}) {beat}" for index, beat in enumerate(chapter.get("beats", []), start=1)
    )
    return f"""---
bab: {chapter['number']}
judul: "{chapter['title']}"
status: todo
pov: "{chapter['pov']}"
target_kata: {chapter['target_words']}
waktu: "{chapter['time']}"
tempat: "{chapter['place']}"
---

## Bab {chapter['number']}: {chapter['title']}

<!-- BRIEF
Fase: {chapter['phase_label']}
Hari/jam/tempat: {chapter.get('day', '-')}, {chapter['time']}, {chapter['place']}
POV: {chapter['pov']} — {side}tetap satu POV untuk seluruh bab.
Fungsi: {chapter['function']}
Tujuan adegan: {chapter.get('goal', '-')}
Adegan: {chapter['scene']}
Komplikasi: {chapter['conflict']}
Beat: {beats}
Perubahan: {chapter.get('change', '-')}
Siapa tahu apa: {chapter.get('knowledge', '-')}
Setup: {chapter.get('setup', '—')}
Payoff: {chapter.get('payoff', '—')}
Humor/awkward: {chapter.get('humor_beat', '—')}
Momen emosional: {chapter.get('emotional_beat', '—')}
Teknik: {chapter.get('technique', '-')}
Hook wajib (kalimat terakhir): {chapter['hook']}
Logika: {chapter.get('logic', '-')}
Yang TIDAK terjadi: {chapter.get('not_happening', '-')}
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
    outline = story.get("outline", {})
    outline_state = (
        "TERKUNCI" if outline.get("status") == "locked"
        else "BELUM TERKUNCI — selesaikan stress test dan jalankan `metropop lock`."
    )
    beats = " ".join(
        f"{index}) {beat}" for index, beat in enumerate(chapter.get("beats", []), start=1)
    )

    return f"""# Paket Penulisan — {story['title']}, Bab {chapter['number']}

## Status Outline

- v{outline.get('version', '0.1')} — **{outline_state}**

## Target

- **{low}–{high} kata** (titik tengah ±{target})
- Satu adegan utama, satu POV: **{chapter['pov']}**
- {chapter.get('day', '-')} · {chapter['time']} · {chapter['place']}
- Fase: {chapter['phase_label']} · Fungsi: {chapter['function']}
- {'**Titik putar** — boleh ±900 kata.' if chapter.get('turning_point') else ('**Bab pembuka** — in medias res.' if chapter['number'] == 1 else 'Bab biasa.')}

## Brief

- **Tujuan adegan:** {chapter.get('goal', '-')}
- **Adegan:** {chapter['scene']}
- **Komplikasi:** {chapter['conflict']}
- **Beat:** {beats}
- **Perubahan:** {chapter.get('change', '-')}
- **Siapa tahu apa:** {chapter.get('knowledge', '-')}
- **Setup yang ditanam:** {chapter.get('setup', '—')}
- **Payoff yang dibayar:** {chapter.get('payoff', '—')}
- **Humor / awkward:** {chapter.get('humor_beat', '—')}
- **Momen emosional:** {chapter.get('emotional_beat', '—')}
- **Teknik naratif:** {chapter.get('technique', '-')}
- **Hook (wajib jadi kalimat terakhir):** {chapter['hook']} (*{chapter.get('hook_type', 'Pertanyaan')}*)
- **Kenapa masuk akal:** {chapter.get('logic', '-')}
- **Pertanyaan pembaca yang dijawab:** {chapter.get('reader_question', '-')}
- **Yang TIDAK terjadi:** {chapter.get('not_happening', '-')}
- **Target kata:** ±{target} (terima {low}–{high})

## Konteks Cerita

- **Logline:** {story['logline']}
- **Blurb:** {story.get('blurb', story['logline'])}
- **Pertanyaan dramatik:** {story['dramatic_question']}
- **Tema:** {story['theme']}
- **Rahasia yang belum boleh dibuka:** {story['secret']}
- **Batas pengungkapan:** jangan ungkap sebelum bab {story['midpoint_chapter']}.
- **Arah akhir (jangan ditulis sekarang):** {story['ending_direction']}

**Akhir bab sebelumnya:**
> {previous_block}
{next_block}
## Tokoh yang Relevan

- **{protagonist['name']}** ({protagonist['call']}) — {protagonist['job']}. Ingin: {protagonist['want']}. Butuh: {protagonist['need']}. Cacat: {protagonist['flaw']}. Tells: {", ".join(protagonist.get('tells', []))}. Benda khas: {protagonist.get('signature_object', '-')}. Tell emosi: {protagonist.get('emotional_tell', '-')}. Suara: {protagonist['voice']}.
- **{love['name']}** ({love['call']}) — {love['job']}. Daya tarik: {love['charm']}. Batas: {love['boundary']}. Rahasia: {love['secret']}. Tells: {", ".join(love.get('tells', []))}.
- **{antagonist['name']}** ({antagonist['call']}) — {antagonist['job'] or antagonist['role']}. Taktik: {antagonist['tactic']}. Titik lemah: {antagonist['vulnerability']}. Tells: {", ".join(antagonist.get('tells', []))}.
- **{ally['name']}** ({ally['call']}) — {ally['role']}. Taruhan: {ally['stake']}. Syarat bantuan: {ally['condition']}.

## Aturan Format

1. Judul bab di teks: `## Bab {chapter['number']}: {chapter['title']}` (2–5 kata).
2. Chat: `**Nama:** *isi pesan*`.
3. Email atau surat yang dibaca tokoh: ditulis miring.
4. Tanpa emoji di narasi maupun chat.
5. Satu bab = satu adegan/beat, selalu berakhir hook.

## Aturan Gaya

1. Bahasa Indonesia kasual urban. Pakai nggak, udah, kayak, banget, aja; jangan kaku atau terasa terjemahan.
2. Kalimat pendek, paragraf pendek, tanpa analogi aneh.
3. Orang ketiga dekat, kala lampau. Tidak ada head-hopping di tengah bab.
4. Minimal 30% dialog. Dialog harus punya subteks; jangan menjelaskan semuanya.
5. Jelaskan istilah kerja sekali secara inline, lalu pakai bebas.
6. Sertakan satu detail konkret dan satu momen awkward/konyol.
7. Jangan menutup bab dengan ringkasan. Tutup dengan {chapter['hook']!r} atau varian yang lebih kuat.
8. Jangan menyelesaikan hook bab sebelumnya di paragraf pertama.
9. Pilih 1–2 tells dari daftar tokoh; ulangi tell utama setiap 3–5 bab, jangan semuanya sekaligus.
10. Sertakan satu momen awkward/konyol yang lahir dari situasi, bukan lelucon yang dipaksakan.

## Swasunting Rubrik (1–5)

Nilai sendiri sebelum kirim. Lulus jika tidak ada nilai di bawah 4 dan total minimal 34/40:
bahasa dan suara · kejelasan · logika dan kontinuitas · kepatuhan outline ·
hook dan ritme · humor dan awkwardness · tokoh dan emosi · teknik naratif.

## Glosarium

{chr(10).join(glossary_lines)}

## Pra-cek 5 Baris (sebelum menulis)

1. Posisi cerita: {chapter.get('day', '-')}, {chapter['time']}, {chapter['place']}.
2. Kondisi protagonis: emosi, benda yang dibawa, urusan yang belum selesai.
3. Hook bab sebelumnya yang harus disambung: lihat konteks di atas.
4. Fakta Ledger yang akan dipakai: cek `ledger.md` bagian A–F.
5. Setup/payoff bab ini: {chapter.get('setup', '—')} / {chapter.get('payoff', '—')}.

## Catatan Kontinuitas (5–8 baris, setelah menulis)

- Waktu dan lokasi bab ini.
- Fakta baru yang muncul (tandai **BARU**).
- Siapa tahu apa sekarang.
- Benda atau urusan yang dibawa ke bab berikutnya.
- Setup yang ditanam atau payoff yang dibayar.
- Risiko kontinuitas yang terlihat.

## Format Pengiriman

1. Teks bab (judul `## Bab N: Judul`).
2. Catatan kontinuitas singkat.
3. Skor swasunting 8 angka dalam satu baris.
4. Penyimpangan dari outline: "tidak ada" atau daftar jujur.
5. Satu pertanyaan untuk editor, hanya jika perlu.

## Setelah Menulis

- Simpan ke `chapters/{chapter_filename(chapter['number'])}`.
- Ubah `status: todo` menjadi `status: done`.
- Perbarui `ledger.md`: timeline, siapa tahu apa, benda, setup/payoff.
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

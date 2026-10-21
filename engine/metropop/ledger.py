"""Story Ledger, stress test, and rubric scaffolds required by the guide."""

from __future__ import annotations

from typing import Any

from .text import truncate


def _people(story: dict[str, Any], chapter: dict[str, Any]) -> str:
    people = [chapter.get("pov", "-")]
    scene = chapter.get("scene", "")
    for person in story.get("cast", {}).values():
        for name in (person.get("call"), person.get("name")):
            if name and name in scene and name not in people:
                people.append(name)
    return ", ".join(people)


def _thread_rows(story: dict[str, Any]) -> list[tuple[str, int, int | None, str]]:
    threads: dict[str, dict[str, Any]] = {}
    for chapter in story.get("chapters", []):
        number = int(chapter["number"])
        setup = chapter.get("setup", "")
        if setup and setup != "—":
            for item in setup.split("; "):
                name = item.split(" — ", 1)[0].strip()
                if name:
                    threads.setdefault(name, {"plant": number, "pay": None, "desc": item})
        payoff = chapter.get("payoff", "")
        if payoff and payoff != "—":
            for item in payoff.split("; "):
                name = item.split(" — ", 1)[0].strip()
                if name:
                    threads.setdefault(name, {"plant": 0, "pay": number, "desc": item})
                    threads[name]["pay"] = number
    rows = []
    for name, info in sorted(threads.items(), key=lambda item: item[1]["plant"]):
        status = "dibayar" if info["pay"] else "terbuka"
        rows.append((name, info["plant"], info["pay"], status))
    return rows


def render_ledger(story: dict[str, Any]) -> str:
    chapters = story.get("chapters", [])
    cast = story.get("cast", {})
    world = story.get("world", {})
    lines = [
        f"# Story Ledger — {story['title']}",
        "",
        "> Dokumen hidup. Perbarui setelah setiap bab. Fakta hanya sah jika ada di sini",
        "> atau di teks bab yang sudah disetujui. Tandai fakta baru dengan **BARU**.",
        "",
        "## A. Timeline Master",
        "",
        "| Bab | Hari / jam | Lokasi | Tokoh hadir | Kejadian kunci |",
        "|---|---|---|---|---|",
    ]
    for chapter in chapters:
        lines.append(
            f"| {chapter['number']} | {chapter.get('day', '-')}, {chapter.get('time', '-')} | "
            f"{chapter.get('place', '-')} | {_people(story, chapter)} | "
            f"{truncate(chapter.get('scene', '-'), 120)} |"
        )

    locations: dict[str, list[int]] = {}
    for chapter in chapters:
        place = chapter.get("place", "-")
        locations.setdefault(place, []).append(int(chapter["number"]))
    lines.extend([
        "",
        "## B. Daftar Lokasi",
        "",
        "| Lokasi | Bab pertama | Bab muncul | Ciri tetap | Jarak / catatan |",
        "|---|---|---|---|---|",
    ])
    for place, numbers in sorted(locations.items(), key=lambda item: item[1][0]):
        joined = ", ".join(str(number) for number in numbers)
        lines.append(f"| {place} | {numbers[0]} | {joined} | isi saat menulis | isi saat menulis |")

    lines.extend([
        "",
        "## C. Matriks Pengetahuan",
        "",
        "| Fakta | Siapa tahu | Sejak bab | Dari mana |",
        "|---|---|---|---|",
        f"| Rahasia utama: {story.get('secret', '-')} | protagonis | 1 | pikiran protagonis |",
        f"| Temuan midpoint: {story.get('midpoint_text', '-')} | protagonis dan sekutu | {story.get('midpoint_chapter', '-')} | bukti |",
    ])
    for fact in story.get("knowledge_facts", []):
        lines.append(f"| {fact} | isi saat menulis | isi saat menulis | isi saat menulis |")
    lines.append(
        f"| Krisis: {story.get('crisis_text', '-')} | antagonis | {story.get('crisis_chapter', '-')} | konfrontasi |"
    )

    lines.extend([
        "",
        "## D. Status Tokoh per Bab",
        "",
        "| Bab | POV | Perubahan / emosi | Benda yang dibawa | Urusan menggantung |",
        "|---|---|---|---|---|",
    ])
    for chapter in chapters:
        pov = chapter.get("pov", "-")
        person = next(
            (item for item in cast.values() if item.get("call") == pov or item.get("name") == pov),
            {},
        )
        lines.append(
            f"| {chapter['number']} | {pov} | {truncate(chapter.get('change', '-'), 120)} | "
            f"{person.get('signature_object', 'isi saat menulis')} | "
            f"{truncate(chapter.get('hook', '-'), 100)} |"
        )

    lines.extend([
        "",
        "## E. Fakta Keras dan Angka",
        "",
        "| Fakta | Nilai | Rujukan |",
        "|---|---|---|",
        f"| Judul | {story.get('title', '-')} | sampul |",
        f"| Jumlah bab | {story.get('chapter_count', '-')} | outline |",
        f"| Target kata per bab | ±{story.get('target_words', '-')} | outline |",
        f"| Kota | {world.get('city', '-')} | bible |",
        f"| Perusahaan | {world.get('company', '-')} | bible |",
        f"| Proyek | {world.get('project', '-')} | bible |",
        f"| Klien | {world.get('client', '-')} | bible |",
    ])
    for person in cast.values():
        lines.append(
            f"| {person.get('name', '-')} | {person.get('age', '-')} tahun; {person.get('job') or person.get('role', '-')} | bible |"
        )
    lines.extend([
        "| Jumlah penerima / peserta | TETAPKAN saat outline | belum ada |",
        "| Nominal uang / gaji / utang | TETAPKAN saat outline | belum ada |",
        "| Versi file / nama dokumen | TETAPKAN saat outline | belum ada |",
        "| Jam operasional layanan | TETAPKAN saat outline | belum ada |",
        "",
        "## F. Benang Terbuka (Setup / Payoff)",
        "",
        "| Benang | Ditaman di bab | Direncanakan dibayar | Status |",
        "|---|---|---|---|",
    ])
    for name, plant, pay, status in _thread_rows(story):
        lines.append(f"| {name} | {plant or '—'} | {pay or '—'} | {status} |")

    lines.extend([
        "",
        "## G. Log Perubahan Canon",
        "",
        "| Versi | Tanggal | Perubahan | Alasan | Bab terdampak |",
        "|---|---|---|---|---|",
        "| 0.1 | — | Outline awal | — | — |",
    ])
    return "\n".join(lines) + "\n"


def render_stress_test(story: dict[str, Any]) -> str:
    chapters = story.get("chapters", [])
    midpoint = story.get("midpoint_chapter", "-")
    crisis = story.get("crisis_chapter", "-")
    questions = [
        ("Kenapa tokoh tidak memperbaiki kesalahannya sejak awal?", "Jalan keluar paling jelas harus ditutup secara eksplisit.", "Bab 2–3"),
        ("Kenapa ia tidak jujur? Apakah alasannya konsisten dengan kelemahannya?", "Hubungkan dengan cacat protagonis dan taruhan personal.", "Bab 1, 4"),
        ("Kenapa ia tidak ketahuan, atau kenapa orang lain tidak sadar?", "Periksa teks yang terlihat orang lain: judul, jam kirim, nama file, tanda tangan.", "Bab 2"),
        ("Kenapa antagonis tidak langsung menyerang? Apa yang menahannya?", "Beri motif dan batas yang masuk akal.", "Bab 4–6"),
        ("Apakah mekanisme teknisnya benar-benar mungkin?", "Tulis aturan sistem di bible dan ledger.", "Bab 2"),
        ("Siapa tahu apa pada hari itu?", "Cek matriks pengetahuan; tidak ada tokoh yang memakai informasi yang belum diterima.", "Ledger C"),
        ("Apakah setiap bukti di klimaks sudah ditanam lebih awal?", "Setiap payoff harus punya setup.", "Ledger F"),
        ("Apakah motif tiap tokoh jelas dan konkret?", "Cek lembar karakter dan rationale antagonis.", "Bible"),
        ("Apakah tokoh baru muncul tiba-tiba?", "Utamakan tokoh yang sudah ada; tokoh baru harus punya setup.", "Bible"),
        ("Apakah ada kebetulan yang menyelamatkan tokoh?", "Hapus, atau jadikan akibat dari pilihan tokoh.", "Semua bab"),
    ]
    lines = [
        f"# Stress Test Outline — {story['title']}",
        "",
        "> Isi sebelum outline dikunci. Jawaban harus merujuk bab, bukan ingatan.",
        "> Setelah semua terisi, jalankan `metropop lock`.",
        "",
        f"- Midpoint: bab {midpoint}",
        f"- Krisis: bab {crisis}",
        f"- Klimaks: bab {story.get('climax_chapter', '-')}",
        "",
        "## 1. Sepuluh Pertanyaan Skeptis",
        "",
        "| No | Pertanyaan | Jawaban | Rujukan | Status |",
        "|---|---|---|---|---|",
    ]
    for index, (question, hint, reference) in enumerate(questions, start=1):
        lines.append(f"| {index} | {question}<br>*{hint}* | isi | {reference} | BELUM |")

    lines.extend([
        "",
        "## 2. Simulasi Tiga Peran",
        "",
        "| Peran | Pertanyaan | Lubang yang ditemukan | Cara menutup |",
        "|---|---|---|---|",
        "| Pembaca awam yang curiga | \"Kok bisa dia tahu?\" | isi | isi |",
        "| Antagonis yang cerdas | \"Kenapa saya tidak melakukan hal yang lebih efektif?\" | isi | isi |",
        "| Protagonis yang logis | \"Kenapa saya tidak memilih jalan keluar paling mudah?\" | isi | isi |",
        "",
        "## 3. Uji Silang",
        "",
        "- [ ] Timeline vs lokasi konsisten.",
        "- [ ] Matriks pengetahuan tidak punya kebocoran.",
        "- [ ] Setiap bukti di klimaks punya setup.",
        "- [ ] Setiap setup punya payoff.",
        "- [ ] Tidak ada tokoh baru tanpa jejak.",
        "- [ ] Bab 1 in medias res.",
        "- [ ] Tidak ada deus ex machina.",
        "- [ ] Semua kolom outline terisi.",
        "",
        "## 4. Checklist Kunci",
        "",
        "- [ ] Semua kolom outline terisi.",
        "- [ ] Sepuluh pertanyaan skeptis terjawab.",
        "- [ ] Simulasi tiga peran selesai.",
        "- [ ] Ledger A–G sudah diisi awal.",
        "- [ ] Pemilik proyek menyetujui versi ini.",
        "",
        "Jika semua siap: `metropop lock --story \"...\"`.",
        "",
        f"Jumlah bab saat ini: {len(chapters)}.",
    ])
    return "\n".join(lines) + "\n"


def render_change_request(story: dict[str, Any]) -> str:
    return f"""# Permintaan Perubahan — {story['title']}

> Isi hanya jika saat menulis menemukan lubang atau ide yang lebih baik.
> Jangan mengubah outline diam-diam. Tunggu persetujuan pemilik proyek.

1. **Masalah:** apa yang tidak masuk akal atau bertentangan?
2. **Usulan perbaikan:** perubahan konkret yang diinginkan.
3. **Bab lain yang terdampak:** nomor bab dan bagian yang perlu diperbarui.
4. **Perlu revisi bab yang sudah ditulis?** ya/tidak, sebutkan babnya.
5. **Dampak pada Ledger:** fakta, timeline, pengetahuan, atau setup/payoff yang berubah.

Setelah disetujui: naikkan versi outline (v1.1, v1.2), catat di Ledger bagian G,
perbarui outline dan bab terdampak sebelum melanjutkan.
"""


def render_rubric(story: dict[str, Any]) -> str:
    lines = [
        f"# Rubrik Swasunting — {story['title']}",
        "",
        "Nilai 1–5 per kriteria. Bab lulus jika **tidak ada nilai di bawah 4** dan",
        "**total minimal 34/40**. Jika tidak lulus, perbaiki dulu, jangan kirim.",
        "",
        "| Bab | Bahasa | Kejelasan | Logika | Outline | Hook | Humor | Tokoh | Teknik | Total | Lulus |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for chapter in story.get("chapters", []):
        lines.append(
            f"| {chapter['number']} |  |  |  |  |  |  |  |  |  |  |"
        )
    lines.extend([
        "",
        "## Catatan Kriteria",
        "",
        "- **Bahasa dan suara:** sehari-hari, mengalir, tidak terasa terjemahan.",
        "- **Kejelasan:** pembaca awam paham; istilah asing dijelaskan sekali.",
        "- **Logika dan kontinuitas:** waktu, tempat, siapa tahu apa konsisten.",
        "- **Kepatuhan outline:** tidak ada fakta/tokoh/urutan yang berubah tanpa izin.",
        "- **Hook dan ritme:** ada perkembangan, tempo pas, akhir menarik.",
        "- **Humor dan awkwardness:** lucu dari situasi, ada momen canggung konkret.",
        "- **Tokoh dan emosi:** tells konsisten, emosi terasa tanpa dijelaskan panjang.",
        "- **Teknik naratif:** dipakai tepat guna, sesuai rencana outline.",
        "",
        "## Tes Pembaca",
        "",
        "1. Maukah aku langsung klik bab berikutnya?",
        "2. Adakah bagian yang membuatku mengernyit atau membaca dua kali?",
        "3. Adakah yang tidak masuk akal bagi orang awam?",
    ])
    return "\n".join(lines) + "\n"

# MetroPop Story Engine

Mesin perencana cerita MetroPop: premis, character sheet, bible, outline 30–40 bab,
Story Ledger, stress test, paket penulisan per bab, dan validasi naskah. Semua jalan
dengan Python 3 standar — tanpa dependensi eksternal, tanpa API key.

**Acuan tertinggi:** `../Panduan Menulis Web Novel Metropop Indonesia.txt`.
Ringkasan operasionalnya ada di `reference/panduan-utama.md`. Engine ini adalah alat
untuk memenuhi panduan itu, bukan penggantinya.

Engine **tidak menulis prosa otomatis**. Tugasnya menyiapkan kerangka yang kuat,
konsisten, dan bisa diulang; prosa ditulis oleh penulis (manusia atau agen AI) memakai
paket penulisan per bab.

## Mulai Cepat

Dari root repo:

```bash
# 1. usul 3 premis
bash engine/bin/metropop ideas

# 2. buat cerita 40 bab
bash engine/bin/metropop new "Salah Kirim" --engine salah-kirim --seed 42

# 3. isi stress test, lalu kunci outline
bash engine/bin/metropop stress --story "story/Salah Kirim"
bash engine/bin/metropop lock --story "story/Salah Kirim"

# 4. paket penulisan bab 1
bash engine/bin/metropop brief 1 --story "story/Salah Kirim"

# 5. validasi
bash engine/bin/metropop check --story "story/Salah Kirim" --strict
bash engine/bin/metropop stats --story "story/Salah Kirim"
```

Jika bit executable diizinkan, `engine/bin/metropop` bisa dipanggil langsung. Di
Android/shared storage, jalankan lewat `bash` seperti contoh di atas. Alternatif:

```bash
cd engine
python3 -m metropop ideas
```

## Perintah

| Perintah | Fungsi |
|---|---|
| `ideas` | Usul 3 opsi premis: judul, logline, tema, tokoh inti, sumber humor. |
| `new [judul]` | Buat folder cerita, `story.json`, bible, outline, Ledger, stress test, rubrik, skeleton bab. |
| `list` | Daftar cerita, jumlah bab, dan progres. |
| `brief <bab>` | Paket penulisan lengkap untuk satu bab. |
| `stress` | Cetak/isi stress test. `--refresh` menulis ulang dari outline. |
| `lock` | Validasi outline dan kunci v1.0. `--force` melewati gate stress test. |
| `ledger` | Tampilkan Story Ledger A–G. `--refresh` menulis ulang dari `story.json`. |
| `rubric` | Tampilkan rubrik swasunting 8 kriteria. `--refresh` menulis ulang. |
| `check [path]` | Validasi 30–40 bab, status, kata, heading, emoji, kolom outline. `--strict` membuat peringatan fatal. |
| `stats [path]` | Statistik kemajuan per fase. |
| `render [path]` | Tulis ulang bible/outline dari `story.json`; Ledger yang diedit tidak ditimpa. |
| `analyze <file>` | Analisis manuskrip referensi: panjang bab, hook, porsi dialog. |
| `engines` | Daftar mesin premis. |

Opsi penting `new`:

- `--engine` — `salah-kirim`, `pura-pura-pacar`, `proyek-bersama`, `identitas-salah`,
  `warisan`, `viral`.
- `--seed` — benih acak; seed sama menghasilkan rencana sama.
- `--chapters` — **30–40** bab (default 40).
- `--target` — target kata per bab (default 750).
- `--no-skeleton` — jangan buat file bab kosong.
- `--root` — folder penyimpanan cerita (default `story/`).

## Alur Kerja

1. **Premis.** `ideas` memberi 3 opsi; pilih satu atau beri premis sendiri.
2. **Buat cerita.** `new` memilih mesin, dunia, nama tokoh, dan 30–40 bab.
3. **Baca `bible.md`.** Periksa premis, character sheet, rahasia, tema, motif, batasan konten.
4. **Isi `stress-test.md`.** Jawab 10 pertanyaan skeptis, simulasi 3 peran, uji silang.
5. **Kunci outline.** `lock` memastikan semua kolom wajib terisi dan Bab 1 in medias res.
6. **Ambil paket bab.** `brief N` memberi konteks, beat, teknik, fakta Ledger, dan hook wajib.
7. **Tulis.** Isi `chapters/bab-XX.md`, ubah `status: todo` menjadi `status: done`.
8. **Perbarui Ledger.** Timeline, pengetahuan, benda, setup/payoff; lalu `check --strict`.

## Yang Ditegakkan

- **30–40 bab**; default 40.
- Target **±750 kata/bab**; rentang 600–900; titik balik 720–950.
- **Bab 1 in medias res** — dibuka di detik pemicu, bukan pagi yang tenang.
- Judul bab **2–5 kata**, heading `## Bab N: Judul`.
- Chat `**Nama:** *isi pesan*`; email/surat ditulis miring; **tanpa emoji**.
- Setiap bab punya satu POV, satu adegan/beat, satu hook.
- Kolom outline wajib: tujuan, komplikasi, 3–5 beat, perubahan, siapa tahu apa,
  setup/payoff, teknik, hook, logika, pertanyaan pembaca, yang TIDAK terjadi.
- Bab tanpa file, hook kosong, atau kolom outline kosong dianggap error.
- Bab `done` di luar rentang kata, heading salah, atau mengandung emoji menjadi peringatan;
  dengan `--strict` menjadi gagal.
- Outline harus dikunci sebelum menulis; `check` memberi peringatan jika belum.

## Struktur Engine

```text
engine/
├── bin/metropop              # wrapper shell
├── metropop/
│   ├── cli.py                # argparse, perintah
│   ├── planner.py            # premis, cast, fase, bab, hook, jadwal humor
│   ├── data.py               # bank data: 6 mesin, nama, tells, konflik, hook
│   ├── render.py             # bible, outline, skeleton, paket bab
│   ├── ledger.py             # Story Ledger, stress test, rubrik, change request
│   ├── checker.py            # validasi outline, status, kata, heading, emoji
│   ├── corpus.py             # analisis manuskrip referensi
│   ├── storage.py            # baca/tulis folder cerita
│   ├── rng.py                # RNG deterministik
│   └── text.py               # frontmatter, word count, slug
└── reference/                # panduan genre, struktur, chapter craft, panduan utama
```

## Cara Planner Bekerja

1. Pilih mesin premis dan dunia: perusahaan, pekerjaan, proyek, klien, kanal.
2. Pilih nama dan arketipe cast, lalu isi character sheet: penampilan, tells, benda khas,
   tell emosi, kebohongan yang diyakini, batas karakter, motif, pola sapaan, contoh dialog.
3. Pilih slot khusus mesin: dokumen, alasan plus-one, warisan, pemicu viral, dan seterusnya.
4. Bagi bab ke lima fase: setup 25%, eskalasi 23%, midpoint 1 bab, kejatuhan 22%, resolusi.
5. **Bab 1 = pemicu**; Bab 2–3 = konsekuensi/aturan; sisanya eskalasi sampai komitmen.
6. Tempatkan beat wajib: pemicu, reaksi, sekutu, tekanan, komitmen, midpoint, titik terendah,
   klimaks, resolusi, citra akhir.
7. Isi kolom outline wajib per bab: beat, perubahan, pengetahuan, setup/payoff, teknik,
   logika, pertanyaan pembaca, yang TIDAK terjadi.
8. Jadwalkan humor/awkward setiap 2–3 bab dan momen emosional setiap ±5 bab.
9. Tulis `story.json`, `bible.md`, `outline.md`, `ledger.md`, `stress-test.md`, `rubric.md`,
   `change-request.md`, dan skeleton bab.

Semua keputusan acak memakai `--seed`, jadi rencana bisa direproduksi.

## Outline Lock

`stress-test.md` berisi 10 pertanyaan skeptis, simulasi tiga peran (pembaca awam,
antagonis cerdas, protagonis logis), uji silang, dan checklist. Isi dulu; `lock` akan
menolak jika masih ada `BELUM`, `isi`, atau kotak kosong.

`lock` memvalidasi:

- 30–40 bab;
- judul 2–5 kata dan tidak duplikat;
- semua kolom outline terisi;
- minimal 3 beat per bab;
- Bab 1 memakai in medias res;
- stress test tidak lagi berisi placeholder.

Setelah lolos, `story.json` menyimpan `outline.status = locked`, versi 1.0, dan Ledger
bagian G dicatat. Jika perlu melewati gate stress test karena pemilik proyek sudah
menyetujui, pakai `--force`.

## Story Ledger

`ledger.md` adalah sumber kebenaran kontinuitas dan **tidak ditimpa** oleh `render`
setelah diedit. Bagian:

- A. Timeline master.
- B. Daftar lokasi.
- C. Matriks pengetahuan.
- D. Status tokoh per bab.
- E. Fakta keras dan angka.
- F. Benang setup/payoff.
- G. Log perubahan canon.

Sebelum menulis, pakai pra-cek 5 baris di `brief`; setelah menulis, isi catatan
kontinuitas 5–8 baris dan perbarui tabel yang berubah.

## Rubrik

`rubric.md` berisi 8 kriteria: bahasa/suara, kejelasan, logika/kontinuitas, kepatuhan
outline, hook/ritme, humor/awkwardness, tokoh/emosi, teknik naratif. Lulus jika tidak ada
nilai di bawah 4 dan total minimal 34/40. `brief` mengingatkan rubrik ini setiap bab.

## Format Bab

```markdown
---
bab: 7
judul: "Nama di Layar"
status: todo
pov: "Alya"
target_kata: 750
waktu: "malam"
tempat: "kantor Lintasan"
---

## Bab 7: Nama di Layar

<!-- BRIEF
... ringkasan beat, hook, teknik, setup/payoff ...
-->

Prosa dimulai di sini.
```

Status: `todo`, `draft`, `done`. Hitungan kata mengabaikan frontmatter, komentar HTML,
heading, dan penanda markdown.

## Menambah Mesin Baru

Tambahkan satu dict ke `ENGINES` di `engine/metropop/data.py`. Field wajib:

```python
{
    "key": "mesin-baru",
    "label": "Nama Mesin",
    "promise": "Janji cerita dalam satu kalimat.",
    "titles": ["Judul 1", "Judul 2"],
    "worlds": [{"company": "...", "sector": "...", "job": "...",
                "project": "...", "client": "...", "city": "Jakarta",
                "channel": "..."}],
    "inciting": "Pemicu yang terjadi di Bab 1.",
    "pemicu_hooks": ["Hook Bab 1."],
    "pemicu_complications": ["Komplikasi yang tidak bisa ditarik."],
    "secret": "...", "midpoint": "...", "crisis": "...",
    "climax": "...", "act_break": "...", "final_image": "...",
    "resolutions": ["..."], "love_jobs": ["..."], "antagonist_roles": ["..."],
    "themes": ["..."], "humor": ["..."], "logic_rules": ["..."],
    "knowledge_facts": ["..."],
    "setup_events": ["..."], "escalation_events": ["..."],
    "fallout_events": ["..."], "act3_events": ["..."],
    "glossary": {"istilah": "arti"},
}
```

`setup_events` adalah kejadian **setelah pemicu**, bukan pengulangan Bab 1. Gunakan
placeholder `{protagonis}`, `{love}`, `{antagonis}`, `{sekutu}`, `{company}`, `{client}`,
`{project}`, `{city}`, `{channel}`, `{secret}`, dan field khusus mesin. Setelah menambah
mesin, jalankan `metropop engines` dan buat cerita uji `--seed 1 --chapters 30`.

## Troubleshooting

**`Permission denied` saat menjalankan `engine/bin/metropop`.**
Shared storage Android sering melarang bit executable. Jalankan
`bash engine/bin/metropop ...` atau `cd engine && python3 -m metropop ...`.

**`Ada beberapa cerita ... Tentukan dengan --story.`**
Tambahkan `--story "story/Judul"`.

**`lock` menolak outline.**
Baca pesan error. Isi `stress-test.md` sampai tidak ada `BELUM`, `isi`, atau `- [ ]`.
`--force` hanya untuk kasus pemilik proyek sudah menyetujui.

**Hitungan kata tidak sesuai.**
`check` mengabaikan frontmatter, komentar, heading, dan markup. Pindahkan catatan ke
komentar HTML.

**Ingin mengubah struktur setelah cerita dibuat.**
`story.json` adalah sumber kebenaran. Setelah mengeditnya, jalankan
`metropop render --story "..."`. File bab dan Ledger tidak disentuh.

## Prinsip

- **Panduan adalah pakem.** Outline dikunci sebelum menulis; perubahan lewat change request.
- **Satu bab, satu beat.** Rencana jelas lebih berguna daripada prosa yang dipaksakan.
- **Kejutan dari karakter, bukan kebetulan.** Tidak ada deus ex machina.
- **Hook adalah janji.** Jangan menutup bab dengan ringkasan.
- **Kontinuitas adalah sumber kebenaran.** Ledger diperbarui setiap bab, bukan di akhir.

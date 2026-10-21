# MetroPop Story Engine

Mesin perencana cerita MetroPop: membuat premis, karakter, bible, outline 30–50 bab,
skeleton tiap bab, paket penulisan, dan validasi naskah. Semua jalan dengan Python 3
standar — tanpa dependensi eksternal, tanpa API key.

Engine ini **tidak menulis prosa otomatis**. Tugasnya menyiapkan kerangka yang kuat,
konsisten, dan bisa diulang; prosa ditulis oleh penulis (manusia atau agen AI) memakai
paket penulisan per bab.

## Mulai Cepat

Dari root repo:

```bash
# lihat mesin yang tersedia
bash engine/bin/metropop engines

# buat cerita 40 bab
bash engine/bin/metropop new "Salah Kirim" --engine salah-kirim --seed 42

# lihat paket penulisan bab 1
bash engine/bin/metropop brief 1 --story "story/Salah Kirim"

# validasi
bash engine/bin/metropop check --story "story/Salah Kirim"
bash engine/bin/metropop stats --story "story/Salah Kirim"
```

Jika bit executable diizinkan di sistemmu, `engine/bin/metropop` bisa dipanggil langsung.
Di Android/shared storage, jalankan lewat `bash` seperti contoh di atas. Alternatif lain:

```bash
cd engine
python3 -m metropop new "Judul" --seed 42
```

## Perintah

| Perintah | Fungsi |
|---|---|
| `new [judul]` | Buat folder cerita, `story.json`, `bible.md`, `outline.md`, dan skeleton bab. |
| `list` | Daftar cerita, jumlah bab, dan progres. |
| `brief <bab>` | Cetak paket penulisan lengkap untuk satu bab. |
| `check [path]` | Validasi jumlah bab, status, dan hitungan kata. `--strict` membuat peringatan fatal. |
| `stats [path]` | Statistik kemajuan per fase. |
| `render [path]` | Tulis ulang `bible.md` dan `outline.md` dari `story.json`. |
| `analyze <file>` | Analisis manuskrip referensi: panjang bab, hook, porsi dialog. |
| `engines` | Daftar mesin premis. |

Opsi penting `new`:

- `--engine` — pilih mesin: `salah-kirim`, `pura-pura-pacar`, `proyek-bersama`,
  `identitas-salah`, `warisan`, `viral`.
- `--seed` — benih acak. Seed yang sama menghasilkan rencana yang sama.
- `--chapters` — jumlah bab, minimal 30 (default 40).
- `--target` — target kata per bab (default 750).
- `--no-skeleton` — jangan buat file bab kosong.
- `--root` — folder penyimpanan cerita (default `story/`).

`brief` juga bisa menyimpan paket ke file:

```bash
bash engine/bin/metropop brief 7 --story "story/Salah Kirim" --out /tmp/bab-07-brief.md
```

## Alur Kerja

1. **Buat cerita.** `new` memilih mesin, dunia, nama tokoh, konflik, dan 30–50 bab.
2. **Baca `bible.md`.** Periksa premis, cast, rahasia, tema, dan aturan kontinuitas.
3. **Baca `outline.md`.** Setiap bab punya fase, fungsi, adegan, konflik, belokan, dan hook.
4. **Ambil paket bab.** `brief N` memberi konteks, aturan gaya, glosarium, dan hook wajib.
5. **Tulis.** Isi `chapters/bab-XX.md`, ubah `status: todo` menjadi `status: done`.
6. **Validasi.** Jalankan `check --strict`; perbaiki bab yang di luar rentang kata.
7. **Ulangi.** Satu bab = satu adegan = satu hook.

## Yang Ditegakkan

- Minimal **30 bab**; default 40; ideal 30–50.
- Target **±750 kata/bab**, rentang diterima **600–900**; bab titik balik **720–950**.
- Setiap bab punya tepat satu hook dan satu POV.
- Bab tanpa file atau dengan hook kosong dianggap error.
- Bab `done` di luar rentang kata dianggap peringatan; dengan `--strict` menjadi gagal.
- Total kata target dihitung dari target tiap bab, bukan sekadar 750 × jumlah bab.

## Struktur Engine

```text
engine/
├── bin/metropop              # wrapper shell
├── metropop/
│   ├── cli.py                # argparse, perintah
│   ├── planner.py            # premis, cast, fase, bab, hook
│   ├── data.py               # bank data: 6 mesin, nama, konflik, hook
│   ├── render.py             # bible, outline, skeleton, paket bab
│   ├── checker.py            # validasi status dan hitungan kata
│   ├── corpus.py             # analisis manuskrip referensi
│   ├── storage.py            # baca/tulis folder cerita
│   ├── rng.py                # RNG deterministik
│   └── text.py               # frontmatter, word count, slug
└── reference/                # panduan genre dan kerajinan bab
```

## Cara Planner Bekerja

1. Pilih mesin premis (atau dari `--engine`).
2. Pilih dunia: perusahaan, pekerjaan protagonis, proyek, klien, kanal komunikasi.
3. Pilih nama dan arketipe cast: protagonis, love interest, antagonis, sekutu, mentor, keluarga.
4. Isi slot khusus mesin: jenis dokumen, alasan plus-one, warisan, pemicu viral, dan seterusnya.
5. Bagi bab ke lima fase: setup 25%, eskalasi 23%, midpoint 1 bab, kejatuhan 22%, resolusi sisanya.
6. Tempatkan beat wajib: pembuka, pemicu, reaksi, sekutu, tekanan, komitmen, midpoint,
   titik terendah, klimaks, resolusi, citra akhir.
7. Isi bab lain dengan bank peristiwa mesin + komplikasi + belokan, tanpa pengulangan langsung.
8. Pilih hook dari bank per fase; fungsi penting (pembuka, pemicu, midpoint, klimaks,
   resolusi) punya hook khusus agar tidak membocorkan beat lebih awal.
9. Tulis `story.json`, `bible.md`, `outline.md`, dan skeleton bab.

Semua keputusan acak memakai `--seed`, jadi rencana bisa direproduksi dan dibandingkan.

## Format Bab

Setiap file bab memakai frontmatter sederhana:

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

# Bab 7: Nama di Layar

<!-- BRIEF
... ringkasan beat dan hook ...
-->

Prosa dimulai di sini.
```

Status yang dikenal: `todo`, `draft`, `done`. Hitungan kata mengabaikan frontmatter,
komentar HTML, heading, dan penanda markdown.

## Menambah Mesin Baru

Tambahkan satu dict ke `ENGINES` di `engine/metropop/data.py`. Field wajib:

```python
{
    "key": "mesin-baru",
    "label": "Nama Mesin",
    "setup_mode": "inciting_first",  # atau inciting_second / inciting_third
    "promise": "Janji cerita dalam satu kalimat.",
    "titles": ["Judul 1", "Judul 2"],
    "worlds": [{"company": "...", "sector": "...", "job": "...",
                "project": "...", "client": "...", "city": "Jakarta",
                "channel": "..."}],
    "inciting": "...", "secret": "...", "midpoint": "...",
    "crisis": "...", "climax": "...", "act_break": "...",
    "final_image": "...", "resolutions": ["..."],
    "love_jobs": ["..."], "antagonist_roles": ["..."],
    "themes": ["..."],
    "setup_events": ["..."], "escalation_events": ["..."],
    "fallout_events": ["..."], "act3_events": ["..."],
    "glossary": {"istilah": "arti"},
}
```

Gunakan placeholder yang tersedia: `{protagonis}`, `{love}`, `{antagonis}`, `{sekutu}`,
`{company}`, `{client}`, `{project}`, `{city}`, `{channel}`, `{secret}`, dan field
khusus mesin. Setelah menambah mesin, jalankan `metropop engines` dan buat satu cerita
uji dengan `--seed 1 --chapters 30`.

## Troubleshooting

**`Permission denied` saat menjalankan `engine/bin/metropop`.**
Shared storage Android sering melarang bit executable. Jalankan `bash engine/bin/metropop ...`
atau `cd engine && python3 -m metropop ...`.

**`Ada beberapa cerita ... Tentukan dengan --story.`**
Ada lebih dari satu folder cerita dan kamu menjalankan perintah dari root. Tambahkan
`--story "story/Judul"`.

**Hitungan kata tidak sesuai.**
`check` mengabaikan frontmatter, komentar, heading, dan markup. Kata dihitung dari prosa
yang tersisa. Jika kamu memakai catatan di dalam bab, pindahkan ke komentar HTML.

**Ingin mengubah struktur setelah cerita dibuat.**
`story.json` adalah sumber kebenaran. Setelah mengeditnya, jalankan
`metropop render --story "..."` untuk memperbarui bible dan outline. File bab yang sudah
ditulis tidak disentuh.

## Prinsip

- **Satu bab, satu beat.** Rencana yang jelas lebih berguna daripada prosa yang dipaksakan.
- **Kejutan dari karakter, bukan dari kebetulan.** Semua belokan harus bisa dilacak ke motif tokoh.
- **Hook adalah janji.** Jangan menutup bab dengan ringkasan; tutup dengan pertanyaan baru.
- **Konsistensi lebih penting daripada kecanggihan.** Nama, umur, uang, dan waktu tidak berubah diam-diam.

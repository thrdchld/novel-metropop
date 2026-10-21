# Folder Story

Satu cerita = satu folder, dinamai sesuai judul. Semua hasil engine dan naskah disimpan
di sini. Acuan penulisan: `../Panduan Menulis Web Novel Metropop Indonesia.txt` dan
ringkasan `../engine/reference/panduan-utama.md`.

```text
story/
└── Salah Kirim/
    ├── story.json          # sumber kebenaran: premis, cast, bab, hook, seed, outline
    ├── bible.md            # snapshot: premis, character sheet, aturan, motif
    ├── outline.md          # peta 30–40 bab + kolom outline wajib
    ├── ledger.md           # Story Ledger A–G (dokumen hidup)
    ├── stress-test.md      # 10 pertanyaan skeptis + simulasi 3 peran
    ├── rubric.md           # rubrik swasunting 8 kriteria per bab
    ├── change-request.md   # template permintaan perubahan outline
    └── chapters/
        ├── bab-01.md
        ├── bab-02.md
        └── ...
```

## File Mana yang Diedit

| File | Boleh diedit? | Catatan |
|---|---|---|
| `story.json` | Ya, hati-hati | Sumber kebenaran untuk `brief`, `check`, `stats`, `lock`. |
| `bible.md` | Ya | Catatan kreatif. `render` menimpanya dari `story.json`. |
| `outline.md` | Ya | Peta bacaan. Perubahan struktural sebaiknya di `story.json`. |
| `ledger.md` | Ya, wajib | Dokumen hidup; diperbarui setiap bab. `render` tidak menimpanya. |
| `stress-test.md` | Ya, wajib | Harus diisi sebelum `lock`. |
| `rubric.md` | Ya | Isi skor 1–5 setiap bab. |
| `change-request.md` | Ya | Dipakai jika menemukan lubang/ide baru saat menulis. |
| `chapters/bab-XX.md` | Ya | Tempat menulis prosa. |

Jika mengubah `story.json`, jalankan:

```bash
bash engine/bin/metropop render --story "story/Judul"
```

Perintah itu menulis ulang `bible.md` dan `outline.md`; file bab dan Ledger tidak disentuh.

`ledger`, `stress`, dan `rubric` bisa diregenerasi dengan `--refresh`:

```bash
bash engine/bin/metropop ledger --story "story/Judul" --refresh
```

Hati-hati: `--refresh` menimpa isian manual. Lakukan hanya jika ingin memulai ulang
dokumen itu dari `story.json`.

## Status Bab

```yaml
---
bab: 1
judul: "Pesan Masuk"
status: todo
pov: "Alya"
target_kata: 750
waktu: "Jumat malam"
tempat: "kantor Lintasan"
---
```

- `todo` — belum ditulis. Tidak dihitung sebagai kesalahan.
- `draft` — sudah ada isi, belum selesai.
- `done` — selesai; hitungan kata, heading, dan emoji diperiksa.

## Alur Kerja

```bash
# 0. usul premis
bash engine/bin/metropop ideas

# 1. buat cerita 30–40 bab
bash engine/bin/metropop new "Judul" --engine salah-kirim --seed 42

# 2. isi stress test (10 pertanyaan + 3 peran)
bash engine/bin/metropop stress --story "story/Judul"

# 3. kunci outline
bash engine/bin/metropop lock --story "story/Judul"

# 4. paket bab 1
bash engine/bin/metropop brief 1 --story "story/Judul"

# 5. tulis chapters/bab-01.md, ubah status menjadi done, perbarui ledger.md

# 6. validasi dan progres
bash engine/bin/metropop check --story "story/Judul" --strict
bash engine/bin/metropop stats --story "story/Judul"

# 7. ulangi untuk bab berikutnya
bash engine/bin/metropop brief 2 --story "story/Judul"
```

## Outline Lock

Outline adalah pakem. Sebelum `lock`:

- semua kolom outline per bab terisi;
- judul bab 2–5 kata dan tidak duplikat;
- Bab 1 memakai in medias res;
- `stress-test.md` tidak lagi berisi `BELUM`, `isi`, atau `- [ ]`;
- pemilik proyek menyetujui versi ini.

`lock` yang berhasil menulis `outline.status = locked` dan versi 1.0. Jika menemukan
lubang setelah outline dikunci, isi `change-request.md`; jangan mengubah outline diam-diam.
Setelah disetujui, naikkan versi (v1.1, v1.2) dan catat di Ledger bagian G.

## Story Ledger

`ledger.md` adalah sumber kebenaran kontinuitas. Setelah setiap bab, perbarui:

- **A. Timeline:** hari/jam, lokasi, tokoh hadir, kejadian kunci.
- **B. Lokasi:** ciri tetap, jarak.
- **C. Pengetahuan:** siapa tahu apa, sejak kapan, dari mana.
- **D. Status tokoh:** emosi, benda, urusan menggantung.
- **E. Fakta keras:** angka, nama, jabatan, aturan sistem.
- **F. Setup/payoff:** benang yang masih terbuka.
- **G. Log perubahan canon.**

Jangan mengarang fakta dari ingatan. Jika tidak ada di Ledger atau teks bab, tandai
`[PERIKSA]` dan tanyakan ke editor.

## Aturan

- **30–40 bab** per cerita.
- Target **±750 kata** per bab; rentang 600–900 (titik balik 720–950).
- **Bab 1 wajib in medias res.**
- Satu bab satu POV, satu adegan/beat, satu hook di kalimat terakhir.
- Judul bab 2–5 kata; heading `## Bab N: Judul`.
- Chat `**Nama:** *isi pesan*`; email/surat ditulis miring; tanpa emoji.
- Istilah asing dijelaskan sekali secara inline.
- Jangan mengubah nama, umur, jabatan, atau fakta keras tanpa memperbarui `story.json`,
  bible, dan Ledger.
- Jangan membuka rahasia utama sebelum bab midpoint.
- Bab sampingan maksimal 10–15% dari total.
- Tidak ada tokoh baru tanpa setup; tidak ada deus ex machina.
- Setiap bab harus menaikkan taruhan, memberi informasi baru, atau mendalamkan hubungan.

## Nama Folder

Folder memakai judul apa adanya. Karakter path yang tidak valid (`/ \ : * ? " < > |`)
diganti tanda hubung. Spasi diperbolehkan; kutip path saat memanggil perintah.

## Melihat Progres

```bash
bash engine/bin/metropop list
bash engine/bin/metropop stats --story "story/Judul"
bash engine/bin/metropop check --story "story/Judul"
bash engine/bin/metropop ledger --story "story/Judul"
bash engine/bin/metropop rubric --story "story/Judul"
```

`check` tanpa path akan memeriksa semua cerita di folder ini.

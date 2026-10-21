# Folder Story

Satu cerita = satu folder, dinamai sesuai judul. Semua hasil engine disimpan di sini.

```text
story/
└── Salah Kirim/
    ├── story.json          # sumber kebenaran: premis, cast, bab, hook, seed
    ├── bible.md            # snapshot yang dibaca manusia
    ├── outline.md          # peta 30–50 bab
    └── chapters/
        ├── bab-01.md
        ├── bab-02.md
        └── ...
```

## File Mana yang Diedit

| File | Boleh diedit? | Catatan |
|---|---|---|
| `story.json` | Ya, hati-hati | Sumber kebenaran untuk `brief`, `check`, `stats`. |
| `bible.md` | Ya | Catatan kreatif. Jalankan `render` jika ingin dibuat ulang. |
| `outline.md` | Ya | Peta bacaan. Perubahan struktural sebaiknya di `story.json`. |
| `chapters/bab-XX.md` | Ya | Tempat menulis prosa. |

Jika mengubah `story.json`, jalankan:

```bash
bash engine/bin/metropop render --story "story/Judul"
```

Perintah itu hanya menulis ulang `bible.md` dan `outline.md`; file bab tidak disentuh.

## Status Bab

Di frontmatter setiap bab:

```yaml
---
bab: 1
judul: "Draft"
status: todo
pov: "Alya"
target_kata: 750
waktu: "pagi"
tempat: "kantor Lintasan"
---
```

- `todo` — belum ditulis. Tidak dihitung sebagai kesalahan.
- `draft` — sudah ada isi, belum selesai.
- `done` — selesai; hitungan kata diperiksa.

Ubah `status: todo` menjadi `status: done` setelah bab selesai.

## Alur Kerja

```bash
# 1. buat cerita
bash engine/bin/metropop new "Judul" --engine salah-kirim --seed 42

# 2. baca bible dan outline
# 3. ambil paket bab 1
bash engine/bin/metropop brief 1 --story "story/Judul"

# 4. tulis chapters/bab-01.md, ubah status menjadi done
# 5. validasi
bash engine/bin/metropop check --story "story/Judul" --strict

# 6. ulangi untuk bab berikutnya
bash engine/bin/metropop brief 2 --story "story/Judul"
```

## Aturan

- Minimal **30 bab** per cerita.
- Target **±750 kata** per bab; rentang 600–900 (bab titik balik 720–950).
- Satu bab satu POV, satu adegan utama, satu hook di kalimat terakhir.
- Jangan mengubah nama, umur, atau jabatan tanpa memperbarui `story.json` dan bible.
- Jangan membuka rahasia utama sebelum bab midpoint.
- Simpan bab sampingan maksimal 10–15% dari total.

## Nama Folder

Folder memakai judul apa adanya. Karakter yang tidak valid di path (`/ \ : * ? " < > |`)
diganti tanda hubung. Spasi diperbolehkan; kutip path saat memanggil perintah:

```bash
bash engine/bin/metropop check --story "story/Salah Kirim"
```

## Melihat Progres

```bash
bash engine/bin/metropop list
bash engine/bin/metropop stats --story "story/Judul"
bash engine/bin/metropop check --story "story/Judul"
```

`check` tanpa path akan memeriksa semua cerita di folder ini.

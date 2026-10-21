# Folder Story

Satu cerita = satu folder, dinamai sesuai judul. Semua canon, outline, ledger, dan naskah
disimpan di sini. Folder ini dibaca oleh agent sebelum menulis.

Acuan penulisan: `../Panduan Menulis Web Novel Metropop Indonesia.txt` dan
`../engine/` (terutama `00-workflow.md`, `03-structure.md`, `07-continuity.md`).

## Struktur

```text
story/
└── <Judul>/
    ├── canon.md          # sumber kebenaran: premis, cast, aturan, motif, ending
    ├── outline.md        # peta 30–40 bab + kolom wajib
    ├── ledger.md         # Story Ledger A–G (dokumen hidup)
    ├── feedback.md       # catatan feedback user dan tindakan
    └── chapters/
        ├── bab-01.md
        ├── bab-02.md
        └── ...
```

Gunakan template di `../engine/templates/`. Jangan mengarang format baru.

## Cara Memulai Cerita Baru

Minta agent:

> Baca `AGENTS.md` dan `engine/README.md`. Saya mau mulai novel MetroPop baru
> berjudul "...".

Agent akan:

1. bertanya maksimal 3 hal yang belum jelas;
2. membuat folder ini dari template;
3. mengisi `canon.md`;
4. menyusun `outline.md` dan stress test;
5. meminta persetujuan;
6. menandai outline **TERKUNCI v1.0**;
7. menulis Bab 1.

Jangan menulis bab sebelum outline terkunci.

## Cara Melanjutkan

Minta agent:

> Baca `AGENTS.md`, `engine/README.md`, dan `story/<Judul>/`. Lanjutkan bab berikutnya.

Agent membaca `canon.md`, `ledger.md`, dan 1–2 bab terakhir, lalu menulis posisi cerita
5 baris sebelum menulis.

## Cara Revisi

Minta agent:

> Baca `engine/09-revision.md`. Revisi Bab 5: ...

Agent mengklasifikasikan feedback, merevisi lokal, memperbarui ledger/canon, dan mencatat
pelajaran jika perlu.

## File dan Tanggung Jawab

| File | Isi | Kapan diperbarui |
|---|---|---|
| `canon.md` | Premis, cast, aturan, motif, ending | Saat canon berubah, dengan persetujuan |
| `outline.md` | Peta bab + kolom wajib | Sebelum menulis; perubahan lewat change request |
| `ledger.md` | Timeline, pengetahuan, benda, setup/payoff | Setelah setiap bab |
| `feedback.md` | Feedback user dan tindakan | Setelah revisi |
| `chapters/bab-NN.md` | Prosa | Setiap bab |

## Aturan

Aturan lengkap dimiliki file di `../engine/`:

- format/struktur: `03-structure.md`
- gaya dan format teks: `05-style.md`
- kerajinan bab: `06-chapter.md`
- kontinuitas: `07-continuity.md`
- rubrik: `08-quality.md`

Ringkasan ini bukan sumber aturan. Jika berbeda, file pemilik menang.

Yang khusus folder ini:

- Simpan bab ke `chapters/bab-NN.md`.
- Perbarui `ledger.md` setelah setiap bab.
- Perubahan canon/outline hanya dengan persetujuan user.
- Catat feedback di `feedback.md`.

## Nama Folder

Folder memakai judul apa adanya. Karakter path yang tidak valid (`/ \ : * ? " < > |`)
diganti tanda hubung. Spasi diperbolehkan.

## Ledger dan Canon

- `canon.md` menjawab “apa yang benar di cerita ini”.
- `ledger.md` menjawab “apa yang terjadi, kapan, di mana, dan siapa tahu apa”.
- Jika dua bab bertentangan, laporkan dan usulkan versi yang dipertahankan.
- Jangan mengarang fakta dari ingatan. Tandai `[PERIKSA]` jika tidak yakin.

## Catatan

Engine Python lama sudah dihapus. Jika perlu referensi implementasi, ambil dari riwayat
git sebelum commit migrasi.

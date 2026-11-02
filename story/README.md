# Folder Story

Satu cerita = satu folder, dinamai sesuai judul. Semua canon, outline, ledger, dan naskah
disimpan di sini. Folder ini wajib dibaca oleh agent sebelum menulis bab berikutnya.

## Acuan Utama

1. **Gaya Bahasa, Diksi, & Penceritaan:** `../acuan-bahasa.docx` dan `../engine/05-style.md`.
2. **Kerangka Plot, Premis, Siklus Coba-Gagal, Planting, & Evaluasi Alur:** `../Kerangka Plot yang Terbukti untuk Web Novel.md`, `../engine/02-premise.md`, `../engine/03-structure.md`, dan `../engine/08-quality.md`.
3. **Alur Kerja & Kontinuitas:** `../AGENTS.md`, `../engine/00-workflow.md`, dan `../engine/07-continuity.md`.
4. **Arsip Panduan Lama:** `../old-documents-unneeded/` (hanya referensi tambahan).

Target pembaca **13+**; latar dan usia tokoh bebas. **Prinsip Pas:** teknik naratif, subplot,
flashback, dan scene ikonik bersifat opsional (boleh nol jika cerita sudah padat).

## Struktur Folder Cerita

```text
story/
├── universe-registry.md  # pendaftar semesta terpadu (portofolio, bank premis, roster tokoh, entitas dunia, protokol cameo 3 tingkat)
└── <Judul>/
    ├── canon.md          # sumber kebenaran: premis (5 slot), kerangka plot, planting 2x, cast, aturan, ending
    ├── outline.md        # peta 30–40 bab (min 6–8 titik balik) + siklus coba-gagal + kolom wajib
    ├── ledger.md         # Story Ledger A–G (dokumen hidup kontinuitas fakta)
    ├── feedback.md       # catatan feedback user dan tindakan revisi
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
2. menjalankan **Uji 5 Slot Kelayakan Premis** dan **7 Langkah Menentukan Kerangka Plot**;
3. membuat folder cerita dari template;
4. mengisi `canon.md` (termasuk rencana **Planting Solusi 2 Kali**);
5. menyusun `outline.md` (lengkap dengan **Siklus Coba-Gagal 6 Komponen**) dan menjalankan **Stress Test (10 Uji Logika & 10 Tanda Bahaya)**;
6. meminta persetujuan user dan menandai outline **TERKUNCI v1.0**;
7. menulis **Bab 1** saja (600–900 kata, *in medias res*, tanpa em dash, tanpa quote di atas bab).

## Cara Melanjutkan Cerita

Minta agent:

> Baca `AGENTS.md`, `engine/README.md`, dan `story/<Judul>/`. Lanjutkan bab berikutnya.

Agent membaca `canon.md`, `outline.md`, `ledger.md`, dan 1–2 bab terakhir, menampilkan
**posisi cerita 5 baris**, meminta konfirmasi, lalu menulis satu bab (600–900 kata).

## Cara Revisi & Evaluasi Alur Cerita

Minta agent:

> Baca `engine/08-quality.md` dan `engine/09-revision.md`. Analisis/revisi alur cerita ini: ...

Agent menjalankan **Diagnosis Alur Cerita** (Uji 5 Slot, 8 Kerangka, Uji 100% Siklus, Planting 2x, 10 Uji Logika, dan 10 Tanda Bahaya), mengklasifikasikan feedback, melakukan revisi lokal, serta memperbarui `ledger.md` dan `canon.md`.

## File dan Tanggung Jawab

| File | Isi Utama | Kapan Diperbarui |
|---|---|---|
| `canon.md` | Premis 5 slot, kerangka plot, planting 2x, cast, aturan dunia, ending | Saat canon berubah (dengan persetujuan user) |
| `outline.md` | Peta babak, siklus coba-gagal, dan rincian per bab | Sebelum menulis; perubahan lewat `change-request.md` |
| `ledger.md` | Timeline, matriks pengetahuan, benda, angka keras, setup/payoff | Setiap selesai menulis/merevisi satu bab |
| `feedback.md` | Log feedback user dan tindakan perbaikan | Setiap selesai revisi |
| `chapters/bab-NN.md` | Naskah prosa bab (600–900 kata) | Setiap bab selesai ditulis |

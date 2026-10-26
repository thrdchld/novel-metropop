# Engine — Otak Agent MetroPop

Folder ini adalah **skill/prompt package** untuk agent penulis. Tidak ada kode yang
perlu dijalankan. Agent cukup membaca markdown di sini, lalu bekerja lewat percakapan.

**Acuan gaya bahasa & cara penulisan:** `../acuan-bahasa.docx` (contoh novel dengan
gaya bahasa, diksi, pilihan kata, dan gaya bercerita yang diinginkan).
**Acuan kerangka plot, premis, & evaluasi alur:** `../Kerangka Plot yang Terbukti untuk Web Novel.md`
(8 kerangka plot terbukti, uji kelayakan 5 slot, resep 9 langkah premis baru, siklus coba-gagal, planting solusi 2x, 10 uji logika, dan 10 tanda bahaya).
Dokumen panduan lama diarsipkan di `../old-documents-unneeded/` sebagai referensi tambahan. Ringkasan
operasional ada di `00-workflow.md` dan file-file di folder ini.

**Prinsip Pas:** teknik naratif, subplot, flashback, dan scene ikonik adalah alat
opsional. Boleh nol jika cerita sudah padat. Jangan memaksakan.

## Cara Kerja

1. Agent membaca `AGENTS.md` di root repo.
2. Agent membaca file ini, lalu `00-workflow.md`.
3. Agent memeriksa `../story/`.
4. Jika sesi baru, agent membalas ringkasan 5 poin + tahap A–G yang relevan.
5. Agent bertanya **satu** pertanyaan: mau ide, project baru, lanjut, revisi, atau riset?
6. Agent mengikuti mode yang dipilih.
7. Setiap selesai bab, agent memperbarui `ledger.md` dan menilai dengan rubrik.
8. Jika feedback berulang, agent memperbarui file di `learnings/` dan file panduan.

## Peta File

| File | Isi |
|---|---|
| `README.md` | Peta paket dan aturan baca. |
| `SKILL.md` | Ringkasan skill untuk tool yang mendukung skill. |
| `00-workflow.md` | Alur sesi, pertanyaan, mode kerja, dan definition of done. |
| `01-genre.md` | Definisi MetroPop, janji pembaca, tone, batasan konten. |
| `02-premise.md` | Rumus 1 kalimat, uji 5 slot, 7 langkah pilih kerangka, resep 9 langkah ide baru, 3 opsi. |
| `03-structure.md` | 8 kerangka plot terbukti, pemetaan 8 tahap, siklus coba-gagal, planting 2x, 30–40 bab, kolom outline. |
| `04-character.md` | Character sheet, tells, dialog, cast, arc. |
| `05-style.md` | Gaya bahasa, POV, dialog, format, before/after. |
| `06-chapter.md` | Struktur bab 600–900 kata, hook, checklist. |
| `07-continuity.md` | Canon, ledger A–G, timeline, pengetahuan, setup/payoff. |
| `08-quality.md` | Rubrik 8 kriteria, 10 uji logika alur, 10 tanda bahaya, stress test. |
| `09-revision.md` | Diagnosis alur cerita, cara menangani feedback, dan revisi lokal. |
| `10-evolution.md` | Cara memperbarui engine dari feedback/teori baru. |
| `templates/` | Template canon, outline, chapter, ledger, character sheet, feedback, idea list. |
| `examples/` | Contoh premis, outline, adegan, dan perbaikan gaya. |
| `sources.md` | Aturan riset, PDF, internet, hak cipta, dan pencatatan sumber. |
| `learnings/` | Kritik editor dan changelog aturan engine. |

## Pemilik Aturan

File-file ini adalah sumber aturan. File lain hanya merujuk, tidak menduplikasi.

| Aturan | File pemilik |
|---|---|
| Alur sesi, tahap A–G, Prinsip Pas | `00-workflow.md` |
| Genre dan batasan konten | `01-genre.md` |
| Premis dan novelty | `02-premise.md` |
| Struktur, outline, lock | `03-structure.md` |
| Karakter dan character sheet | `04-character.md` |
| Gaya bahasa dan format | `05-style.md` |
| Kerajinan bab | `06-chapter.md` |
| Kontinuitas dan Ledger | `07-continuity.md` |
| Rubrik dan anti plot hole | `08-quality.md` |
| Revisi | `09-revision.md` |
| Evolusi engine | `10-evolution.md` |
| Riset dan sumber | `sources.md` |

## Aturan Baca

- Folder ini adalah paket markdown. Tidak ada kode yang perlu dijalankan.
- Target pembaca **13+**; latar dan usia tokoh bebas.
- **Prinsip Pas:** alat tambahan opsional; boleh nol.
- Jangan menulis prosa sebelum mode dipilih, canon ada, dan outline disetujui.
- Jangan mengubah canon/outline diam-diam.
- Jangan menambah tokoh baru tanpa setup.
- Jangan memakai emoji atau umpatan kasar.
- Satu bab per respons adalah default.

## Mulai Cepat

**Project baru:**

> Baca `AGENTS.md` dan `engine/README.md`. Saya mau mulai novel MetroPop baru.

Agent akan menanyakan maksimal 3 hal yang belum jelas. Default: 30–40 bab, ±750 kata,
tone hangat/jenaka/getir, ending tidak sempurna namun memuaskan (ada harga nyata yang dibayar). Jika premis belum ada, agent
memberi 3 opsi premis dulu (menggunakan Resep 9 Langkah & Uji 5 Slot).

**Lanjutkan cerita:**

> Baca `AGENTS.md`, `engine/README.md`, dan `story/<Judul>/`. Lanjutkan bab berikutnya.

Agent akan membaca canon, ledger, dan bab terakhir; menulis posisi cerita 5 baris;
meminta konfirmasi; lalu menulis satu bab.

**Revisi:**

> Baca `AGENTS.md` dan `engine/09-revision.md`. Revisi Bab 5: ...

Agent akan mengklasifikasikan feedback, merevisi lokal, memperbarui ledger/canon, dan
mencatat pelajaran jika perlu.

## Struktur Story

Setiap cerita di `story/` memakai:

```text
story/<Judul>/
├── canon.md
├── outline.md
├── ledger.md
├── feedback.md
└── chapters/
    ├── bab-01.md
    └── ...
```

Gunakan template di `templates/`. Jangan mengarang format baru.

## Prinsip

- **Canon adalah sumber kebenaran untuk fakta cerita.** Aturan craft/format ada di
  file pemilik di tabel atas.
- **Outline adalah pakem.** Perubahan lewat Permintaan Perubahan.
- **Satu bab, satu beat.** Jangan menulis semua bab sekaligus.
- **Rubrik sebelum kirim.** Perbaiki dulu jika belum lulus.
- **Engine belajar dari feedback.** Perubahan aturan dicatat, bukan diam-diam.

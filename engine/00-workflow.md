# 00 — Alur Kerja (Workflow A–G) & Smart-Reading

> **File Pemilik Tunggal:** File ini mengatur **Tahap Proyek A–G, Protokol Smart-Reading (Efisiensi Konteks AI), Urutan Mode Kerja A–E, Loop Pasca-Tulis Bab, dan Definition of Done**.

---

## 1. Tahap Proyek A–G (Dari Ide Sampai Novel Selesai)

| Tahap | Fokus Kerja | Dokumen Utama | Selesai Jika |
|---|---|---|---|
| **A. Ide & Premis** | Cek `story/universe-registry.md`, susun ABCD, jalankan Brainstorming 7 Langkah, tutup jalan mudah (7 cara), uji *Spider-Man Test* & 5 Slot | `02-premise.md`, `story/universe-registry.md` | Pengguna memilih premis & konflik inti, tercatat di Universe Registry |
| **B. Dokumen Dasar (Canon)** | Isi `canon.md` (5 slot, 5+ jalan mudah tertutup, kerangka plot, planting 2x, cast, world building, matriks sapaan) & inisialisasi `state.md` | `02-premise.md`, `04-character.md`, `11-worldbuilding.md`, `templates/` | Pengguna menyetujui `canon.md` |
| **C. Outline Per Bab** | Susun 30–40 bab (min 6–8 titik balik, 3–6 siklus coba-gagal lolos Uji 100%, planting 2x, 18 kolom per bab) | `03-structure.md`, `templates/outline.md` | Seluruh bab terisi 18 kolom lengkap |
| **D. Stress Test** | Uji dengan 10 Uji Logika, 10 Tanda Bahaya, Tabel Uji Menutup Jalan Mudah, Uji Ruang Lingkup Minimal, & Pelacakan Mundur dari Klimaks | `02-premise.md`, `08-quality.md` | Semua lubang logika tertutup |
| **E. Lock Outline** | Presentasikan ringkasan outline & penutupan lubang logika ke pengguna | `story/<Judul>/outline.md` | Status ditandai **TERKUNCI v1.0** |
| **F. Tulis Bab (1 per 1)** | Tampilkan *Pre-Flight Continuity Gate* 5 poin -> tulis 1 bab (600–900 kata, teks polos, tone `acuan-bahasa.docx`) -> update `state.md` & `ledger.md` -> jalankan linter Python | `05-style.md`, `06-chapter.md`, `07-continuity.md`, `08-quality.md` | Lulus rubrik ≥34/40 & 0 error linter |
| **G. Revisi & Audit** | Audit 5 Tahap & Remediasi Beruntun R1–R5, Revisi 4 Lapis dengan rasio 74/18/8 | `09-revision.md` | Pengguna puas & bebas regresi |

---

## 2. Protokol Smart-Reading (Agar AI Tidak Bingung / Kebanjiran Konteks)

**ATURAN PENTING:** Jangan membaca seluruh file di repo sekaligus! Baca **HANYA** file yang relevan dengan mode yang sedang dikerjakan:

| Mode / Tugas Saat Ini | File yang WAJIB Dibaca | File yang DILARANG Dibaca |
|---|---|---|
| **Pembuka Sesi Baru** | `AGENTS.md`, `engine/README.md`, `engine/00-workflow.md`, cek daftar folder di `story/` | Bab cerita, `engine/learnings/`, dan file detail lainnya |
| **Mode A (Brainstorming Ide / Premis / Konflik)** | `story/universe-registry.md`, `engine/01-genre.md`, `engine/02-premise.md` | `06-chapter.md`, `07-continuity.md`, `09-revision.md`, `learnings/` |
| **Mode B (Project Baru: Canon & Outline)** | `story/universe-registry.md`, `engine/02-premise.md`, `engine/03-structure.md`, `engine/04-character.md`, `engine/08-quality.md`, `engine/11-worldbuilding.md`, `engine/templates/` | `09-revision.md`, `10-evolution.md`, `learnings/` |
| **Mode C (Menulis Bab Baru)** | `story/<Judul>/state.md`, `canon.md`, `outline.md` (bab terkait), `ledger.md`, 1–2 bab terakhir, `engine/05-style.md`, `engine/06-chapter.md`, `engine/07-continuity.md` | `story/universe-registry.md`, `01-genre.md`, `02-premise.md`, `learnings/`, bab-bab lama yang jauh |
| **Mode D (Revisi Bab / Audit Alur)** | `engine/05-style.md`, `engine/08-quality.md`, `engine/09-revision.md`, `canon.md`, `state.md`, `ledger.md`, bab yang direvisi | `01-genre.md`, `templates/`, `learnings/` |
| **Mode E (Riset / Update Engine)** | `engine/sources.md`, `engine/10-evolution.md`, dan file pemilik yang akan di-update | File cerita yang tidak sedang diubah |

**Prinsip Pas:** Teknik naratif, subplot, flashback, dan scene ikonik adalah alat opsional (angka adalah batas atas, **boleh nol** jika cerita sudah padat).

---

## 3. Mulai Sesi

1. Pada awal sesi baru, beri **ringkasan pemahaman 5 poin**, sebutkan posisi folder `story/` dalam 2–3 baris, dan sebutkan tahap A–G yang relevan.
2. Ajukan **satu pertanyaan pembuka**:
   > Mau apa hari ini: (A) cari ide/premis baru, (B) mulai project baru, (C) lanjutkan cerita yang ada, (D) revisi/evaluasi cerita, atau (E) analisis referensi/riset?
3. Jangan menulis prosa sebelum mode dipilih dan outline terkunci.

---

## 4. Rincian Mode Kerja A–E

### Mode A: Ide, Premis (ABCD Ringkas), & Pengembangan ke Kerangka Cerita
1. Baca `story/universe-registry.md`, `01-genre.md`, dan `02-premise.md`.
2. Patuhi **Aturan Anti-Penawaran Ulang & Anti-Duplikasi** (dilarang menawarkan ide yang sudah ditolak, menduplikasi nama/watak/profesi tokoh lama, atau memakai trope di Daftar Hitam Trope).
3. **Wajib Jalankan Filter Anti-Yes-Man (Debat Ide Sejak Akar):** Jika pengguna mengajukan ide mentah atau premis yang dari akarnya sudah sulit diterima akal sehat manusia (misal jenis usahanya tidak dibutuhkan di dunia nyata atau mudah digantikan aplikasi umum), **AI dilarang asal setuju ("yes-man")**. AI wajib mendebat dan membedah kelemahan ide tersebut dari segala arah, lalu merekomendasikan perombakan konsep dasar.
4. **Tahap 1 — Susun ABCD Premis Secara Ringkas (Jangan Over-Detail):** Rumuskan premis hanya dalam 4 poin singkat (1 kalimat per huruf): **A (Character)**, **B (Routine)**, **C (Inciting Incident)**, dan **D (Action)**. Jangan menjejalkan detil rintangan berlapis atau akhir cerita ke tahap ABCD ini.
5. **Tahap 2 — Pengembangan Premis Menuju Kerangka Cerita / Outline:** Baru setelah pengguna menyetujui ABCD premis dasar, kembangkan ide tersebut ke kerangka cerita (`03-structure.md`), tutup jalan mudah, dan susun outline untuk menguji apakah ide itu bisa berjalan 30–40 bab.
6. Catat keputusan ke `story/universe-registry.md` (`DITERIMA / AKTIF`, `CADANGAN / BACKLOG`, atau `DITOLAK / JANGAN DITAWARKAN LAGI`).

### Mode B: Project Baru (Canon -> Outline -> Stress Test -> Lock -> Bab 1)
1. Tanyakan maksimal 3 hal yang belum jelas (Default: 30–40 bab, ±750 kata/bab, tone hangat/sarkas/membumi ala `acuan-bahasa.docx`, akhir tidak sempurna dengan harga nyata, target 13+).
2. Buat folder `story/<Judul>/` memakai template di `engine/templates/` (`canon.md`, `state.md`, `outline.md`, `ledger.md`, `feedback.md`, `chapters/`).
3. Isi `canon.md` lengkap (premis ABCD & 5 slot, tabel penutupan minimal 5 jalan mudah, kerangka plot utama + pendamping, rencana planting 2x, character sheet, world building kelas menengah nyata, matriks sapaan).
4. Isi `outline.md` sesuai `03-structure.md` (18 kolom per bab, min 6–8 titik balik, siklus coba-gagal lolos Uji 100%).
5. Jalankan **Stress Test Outline** (`08-quality.md` Bagian 4 & 4A). Tutup semua lubang logika, presentasikan ke pengguna, dan setelah disetujui tandai **TERKUNCI v1.0**.
6. Tulis **Bab 1 saja** sesuai `06-chapter.md`.

### Mode C: Lanjutkan Cerita (Menulis Bab demi Bab)
1. Baca `story/<Judul>/state.md`, `canon.md`, `outline.md` (bab aktif), `ledger.md`, dan 1–2 bab terakhir.
2. Wajib tampilkan **Gerbang Pra-Tulis Kontinuitas (Pre-Flight Continuity Gate) 5 Poin** (`07-continuity.md` Bagian 3).
3. Tulis satu bab (standar 600–900 kata; darurat maks. 1.200 kata; 100% teks polos tanpa simbol format bintang/tebal/miring, 0 em dash, 0 quote pembuka).
4. Jalankan **Loop Setelah Menulis Bab** (Bagian 5 di bawah).

### Mode D: Revisi & Evaluasi Alur Cerita
1. Ikuti `09-revision.md`: jalankan Audit 5 Tahap dan Alur Remediasi Beruntun **R1–R5** (Canon -> Outline -> State/Ledger -> Revisi Lokal 74/18/8 & 4 Lapis -> Verifikasi Linter).

### Mode E: Riset Referensi & Pembaruan Anti-AI Slop
1. Ikuti `sources.md` dan `10-evolution.md`: jadikan repo sebagai rujukan utama; gunakan internet hanya untuk mengecek fakta dunia nyata/kosakata terbaru dan memperbarui teknik pencegahan halusinasi serta *AI slop*.

---

## 5. Loop Setelah Menulis Bab & Definition of Done

Setiap selesai menulis satu bab, simpan ke `story/<Judul>/chapters/bab-NN.md`, lalu lakukan urutan tetap ini:
1. **Kirim teks bab** (`## Bab N: Judul`, 600–900 kata, teks polos, tanpa em dash, tanpa quote di atas bab, berakhir hook).
2. **Catatan kontinuitas 5–8 baris & Factual Diff** (waktu/lokasi, fakta **BARU**, siapa tahu apa & saluran fisiknya, benda bawaan, setup/planting & payoff, risiko kontinuitas).
3. **Sinkronisasi Dokumen Negara:** Perbarui `state.md` dan `ledger.md`.
4. **Verifikasi Skrip Mekanis:** Jalankan `python3 scripts/audit-continuity.py "story/<Judul>"` dan `python3 scripts/analyze-prose.py "story/<Judul>"`.
5. **Skor rubrik 8 kriteria** dalam satu baris (1–5). Lulus jika tidak ada nilai <4 dan total ≥34/40.
6. **Penyimpangan outline:** "tidak ada" atau daftar jujur.
7. **Satu pertanyaan** ke pengguna, hanya jika perlu.

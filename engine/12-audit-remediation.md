# 12 — Standar Audit & Remediasi Menyeluruh per Judul

> **File Pemilik:** File ini memiliki aturan **Protokol Pemeriksaan Berurutan (Audit Sequence), Protokol Perbaikan Berurutan (Cascading Remediation), Matriks Diagnostik Cacat, dan Jaminan Tanpa Regresi (Zero-Regression Protocol)** per judul novel.
> Untuk kriteria logika dan kualitas lihat `08-quality.md`, teknik revisi 4 lapis di `09-revision.md`, aturan kontinuitas di `07-continuity.md`, struktur di `03-structure.md`, dan world building di `11-worldbuilding.md`.

---

## 1. Prinsip Piramida Ketergantungan Struktur

Kesalahan fatal dalam penyuntingan naskah (terutama saat dibantu AI) adalah **melakukan revisi secara acak**. Jika penulis merevisi dialog atau emosi di Bab 15 sebelum menyadari bahwa di Bab 4 ada klausul kontrak di `canon.md` yang salah atau ada titik balik di `outline.md` yang bolong, maka seluruh revisi Bab 15 akan sia-sia atau justru merusak bab-bab lainnya.

Sebuah judul novel MetroPop dibangun di atas **Piramida Ketergantungan Hierarkis**:

```
+---------------------------------------------------------------------------------------------------+
|                     PIRAMIDA KETERGANTUNGAN STRUKTUR NOVEL METROPOP                               |
+---------------------------------------------------------------------------------------------------+
| TINGKAT 1: FONDASI CANON & WORLD BUILDING                                                         |
|            (Premis 5 Slot, Aturan Dunia, Hukum Positif RI, Nilai Uang, Cast, Sapaan)              |
|            |                                                                                      |
|            v                                                                                      |
| TINGKAT 2: ARSITEKTUR OUTLINE & PLOT MAKRO                                                        |
|            (8 Kerangka Plot, Hitungan Titik Balik, Siklus Coba-Gagal Uji 100%, Planting 2x)       |
|            |                                                                                      |
|            v                                                                                      |
| TINGKAT 3: INTEGRITAS KONTINUITAS & STATE MACHINE                                                 |
|            (state.md, ledger.md, Jangkar Waktu Relatif, Status Hubungan, Log Fakta Fisik Mikro)   |
|            |                                                                                      |
|            v                                                                                      |
| TINGKAT 4: ANATOMI ADEGAN & MESIN MIKRO BAB                                                       |
|            (Target 600-900 Kata, Beat, Pola Berhasil tapi / Gagal malah, Geser Emosi, Hook)       |
|            |                                                                                      |
|            v                                                                                      |
| TINGKAT 5: KUALITAS PROSA, DIALOG, & BAHASA LOKAL                                                 |
|            (4-Pass Prosa, Anti-AI Slop, Bebas Em Dash, Matriks Sapaan, Detail 2 Indera)           |
+---------------------------------------------------------------------------------------------------+
```

### Hukum Aliran ke Bawah (*The Downward Cascade Law*)
1. **Arah Pemeriksaan (*Audit*):** Dilakukan **Top-Down** (dari Tingkat 1 turun ke Tingkat 5). Jangan memeriksa kehalusan diksi kata jika premis atau siklus coba-gagalnya masih cacat logika.
2. **Arah Perbaikan (*Remediation*):** Wajib diperbaiki dari **tingkat tertinggi yang cacat**, lalu disinkronkan secara berurutan (*cascading*) ke tingkat-tingkat di bawahnya.
3. **Karantina Dampak (*Impacted Scope Isolation*):** Setiap perbaikan harus memetakan rentang bab yang terdampak. Bab di luar rentang tersebut dilarang diubah sembarangan guna mencegah efek domino.

---

## 2. Lima Tahap Pemeriksaan Berurutan (*Audit Pipeline*)

Jalankan 5 tahap audit ini secara berurutan per judul cerita:

```
[Tahap 1: Audit Fondasi Canon] ---> [Tahap 2: Audit Outline Makro] ---> [Tahap 3: Audit Kontinuitas & State]
                                                                                        |
[Tahap 5: Audit Prosa & Diksi] <--- [Tahap 4: Audit Mesin Mikro Bab] <------------------+
```

---

### Tahap 1 — Audit Fondasi Canon & World Building (Tingkat 1)
- **Dokumen yang Diperiksa:** `canon.md` (mengacu pada `01-genre.md`, `02-premise.md`, `11-worldbuilding.md`).
- **Checklist Pemeriksaan:**
  1. *Uji 5 Slot Kelayakan Premis:* Keinginan vs kebutuhan berbeda; masalah & tenggat luar jelas; konsekuensi gagal konkret terukur; minimal 3 jalan mudah tertutup alasan tertulis; akhir tidak sempurna dengan harga nyata.
  2. *Uji Realitas World Building:* Wilayah geografis nyata vs entitas komersial fiktif; tahun kejadian spesifik; daya beli uang wajar (skala utang Rp15-60 juta, anti-utang miliaran); moda transportasi & jam sibuk masuk akal.
  3. *Uji Batasan Hukum & Regulasi Indonesia:* Prosedur Laporan Polisi resmi; UU ITE / doxxing; kerahasiaan bank mutlak (anti-retasan mutasi rekening oleh tim IT swasta); aturan tender korporat & *conflict of interest*.
  4. *Uji Aturan Khusus Premis:* 6 klausul wajib (hak/imbalan DP vs pelunasan, kewajiban peran, batasan fisik/emosi, sanksi batal, objek bukti fisik, tenggat waktu).
  5. *Matriks Sapaan & Kata Ganti:* Register panggilan narasi POV 1 vs dialog formal/akrab/konflik.
- **Kriteria Lolos (Gate Pass):** Seluruh slot kelayakan dan hukum dunia terisi tanpa lubang logika.

---

### Tahap 2 — Audit Arsitektur Plot & Kerangka Outline (Tingkat 2)
- **Dokumen yang Diperiksa:** `outline.md` (mengacu pada `03-structure.md`, `08-quality.md`).
- **Checklist Pemeriksaan:**
  1. *Kesesuaian 8 Kerangka Plot:* Cerita bertumpu pada salah satu kerangka terbukti, bukan alur acak.
  2. *Hitungan Titik Balik:* Minimal 6 titik balik untuk 30 bab, minimal 8 titik balik untuk 40 bab.
  3. *Siklus Coba-Gagal (Babak 2):* Setiap siklus memiliki 6 komponen dan wajib lolos **Uji 100%** (jika cara itu berhasil penuh, apakah masalah inti selesai? Jika tidak, itu *filler*).
  4. *Rencana Menanam Solusi (Planting 2 Kali):* Bahan solusi akhir (orang, benda, kebiasaan, info) sudah dijadwalkan ditanam minimal dua kali di Babak 1-2 (satu tampak sepele, satu tampak seperti hiasan).
  5. *Tipe In Medias Res:* Menetapkan Tipe 1 (Direct Action Linier) atau Tipe 2 (Flash-Forward Hook Framing dengan titik *Loop Closure* terjadwal di tengah cerita).
  6. *Pindai 10 Tanda Bahaya (Red Flags):* Tidak ada masalah yang selesai hanya dengan satu obrolan jujur; taruhan terus naik; kebetulan hanya boleh memperburuk keadaan (dilarang *deus ex machina*).
- **Kriteria Lolos (Gate Pass):** Struktur outline bebas dari adegan pengisi (*filler*) dan rantai kausalitas sebab-akibat antar-bab terhubung kokoh.

---

### Tahap 3 — Audit Integritas Kontinuitas Lintas-Bab (Tingkat 3)
- **Dokumen yang Diperiksa:** `state.md`, `ledger.md`, seluruh teks bab di `chapters/`.
- **Checklist Pemeriksaan:**
  1. *Keberadaan 3 Pilar Kebenaran:* `canon.md`, `state.md`, dan `ledger.md` lengkap dan saling sinkron.
  2. *Audit Otomatis Linter:* Jalankan perintah `python3 scripts/audit-continuity.py "story/<Judul>"`. Wajib 0 FAIL.
  3. *Verifikasi Jangkar Waktu Relatif:* Tidak ada kata "kemarin" yang merujuk pada hari yang salah; istilah relatif ("semalam", "dua hari lalu", "minggu lalu") sesuai dengan kalender kronologis cerita.
  4. *Register Status Hubungan:* Tidak ada lompatan label hubungan prematur (contoh: di Bab 1 butuh pacar, di Bab 2 mendadak disebut "calon istri" tanpa adegan lamaran sah).
  5. *Log Pemerolehan Fakta Fisik & Anti-Telepati Data Mikro:* Tidak ada tokoh yang melafalkan nomor pelat kendaraan, nama lengkap, gelar/IPK, nomor telepon, alamat, atau kode tagihan tanpa melalui **3 saluran fisik sah** (melihat visual langsung, mendengar di dialog, atau membaca dokumen fisik/layar HP).
  6. *Kunci Ambang Batas Kejadian Pertama (Milestone Lock):* Tidak ada adegan "pertama kali" yang terulang dua kali (misal: dua kali pertama bertemu calon mertua, dua kali pertama melepas masker).
- **Kriteria Lolos (Gate Pass):** Skrip audit kontinuitas bersih 100% dan seluruh asimetri pengetahuan tokoh terjaga ketat.

---

### Tahap 4 — Audit Desain Adegan & Mesin Mikro Bab (Tingkat 4)
- **Dokumen yang Diperiksa:** Setiap bab di `chapters/bab-NN.md`.
- **Checklist Pemeriksaan:**
  1. *Rentang Kata Wajib:* Standar 600-900 kata per bab (target ideal ±750 kata; kelonggaran darurat maks. 1.200 kata hanya jika benar-benar mendesak agar tidak memotong adegan penting). Dilarang di bawah 600 kata.
  2. *Mesin Mikro Adegan:* Setiap bab memiliki Tujuan Jelas -> Rintangan Nyata -> Pola Hasil (`Berhasil, tapi...` atau `Gagal, dan malah...`). Dilarang kemenangan mulus tanpa komplikasi di bab tengah.
  3. *Pergeseran Emosi Tokoh:* Emosi protagonis saat keluar dari bab berbeda dengan saat masuk bab.
  4. *Variasi Hook Akhir Bab:* Kalimat terakhir wajib berupa hook tajam yang memancing lanjut membaca; jenis hook bervariasi (tidak memakai tipe yang sama 2 bab berurutan); dilarang kesimpulan moral/bahagia.
  5. *Gerbang Khusus Bab 1:* Khusus Bab 1 wajib in medias res, lulus Uji Kalimat Pertama, Uji Janji Pembaca, Uji Perkenalan Protagonis & Kelemahan, Uji Benih Tema, dan Uji Tarikan Akhir.
- **Kriteria Lolos (Gate Pass):** Setiap bab terasa padat, berdegup, dan mendorong pembaca mengklik bab selanjutnya.

---

### Tahap 5 — Audit Prosa, Dialog, & Diksi Lokal (Tingkat 5)
- **Dokumen yang Diperiksa:** Naskah bab, skrip analisis prosa `analyze-prose.py`.
- **Checklist Pemeriksaan (Sistem 4 Lapis):**
  1. *Lapis 1 (Dialog & Subteks):* Uji Tutup-Nama; anti-eksposisi rasa narator (pisahkan ucapan singkat di dialog vs gerutuan di monolog batin); patuh Matriks Sapaan; ada gesekan subteks.
  2. *Lapis 2 (Logika Fisik & Dimensi):* Kemurnian POV 1 murni (tanpa sisa POV 3); ukuran benda masuk akal dengan wadahnya (kertas A4 di map A4, kotak kue di tas jinjing, sup di rantang); prosedur lokal Indonesia nyata.
  3. *Lapis 3 (Bahasa Sehari-hari & Anti-AI Slop):* **0 em dash (`—`)**; **0 quote pembuka di atas bab**; bersih dari 5 pola sintaksis AI (*Sambil... / ..., membuat...*); pangkas tag buku pelajaran (*ujarnya/tuturnya*); sertakan minimal 2 indera lokal konkret; deretan kalimat panjang seragam dipecah; jalankan `python3 scripts/analyze-prose.py`.
  4. *Lapis 4 (Gelombang Ketegangan & Rasa Baca):* Skor tensi naik-turun dinamis; lulus uji Persona Pembaca HP Indonesia (*Reader-Sim*).
- **Kriteria Lolos (Gate Pass):** Skor rubrik kualitas 8 kriteria mencapai minimal 34/40 tanpa ada nilai di bawah 4.

---

## 3. Matriks Diagnostik Cacat (*The Defect Matrix*)

Saat menjalankan audit menyeluruh, catat semua temuan ke dalam format matriks standar ini sebelum melakukan tindakan perbaikan:

| ID Cacat | Tingkat (1-5) | Bab / Dokumen Terdampak | Deskripsi Cacat (Fakta vs Seharusnya) | Derajat Keparahan | Akar Masalah |
|---|---|---|---|---|---|
| C-01 | Tingkat 1 | `canon.md`, Bab 02 | Rian menyebut pelat motor Ayu padahal belum pernah melihat | **Major** | Telepati data mikro tanpa saluran fisik |
| C-02 | Tingkat 3 | Bab 02 | Status disebut "calon istri" padahal baru pacar pura-pura | **Critical** | Pelanggaran kontinuitas status hubungan |
| C-03 | Tingkat 5 | Bab 07 | Dialog Ayu menjelaskan kronologi A4 seperti narator | **Minor** | Dialog eksposisi narator |

### Klasifikasi Derajat Keparahan:
- **Critical (Blocker):** Merusak premis, melanggar hukum dunia, atau merusak rantai logika plot antarbab. Wajib diselesaikan sebelum menyentuh prosa.
- **Major (Structural):** Kebocoran kontinuitas waktu, telepati data mikro, atau lompatan emosi tanpa pemicu. Wajib sinkronisasi di `state.md` dan outline sebelum revisi bab.
- **Minor (Local/Prose):** Cacat diksi, kalimat seragam, em dash, atau AI slop lokal yang bisa diselesaikan di level teks bab.

---

## 4. Lima Tahap Perbaikan Terstruktur (*Remediation SOP: Cascading Top-Down*)

Untuk menjamin perbaikan **tepat sasaran dan tidak merusak langkah sebelumnya**, lakukan proses perbaikan dengan urutan wajib berikut:

```
+---------------------------------------------------------------------------------------------------+
|                        ALUR PERBAIKAN BERUNTUN (CASCADING TOP-DOWN)                               |
+---------------------------------------------------------------------------------------------------+
| LANGKAH R1: PERBAIKI FONDASI CANON & WORLDBUILDING (Jika Cacat Ada di Tingkat 1)                  |
|             (Buat Change Request, kunci aturan hukum, daya beli, atau klausul kontrak baru)       |
|             |                                                                                     |
|             v                                                                                     |
| LANGKAH R2: PERBAIKI ARSITEKTUR OUTLINE & TITIK BALIK (Jika Cacat Ada di Tingkat 2)               |
|             (Sesuaikan beat, uji 100% siklus coba-gagal, jadwal planting 2x, tetapkan babak)       |
|             |                                                                                     |
|             v                                                                                     |
| LANGKAH R3: SINKRONISASI STATE MACHINE & LEDGER (Kunci Wajib Tingkat 3)                           |
|             (Update state.md & ledger.md: kunci jangkar waktu, register hubungan, log fakta mikro)|
|             |                                                                                     |
|             v                                                                                     |
| LANGKAH R4: EKSEKUSI REVISI LOKAL PROSA BAB TERDAMPAK (Tingkat 4 & 5)                             |
|             (Rasio edit 74/18/8, Uji Hapus, 4-Pass Revision, 600-900 kata, 0 em dash)            |
|             |                                                                                     |
|             v                                                                                     |
| LANGKAH R5: VERIFIKASI REGRESI OTOMATIS & INTEGRITAS KESELURUHAN (Zero-Regression Verification)   |
|             (Jalankan audit-continuity.py & analyze-prose.py; cek bab sambungan depan-belakang)   |
+---------------------------------------------------------------------------------------------------+
```

---

### Langkah R1 — Perbaiki Fondasi Canon & Aturan Dunia (Tingkat 1)
1. Jika cacat berada di level premis, aturan dunia, cast, atau hukum, buat draf perubahan di `templates/change-request.md`.
2. Dapatkan konfirmasi atau tetapkan versi baru `canon.md` (misal naik dari v2.0 ke v2.1).
3. **Pilar Pengunci:** Pastikan klausul kontrak, nilai uang, dan aturan hukum sudah tertulis definitif.

---

### Langkah R2 — Perbaiki Arsitektur Outline (Tingkat 2)
1. Perbarui `outline.md` hanya pada bab-bab yang terpengaruh oleh perubahan Canon.
2. Gunakan salah satu dari **4 Teknik Bedah Alur (*4 Surgical Rerouting Techniques*)** di `08-quality.md`: (1) Pengalihan Rute Kausal, (2) Memeluk Kemustahilan Jadi Komplikasi, (3) Jahitan Bedah Mikro, atau (4) Pertukaran Beban Pembuktian, agar alur diselamatkan secara elegan tanpa merombak bab awal.
3. Pastikan titik balik, siklus coba-gagal baru (lolos Uji 100%), dan *planting 2x* berada di posisi bab yang tepat.
4. Kunci kembali outline sebagai acuan menulis adegan.

---

### Langkah R3 — Sinkronisasi State Machine & Garis Waktu (Tingkat 3)
1. **Perbarui `state.md`:** Masukkan fakta baru, waktu kalender yang benar, status hubungan resmi, dan daftarkan data mikro ke tabel pemerolehan fisik (Komponen VI).
2. **Perbarui `ledger.md`:** Perbaiki entri kronologis yang terdampak agar arsip sejarah cerita tetap akurat.
3. **Tetapkan Jangkauan Bab Terdampak (*Impacted Scope*):** Batasi dengan tegas nomor bab awal sampai nomor bab akhir yang harus diedit (misal: hanya Bab 02 sampai Bab 04). **Dilarang mengubah bab lain yang sudah steril.**

---

### Langkah R4 — Eksekusi Revisi Lokal Prosa Bab Terdampak (Tingkat 4 & 5)
1. Buka file bab di dalam jangkauan terdampak satu per satu.
2. **Terapkan Rasio Edit Profesional (74% Ganti / 18% Hapus / 8% Tambah):**
   - Jangan menulis ulang satu bab penuh jika masalahnya hanya 2 paragraf dialog atau salah data mikro.
   - Jalankan **Uji Hapus (*Deletion Test*)**: jika kalimat baru dihapus maknanya tetap utuh, jangan tambahkan kalimat itu.
3. **Jalankan 4 Lapis Revisi Terfokus:**
   - Lapis 1: Dialog subteks, anti-eksposisi narator, Matriks Sapaan.
   - Lapis 2: Logika fisik wadah/benda, saluran fisik data mikro, kemurnian POV 1.
   - Lapis 3: Diksi lisan Indonesia, hapus em dash (`—`), hapus quote pembuka, hapus AI slop.
   - Lapis 4: Gelombang tensi, pola `Berhasil tapi / Gagal malah`, dan ketajaman hook akhir.
4. Pastikan jumlah kata tetap **600-900 kata** (darurat maks. 1.200 kata).

---

### Langkah R5 — Verifikasi Regresi Otomatis (*Zero-Regression Protocol*)
Setelah selesai merevisi bab terdampak, lakukan verifikasi penutup:
1. **Audit Kontinuitas Skrip:**
   ```bash
   python3 scripts/audit-continuity.py "story/<Judul>"
   ```
   *Wajib: 0 Fail, seluruh klaim waktu dan status hubungan cocok dengan ledger.*
2. **Analisis Prosa Mekanis Skrip:**
   ```bash
   python3 scripts/analyze-prose.py "story/<Judul>"
   ```
   *Wajib: 0 Em Dash, 0 Frasa AI Slop, panjang kata valid di semua bab.*
3. **Uji Sambungan Bab Depan-Belakang (*Boundary Seam Test*):**
   - Baca 2 paragraf terakhir dari bab sebelum jangkauan revisi (Bab N-1) dan 2 paragraf pertama dari bab hasil revisi (Bab N). Apakah sambungannya mengalir alami?
   - Baca 2 paragraf terakhir dari bab hasil revisi (Bab M) dan 2 paragraf pertama dari bab berikutnya (Bab M+1). Apakah konsekuensi kejadian tersambung mulus tanpa ada yang terlupakan?
4. Jika seluruh uji lulus, status revisi dinyatakan **SELESAI & TERVERIFIKASI PENUH**.

---

## 5. Ringkasan Cepat: Checklist Kerja Auditor/Editor

Saat diminta memeriksa dan memperbaiki novel:
1. **Audit 1-2-3-4-5:** Pindai dari Canon -> Outline -> State/Ledger -> Bab -> Prosa.
2. **Susun Matriks Cacat:** Catat semua lubang logika sebelum mengetik perbaikan.
3. **Remediasi R1-R2-R3-R4-R5:** Perbaiki dari Canon/Outline -> State/Ledger -> Teks Bab -> Skrip Verifikasi.
4. **Laporkan Hasil dengan Jujur:** Sebutkan apa yang berubah, file apa yang diperbarui, dan skor akhir audit skrip.
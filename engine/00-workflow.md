# 00 — Workflow

## 0. Tahap Proyek A–G

| Tahap | Isi | Selesai jika |
|---|---|---|
| A. Premis | 3 opsi (Resep 9 Langkah & Uji 5 Slot) atau premis dari user + pilih Kerangka Plot (7 Langkah) | User memilih |
| B. Dokumen Dasar | Canon: 5 slot premis, kerangka utama & pendamping, tokoh, dunia, mekanisme, planting solusi (2x), timeline, rahasia/bukti + Penjaga State (`state.md`) | User setuju |
| C. Outline | Semua bab lengkap (alokasi titik balik, siklus coba-gagal 6 komponen, planting) | Semua kolom terisi |
| D. Stress test | 10 Uji Logika + 10 Tanda Bahaya + 3 peran + uji silang | Semua lubang tertutup |
| E. Lock | Presentasi ke user | Outline v1.0 TERKUNCI |
| F. Tulis | Pre-flight continuity gate, tulis (600–900 kata), nilai rubrik, sinkronisasi state.md/ledger.md | User menyetujui |
| G. Revisi | Diagnosis alur / klasifikasi feedback, revisi lokal | User puas |

## 0.1 Prinsip Pas

Teknik naratif, subplot, flashback, dan scene ikonik adalah **alat opsional**, bukan
kewajiban. Angka seperti "1–3 subplot" atau "3–5 scene ikonik" adalah **batas atas**,
bukan target. **Nol pun boleh** jika cerita sudah padat.

Pakai alat hanya jika lolos Tes Pas:

1. cerita benar-benar membutuhkannya;
2. jika dihapus, ada yang hilang;
3. tidak menambah risiko plot hole;
4. tidak melebarkan cerita dari masalah utama.

Jika ragu, jangan masukkan. Cerita solid dan pas lebih penting daripada penuh teknik.

## 0.2 Protokol *Smart-Reading* (Efisiensi Konteks & Anti-Dilusi Fokus AI)

Jangan memuat seluruh 12 file di `engine/` sekaligus pada setiap giliran percakapan karena akan menguras jendela konteks dan memecah perhatian AI terhadap detail mikro. Gunakan pemetaan *on-demand* berikut:

| Mode / Tugas Saat Ini | File yang Wajib Dibaca | File yang JANGAN Dibaca Dulu |
|---|---|---|
| **Pembuka Sesi Baru** | `AGENTS.md`, `00-workflow.md`, cek daftar folder di `story/` | Seluruh bab cerita & file detail craft lainnya |
| **Mode A (Cari Ide / Premis Baru)** | `01-genre.md`, `02-premise.md`, `Kerangka Plot yang Terbukti untuk Web Novel.md` | `06-chapter.md`, `07-continuity.md`, `09-revision.md` |
| **Mode B (Project Baru: Canon & Outline)** | `02-premise.md`, `03-structure.md`, `04-character.md`, `07-continuity.md`, `08-quality.md`, `templates/` | `09-revision.md`, `10-evolution.md` |
| **Mode C (Menulis Bab Baru)** | `story/<Judul>/state.md`, `canon.md`, `outline.md` (bagian bab terkait), `ledger.md`, 1–2 bab terakhir, `05-style.md`, `06-chapter.md` | `01-genre.md`, `02-premise.md`, `10-evolution.md`, bab-bab lama yang tidak terkait |
| **Mode D (Revisi Bab / Audit Alur)** | `05-style.md`, `07-continuity.md`, `08-quality.md`, `09-revision.md`, `canon.md`, `state.md`, `ledger.md`, bab yang direvisi | `01-genre.md`, `templates/` |
| **Mode E (Riset / Evolusi Engine)** | `sources.md`, `10-evolution.md`, `learnings/editor-feedback.md`, `learnings/changelog.md` | File proyek cerita yang tidak sedang diubah |

**Aturan *Active Cache*:** Jangan membaca ulang file yang sudah dibaca di sesi yang sama kecuali file tersebut baru saja diubah.

## 1. Mulai Sesi

1. Baca `AGENTS.md`, `engine/README.md`, lalu file ini (`engine/00-workflow.md`),
   `acuan-bahasa.docx`, dan `Kerangka Plot yang Terbukti untuk Web Novel.md`.
2. Periksa `../story/`.
3. Jika ini pertama kali membaca panduan di sesi ini, balas **3 hal**: ringkasan
   pemahaman 5 poin, tahap A–G yang relevan, dan satu pertanyaan.
4. Jika bukan pertama kali, ringkas posisi repo 2–3 baris dan sebut tahap A–G.
5. Tanya **satu** pertanyaan:

> Mau apa hari ini: (A) cari ide/premis baru, (B) mulai project baru, (C) lanjutkan
> cerita yang ada, (D) revisi/analisis alur cerita, atau (E) analisis referensi/riset?

Jangan bertanya lebih dari satu pertanyaan pembuka. Jangan menulis prosa sebelum user
memilih mode.

## 2. Mode A — Ide / Premis Baru

Baca `01-genre.md`, `02-premise.md`, dan `../Kerangka Plot yang Terbukti untuk Web Novel.md`.
Gunakan **Resep 9 Langkah (arah terbalik dari kelemahan tokoh & kerangka)** dan pastikan
setiap opsi lolos **Uji Kelayakan 5 Slot**. Beri **3 opsi** dengan format:

```markdown
## Opsi 1 — "Judul"
- **Logline (1 kalimat):** [Tokoh] ingin [X], tapi [masalah mendadak], dan kalau gagal [konsekuensi nyata].
- **Kerangka Plot:** Kerangka Utama + Pendamping (beserta alasan singkat 1 kalimat).
- **Tema & Pertanyaan Dramatik:** ...
- **Tokoh Inti (3):** nama, usia, pekerjaan, kelemahan khas (mesin plot).
- **Uji 5 Slot Kelayakan:**
  1. *Keinginan vs Kebutuhan:* ...
  2. *Masalah & Tenggat Luar:* ...
  3. *Konsekuensi Nyata:* ...
  4. *3 Jalan Mudah yang Ditutup:* ...
  5. *Perubahan Akhir & Harganya:* ...
- **Benih Solusi (Planting):** apa yang ditanam sejak awal untuk solusi akhir.
- **Sumber Humor/Awkward:** 3 contoh adegan konkret.
```

Jangan menulis bab. Tunggu user memilih, meminta variasi, atau memberi premis sendiri.
Jika user memberi premis sendiri, **jangan mengubah keputusan user**; lengkapi slot yang
kosong dan perbaiki logikanya.

## 3. Mode B — Project Baru

### 3.1 Klarifikasi & Penentuan Kerangka (7 Langkah)

Tanyakan maksimal 3 hal yang belum jelas. Jika user tidak menentukan, pakai default
berikut tanpa bertanya:

- 30–40 bab, ±750 kata/bab (rentang wajib 600–900 kata);
- tone hangat/jenaka/getir;
- ending tidak sempurna namun memuaskan (ada harga nyata yang dibayar);
- latar dan usia tokoh: pilih yang paling kuat untuk premis; target pembaca 13+;
- 1 POV utama, bab sampingan maksimal 10–15%.

Jika user belum memberi premis, jalankan Mode A dulu (3 opsi) sebelum membuat canon.
Jika premis sudah ada, jalankan **7 Langkah Menentukan Kerangka dari Premis** di `02-premise.md`
(Ringkas 1 kalimat -> Isi 5 slot -> Inti emosi -> Bentuk konflik -> Kerangka Utama -> Pendamping -> Hitung titik balik & siklus).

### 3.2 Buat Folder

Buat `story/<Judul>/` dengan:

```text
canon.md
state.md
outline.md
ledger.md
feedback.md
chapters/
```

Gunakan template di `templates/`. Jangan mengarang format baru.

### 3.3 Isi Canon

Canon wajib memuat:

- judul, logline 1 kalimat, blurb 3–5 kalimat;
- **Uji 5 Slot Kelayakan Premis** dan **Kerangka Plot (Utama + Pendamping)**;
- tema dan pertanyaan dramatik;
- janji ke pembaca;
- **world building & aturan dunia (`11-worldbuilding.md`):** latar spasial (negara, kota, zonasi elit vs pemukiman), latar temporal (tahun kejadian, era teknologi, patokan ekonomi riil), aturan hukum nyata Indonesia (UU ITE, SOP kepolisian, rahasia bank), norma sosial-budaya, dan aturan khusus premis (hak, kewajiban, larangan, penalti, tenggat);
- cast table + character sheet lengkap (kelemahan tokoh sebagai mesin plot);
- aturan dunia dan mekanisme teknis yang menggerakkan plot, ditulis langkah demi
  langkah, **lengkap dengan minimal 3 jalan mudah yang ditutup beserta alasannya**;
- **rencana menanam solusi (Planting 2 Kali):** bahan solusi (orang, benda, kebiasaan, info) yang ditanam minimal 2 kali di Babak 1–2;
- **daftar rahasia dan bukti:** apa, siapa tahu, sejak kapan, dari mana, di bab berapa terungkap;
- **timeline masa lalu (A2)** untuk flashback/backstory;
- **tokoh kecil berulang** dan peran mereka nanti;
- motif (refleks, objek, aturan, tekanan keluarga);
- tekanan keluarga dan taruhan personal;
- subplot/backstory/flashback yang dipakai — opsional, 0 boleh;
- scene ikonik — opsional, 0 boleh;
- arah ending dan harga nyata yang dibayar;
- batasan konten 13+.

### 3.4 Daftar Usulan Ide (sebelum outline)

Agent **aktif mengusulkan** ide tambahan (subplot, flashback, tokoh kecil, momen awkward,
twist kecil, scene ikonik) supaya cerita kaya dan tidak datar. Lebih baik 3 ide yang
pas dan terpakai daripada 10 ide yang dipaksakan. Kalau tidak ada ide tambahan yang
benar-benar dibutuhkan, katakan itu dan lanjutkan ceritanya apa adanya.

Kumpulkan ide di `idea-list.md` sebelum outline. Untuk tiap ide tulis: ide, fungsi, bab
yang cocok, risiko. Uji dengan Tes Pas di `03-structure.md`. User memilih; hanya
yang disetujui masuk outline. Setelah outline terkunci, ide baru hanya lewat Permintaan
Perubahan.

### 3.5 Isi Outline

Baca `03-structure.md`. Outline wajib punya:

- status versi (mulai v0.1 DRAFT);
- penentuan **Tipe In Medias Res** (Tipe 1: Direct Action Linier vs Tipe 2: Flash-Forward Hook Framing dengan Loop Closure di Midpoint/Krisis);
- kerangka plot utama & pendamping, hitungan titik balik (minimal 6 untuk 30 bab, 8 untuk 40 bab), dan pemetaan Siklus Coba-Gagal;
- peta babak sesuai kerangka yang dipilih;
- untuk setiap bab: nomor, judul 2–5 kata, hari/jam/lokasi, POV, posisi kerangka & siklus,
  tujuan adegan, komplikasi, 3–5 beat, perubahan, siapa tahu apa, setup/planting & payoff,
  teknik naratif, hook, alasan logis, jalan mudah yang ditutup, pertanyaan pembaca yang dijawab,
  dan yang **TIDAK** terjadi;
- daftar bahan solusi yang ditanam minimal 2 kali (*planting*).

### 3.6 Stress Test

Jalankan prosedur di `08-quality.md`:
1. **10 Uji Logika Alur Cerita** (termasuk Uji 100% pada tiap siklus coba-gagal, tenggat luar, dan planting 2x) dengan merujuk nomor bab.
2. **Pemeriksaan 10 Tanda Bahaya (*Red Flags*)**.
3. **Simulasi Tiga Peran:** pembaca awam yang curiga, antagonis yang cerdas, dan protagonis yang berpikir logis.
4. **Empat Teknik Preventif Ketat (Bagian 4A):** *Backward Dependency Tracing* dari klimaks, *World Building Stress-Test* (hukum/jarak/uang nyata), *Adversarial 'Why Not Do X?' Test*, dan *Pre-Outline Knowledge Graph*.

Tutup semua lubang sebelum meminta persetujuan.

### 3.7 Persetujuan dan Lock

Presentasikan:

- ringkasan premis (5 slot), kerangka plot, dan cast;
- peta babak & siklus coba-gagal;
- 3–5 bab pertama secara ringkas;
- lubang/tanda bahaya yang ditemukan dan cara menutupnya;
- risiko yang masih ada.

Minta persetujuan user. Setelah disetujui, tandai:

```markdown
**Status:** TERKUNCI v1.0
**Tanggal lock:** YYYY-MM-DD
```

Jangan menulis Bab 1 sebelum status terkunci.

### 3.8 Tulis Bab 1

Baca `06-chapter.md`. Bab 1 wajib in medias res (pilih Tipe 1 Direct Action atau Tipe 2 Flash-Forward Framing sesuai outline). Tulis satu bab saja (600–900 kata). Setelah selesai,
ikuti Loop Bab di bagian 7.

## 4. Mode C — Lanjutkan Cerita

1. Baca `story/<Judul>/state.md`, `canon.md`, `outline.md`, `ledger.md`, dan 1–2 bab terakhir.
2. Tampilkan **Gerbang Pra-Tulis Kontinuitas (Pre-Flight Continuity Gate) 5 Poin** (Lapis 1):
   - **Waktu & Jangkar:** Hari [X], [Nama Hari], [Jam] | "Kemarin" merujuk ke [Hari X-1] | Rujukan lampau yang sah: [Hari Y lalu]
   - **Status Hubungan Sah:** [Label resmi aktif] | DILARANG: [Diksi terlarang/prematur]
   - **Inventaris Fisik:** Benda yang dibawa tokoh utama | Lokasi objek krusial
   - **Asimetri Pengetahuan:** Tokoh hadir tahu [...] tapi belum tahu [...]
   - **Kunci Milestone:** Ambang batas kejadian pertama yang berlaku di bab ini
3. Minta konfirmasi user (jika user minta langsung lanjut tanpa konfirmasi, tetap wajib tampilkan blok gerbang sebelum bab).
4. Setelah dikonfirmasi, tulis satu bab (600–900 kata).
5. Ekstrak *Factual State Diff* dan update `state.md` (potret instan untuk bab berikutnya).
6. Update `ledger.md` (arsip baris kronologis); update `canon.md` jika ada fakta baru.
7. Jalankan audit silang `python3 scripts/audit-continuity.py "story/<Judul>"`.
8. Laporkan penyimpangan outline dengan jujur.

## 5. Mode D — Revisi & Evaluasi Alur Cerita

Baca `08-quality.md`, `09-revision.md`, `07-continuity.md`, dan **panduan master audit & perbaikan menyeluruh `12-audit-remediation.md`**.

1. Tanyakan atau identifikasi: bab/bagian mana, feedback-nya apa, boleh mengubah canon/outline/state atau tidak.
2. Jika diminta menilai/menganalisis naskah secara menyeluruh per judul, jalankan **Pemeriksaan 5 Tahap Berurutan** di `12-audit-remediation.md` (Tahap 1 Canon -> Tahap 2 Outline -> Tahap 3 Kontinuitas -> Tahap 4 Mesin Mikro Bab -> Tahap 5 Prosa) dan buat Matriks Diagnostik Cacat.
3. Saat melakukan perbaikan menyeluruh, wajib ikuti **Alur Perbaikan Beruntun (*Cascading Remediation*) R1–R5** agar tidak merusak langkah sebelumnya:
   - **R1:** Kunci perubahan fakta/hukum di `canon.md` (buat Permintaan Perubahan);
   - **R2:** Sinkronkan beat adegan & siklus coba-gagal di `outline.md`;
   - **R3:** Kunci ulang kondisi di `state.md` & `ledger.md`, serta isolasi **Jangkauan Bab Terdampak**;
   - **R4:** Eksekusi revisi lokal prosa bab terdampak memakai rasio 74/18/8 dan Sistem Revisi 4 Lapis Terfokus;
   - **R5:** Verifikasi otomatis tanpa regresi (`audit-continuity.py`, `analyze-prose.py`, dan tes sambungan bab).
4. Klasifikasikan:
   - **gaya** → terapkan ke semua bab terdampak;
   - **logika/plot** → Permintaan Perubahan + update outline/ledger/state.md;
   - **preferensi baru** → catat di `learnings/editor-feedback.md` dan update file engine.
5. Laporkan perubahan, file yang diperbarui, dan hasil verifikasi bebas regresi.

## 6. Mode E — Riset / Referensi

Baca `sources.md`.

- PDF/teks/URL: ekstrak, ringkas, ambil prinsip.
- Jangan menyalin karya berhak cipta.
- Simpan catatan di `sources.md` atau `learnings/`.
- Tanyakan apakah temuan mau dijadikan aturan engine atau hanya referensi project.

## 7. Loop Setelah Menulis Bab

Setiap selesai satu bab, simpan ke `story/<Judul>/chapters/bab-NN.md`, lalu kirim dengan
urutan tetap:

1. **Teks bab** (600–900 kata, tanpa em dash, tanpa quote di atas bab).
2. **Catatan kontinuitas 5–8 baris & Factual Diff**:
   - waktu/lokasi;
   - fakta baru (tandai **BARU**);
   - siapa tahu apa sekarang;
   - benda/urusan yang dibawa;
   - setup/planting & payoff;
   - risiko kontinuitas.
3. **Sinkronisasi State & Ledger**: Perbarui `state.md` (potret instan bab berikutnya) dan `ledger.md` (arsip kronologis).
4. **Audit Kontinuitas Skrip**: Jalankan `python3 scripts/audit-continuity.py "story/<Judul>"` untuk memastikan 0 kesalahan status hubungan, waktu relatif, dan perkenalan tokoh ganda.
5. **Skor rubrik 8 kriteria** dalam satu baris (1–5), plus alasan singkat jika ada nilai di bawah 5. Lulus jika tidak ada nilai <4 dan total ≥34/40.
6. **Penyimpangan outline**: "tidak ada" atau daftar jujur.
7. **Satu pertanyaan** ke user, hanya jika perlu.

Sebelum mengirim, cek:

- semua beat outline muncul di teks;
- semua setup/planting/payoff benar-benar ditanam/dibayar;
- ledger hanya memuat fakta yang ada di teks;
- POV tidak menulis isi kepala tokoh lain;
- **Tes Pas:** tidak ada teknik/ide yang terasa ditempel;
- bab memberi alasan untuk lanjut, bukan bab pengisi.

Jangan menambahkan ringkasan panjang atau pujian diri.

## 8. Definition of Done per Bab

- 600–900 kata; titik balik target 900, maksimal 900.
- Satu POV, satu adegan/beat, satu perubahan.
- Format `## Bab N: Judul`, judul 2–5 kata, tanpa quote pembuka.
- Hook adalah kalimat terakhir.
- Tidak ada em dash (`—`), emoji, atau umpatan kasar.
- Istilah asing dijelaskan sekali.
- Tidak ada tokoh/fakta baru tanpa setup.
- Catatan kontinuitas dan update ledger sudah dibuat.
- Rubrik ≥34/40 tanpa nilai <4.
- Lolos Tes Pas; tidak ada teknik/ide yang terasa ditempel.
- Penyimpangan outline dicatat.

## 9. Batas Respons

- Satu bab per respons adalah default.
- Batch hanya jika user meminta.
- Jangan menampilkan seluruh outline/ledger; tampilkan bagian yang berubah.
- Jangan mengulang isi panduan; rujuk nomor file.
- Revisi lokal, bukan menulis ulang seluruh bab.

## 10. File Tanggung Jawab

| File | Siapa yang mengubah | Kapan |
|---|---|---|
| `canon.md` | Agent, dengan persetujuan user | Fakta baru/arc berubah |
| `outline.md` | Agent, lewat change request | Sebelum menulis bab |
| `ledger.md` | Agent | Setelah setiap bab |
| `feedback.md` | Agent | Setelah feedback user |
| `learnings/editor-feedback.md` | Agent | Feedback berulang |
| `learnings/changelog.md` | Agent | Setiap perubahan aturan engine |

## 11. Jika Ada Konflik

1. Instruksi user terbaru.
2. Outline terkunci dan canon project — untuk fakta cerita.
3. `acuan-bahasa.docx` dan `engine/05-style.md` — untuk gaya, diksi, dan cara penulisan.
4. `Kerangka Plot yang Terbukti untuk Web Novel.md`, `engine/02-premise.md`, `engine/03-structure.md`, dan `engine/08-quality.md` — untuk kerangka plot, kelayakan premis, siklus coba-gagal, planting, dan uji logika alur cerita.
5. File lain di `engine/`.
6. Dokumen arsip di `old-documents-unneeded/`.
7. Hal lainnya.

Jika outline/canon bertentangan dengan aturan craft: outline/canon menang untuk fakta,
panduan/engine menang untuk cara menulis. Jika dua file engine bertentangan, laporkan dan
usulkan versi yang dipertahankan.

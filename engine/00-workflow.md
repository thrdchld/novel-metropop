# 00 — Workflow

## 1. Mulai Sesi

1. Baca `AGENTS.md`, `engine/README.md`, lalu file ini (`engine/00-workflow.md`), dan
   panduan sumber.
2. Periksa `../story/`.
3. Ringkas posisi repo 2–3 baris.
4. Tanya **satu** pertanyaan:

> Mau apa hari ini: (A) cari ide/premis baru, (B) mulai project baru, (C) lanjutkan
> cerita yang ada, (D) revisi cerita, atau (E) analisis referensi/riset?

Jangan bertanya lebih dari satu pertanyaan pembuka. Jangan menulis prosa sebelum user
memilih mode.

## 2. Mode A — Ide / Premis Baru

Baca `02-premise.md`. Beri **3 opsi**. Format tiap opsi:

```markdown
## Opsi 1 — "Judul"
- **Logline:** satu kalimat.
- **Tema:** satu pertanyaan/idea.
- **Tokoh inti:**
  - Protagonis: nama, pekerjaan, cacat khas.
  - Love interest: nama, pekerjaan, hambatan struktural.
  - Antagonis: nama, posisi, motif yang ia percaya benar.
  - Sekutu: nama, peran, taruhan.
- **Sumber humor:** 2–3 situasi.
- **Pertanyaan dramatik:** apakah ...?
```

Jangan menulis bab. Tunggu user memilih, meminta variasi, atau memberi premis sendiri.
Jika user memberi premis, jangan mengganti; kembangkan.

## 3. Mode B — Project Baru

### 3.1 Klarifikasi

Tanyakan maksimal 3 hal yang belum jelas. Jika user tidak menentukan, pakai default
berikut tanpa bertanya:

- 30–40 bab, ±750 kata/bab;
- tone hangat/jenaka/getir;
- ending terbuka atau bahagia;
- 1 POV utama, bab sampingan maksimal 10–15%.

Jika user belum memberi premis, jalankan Mode A dulu (3 opsi) sebelum membuat canon.

### 3.2 Buat Folder

Buat `story/<Judul>/` dengan:

```text
canon.md
outline.md
ledger.md
feedback.md
chapters/
```

Gunakan template di `templates/`. Jangan mengarang format baru.

### 3.3 Isi Canon

Canon wajib memuat:

- judul, logline, blurb 3–5 kalimat;
- tema dan pertanyaan dramatik;
- janji ke pembaca;
- setting: kota, perusahaan, pekerjaan, proyek, kanal komunikasi;
- cast table + character sheet lengkap;
- aturan dunia dan mekanisme teknis yang menggerakkan plot;
- motif (refleks, objek, aturan, tekanan keluarga);
- tekanan keluarga dan taruhan personal;
- arah ending (boleh spoiler; ini dokumen kerja);
- batasan konten.

### 3.4 Isi Outline

Baca `03-structure.md`. Outline wajib punya:

- status versi (mulai v0.1 DRAFT);
- peta babak;
- untuk setiap bab: nomor, judul 2–5 kata, hari/jam/lokasi, POV, tujuan adegan,
  komplikasi, 3–5 beat, perubahan, siapa tahu apa, setup/payoff, teknik naratif, hook,
  alasan logis, pertanyaan pembaca yang dijawab, dan yang **TIDAK** terjadi;
- titik putar dan midpoint;
- catatan setup/payoff.

### 3.5 Stress Test

Jawab 10 pertanyaan skeptis di `08-quality.md` dengan merujuk bab. Lakukan simulasi tiga
peran:

1. pembaca awam yang curiga;
2. antagonis yang cerdas;
3. protagonis yang berpikir logis.

Tutup semua lubang sebelum meminta persetujuan.

### 3.6 Persetujuan dan Lock

Presentasikan:

- ringkasan premis dan cast;
- peta babak;
- 3–5 bab pertama secara ringkas;
- lubang yang ditemukan dan cara menutupnya;
- risiko yang masih ada.

Minta persetujuan user. Setelah disetujui, tandai:

```markdown
**Status:** TERKUNCI v1.0
**Tanggal lock:** YYYY-MM-DD
```

Jangan menulis Bab 1 sebelum status terkunci.

### 3.7 Tulis Bab 1

Baca `06-chapter.md`. Bab 1 wajib in medias res. Tulis satu bab saja. Setelah selesai,
ikuti Loop Bab di bagian 7.

## 4. Mode C — Lanjutkan Cerita

1. Baca `canon.md`, `ledger.md`, dan 1–2 bab terakhir.
2. Tulis **posisi cerita 5 baris**:
   - hari/jam/lokasi terakhir;
   - kondisi protagonis (emosi, benda, urusan menggantung);
   - hook bab terakhir;
   - fakta canon/ledger yang akan dipakai;
   - setup/payoff yang harus ditanam atau dibayar.
3. Minta konfirmasi user.
4. Setelah dikonfirmasi, tulis satu bab.
5. Update `ledger.md`; update `canon.md` jika ada fakta baru.
6. Laporkan penyimpangan outline dengan jujur.

Jika user minta lanjut tanpa konfirmasi, tetap tampilkan posisi 5 baris sebelum menulis.

## 5. Mode D — Revisi

Baca `09-revision.md`.

1. Tanyakan: bab mana, feedback-nya apa, boleh mengubah canon atau tidak.
2. Klasifikasikan:
   - **gaya** → terapkan ke semua bab terdampak;
   - **logika/plot** → Permintaan Perubahan + update outline/ledger;
   - **preferensi baru** → catat di `learnings/editor-feedback.md`.
3. Revisi lokal; jangan menulis ulang bab penuh jika masalahnya lokal.
4. Cek timeline, pengetahuan tokoh, dan setup/payoff.
5. Laporkan perubahan dan file yang diperbarui.

## 6. Mode E — Riset / Referensi

Baca `sources.md`.

- PDF/teks/URL: ekstrak, ringkas, ambil prinsip.
- Jangan menyalin karya berhak cipta.
- Simpan catatan di `sources.md` atau `learnings/`.
- Tanyakan apakah temuan mau dijadikan aturan engine atau hanya referensi project.

## 7. Loop Setelah Menulis Bab

Setiap selesai satu bab, simpan ke `story/<Judul>/chapters/bab-NN.md`, lalu kirim dengan
urutan tetap:

1. **Teks bab**.
2. **Catatan kontinuitas 5–8 baris**:
   - waktu/lokasi;
   - fakta baru (tandai **BARU**);
   - siapa tahu apa sekarang;
   - benda/urusan yang dibawa;
   - setup/payoff;
   - risiko kontinuitas.
3. **Skor rubrik 8 kriteria** dalam satu baris (1–5). Lulus jika tidak ada nilai <4
   dan total ≥34/40.
4. **Penyimpangan outline**: “tidak ada” atau daftar jujur.
5. **Satu pertanyaan** ke user, hanya jika perlu.

Jangan menambahkan ringkasan panjang atau pujian diri.

## 8. Definition of Done per Bab

- 600–900 kata (titik balik 720–950).
- Satu POV, satu adegan/beat, satu perubahan.
- Format `## Bab N: Judul`, judul 2–5 kata.
- Hook adalah kalimat terakhir.
- Tidak ada emoji/umpatan.
- Istilah asing dijelaskan sekali.
- Tidak ada tokoh/fakta baru tanpa setup.
- Catatan kontinuitas dan update ledger sudah dibuat.
- Rubrik ≥34/40 tanpa nilai <4.
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

- **Fakta cerita:** instruksi user terbaru > `canon.md` project.
- **Aturan menulis:** instruksi user terbaru > panduan sumber > file di `engine/`.
- Jika canon bertentangan dengan aturan craft: canon menang untuk fakta, engine menang
  untuk cara menulis.
- Jika dua file engine bertentangan, laporkan dan usulkan versi yang dipertahankan.

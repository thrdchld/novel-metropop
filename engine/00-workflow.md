# 00 — Alur Kerja Simpel (Bebas Over-Engineering) & Smart-Reading

> **File Pemilik Tunggal:** File ini mengatur **Alur Kerja 4 Tahap yang Simpel, Filter Anti-Yes-Man (Kapan Ide Harus Dibuang), Protokol Smart-Reading, dan Urutan Menulis Bab**.

---

## 1. Prinsip Utama Repo Ini: Simpel, Relate dengan Kehidupan Harian Indonesia, dan Bermakna

1. **Ini Novel Web Cerita Harian, BUKAN Novel Ekonomi, Kriminal, Hukum, atau Detektif Berat:**
   - Cerita di repo ini adalah kisah keseharian manusia Indonesia (pekerja kantoran biasa, mahasiswa, keluarga, sahabat, tetangga, usaha kecil) yang **sederhana, dekat dengan kehidupan nyata (*relate*), punya humor ringan yang alami, dan punya makna emosional yang hangat**.
   - **DILARANG KERAS (*Over-Engineering Ban*):** Jangan pernah mengubah cerita harian menjadi sengketa uang puluhan/ratusan juta, audit kuitansi, pemerasan, kontrak perjanjian palsu 30 hari, atau investigasi barang bukti berbelit-belit.
2. **Aturan Anti-Yes-Man Mutlak: "Kalau Ide Terpaksa, BUANG, Jangan Ditambal!"**
   - Kelemahan terbesar AI adalah selalu berusaha membuat setiap ide terlihat "bisa dilanjut" dengan cara menambalnya memakai aturan kontrak, denda uang, atau kebetulan palsu.
   - **Mulai sekarang, AI DILARANG menambal ide yang tidak alami.** Jika sebuah ide (baik dari pengguna maupun dari AI sendiri) membutuhkan profesi/jasa yang aneh di dunia nyata, atau jalan ceritanya baru bisa berjalan kalau ada skenario jebakan rumit dan kebetulan yang dipaksakan, **AI WAJIB menyatakan secara jujur bahwa ide itu TIDAK BISA DILANJUTKAN dan harus dibuang/diganti dari akarnya.**

---

## 2. Empat Tahap Kerja yang Simpel (Tanpa Birokrasi Tabel Rumit)

Jangan pernah melompat langsung membuat daftar puluhan bab sebelum jalan cerita utuhnya diuji secara sederhana! Ikuti 4 tahap ini secara berurutan:

| Tahap | Apa yang Dikerjakan | Aturan Lulus / Buang |
|---|---|---|
| **Tahap 1: Premis ABCD Simpel** | Tulis 4 kalimat sederhana: **A (Tokoh)**, **B (Keseharian)**, **C (Kejadian Pemicu)**, **D (Tindakan Utama)**. | Jika pekerjaan/rutinitas di **B** atau pemicu di **C** tidak wajar dialami orang Indonesia sehari-hari -> **BUANG IDENYA, jangan dilanjut!** |
| **Tahap 2: Cerita Utuh Awal-Tengah-Akhir (4-5 Paragraf)** | Sebelum membuat daftar bab, tulis dulu **jalan cerita utuh dari Awal, Tengah, sampai Akhir dalam 4-5 paragraf bahasa manusia biasa**. | Uji pakai akal sehat: Apakah reaksi tokoh wajar sebagai manusia? Apakah ada bagian yang dipaksakan? Jika terasa mengada-ada -> **BERHENTI & GANTI CERITA di tahap ini.** |
| **Tahap 3: Outline Per Bab Simpel (4 Poin per Bab)** | Setelah Cerita Utuh 4-5 paragraf disetujui pengguna, pecah menjadi daftar bab (misal 25-34 bab). **Setiap bab cukup 4 poin singkat** (bukan 18 kolom!): (1) Waktu & Tempat, (2) Kejadian Inti, (3) Perubahan Emosi/Hubungan, (4) Detail Kecil / *Planting-Callback*. | Kunci `outline.md` (**TERKUNCI v1.0**). Outline ini menjadi rel tetap yang wajib diikuti 100% saat menulis bab. |
| **Tahap 4: Menulis Bab (1 per 1)** | Tulis 1 bab (600-900 kata, teks polos tanpa bintang tebal/miring, 0 em dash) mengikuti `outline.md` secara lurus dengan gaya bercerita sederhana & *to the point* (`05-style.md`). Perbarui `state.md` & `ledger.md`. | Cerita mengalir sesuai outline tanpa mengarang konflik baru di luar outline. |

---

## 3. Protokol Smart-Reading (Baca Hanya yang Dibutuhkan)

| Mode Kerja | File yang Dibaca |
|---|---|
| **Awal Sesi Baru** | `AGENTS.md`, `engine/README.md`, `engine/00-workflow.md`, cek daftar folder di `story/` |
| **Mode A (Cari Ide / Premis ABCD & Cerita Utuh 5 Paragraf)** | `story/universe-registry.md`, `engine/01-genre.md`, `engine/02-premise.md`, `engine/11-worldbuilding.md` |
| **Mode B (Susun Canon & Outline Simpel 4 Poin/Bab)** | `engine/03-structure.md`, `engine/04-character.md`, `engine/11-worldbuilding.md`, `engine/templates/` |
| **Mode C (Menulis Bab)** | `story/<Judul>/state.md`, `canon.md`, `outline.md` (bab aktif), `ledger.md`, 1 bab terakhir, `engine/05-style.md`, `engine/06-chapter.md`, `engine/07-continuity.md` |
| **Mode D (Revisi / Evaluasi)** | `engine/05-style.md`, `engine/08-quality.md`, `engine/09-revision.md`, dan bab terkait |
| **Mode E (Riset / Update Engine)** | `engine/sources.md`, `engine/10-evolution.md` |

*(Jangan pernah membaca `engine/learnings/` saat sesi kerja normal).*

---

## 4. Loop Setelah Menulis Bab

Setiap selesai menulis satu bab ke `story/<Judul>/chapters/bab-NN.md`:
1. **Tampilkan teks bab** (`## Bab N: Judul`, 600-900 kata, teks polos, 0 em dash, 0 quote pembuka).
2. **Catatan kontinuitas singkat (3-5 baris):** waktu/lokasi, kejadian baru, dan benih *planting/callback* yang ditanam atau dibayar.
3. **Perbarui `state.md` & `ledger.md`**, lalu **WAJIB** jalankan satu perintah Gatekeeper Terpadu:
   `python3 scripts/stress-test.py "story/<Judul>"`
   *(Skrip ini otomatis menguji seluruh 16 aturan repo sekaligus: rentang kata 600-900, 100% teks polos, aturan judul bab tanpa nama tokoh, pembuka In Medias Res, batas dialog <=20 kata, 0 eksposisi 'As You Know, Bob' di dialog, 0 kata filter persepsi, 0 stock tells, 0 sintaksis AI, 0 tag buku pelajaran, 0 AI slop/klinis, batas anatomi/bau <=2, EndQ <=75%, 0 deret kalimat seragam, dan audit kontinuitas penuh).* AI dilarang mengirim hasil atau melakukan commit jika `stress-test.py` masih mengembalikan `[GAGAL]`.

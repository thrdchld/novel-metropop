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
| **Tahap 2: Cerita Utuh Awal-Tengah-Akhir (4-5 Paragraf)** | Sebelum membuat daftar bab, tulis dulu **jalan cerita utuh dari Awal, Tengah, sampai Akhir dalam 4-5 paragraf bahasa manusia biasa**. | Susun bagian **"Bukti G1"** di atas `outline.md` sesuai `engine/CORE.md`. Lulus ditentukan gerbang eksternal **G1** (`novel-editor`) tanpa temuan HIGH/BLOCKER. Jika gagal/dipaksakan -> **BERHENTI & GANTI CERITA.** |
| **Tahap 3: Outline Skenario Adegan (Scene Treatment)** | Setelah Cerita Utuh 4-5 paragraf disetujui, pecah menjadi daftar bab dengan format **Skenario Adegan (`03-structure.md`)**: (1) Adegan & Tokoh (+alasan fisik hadir), (2) Variasi Pembuka & Skenario Masuk, (3) Ketukan Aksi & Reaksi (1-2-3), (4) Bentuk Hook & Skenario Penutup, (5) Detail Fisik / Planting. | Susun bagian **"Bukti G2"** di `outline.md` sesuai `engine/CORE.md`. Lulus ditentukan gerbang eksternal **G2** (`novel-editor`); outline baru boleh dikunci (**TERKUNCI v1.0**) bila laporan G2 bebas HIGH/BLOCKER. |
| **Tahap 4: Menulis Bab (1 per 1)** | Tulis 1 bab (600-900 kata, teks polos tanpa bintang tebal/miring, 0 em dash) mengikuti `outline.md` secara lurus dengan gaya bercerita sederhana & *to the point* (`05-style.md`). Perbarui `state.md` & `ledger.md`. | Tulis **"Bukti tiap bab"** di `ledger.md` sesuai `engine/CORE.md`, lulus Pilar 1 (`stress-test.py`), dan lakukan audit mandiri Pilar 2 sebagai persiapan. Lulus akhir ditentukan oleh bukti tertulis di `ledger.md` dan gerbang eksternal **G3** (`novel-editor`). |

---

## 3. Protokol Smart-Reading (Baca Hanya yang Dibutuhkan)

| Mode Kerja | File yang Dibaca |
|---|---|
| **Awal sesi** | `AGENTS.md`, `engine/CORE.md` |
| **Mode A (ide/premis)** | `engine/01-genre.md`, `engine/02-premise.md`, `engine/11-worldbuilding.md`, `story/universe-registry.md` |
| **Mode B (canon dan outline)** | `engine/03-structure.md`, `engine/04-character.md`, `engine/11-worldbuilding.md`, `engine/08-quality.md` (§2, §4, §4A), `engine/templates/` |
| **Mode C (menulis bab)** | `state.md`, `canon.md`, `outline.md` (bab aktif), `ledger.md`, 1 bab terakhir, `engine/05-style.md`, `engine/06-chapter.md`, `engine/07-continuity.md`, `engine/08-quality.md` (§2B) |
| **Mode D (revisi)** | `engine/05-style.md`, `engine/08-quality.md`, `engine/09-revision.md`, dan bab terkait |

*(Jangan pernah membaca `engine/learnings/` saat sesi kerja normal).*

---

## 4. Loop Setelah Menulis Bab

Setiap selesai menulis satu bab ke `story/<Judul>/chapters/bab-NN.md`:
1. **Tampilkan teks bab** (`## Bab N: Judul`, 600-900 kata, teks polos, 0 em dash, 0 quote pembuka).
2. **Catatan kontinuitas singkat (3-5 baris):** waktu/lokasi, kejadian baru, dan benih *planting/callback* yang ditanam atau dibayar.
3. **Perbarui `state.md` & `ledger.md`**, lalu **WAJIB** jalankan langkah persiapan dan verifikasi berikut:
   - **Pilar 1 (Uji Kelayakan Teknis):**
     `python3 scripts/stress-test.py "story/<Judul>"`
     *(Skrip ini otomatis menguji 22 pemeriksaan teknis: 8 sinkronisasi aset + 14 aturan format prosa polos, batas dialog, 0 em dash, dan header). Wajib berstatus `[LULUS]` (0 pelanggaran). Gunakan `--fix` untuk sinkronisasi otomatis aset turunan.*
   - **Pilar 2 (Persiapan Kelayakan Baca / Finishing Manusiawi):**
     Audit mandiri berdasarkan 5 filter di `engine/08-quality.md` §1B (sebab-akibat nyata, psikologi manusiawi, anti-garing, kewajaran tutur lisan, dan musikalitas irama prosa) tetap dilakukan sebagai persiapan sebelum menyetorkan bab, **tetapi bukan penentu lulus**. Yang menentukan kelulusan adalah **bukti tertulis per bab di `ledger.md`** (sesuai `engine/CORE.md`) serta laporan gerbang eksternal **G3** (`novel-editor`, tiap 10 bab dan saat tamat, tanpa temuan HIGH/BLOCKER).
   AI dilarang mengirim hasil, mengklaim bab lulus, atau menyatakan tamat jika Pilar 1 belum lulus 100%, bukti tertulis di `ledger.md` belum lengkap, atau laporan G3 terakhir masih memuat temuan HIGH/BLOCKER.

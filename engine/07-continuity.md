# 07 — Kontinuitas: Canon dan Story Ledger

> **File Pemilik:** File ini memiliki aturan **Pengelolaan Canon vs Story Ledger (A–G), Pra-cek 5 Baris, Catatan Kontinuitas Pasca-Bab, dan Anti-Halusinasi Fakta**.

## 1. Dua Sumber Kebenaran Cerita

- **`canon.md` (Dokumen Dasar / Bible):** Menyimpan rencana dasar cerita: premis, 5 slot kelayakan, kerangka plot, rencana *planting* 2 kali, profil karakter, aturan dunia, dan arah ending.
- **`ledger.md` (Story Ledger / Dokumen Hidup):** Mencatat fakta yang **benar-benar sudah terjadi di teks bab** yang telah ditulis: timeline, lokasi, matriks pengetahuan, status/benda tokoh, angka keras, status *setup/planting & payoff*, serta log perubahan.

### Aturan Prioritas Fakta
1. Timeline di `canon.md` adalah rencana awal. Begitu bab selesai ditulis, **Ledger A menjadi master timeline**.
2. Fakta yang dianggap sah telah terjadi hanyalah fakta yang tertulis di **teks bab** dan tercatat di **`ledger.md`**.
3. Jangan pernah mengklaim di ledger bahwa suatu fakta atau *planting* sudah terjadi jika kalimatnya tidak ada di dalam teks bab.
4. Jika ragu atau fakta belum ditentukan, jangan mengarang dari ingatan—tandai `[PERIKSA]` dan cek kembali file.

---

## 2. Struktur Story Ledger (Bagian A–G)

Perbarui bagian yang berubah setiap kali selesai menulis satu bab:

- **A. Timeline Master:** `Bab | Hari/jam | Lokasi | Tokoh hadir | Kejadian kunci`. Pastikan selang waktu antarbab, jam operasional, dan waktu tempuh masuk akal.
- **A2. Timeline Masa Lalu:** `Tokoh | Usia/tahun | Kejadian penting | Dirujuk di bab`. Menjaga agar backstory/flashback tidak bertabrakan dengan usia dan kronologi masa kini.
- **B. Daftar Lokasi:** `Lokasi | Bab pertama | Ciri tetap | Siapa sering di situ | Jarak/waktu`.
- **C. Matriks Pengetahuan (Siapa Tahu Apa):** `Fakta/rahasia | Siapa tahu | Sejak bab | Dari mana`. Sebelum seorang tokoh mengucapkan atau memakai informasi, wajib periksa tabel ini agar tidak bocor (*knowledge leak*).
- **D. Status Tokoh per Bab:** `Bab | POV | Emosi/perubahan | Benda yang dibawa | Hubungan terakhir | Rahasia yang dipegang | Urusan menggantung`. Benda yang dipegang, pakaian, luka, atau chat yang belum dibalas tidak boleh lenyap begitu saja di bab berikutnya.
- **E. Fakta Keras dan Angka:** `Fakta | Nilai | Rujukan bab`. Mencatat angka spesifik (nominal uang, jam tenggat, nomor lantai, IPK, durasi kontrak) agar selalu konsisten.
- **F. Benang Terbuka (Setup / Planting 2x & Payoff):** `Bahan/Benang | Tanaman 1 (Sepele) | Tanaman 2 (Tampak Hiasan) | Payoff/Dibayar | Status`. Memastikan semua bahan solusi akhir sudah ditanam minimal dua kali sebelum titik terendah.
- **G. Log Perubahan Canon/Outline:** `Versi | Tanggal | Perubahan | Alasan | Bab terdampak`.

---

## 3. Prosedur Wajib Sebelum & Sesudah Menulis Bab

### Pra-Cek 5 Baris (Sebelum Menulis Bab Baru)
Baca `canon.md`, `outline.md`, `ledger.md`, dan 1–2 bab terakhir, lalu tampilkan:
1. **Waktu & Lokasi Terakhir:** Hari, jam, dan lokasi akhir bab sebelumnya.
2. **Kondisi Protagonis:** Emosi terakhir, benda yang sedang dibawa, dan urusan yang menggantung.
3. **Sambungan Hook:** Kalimat hook bab sebelumnya yang wajib langsung dijawab/disambung.
4. **Fakta & Siklus Aktif:** Fakta canon/ledger dan posisi Siklus Coba-Gagal yang akan dijalankan di bab ini.
5. **Target Planting / Payoff:** Bahan solusi (Tanaman 1 / Tanaman 2) yang harus ditanam atau dibayar di bab ini.

### Catatan Kontinuitas 5–8 Baris (Setelah Menulis Bab)
Kirimkan bersama teks bab:
- Waktu dan lokasi bab ini;
- Fakta baru yang muncul di teks (tandai **BARU**);
- Siapa tahu apa sekarang (perubahan matriks pengetahuan);
- Benda atau urusan yang dibawa ke bab berikutnya;
- *Setup/planting* yang berhasil ditanam atau *payoff* yang dibayar;
- Risiko kontinuitas untuk bab selanjutnya.

---

## 4. Protokol Ganti Sesi (Anti-Amnesia AI)

Jika percakapan dimulai di sesi baru atau setelah konteks dipadatkan (*compaction*), AI **dilarang langsung menulis bab** sebelum membaca ulang:
1. `AGENTS.md` dan `engine/00-workflow.md`
2. `story/<Judul>/canon.md`
3. `story/<Judul>/outline.md`
4. `story/<Judul>/ledger.md`
5. Teks bab terakhir di `story/<Judul>/chapters/`

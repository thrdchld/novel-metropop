# 09 — Revisi, Audit 5 Tahap, dan Remediasi Beruntun (R1-R5)

> **File Pemilik Tunggal:** File ini adalah rujukan utama untuk **Klasifikasi Feedback, Audit Menyeluruh 5 Tahap (Top-Down), Alur Remediasi Beruntun (*Cascading Remediation* R1-R5), Sistem Revisi 4 Lapis Terfokus (*4-Pass Revision*), Rasio Edit Profesional (74/18/8), dan Permintaan Perubahan**.
>
> Untuk kriteria rubrik 8 poin, 10 Uji Logika, dan 10 Tanda Bahaya lihat `08-quality.md`.

---

## 1. Prinsip Piramida Ketergantungan Struktur (Top-Down)

Kesalahan fatal saat merevisi naskah adalah mengedit dialog atau kalimat secara acak ketika struktur di atasnya masih bermasalah. Sebuah novel dibangun di atas **5 Tingkat Ketergantungan**:

1. **Tingkat 1: Fondasi Canon & World Building** (`canon.md` - Premis 5 Slot, Aturan Dunia, Nilai Uang, Cast, Matriks Sapaan)
2. **Tingkat 2: Arsitektur Outline & Plot Makro** (`outline.md` - 8 Kerangka Plot, Titik Balik, Siklus Coba-Gagal Uji 100%, Planting 2x)
3. **Tingkat 3: Integritas Kontinuitas & State Machine** (`state.md`, `ledger.md` - Jangkar Waktu Relatif, Status Hubungan, Log Fakta Fisik Mikro)
4. **Tingkat 4: Anatomi Adegan & Mesin Mikro Bab** (`chapters/` - 600-900 Kata, Beat, Pola `Berhasil, tapi...` / `Gagal, dan malah...`, Geser Emosi, Hook)
5. **Tingkat 5: Kualitas Prosa, Dialog, & Bahasa Lokal** (4-Pass Prosa, Anti-AI Slop, 0 Em Dash, Teks Polos)

**Hukum Aliran ke Bawah (*Downward Cascade Law*):** Pemeriksaan (*Audit*) dan perbaikan (*Remediation*) wajib berjalan dari tingkat tertinggi yang bermasalah turun ke tingkat di bawahnya, dengan mengisolasi rentang bab terdampak agar bab steril tidak rusak.

---

## 2. Klasifikasi Feedback

| Jenis Feedback | Contoh | Tindakan |
|---|---|---|
| **Gaya & Bahasa** | "Terlalu baku", "berasa AI slop", "ada em dash", "dialog kaku" | Perbaiki di bab terdampak (R4), catat aturan di `05-style.md` bila belum ada |
| **Logika / Plot / Alur** | "Janggal", "kenapa nggak pakai cara gampang aja?" | Jalankan R1-R5: uji dengan 7 Cara Menutup Jalan Mudah & Uji Ruang Lingkup Minimal (`02-premise.md`), buat Permintaan Perubahan, update canon/outline/state |
| **Preferensi Baru** | "Aku mau tone seperti *Resign!*", "nama jasa diganti Bolu Ketan" | Terapkan ke file panduan terkait di `engine/` dan catat di `learnings/` |
| **Fakta Canon / Kontinuitas** | "Umurnya 27, bukan 28", "kemarin merujuk hari yang salah" | Update `canon.md`, `state.md`, dan `ledger.md`, lalu perbaiki bab terdampak |
| **Format & Panjang Kata** | Bab di bawah 600 kata, ada tanda bintang/tebal/miring di naskah | Bersihkan ke teks polos dan sesuaikan panjang kata ke 600-900 kata |

---

## 3. Prosedur Audit 5 Tahap & Remediasi Beruntun (R1-R5)

Saat diminta menilai atau memperbaiki naskah secara menyeluruh, jalankan **Audit 5 Tahap** untuk menyusun Matriks Diagnostik Cacat (berlabel *Critical*, *Major*, *Minor*), lalu eksekusi **Remediasi R1-R5**:

### Langkah R1 — Perbaiki Fondasi Canon & World Building (Tingkat 1)
- Periksa `canon.md`: pastikan 5 slot kelayakan premis, penutupan minimal 5 jalan mudah, skala ekonomi kelas menengah Indonesia, dan Matriks Sapaan tidak punya celah logika.
- Jika ada perubahan aturan/premis, buat draf di `templates/change-request.md`.

### Langkah R2 — Sinkronkan Arsitektur Outline (Tingkat 2)
- Periksa `outline.md`: pastikan sesuai salah satu dari 8 Kerangka Plot Terbukti (`03-structure.md`), mencapai minimal 6-8 titik balik, setiap siklus coba-gagal lolos **Uji 100%**, dan benih solusi ditanam minimal 2 kali.
- Jika masalah ditemukan di tengah penulisan bab, gunakan **4 Teknik Bedah Alur** (`08-quality.md` Bagian 4B: Pengalihan Rute Kausal, Memeluk Kemustahilan Jadi Komplikasi, Jahitan Bedah Mikro, atau Pertukaran Beban Pembuktian) tanpa merombak bab awal yang sudah steril.

### Langkah R3 — Sinkronisasi State Machine & Isolasi Bab Terdampak (Tingkat 3)
- Perbarui `state.md` dan `ledger.md` (jangkar waktu relatif, status hubungan resmi, inventaris benda, dan saluran fisik pemerolehan data mikro).
- Tetapkan dengan tegas nomor bab awal sampai bab akhir yang terdampak. **Dilarang mengubah bab di luar jangkauan yang sudah steril.**

### Langkah R4 — Eksekusi Revisi Lokal Prosa Bab Terdampak (Tingkat 4 & 5)
- Gunakan **Rasio Edit Profesional (74% Ganti / 18% Hapus / 8% Tambah)** untuk mencegah *lexical dilution*:
  1. **Uji Hapus (*Deletion Test*):** Jika kata/klausa tambahan dicoret dan maknanya tetap utuh, hapus tambahan itu.
  2. **Uji Kembali ke Asal (*Reversion Test*):** Jika kalimat asli sudah lebih pendek, lincah, dan logis, pertahankan kalimat asli.
- Jalankan **Sistem Revisi 4 Lapis Terfokus** (Bagian 4 di bawah).

### Langkah R5 — Verifikasi Regresi Otomatis (*Zero-Regression Gate*)
1. Jalankan `python3 scripts/audit-continuity.py "story/<Judul>"` (wajib 0 FAIL).
2. Jalankan `python3 scripts/analyze-prose.py "story/<Judul>"` (wajib 0 em dash, 0 format bintang/markup, panjang kata 600-900 kata).
3. **Uji Sambungan Bab (*Boundary Seam Test*):** Baca 2 paragraf terakhir Bab N-1 dan 2 paragraf pertama Bab N untuk memastikan transisi mengalir mulus.

---

## 4. Sistem Revisi 4 Lapis Terfokus (*4-Pass Revision System*)

Saat memeriksa atau mengedit bab, jalankan 4 lapis pemeriksaan terpisah ini:

### Lapis 1 — Audit Dialog, Subteks, & Anti-Narator
1. **Uji Tutup-Nama (*Cover-the-Names Test*):** Jika label pembicara ditutup, apakah pembaca tetap tahu siapa yang berbicara dari diksi dan kata gantinya?
2. **Uji Anti-Eksposisi Rasa Narator:** Pangkas dialog yang mengulang kronologi narasi atau menyebut spesifikasi teknis (*"ukuran A4"*); jadikan ucapan lisan singkat, dan pindahkan gerutuannya ke monolog batin.
3. **Uji Gesekan & Subteks:** Pastikan ada tarik-ulur, gengsi, ngeles, atau *action beat* fisik kecil sesuai `acuan-bahasa.docx`.
4. **Cek Matriks Sapaan Kontekstual:** Sesuaikan panggilan antar-tokoh dengan tabel di `canon.md`.

### Lapis 2 — Audit Logika Fisik, Ukuran Benda, & Asimetri Pengetahuan
1. **Kemurnian POV 1:** Tidak ada bocoran nama *Character Sheet* POV 3 (seperti menyebut ibu sendiri dengan nama lengkap) atau membaca isi kepala tokoh lain.
2. **Uji Asimetri Pengetahuan (*"Kok Dia Tahu Info Itu?"*):** Tokoh lain hanya boleh tahu fakta/data mikro jika sudah melihat langsung, mendengar di dialog, atau membaca dokumen/layar (`07-continuity.md`).
3. **Uji Ukuran, Dimensi, & Wadah Benda:** Pastikan ukuran benda masuk akal dengan wadahnya (`08-quality.md`).
4. **Uji Prosedur Dunia Nyata & Hitungan Uang:** Pastikan prosedur sehari-hari dan hitungan uang akurat secara matematis.

### Lapis 3 — Audit Bahasa Sehari-hari Indonesia, Anti-AI Slop, & Format Polos
1. **Sapu Bersih Larangan Mutlak:** **0 em dash (`—`)**, **0 quote pembuka di atas bab**, **0 simbol tebal/miring/markup (`*`, `**`)**, dan **0 terjemahan harfiah bahasa Inggris**.
2. **Sapu Bersih AI Slop (`05-style.md`):** Hapus kalimat kesimpulan moral di akhir adegan, pecah klausa *"Sambil..., aku..."* / *"..., membuat..."*, hapus tag dialog buku pelajaran (*ujarnya/tuturnya/tukasnya*), batasi sensasi anatomi tubuh maksimal 1-2 puncak per bab, dan kembalikan kata hubung lisan (`soalnya, gara-gara, masalahnya, makanya, habisnya`).
3. **Cek Posisi Kalimat:** Pastikan paragraf berdialog tidak $>75\%$ berakhir di tanda kutip penutup, dan pecah deretan $\ge 3$ kalimat berurutan yang panjangnya seragam.

### Lapis 4 — Audit Gelombang Ketegangan, *Reader-Sim*, & Hook
1. **Peta Ketegangan & Pola Hasil:** Pastikan adegan berpola `Berhasil, tapi...` atau `Gagal, dan malah...` dengan pergeseran emosi yang nyata.
2. **Ketajaman Hook Akhir:** Pastikan kalimat terakhir membuat pembaca ingin langsung membuka bab berikutnya.

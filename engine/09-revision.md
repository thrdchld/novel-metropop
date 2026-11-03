# 09 — Revisi, Feedback, dan Diagnosis Alur Cerita

> **File Pemilik:** File ini memiliki aturan **Klasifikasi Feedback, Prosedur Diagnosis Alur Cerita, Sistem Revisi 4 Lapis Terfokus (*4-Pass Revision*), Rasio Edit Profesional (74/18/8), dan Permintaan Perubahan**.
> Untuk standar pemeriksaan menyeluruh per judul secara berurutan dan alur perbaikan terstruktur anti-regresi, ikuti panduan master: `12-audit-remediation.md`.

## 1. Langkah Awal

Saat user meminta revisi atau analisis naskah/cerita:
1. Tanyakan atau identifikasi: bab/bagian mana yang direvisi, apa masukannya, dan apakah revisi boleh mengubah canon/outline.
2. Jika user meminta **analisis, evaluasi, atau perbaikan alur cerita secara menyeluruh per judul**, wajib ikuti **Standar Pemeriksaan Berurutan (Tahap 1-5) dan Perbaikan Berurutan (Langkah R1-R5)** di `12-audit-remediation.md` agar perbaikan tidak merusak bagian lain.
3. Jangan langsung menulis ulang prosa sebelum masalah logika, kontinuitas, dan kerangka terpetakan.

---

## 2. Klasifikasi Feedback

| Jenis | Contoh | Tindakan |
|---|---|---|
| **Gaya & Bahasa** | "Terlalu baku", "berasa AI slop", "ada em dash", "dialog kaku" | Perbaiki di semua bab terdampak, catat aturan di `learnings/editor-feedback.md` |
| **Logika / Plot / Alur** | "Janggal", "alasan kurang to the point", "kenapa nggak jujur aja?" | Uji dengan **10 Uji Logika & 10 Tanda Bahaya**, buat Permintaan Perubahan, update canon/outline/ledger |
| **Preferensi Baru** | "Aku mau tone lebih getir", "hapus quote di atas bab" | Catat di `learnings/editor-feedback.md`, update file engine terkait, terapkan konsisten |
| **Fakta Canon** | "Umurnya 27, bukan 28" | Update canon dan ledger, cari semua kemunculan di bab lain |
| **Format & Panjang Kata** | Bab di bawah 600 kata, heading salah, ada tanda bintang/tebal/miring di naskah | Perbaiki mekanis, bersihkan ke teks polos, dan sesuaikan panjang kata ke 600–900 kata |

---

## 3. Prosedur Diagnosis & Menilai Alur Cerita

Gunakan prosedur ini (berdasarkan `../Kerangka Plot yang Terbukti untuk Web Novel.md`) saat menilai draf novel atau outline:

1. **Uji Kelayakan Premis (5 Slot):**
   - Apakah keinginan vs kebutuhan tokoh sudah berbeda?
   - Apakah masalah dan tenggat waktu datang dari pihak luar?
   - Apakah konsekuensi gagal konkret dan terukur (bukan sekadar malu)?
   - Apakah 3 jalan keluar termudah sudah ditutup dengan alasan tertulis (tanpa membuat tokoh tampak bodoh)?
   - Apakah ada perubahan di akhir beserta harga nyata yang dibayar?
2. **Identifikasi Kerangka Plot & Hitungan Titik Balik:**
   - Petakan cerita ke salah satu dari **8 Kerangka Plot Terbukti** (`03-structure.md`).
   - Hitung jumlah titik balik: apakah mencapai minimal **6 titik balik** (30 bab) atau **8 titik balik** (40 bab)?
3. **Evaluasi Siklus Coba-Gagal di Bagian Tengah:**
   - Periksa apakah tiap percobaan memiliki 6 komponen (Tujuan, Alasan memilih, Cara, Hambatan dari watak/aturan dunia, Hasil, Akibat + momen canggung).
   - Jalankan **Uji 100%**: jika percobaan itu berhasil penuh, apakah masalah inti selesai? Jika tidak, tandai sebagai *filler* dan ganti.
4. **Evaluasi Planting Solusi Akhir:**
   - Periksa apakah bahan solusi akhir (orang, benda, kebiasaan, informasi) sudah ditanam **minimal dua kali** di Babak 1–2 (satu sepele, satu tampak seperti hiasan).
5. **Pindai 10 Tanda Bahaya (*Red Flags*) & 7 Uji Logika Mikro:**
   - Cocokkan dengan tabel 10 Tanda Bahaya dan **7 Uji Logika Mikro & Prosedur Dunia Nyata** di `08-quality.md` (urut sebab-akibat dialog, prosedur parkir/bank/hukum di dunia nyata, hitungan matematika uang DP vs lunas, posisi fisik/masker/benda bawaan, dan jalur informasi/nomor telepon).
   - Ambil perbaikan paling logis dan tulis alasannya dalam satu kalimat.

---

## 4. Sistem Revisi 4 Lapis Terfokus (*4-Pass Revision System*)

Jangan memeriksa semua aspek sekaligus dalam satu kali baca karena detail mikro pasti ada yang terlewat. Saat merevisi bab (baik satu bab maupun *batch*), jalankan **4 Lapis Pemeriksaan Terpisah** secara berurutan:

### Lapis 1 — Audit Dialog, Subteks, & Anti-Narator (*Dialogue & Subtext Pass*)
1. **Uji Tutup-Nama (*Cover-the-Names Test*):** Jika semua label pembicara ditutup, apakah pembaca tetap tahu siapa yang berbicara dari pilihan kata, panjang kalimat, dan kata gantinya (*gue-lu* Bang Bobi vs *aku-kamu* Rian vs *aku-Ibu*)?
2. **Uji Anti-Eksposisi Rasa Narator:** Apakah ada tokoh yang mengulang kronologi narasi secara panjang lebar di dialog, atau menyebutkan ukuran teknis benda (*"ukuran A4"*, mengeja nomor pelat motor milik lawan bicara sendiri)? Jika ada, pangkas dialognya menjadi respons lisan yang singkat dan spontan, lalu pindahkan gerutuan/penjelasannya ke monolog batin atau narasi.
3. **Uji Gesekan & Subteks:** Apakah dua tokoh terlalu cepat setuju tanpa gesekan? Pastikan ada tarik-ulur, gengsi, atau *action beat* fisik kecil (mengelap tangan, melirik jam, meremas tali tas) sebagai pengganti tag dialog membosankan.
4. **Cek Matriks Sapaan Kontekstual:** Pastikan panggilan antar-tokoh sesuai dengan tabel **Matriks Sapaan & Kata Ganti** di `canon.md`.

### Lapis 2 — Audit Logika Fisik, Ukuran Benda, & Asimetri Pengetahuan (*Logic, Physical Scale, & Continuity Pass*)
1. **Kemurnian POV 1:** Pastikan tidak ada bocoran nama *Character Sheet* POV 3 (seperti menyebut ibu kandung dengan *"Ibu Sumi"* atau menyebut tetangga akrab *"Bobi"* tanpa *"Bang"*), julukan berjarak (*"bos muda itu"*), atau pikiran tokoh lain yang tidak mungkin diketahui *"Aku"*.
2. **Uji Asimetri Pengetahuan (*"Kok Dia Tahu Info Itu?"*):** Untuk setiap informasi yang diucapkan Tokoh B, cek di bab berapa Tokoh B melihat atau mendengar informasi itu. Tokoh lain dilarang tahu fakta yang baru ada di monolog batin protagonis.
3. **Uji Ukuran, Dimensi, & Wadah Benda (*Physical Scale*):** Apakah ukuran benda masuk akal dengan wadahnya (kertas A4 terselip bersama katalog A4 di dalam map bekas; kotak kue dibawa dengan *tas jinjing/tote bag*, bukan tas selempang kecil; makanan berkuah dibungkus *rantang susun*)?
4. **Uji Prosedur Dunia Nyata & Hitungan Uang:** Pastikan cara kerja parkir, aturan bank/hukum, dan hitungan uang (DP vs pelunasan vs sisa saldo) 100% akurat secara matematis.

5. **Audit Silang Antarbab (`07-continuity.md`):** Jalankan `scripts/audit-continuity.py` dan cocokkan label status hubungan, waktu relatif, perkenalan tokoh, dan jam kejadian dengan `ledger.md`. Lapis ini wajib dijalankan **setelah** menyisipkan atau menomori ulang bab.

### Lapis 3 — Audit Bahasa Sehari-hari Indonesia, Insting AI, & Ritme Kalimat (*Indonesian Natural Prose Pass*)
1. **Sapu Bersih Larangan Mutlak:** **0 karakter *em dash* (`—`)**, **0 *quote/epigraph* di atas bab**, dan **0 terjemahan harfiah bahasa Inggris** (*arah jam sebelas, izin diberikan, penghangat kabin mobil*).
2. **Sapu Bersih AI Slop, 5 Penyakit Insting AI, & 5 Pola Sintaksis AI (`05-style.md`):**
   - Pastikan monolog batin tidak rapi seperti esai (*non-essayistic interiority*);
   - Hapus kalimat kesimpulan moral / komentar emosional di akhir adegan (*tidy-summary endings*);
   - Jangan meredakan ketegangan terlalu cepat di paragraf yang sama (*positive sentiment skew*);
   - Pecahkan **5 Pola Sintaksis AI**: klausa pembuka/penutup *"Sambil..., aku..."* / *"..., membuat..."*, kata benda pembungkus (*"Sebuah perasaan X menyelimuti"*), nominalisasi subjek, pasangan abstrak kembar, dan kata filter persepsi;
   - Kembalikan **register manusia Indonesia yang ditekan AI**: kata hubung kausal lugas (`soalnya, gara-gara, masalahnya, makanya, habisnya`), kalimat sanggahan (`Bukan karena..., tapi...`), dan tag dialog lugas (`kata/tanya`, **0 rotasi `ujarnya/tuturnya/timpalnya/tukasnya`**).
3. **Batas Sensasi Tubuh (*Over-Embodied Cap*), Jatah Penciuman, & Pijakan Ruang Aksi:**
   - Pastikan emosi campuran **3 mode manusia** (tindakan pada benda konkret + penyebutan jujur *"Jujur, aku takut banget"* + sensasi anatomi tubuh **maksimal 1–2 puncak per bab**);
   - Batasi deskripsi bau/aroma maksimal **1–2 kali per bab**, dan buka adegan di **Ruang Aksi (*Action Space*)**, bukan *Perceived Space*.
4. **Cek 4 Pola Posisi Kalimat (*Discourse Position Tells*) & `scripts/analyze-prose.py`:**
   - Pastikan paragraf berdialog tidak $>75\%$ berakhir di tanda kutip penutup;
   - Pecah deretan $\ge 3$ kalimat berurutan yang panjangnya seragam dan hindari daftar serba tiga (*Rule of Three*);
   - Pastikan ada minimal 1 paragraf perbandingan/kontradiksi ekspektasi vs realitas (*QUD Check*);
   - Jalankan `scripts/analyze-prose.py` untuk verifikasi mekanis otomatis.

### Lapis 4 — Audit Gelombang Ketegangan, *Reader-Sim*, & Hook (*Tension Wave & Pacing Pass*)
1. **Peta Ketegangan Bab (Skala 1–10):** Nilai tingkat ketegangan di **Awal $\rightarrow$ Tengah $\rightarrow$ Akhir Bab**. Jika angkanya datar (misal `4 -> 4 -> 4`), tambahkan gesekan atau komplikasi di tengah bab.
2. **Pergeseran Emosi & *Romance Micro-Shift*:** Kondisi emosional protagonis di akhir bab **wajib berbeda** dari saat bab dibuka (berpola `Berhasil, tapi...` atau `Gagal, dan malah...`), dan setiap pertemuan dengan *love interest* wajib menggeser dinamika mereka satu langkah kecil tanpa mengumumkan *chemistry* secara abstrak.
3. **Uji *Reader-Sim MetroPop* (`08-quality.md`):** Pastikan tidak ada bagian tengah bab yang membuat pembaca HP ingin *scroll* cepat karena kehilangan rasa penasaran.
4. **Ketajaman Hook Kalimat Terakhir:** Pastikan kalimat paling akhir membuat pembaca tidak tahan untuk tidak membuka bab berikutnya.

---

## 5. Revisi Lokal, Rasio Edit Profesional (74/18/8), & Permintaan Perubahan

### Revisi Lokal & Rasio Edit Profesional (74% Ganti / 18% Hapus / 8% Tambah)
- Jangan menulis ulang satu bab penuh jika masalahnya hanya beberapa kalimat atau satu motivasi yang janggal.
- **Waspadai Penyakit Revisi AI (*Lexical Dilution*):** Riset *LAMP Corpus* membuktikan bahwa saat AI diminta mengedit naskah, AI cenderung menambahkan banyak kata sifat pengisi dan penjelasan basa-basi sehingga kepadatan makna turun drastis ($d = -3.10$). Sebaliknya, editor profesional manusia bekerja dengan rasio **74% Mengganti kata yang kurang pas (*Replace*), 18% Menghapus kata mubazir (*Delete*), dan hanya 8% Menambah kalimat baru (*Insert*)**.
- Saat merevisi kalimat atau paragraf, jalankan dua uji wajib ini:
  1. **Uji Hapus (*Deletion Test*):** Untuk setiap kata atau klausa baru yang kamu tambahkan saat revisi, coba coret lagi dalam hati. Jika makna, logika, dan emosinya tetap utuh tanpa tambahan itu, **hapus tambahan tersebut**.
  2. **Uji Kembali ke Asal (*Reversion Test*):** Bandingkan kalimat hasil revisimu dengan kalimat draf aslinya. Jika draf asli sebenarnya sudah lebih pendek, lebih lincah, dan tidak melanggar logika, **pertahankan kalimat asli**.
- Pastikan panjang bab hasil revisi tetap berada di rentang **600–900 kata** (atau hingga **maksimal 1.200 kata hanya jika darurat/urgent** agar tidak memotong kejadian penting).

### Permintaan Perubahan (Jika Mengubah Plot/Canon)
```markdown
# Permintaan Perubahan
1. **Masalah / Tanda Bahaya yang Ditemukan:** ...
2. **Usulan Perbaikan (Berdasarkan Kerangka & Uji Logika):** ...
3. **Bab Lain yang Terdampak:** ...
4. **Perlu Revisi Bab yang Sudah Ditulis?** ...
5. **Dampak pada Canon & Ledger:** ...
```

---

## 6. Cek Pasca-Revisi & Daftar Kritik Editor

### Cek Setelah Revisi
- Lolos seluruh **4 Lapis Pemeriksaan Revisi** di atas;
- Timeline, jam, dan lokasi konsisten;
- Siapa tahu apa tidak bocor;
- Setup/planting (2x) dan payoff terjaga;
- Panjang bab 600–900 kata (maks. 1.200 kata jika darurat), tanpa em dash (`—`), tanpa quote di atas bab;
- Hook akhir bab tetap tajam.

### Daftar Kritik Editor (Jangan Terulang)
1. Bahasa terlalu formal/baku dan tidak seperti obrolan sehari-hari orang Indonesia.
2. Deskripsi melodramatis atau kaku buatan mesin (*AI slop*).
3. Pemakaian em dash (`—`) di narasi atau dialog (dilarang keras di semua novel).
4. Pemakaian quote/epigraph di atas bab (dilarang agar tidak mencontek novel referensi).
5. Bab terlalu pendek di bawah 600 kata.
6. Tindakan atau motivasi tokoh janggal/klise dan tidak *to the point* sesuai karakter.
7. Jalan keluar mudah belum ditutup sehingga pembaca bertanya "kenapa nggak gini aja?".
8. Plot hole atau perubahan aturan mekanisme di tengah penulisan.
9. Kebocoran POV 3 di dalam cerita POV 1 (menyebut ibu kandung dengan nama *character sheet* *"Ibu Sumi"*, menyebut *"Bobi"* tanpa *"Bang"*, atau memakai julukan berjarak *"bos muda itu"*).
10. Asimetri pengetahuan (*"Kok dia tahu info itu?"*) dan *retroactive planting* (mengklaim kejadian masa lalu di dialog padahal adegannya tidak pernah ditulis di bab sebelumnya).
11. Cacat logika ukuran/dimensi benda vs wadahnya (misal kertas A4 terselip di map yang hanya berisi KTP kecil).
13. Kontinuitas lintas bab bocor: status hubungan naik tanpa pemicu (pacar jadi calon istri), "kemarin" untuk kejadian seminggu lalu, tokoh diperkenalkan dua kali, atau adegan "pertama kali" terjadi dua kali.
12. Dialog terlalu panjang menjelaskan kronologi seperti narator, bukannya dipisah antara ucapan lisan singkat dan gerutuan di monolog batin.

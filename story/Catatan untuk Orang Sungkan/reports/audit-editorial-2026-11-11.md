# Audit Editorial — Catatan untuk Orang Sungkan

**Tanggal:** 11 November 2026  
**Mode:** Audit penuh, read-only terhadap manuskrip  
**Repository:** `thrdchld/novel-metropop`  
**Branch:** `main`  
**Judul kanonis:** Catatan untuk Orang Sungkan  
**Status keputusan:** READY TO PUBLISH  
**Rekomendasi:** Tiga perbaikan wajib telah diterapkan dan diverifikasi. Novel siap dipublikasikan; tidak diperlukan restrukturisasi.

---

## 1. Ringkasan keputusan

Novel telah tamat dalam 32 bab. Pembacaan dilakukan terhadap naskah gabungan dan pemeriksaan silang dengan 32 file bab individual, outline, canon, ledger, continuity state, serta paket publikasi. Seluruh isi bab individual cocok dengan bagian yang bersesuaian di `manuscript.md`; tidak ditemukan perbedaan teks antarsalinan.

Cerita memiliki premis yang jelas, perkembangan protagonis yang dapat ditelusuri, konflik romance yang sesuai dengan genre MetroPop, dan payoff yang ditanam sejak awal. Konflik utama selesai. Ending membayar perubahan Nadia dan perkembangan hubungan Nadia–Saka.

Tidak ditemukan BLOCKER struktural yang membuat pembaca gagal memahami cerita atau membuat konflik utama runtuh. Tiga masalah lokal yang ditemukan dalam audit awal telah diperbaiki dan diverifikasi sebelum keputusan publikasi ini ditetapkan.

**Keputusan ini bukan READY TO PUBLISH tanpa syarat.** Status READY WITH MINOR FIXES dipilih karena ada koreksi kontinuitas dan penyelarasan dokumen yang spesifik, bukan karena novel membutuhkan rewrite besar.

## 2. Cakupan audit

Dokumen yang diperiksa:
- `story/Catatan untuk Orang Sungkan/manuscript.md`
- `story/Catatan untuk Orang Sungkan/chapters/bab-01.md` sampai `bab-32.md`
- `outline.md`, `canon.md`, `ledger.md`, `state.md`, dan `publish-stuff.md`
- `AGENTS.md`, `engine/00-workflow.md`, dan `engine/05-style.md` dari novel-metropop
- Standar kerja novel-editor: `AGENTS.md`, `EDITOR-PROTOCOL.md`, serta rules 09, 15, 16, dan 17.

Cakupan penilaian meliputi fondasi cerita, struktur, perkembangan karakter, kausalitas, pengalaman pembaca, adegan, POV, continuity, timeline, planting/payoff, gaya bahasa, format, dan kesiapan publikasi.

## 3. Temuan utama

### F-01 — Durasi adegan Bab 4 tidak cocok dengan kronologi Bab 3

**Status setelah revisi:** FIXED

**Severity:** ERROR  
**Release impact:** FIX BEFORE RELEASE  
**Confidence:** Tinggi  
**Klasifikasi:** MANUSCRIPT ERROR

Bab 3 menempatkan rapat pada Selasa pukul 09.10. Rapat selesai lima belas menit kemudian, lalu Nadia memindahkan barang ke meja proyek lima menit setelahnya. Bab 4 dibuka dengan kalimat:

> “Selama hampir enam jam duduk bersebelahan dengan Saka Wijaya ...”

Adegan Bab 4 kemudian mencapai pukul 17.01. Jika Nadia dan Saka sudah duduk bersama sekitar pukul 09.30, durasinya sekitar tujuh setengah jam, bukan hampir enam jam.

**Perbaikan minimum:** Ubah durasi menjadi keterangan yang sesuai dengan waktu yang sudah ditetapkan, atau tambahkan penanda bahwa mereka baru mulai bekerja bersama lebih siang. Pilihan paling kecil adalah membetulkan durasinya.

### F-02 — Informasi yang diketahui Tari di Bab 29 belum memiliki jalur yang tampak

**Status setelah revisi:** FIXED

**Severity:** REVIEW  
**Release impact:** FIX BEFORE RELEASE  
**Confidence:** Tinggi  
**Klasifikasi:** MANUSCRIPT CONTINUITY / CHARACTER KNOWLEDGE

Di Bab 29, Tari berkata:

> “Gue barusan udah kirim pesan panjang ke WhatsApp Mas Saka buat ngasih tahu kalau semalam lo udah nolak Dimas di depan nyokap lo.”

Namun, sebelum ucapan itu, manuskrip belum memperlihatkan Nadia memberi tahu Tari tentang kejadian makan malam di Bab 27–28. Tari memang mengetahui Nadia sedang mempertimbangkan balikan, tetapi belum ada jalur informasi yang memastikan ia tahu keputusan final dan detail penolakan tersebut.

**Perbaikan minimum:** Tambahkan satu kalimat atau satu beat singkat yang menunjukkan Nadia mengabari Tari setelah makan malam. Tidak perlu membuat adegan baru atau menjelaskan ulang konflik Dimas.

### F-03 — Ringkasan backstory Saka di outline berbeda dari manuskrip

**Status setelah revisi:** FIXED

**Severity:** ERROR pada dokumen pendamping  
**Release impact:** FIX BEFORE RELEASE untuk sinkronisasi arsip  
**Confidence:** Tinggi  
**Klasifikasi:** OUTLINE ERROR

Ringkasan alur di `outline.md` menyebut uang tabungan dan naskah buku Saka dibawa kabur oleh temannya. Namun, Bab 12 manuskrip menjelaskan bahwa Saka terus menalangi sewa studio dan mengerjakan bagian temannya sampai tabungannya habis, studio tutup karena utang sewa, lalu temannya lepas tangan. Tidak ada kejadian naskah buku dibawa kabur di manuskrip.

Ledger mengikuti versi manuskrip, bukan detail pencurian naskah tersebut.

**Perbaikan minimum:** Selaraskan ringkasan alur outline dengan kejadian yang benar-benar ada di Bab 12. Jangan menambahkan pencurian naskah ke manuskrip hanya demi mempertahankan satu detail outline yang tidak dipakai dalam cerita.

## 4. Temuan gaya dan teknis

### F-04 — Enam judul bab melampaui batas 2–5 kata

**Severity:** ERROR format ringan  
**Release impact:** OPTIONAL POLISH  
**Confidence:** Tinggi

Aturan `engine/05-style.md` menetapkan judul bab 2–5 kata. Judul yang melampaui batas:
- Bab 5 — Latihan Pertama dan Utang Ayam Bakar
- Bab 10 — Anak Tengah di Meja Makan Keluarga
- Bab 12 — Cerita dari Yogyakarta dan Botol Penyok
- Bab 18 — Pergeseran Kecil di Meja Nomor Empat
- Bab 23 — Bujukan Ibu dan Hati yang Goyah
- Bab 29 — Kursi Kosong dan Penyesalan yang Terlambat

**Rekomendasi:** Ringkas judul tanpa menghilangkan identitas adegan. Ini konsistensi format, bukan masalah plot.

### F-05 — Beberapa bab melewati rentang standar 600–900 kata

**Severity:** INFO  
**Release impact:** OPTIONAL POLISH  
**Confidence:** Tinggi

Bab yang berada di atas 900 kata:
- Bab 1: sekitar 974 kata
- Bab 2: sekitar 903 kata
- Bab 3: sekitar 921 kata
- Bab 5: sekitar 946 kata
- Bab 31: sekitar 971 kata

Semuanya masih di bawah batas maksimum 1.200 kata yang diperbolehkan outline bila adegan perlu utuh. Karena itu, ini bukan pelanggaran yang otomatis harus dipangkas. Periksa hanya jika ada repetisi yang dapat dipotong tanpa mengurangi adegan.

### F-06 — Reaksi fisik emosional berulang di sejumlah bab

**Severity:** REVIEW  
**Release impact:** OPTIONAL POLISH  
**Confidence:** Tinggi

Aturan gaya MetroPop meminta sensasi tubuh digunakan secara hemat, sekitar satu sampai dua puncak per bab. Sejumlah bab menumpuk beberapa bentuk reaksi fisik sekaligus, terutama Bab 2, 5, 7, 13, 25, dan 30: dada sesak/panas, napas tertahan atau memburu, jantung berdegup, tangan gemetar, tenggorokan tercekat, dan keringat.

Pola ini tidak merusak pemahaman cerita, tetapi bila terus berulang dapat membuat emosi terasa memakai perangkat yang sama.

**Rekomendasi:** Pada revisi gaya, pertahankan satu atau dua reaksi fisik terkuat per adegan emosional. Ganti sisanya dengan tindakan spesifik Nadia terhadap benda atau lingkungan, atau penyebutan perasaan yang lebih lugas.

### F-07 — Beberapa penutup bab menjelaskan kembali makna emosi

**Severity:** REVIEW  
**Release impact:** OPTIONAL POLISH  
**Confidence:** Tinggi

Beberapa penutup menyampaikan kesimpulan emosional setelah adegan sebenarnya sudah berhasil memperlihatkannya. Contoh yang paling jelas adalah penutup Bab 17:

> “Malam itu, bukan cuma perutku yang kenyang oleh cokelat keju, tapi hatiku juga penuh oleh bunyi klik dua kali yang paling manis sedunia.”

Pola serupa muncul pada beberapa penutup reflektif lain. Ini tidak membuat alur gagal, tetapi sedikit mengurangi ruang bagi pembaca untuk menarik kesimpulan sendiri.

**Rekomendasi:** Pertahankan penutup yang sudah kuat melalui tindakan, objek, atau callback. Pangkas kalimat kesimpulan bila tidak menambah informasi atau efek baru.

## 5. Hal yang sudah bekerja

1. **Premis dan fokus:** Perubahan Nadia dari people-pleaser menjadi orang yang mampu menetapkan batas diri menjadi tulang punggung cerita yang jelas.
2. **Kausalitas utama:** Pertemuan dengan Saka, latihan menolak, tekanan keluarga, keraguan soal kepulangan Saka, dan keputusan akhir Nadia tersambung dengan cukup baik.
3. **Character arc Nadia:** Nadia tidak berubah secara instan. Ia berhasil menolak Dimas, kemudian masih goyah ketika tekanan menyentuh keluarga dan rasa takut ditinggalkan. Kemunduran sementara itu membuat perubahan akhirnya lebih masuk akal.
4. **Karakter Saka:** Perhatiannya diwujudkan lewat tindakan dan detail kecil, bukan hanya deklarasi romantis.
5. **Dimas:** Sikap baiknya saat membantu Ibu tidak otomatis menghapus pola lama. Adegan makan malam memperlihatkan bahwa tindakan baik sesaat belum berarti perubahan sikap yang mendasar.
6. **Planting dan payoff:** Post-it kuning, gaya operator customer service, botol penyok, dua klik tutup botol, dan ilustrasi kursi kosong dibayar kembali secara terbaca.
7. **POV:** Narasi orang pertama Nadia terjaga. Tidak ditemukan perpindahan ke isi pikiran tokoh lain yang tidak mungkin diketahui Nadia.
8. **Ending:** Konflik Dimas ditutup, perkembangan Nadia dituntaskan, dan hubungan Nadia–Saka mendapat resolusi yang sesuai dengan nada romance ringan.
9. **Format manuskrip:** Tidak ditemukan em dash, markup tebal/miring, backtick, strikethrough, atau placeholder. Ada 32 heading bab.

## 6. Penilaian delapan gerbang publikasi

| Gerbang | Hasil | Catatan |
|---|---|---|
| Fondasi dan janji cerita | LULUS | Premis dan fokus konsisten |
| Struktur dan perkembangan | LULUS | Ada progres dan payoff |
| Kausalitas, karakter, konflik | LULUS DENGAN CATATAN | Jalur informasi Tari perlu ditampilkan |
| Narasi dan orientasi pembaca | LULUS | Urutan utama dapat diikuti |
| Adegan dan keterbacaan | LULUS | Tidak ditemukan adegan utama yang gagal dipahami |
| Continuity, timeline, dunia cerita | LULUS DENGAN PERBAIKAN LOKAL | Durasi Bab 4 dan jalur informasi Bab 29 |
| Prosa dan teknis naskah | LULUS DENGAN CATATAN | Ada repetisi reaksi fisik dan beberapa judul terlalu panjang |
| Ketuntasan dan payoff | LULUS | Konflik utama dan callback dibayar |

## 7. Daftar tindakan sebelum rilis

**Perbaikan wajib — seluruhnya selesai:**
1. Bab 4: durasi diubah dari “hampir enam jam” menjadi “hampir delapan jam”, sesuai rentang sekitar pukul 09.30 sampai 17.01.
2. Bab 29: ditambahkan satu beat bahwa Nadia mengabari Tari setelah makan malam di Rawamangun, sehingga Tari memiliki jalur informasi sebelum mengirim pesan kepada Saka.
3. Outline: ringkasan backstory Saka diselaraskan dengan Bab 12; tabungan terkuras untuk menalangi sewa studio dan mengerjakan bagian temannya, studio tutup karena utang sewa, lalu temannya lepas tangan.

**Opsional, tidak menahan publikasi (tidak diubah dalam revisi ini):**
1. Ringkas enam judul bab yang melebihi lima kata.
2. Kurangi repetisi sensasi fisik emosional di bab-bab yang padat.
3. Pangkas kesimpulan emosional yang mengulang efek adegan.
4. Pangkas bab di atas 900 kata hanya jika ditemukan repetisi yang tidak diperlukan.

## 8. Status akhir dan batas audit

**READY TO PUBLISH.**

Tiga tindakan wajib telah selesai. Pemeriksaan ulang memastikan teks Bab 4 dan Bab 29 pada file bab individual identik dengan bagian yang bersesuaian di `manuscript.md`, serta detail backstory pada outline telah sesuai dengan Bab 12. Tidak ada alasan editorial untuk merombak struktur, mengganti premis, mengubah pasangan akhir, atau menulis ulang novel dari awal.

Audit ini tidak mengubah file manuskrip. Status ini menilai keterbacaan dan integritas cerita, bukan jaminan penerimaan platform, legalitas hak cipta, atau keberhasilan pasar.


## 9. Catatan revisi dan verifikasi — 11 November 2026

Perbaikan F-01, F-02, dan F-03 diterapkan pada branch `main`. Pemeriksaan pascarevisi dilakukan dengan mengambil ulang file dari GitHub:

- `chapters/bab-04.md` identik dengan bagian Bab 4 dalam `manuscript.md` setelah koreksi durasi.
- `chapters/bab-29.md` identik dengan bagian Bab 29 dalam `manuscript.md` setelah penambahan jalur informasi Nadia kepada Tari.
- `outline.md` tidak lagi memuat klaim bahwa naskah buku Saka dibawa kabur; ringkasannya kini mengikuti peristiwa yang benar-benar diceritakan dalam Bab 12.
- Tidak ada bab lain atau bagian manuskrip yang diubah. Temuan F-04 sampai F-07 tetap menjadi polish opsional dan tidak dijadikan syarat publikasi.

**Keputusan pascarevisi: READY TO PUBLISH.** Status ini menilai kesiapan cerita untuk dibaca dan diterbitkan berdasarkan audit editorial, bukan jaminan penerimaan platform atau keberhasilan pasar.

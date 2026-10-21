# Case Study: “Reply All”

Sumber: `../../referensi` — blueprint 40 bab plus manuskrip 10 bab.

## Angka Manuskrip

Dihasilkan dengan `bash engine/bin/metropop analyze referensi`:

| Metrik | Nilai |
|---|---:|
| Bab terdeteksi | 10 |
| Total kata | 6.462 |
| Rata-rata | 646 kata |
| Median | 644 kata |
| Rentang | 558–749 kata |
| Bab dalam 600–900 kata | 8 dari 10 |
| Porsi paragraf dialog | 45,2% |

Dua bab di bawah 600 kata: Bab 2 (598) dan Bab 8 (558). Keduanya masih berfungsi karena
adegannya tunggal dan hook-nya kuat, tetapi untuk konsistensi engine, keduanya akan
ditandai sebagai peringatan.

## Struktur Blueprint

| Babak | Bab | Isi |
|---|---|---|
| Babak 1 | 1–10 | Kecelakaan, reaksi, pujian, forum pertama. |
| Babak 2 | 11–30 | Eskalasi, romansa, bukti, keputusan melawan. |
| Babak 3 | 31–40 | Rencana, konfrontasi, pengakuan, mundur. |

Titik putar blueprint: **Bab 10** (komitmen), **Bab 20** (tekanan publik), **Bab 30**
(bukti). Catatan penting: bukti besar baru muncul di Bab 29–30, yaitu sekitar **75%**,
bukan 50%. Ini “midpoint terlambat” yang bekerja karena Babak 2A panjang dan penuh
eskalasi. Engine versi ini menempatkan midpoint di 50%; saat mengadaptasi pola ini,
pindahkan penemuan bukti lebih awal atau tambah konsekuensi setelahnya.

## Kenapa Berhasil

1. **Kesalahan yang bisa dikenali.** Salah kirim email adalah rasa malu universal.
2. **Kebohongan yang simpatik.** Nadia tidak berbohong untuk menipu; ia diam karena
   takut. Pembaca tetap bersimpati.
3. **Eskalasi memakai logika institusi.** IT punya kebijakan, CEO harus menyetujui,
   klien punya kontrak. Tidak ada penjahat yang perlu menculik siapa pun.
4. **Setiap tokoh punya fungsi.** Laras membawa data, Arga mengelola citra, Rendra
   membawa konflik kepentingan, Mama membawa taruhan emosional, Pak Bimo membuka pintu
   dan menutupnya.
5. **Hook berupa kalimat konkret.** “Dibaca oleh 52 orang.” “Kamu nggak sendirian lagi,
   Nad.” “Kita bicara nanti soal beban kerjamu.”
6. **Suara yang konsisten.** Kasual, jenaka, dan sadar diri. Istilah kerja dijelaskan
   inline tanpa menghentikan adegan.
7. **Kritik sosial lewat biaya.** Lembur, target, dan urgent call tidak diceramahkan;
   ditunjukkan lewat kopi dingin, cuti yang ditolak, dan telepon Sabtu pagi.

## Pola yang Bisa Dipakai Ulang

- **Pahlawan kecelakaan:** kesalahan disalahartikan sebagai keberanian.
- **Pujian sebagai jebakan:** atasan memuji di depan publik agar protagonis tidak bisa
  mundur.
- **Sekutu dengan data:** seseorang yang pendiam membawa angka yang mengubah arah.
- **Antagonis yang memakai kebaikan:** Arga menyerang lewat pelukan dan pujian.
- **Keluarga yang bangga:** kebanggaan Mama menaikkan taruhan tanpa perlu antagonis baru.
- **Midpoint berupa bukti:** dokumen mengubah "keluhan" menjadi "kebenaran".
- **Pengakuan publik:** protagonis mengaku, lalu tetap menyuarakan isi yang benar.
- **Akhir berupa pilihan:** Nadia menekan Send dengan sengaja.

## Yang Tidak Boleh Ditiru

- Nama, perusahaan, nama klien, dan isi email.
- Urutan beat kata per kata.
- Detail spesifik seperti “412 karyawan” atau “lima detik undo” tanpa menyesuaikan
  dengan dunia cerita baru.
- Struktur 10/20/10 dengan midpoint di 75% tanpa menyesuaikan tekanan Babak 2A.
- Romansa yang terlalu cepat menjadi penyelamat plot.

## Pemetaan ke Engine

“Reply All” adalah prototipe mesin **`salah-kirim`**:

- Bab 1 = pemicu (in medias res), lalu `setup_events` berisi reaksi, aturan main, tekanan,
  sekutu, dan komitmen.
- `midpoint` — protagonis menemukan bahwa masalah yang ia tulis memang dipertahankan.
- `crisis` — antagonis membongkar bahwa pesan itu salah kirim.
- `climax` — pengakuan publik, lalu isi pesan tetap dibacakan.
- `final_image` — menekan Send dengan sengaja.

Bank data engine memakai pola ini, tetapi mengganti nama, dunia, dokumen, dan detail
agar tidak menjadi salinan.

## Pelajaran untuk Penulisan

1. **Jangan membocorkan pemicu di Bab 1.** Hook Bab 1 harus tentang dunia yang retak,
   bukan tentang pesan yang sudah terkirim.
2. **Setiap hook harus sesuai fungsi bab.** Hook “pesan terkirim” tidak boleh muncul
   sebelum bab pemicu.
3. **Nama belakang tidak boleh bentrok.** Pembaca cepat bingung jika dua tokoh utama
   berbagi marga tanpa alasan keluarga.
4. **Target kata bukan angka mati.** 558 kata bisa bekerja, tetapi konsistensi 600–900
   lebih aman untuk ritme web novel.
5. **Dialog tinggi bukan masalah** jika setiap pertukaran mengubah taruhan. Referensi
   mencapai 45% dialog karena hampir semua adegan adalah percakapan dengan tekanan.
6. **Glosarium inline adalah alat, bukan gangguan.** Satu definisi pendek di kemunculan
   pertama cukup.

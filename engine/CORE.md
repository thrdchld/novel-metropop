# CORE: Inti Wajib Baca (satu halaman)

Baca file ini di awal setiap sesi. Detail ada di engine/. File ini memuat apa yang HARUS dibuktikan secara tertulis, bukan sekadar merasa sudah lulus.

## Prinsip
1. Cerita harian yang simpel dan relate (engine/01, 02). Ide yang butuh tambalan atau kebetulan berlapis dibuang (engine/02 §2).
2. "Lulus" hanya sah jika ada BUKTI TERTULIS (daftar di bawah) di outline.md atau ledger.md. Klaim "sudah diuji" tanpa bukti = belum lulus.
3. Penilai akhir bukan kamu. Gerbang G1, G2, G3 dinilai repo novel-editor di sesi terpisah. Kamu tidak boleh menyatakan outline "terkunci" atau cerita "tamat" sebelum laporan gerbang terakhir tidak memuat temuan HIGH/BLOCKER.

## Bukti per tahap
G1, setelah Tahap 2. Letakkan sebagai bagian "Bukti G1" di atas outline.md:
- Titik balik (minimal 6 untuk 30 bab, 8 untuk 40 bab), satu baris tiap titik: "Karena [A], [tokoh] memilih [Y]. Jalan pintas: [Z]. Kenapa Z tertutup: [salah satu dari 7 cara sah di engine/08 §4A.3, konkret]". Alasan "karena sifat tokoh" saja = belum lulus.
- Proses dunia nyata yang dipakai (kerja, cetak/penerbitan, bank, hukum, transportasi, birokrasi, medis): proses | durasi atau urutan nyata | URL sumber (cari di web). Jika tidak bisa diverifikasi, tulis UNVERIFIED lalu ganti prosesnya.
- Tiga Uji Mati/Lanjut (engine/02 §2), satu kalimat jawaban tiap uji.

G2, setelah Tahap 3. Letakkan sebagai bagian "Bukti G2" di outline.md:
- Kalender: hari dan minggu tiap bab, serta jarak waktu antarperistiwa.
- Peta pengetahuan: informasi/rahasia | siapa tahu sejak bab berapa | siapa tidak boleh tahu sampai bab berapa | saluran (lihat/dengar/baca).
- Jejak mundur dari klimaks: tiap syarat klimaks | ditanam di bab mana (minimal 2 kali) (engine/08 §4A.1).
- Rujukan mundur: fakta masa lalu yang dipakai sebagai pemicu | bab penanaman (harus lebih kecil dari bab pemakaian).
- Simulasi tiga peran (engine/08 §4), jawaban ringkas.

Tahap 4, tiap bab, di ledger.md:
- Hari, jam, lokasi bab ini beserta sumber waktunya dari bab sebelumnya.
- Rujukan mundur yang dipakai: fakta | ditanam di bab N | kutipan penanda (3-6 kata persis dari bab N).
- Informasi baru yang diketahui tokoh: siapa tahu apa | dari mana (lihat/dengar/baca).
- Uji mikro yang tersentuh bab ini (engine/08 §2B): satu baris bukti tiap uji yang relevan.
- Kebetulan hanya boleh memperburuk keadaan, tidak boleh menyelesaikan masalah.

## 12 cacat yang paling sering lolos (tanyakan ke tiap bab)
1. Kenapa tokoh tidak melakukan hal paling mudah (bertanya, menelepon, jujur)? Alasannya tampak di halaman?
2. Adakah rujukan ke kejadian, ucapan, atau tempat lama yang tidak pernah ditulis? Cari di bab sebelumnya.
3. Dari mana tokoh tahu ini? Harus lewat lihat, dengar, atau baca, bukan dari batin narator.
4. Adakah petunjuk yang sudah dilihat tokoh dan bertentangan dengan kesimpulannya? Apakah ditanggapi?
5. Hari, jam, jarak, durasi konsisten? "Kemarin" dan "minggu lalu" cocok dengan kalender?
6. Prosedur dunia nyata (cetak buku, kereta, bank, kantor, hukum) sesuai durasi nyata dan sudah dicek sumbernya?
7. Konsistensi benda dan tempat: tas, tangan, pakaian, uang, lokasi tinggal.
8. Satu informasi diucapkan lagi oleh tokoh lain seolah belum pernah disebut.
9. Tokoh licin atau bodoh mendadak demi plot (karakter tidak konsisten).
10. Kebetulan menyelesaikan masalah.
11. Bab menceritakan perasaan ("dadaku nyeri") tanpa peristiwa yang membuktikannya.
12. Perasaan atau hubungan berubah tanpa kejadian pemicu di halaman.

## Gerbang eksternal dan aturan keluar-loop
- G1 (setelah Tahap 2), G2 (setelah Tahap 3, sebelum bab 1), G3 (tiap 10 bab dan saat tamat) dijalankan repo novel-editor di sesi terpisah. Laporan dibaca dari branch audit/<judul>/<gerbang> pada https://github.com/thrdchld/novel-editor (berkas validation/<gerbang>.md). Simpan hanya laporan terakhir tiap gerbang.
- Maksimal 2 putaran perbaikan per gerbang. Jika masih ada temuan HIGH setelah putaran kedua, jangan menambal bab satu per satu: kembali ke Tahap 2 lalu rombak rantai sebab-akibat atau buang premis.
- Perubahan sebab-akibat diubah di outline dulu, baru di bab.
- Keluhan gaya baru dicatat di engine/learnings/editor-feedback.md. Baru menjadi aturan jika muncul pada >= 2 cerita berbeda. Tidak menambah pemeriksaan stress-test selama 30 hari.

## Peta baca (menggantikan tabel Smart-Reading lama)
- Awal sesi: AGENTS.md, CORE.md.
- Mode A (ide/premis): engine/01, 02, 11, story/universe-registry.md.
- Mode B (canon dan outline): engine/03, 04, 11, 08 (§2, §4, §4A), templates/.
- Mode C (menulis bab): state.md, canon.md, outline.md (bab aktif), ledger.md, 1 bab terakhir, engine/05, 06, 07, 08 (§2B).
- Mode D (revisi): engine/05, 08, 09 dan bab terkait.

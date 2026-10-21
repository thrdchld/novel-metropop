# Panduan Utama (Ringkasan Operasional)

Dokumen sumber: **`../../Panduan Menulis Web Novel Metropop Indonesia.txt`**.
File itu adalah acuan tertinggi. Ringkasan ini hanya menerjemahkan aturannya menjadi
checklist dan perintah engine. Jika ada konflik, panduan sumber menang.

## 1. Peran

- Pemilik proyek = editor dan pengawas. Ia menilai hasil, memberi kritik, dan menyetujui outline.
- AI/penulis = menyusun premis, alur, karakter, dan draf.
- Instruksi baru dari pemilik proyek mengalahkan dokumen lama.

## 2. Definisi MetroPop

Cerita orang kota usia 18–50 dengan masalah nyata: kerja, uang, keluarga, pertemanan,
dan percintaan. Relatable, hangat, lucu, tetapi punya inti yang menyentuh. Romansa adalah
lapisan, bukan satu-satunya mesin cerita. Tema biasanya satu pertanyaan sederhana.

## 3. Format Wajib

| Aturan | Nilai |
|---|---|
| Jumlah bab | 30–40 |
| Panjang bab | 600–900 kata, target ±750 |
| Total | ±30.000 kata |
| Struktur | 25% awal / 50% tengah / 25% akhir |
| Contoh 40 bab | 10 / 20 / 10 |
| Titik putar | Bab 10, 20, 30 (boleh ±900 kata) |
| Judul bab | `## Bab N: Judul`, 2–5 kata |
| Chat | `**Nama:** *isi pesan*` |
| Email/surat | ditulis miring |
| Emoji | dilarang |
| Rilis | 3–5 bab per minggu |

Tiga bab pertama harus membuat pembaca tahu: siapa tokohnya, apa masalahnya, kenapa ia
tidak bisa keluar, dan apa taruhannya. **Bab 1 wajib in medias res.** Bab 2 menegaskan
konsekuensi dan aturan main. Bab 3 memperjelas taruhan dan pertanyaan dramatik.

## 4. Premis

Rumus: tokoh dengan satu kelemahan khas + kesalahan/kenakalan kecil + pemicu logis +
eskalasi yang tidak bisa dihentikan + dilema dengan harga nyata.

Tujuh syarat premis:

1. Bisa dijelaskan dalam satu kalimat.
2. Pemicu masuk akal, tanpa kebetulan ajaib.
3. Kesalahan awal kecil dan manusiawi.
4. Menutupnya lebih mudah daripada mengakuinya.
5. Taruhan dua lapis: profesional dan personal.
6. Penuh ruang awkward dan ironi.
7. Ending punya harga nyata.

Saat mengusulkan, beri **3 opsi**: judul, logline, tema, tokoh inti, sumber humor.

Perintah engine:

```bash
bash engine/bin/metropop ideas
bash engine/bin/metropop ideas --seed 42
```

## 5. Karakter

Setiap tokoh inti dan tokoh berulang punya:

- identitas: nama, panggilan, usia, pekerjaan, tempat tinggal, latar singkat;
- penampilan khas maksimal 3;
- tells fisik/kebiasaan 3–5;
- pola bicara: kalimat andalan, panjang kalimat, kata favorit, cara menyapa, cara gugup/marah/berbohong;
- benda khas;
- tell emosi;
- kelemahan fatal, ketakutan, keinginan vs kebutuhan, kebohongan yang diyakini;
- batas karakter (yang tidak akan pernah ia lakukan);
- rahasia, motif, dan arc;
- contoh dialog 3 baris.

Aturan pakai: 1–2 tells per adegan, ulangi tell utama setiap 3–5 bab, ubah tell untuk
menunjukkan perkembangan. Show, don't tell dipakai untuk momen penting, bukan setiap kalimat.

Engine menaruh character sheet di `bible.md` dan ringkasannya di `brief` per bab.

## 6. Alur

Beat wajib:

1. Pemicu (bab 1–2).
2. Reaksi tak terduga: dunia menafsirkan kesalahan secara berbeda.
3. Kebohongan pasif: tokoh membiarkan salah paham tumbuh.
4. Eskalasi bertahap.
5. Kesalahan fatal pertama karena panik, bukan kebodohan yang dipaksakan.
6. Midpoint: fakta baru mengubah tujuan.
7. Tekanan memuncak.
8. Dilema puncak: tiga pilihan buruk.
9. Klimaks: pengakuan/tindakan khas tokoh.
10. Konsekuensi nyata, tidak semua beres.
11. Penutup: versi sadar dari hal yang dulu terjadi tanpa sengaja.

Aturan eskalasi: tidak ada bab yang hanya mengulang. Setiap bab harus menaikkan taruhan,
memberi informasi baru, atau mendalamkan hubungan. Minimal satu adegan awkward/konyol
setiap 2–3 bab dan satu momen emosional tulus setiap ±5 bab.

Engine menyimpan jadwal humor dan momen emosional di setiap bab (`humor_beat`,
`emotional_beat`).

## 7. Teknik Naratif

**Wajib:** in medias res di Bab 1, hook di akhir setiap bab, Chekhov's gun.

**Sering:** show don't tell, action beats, dramatic irony, pacing naik-turun.

**Sesekali:** foreshadowing, motif, flashback pendek, stream of consciousness, red herring,
plot twist yang fair, allusion.

**Jarang:** frame story, flashforward, unreliable narrator.

**Dilarang:** deus ex machina. Kebetulan boleh memperburuk, tidak boleh menyelamatkan.

Engine mencatat `technique` per bab di outline.

## 8. Anti Plot Hole dan Outline Lock

Sebelum menulis, jawab 10 pertanyaan skeptis:

1. Kenapa tokoh tidak memperbaiki kesalahan sejak awal?
2. Kenapa ia tidak jujur? Apakah alasannya konsisten dengan kelemahannya?
3. Kenapa ia tidak ketahuan?
4. Kenapa antagonis tidak langsung menyerang?
5. Apakah mekanisme teknisnya mungkin?
6. Siapa tahu apa pada hari itu?
7. Apakah bukti klimaks sudah ditanam?
8. Apakah motif tiap tokoh jelas?
9. Apakah ada tokoh baru yang muncul tiba-tiba?
10. Apakah ada kebetulan yang menyelamatkan?

Outline adalah pakem. Semua kolom per bab harus terisi:

- nomor, judul, hari/jam/lokasi;
- tujuan adegan dan komplikasi;
- 3–5 beat;
- perubahan di akhir bab;
- siapa tahu apa;
- setup yang ditanam dan payoff yang dibayar;
- teknik naratif;
- hook;
- alasan logis dan pertanyaan pembaca yang dijawab;
- apa yang **TIDAK** terjadi.

Saat menulis, yang boleh dikreasikan: kalimat, dialog, detail sensorik, tells, lelucon,
urutan kecil. Yang tidak boleh diubah tanpa izin: urutan kejadian, fakta plot, perubahan
pengetahuan, tokoh baru, aturan dunia, hasil adegan, dan hook.

Jika menemukan lubang/ide baru: isi `change-request.md`, jangan menulis ulang outline
diam-diam.

Perintah engine:

```bash
bash engine/bin/metropop stress --story "story/Judul"   # 10 pertanyaan + simulasi 3 peran
bash engine/bin/metropop lock --story "story/Judul"     # validasi + kunci v1.0
```

`lock` gagal jika stress test masih berisi `BELUM`, `isi`, atau kotak kosong. Gunakan
`--force` hanya jika pemilik proyek sudah menyetujui.

## 9. Story Ledger

`ledger.md` adalah sumber kebenaran kontinuitas. Bagian:

- **A. Timeline master:** bab, hari/jam, lokasi, tokoh hadir, kejadian kunci.
- **B. Daftar lokasi:** ciri tetap, siapa sering di situ, jarak.
- **C. Matriks pengetahuan:** fakta, siapa tahu, sejak bab, dari mana.
- **D. Status tokoh per bab:** emosi, benda, hubungan, rahasia, urusan menggantung.
- **E. Fakta keras dan angka:** jumlah orang, nominal, versi file, nama, jabatan, usia, aturan sistem.
- **F. Benang terbuka:** setup, bab tanam, rencana payoff, status.
- **G. Log perubahan canon.**

Protokol:

- Sebelum menulis: 5 baris pra-cek (posisi cerita, kondisi tokoh, hook sebelumnya,
  fakta Ledger, setup/payoff).
- Setelah menulis: 5–8 baris catatan kontinuitas, lalu perbarui Ledger.
- Jangan mengarang fakta dari ingatan. Jika tidak ada di Ledger/teks, tandai `[PERIKSA]`.
- Jangan membuat tokoh tahu sesuatu karena penulis membutuhkannya.
- Jangan menutup lubang dengan kebetulan.

Perintah engine: `bash engine/bin/metropop ledger --story "story/Judul"`.

## 10. Bahasa dan Gaya

- Bahasa sehari-hari orang Indonesia, nada ngobrol: nggak, udah, kayak, ngetik, nyender,
  banget, aja, bikin, tuh.
- Kalimat pendek, paragraf pendek. Hindari kalimat bertingkat dan susunan rancu.
- Serapan Inggris kantor dipakai wajar: meeting, deadline, urgent call, follow up, feedback,
  spreadsheet, Slack.
- Istilah asing dijelaskan sekali secara inline.
- Hindari analogi aneh/terjemahan literal.
- Humor lahir dari situasi, bukan kalimat yang dipaksa lucu.
- Dialog natural: menyela, mengelak, setengah menjawab.
- Tunjukkan lewat tindakan, bukan penjelasan panjang perasaan.
- Tanpa emoji dan umpatan kasar.
- Detail dunia nyata secukupnya: Kuningan, KRL, ojol, kos Tebet, kopi susu.

## 11. POV dan Tense

Default orang ketiga terbatas, dekat dengan satu tokoh per adegan, kala lampau, konsisten.
Pindah POV hanya jika ada di outline dan diberi pemisah jelas. Pikiran langsung ditulis
miring dan singkat. Utamakan action beats daripada label dialog berulang.

## 12. Struktur Satu Bab

1. Buka langsung di adegan.
2. Satu tujuan dan satu komplikasi.
3. Satu detail lucu/awkward konkret.
4. Setidaknya satu hal berubah.
5. Hook penutup yang konkret.
6. 600–900 kata; jangan mengulang informasi.

## 13. Rubrik dan Pengiriman

Nilai 1–5 untuk 8 kriteria: bahasa/suara, kejelasan, logika/kontinuitas, kepatuhan
outline, hook/ritme, humor/awkwardness, tokoh/emosi, teknik naratif.

Lulus jika **tidak ada nilai di bawah 4** dan **total minimal 34/40**.

Format pengiriman: teks bab, catatan kontinuitas, skor 8 angka, penyimpangan outline,
satu pertanyaan untuk editor jika perlu. Tanpa ringkasan panjang atau pujian diri.

Rubrik per bab tersedia di `rubric.md` dan bisa dicetak dengan
`bash engine/bin/metropop rubric --story "story/Judul"`.

## 14. Batasan Konten

- Nama tokoh, perusahaan, dan produk fiktif; hindari merek nyata dan tokoh publik.
- Hindari stereotip yang merendahkan dan topik SARA yang memicu polemik.
- Tanpa konten eksplisit dan umpatan kasar.
- Tema berat ditangani dengan empati dan humor yang tidak menertawakan penderitaan.

## 15. Perintah Engine yang Selaras

| Kebutuhan | Perintah |
|---|---|
| Usul 3 premis | `metropop ideas` |
| Buat cerita | `metropop new "Judul" --chapters 40` |
| Isi stress test | `metropop stress --story "..."` |
| Kunci outline | `metropop lock --story "..."` |
| Paket bab | `metropop brief 1 --story "..."` |
| Ledger | `metropop ledger --story "..."` |
| Rubrik | `metropop rubric --story "..."` |
| Validasi | `metropop check --story "..." --strict` |
| Regenerate snapshot | `metropop render --story "..."` |

Semua perintah dijalankan lewat `bash engine/bin/metropop ...` di Android/shared storage,
atau `python3 -m metropop ...` dari folder `engine/`.

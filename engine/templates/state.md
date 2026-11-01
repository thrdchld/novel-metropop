# Continuity State — <Judul Cerita>

> **File Penjaga Kondisi Aktif Cerita (Engine v2.4)**
> Dokumen ini adalah **peta keadaan langsung (live state snapshot)** cerita. Berbeda dengan `ledger.md` yang mencatat arsip sejarah panjang, file ini mencatat **kondisi saat ini** di garis depan penulisan (*writing frontier*).
> AI **WAJIB** membaca file ini dan menampilkan **Pre-Flight Continuity Gate** sebelum menulis bab baru, serta memperbarui file ini setelah bab selesai ditulis.

---

## I. Status Garis Depan Penulisan (Writing Frontier)

- **Bab Terakhir Selesai:** Bab [N]
- **Bab Berikutnya yang Akan Ditulis:** Bab [N+1]
- **Titik Waktu Cerita:** Hari [X] ([Nama Hari]), Pukul [JJ.MM] WIB
- **Lokasi Terkini Tokoh Utama:** [Ruangan / Tempat spesifik]
- **Cuaca / Suasana Fisik:** [Hujan / Terik / Malam tenang]
- **POV Aktif:** [Nama Tokoh, biasanya POV 1 "aku"]
- **Kondisi Emosi Tokoh Utama:** [Cemas / Lega / Waspada / Marah]

---

## II. Jangkar Waktu Relatif (Relative Time Anchor)

Gunakan tabel ini untuk memastikan tidak ada salah sebut "kemarin", "tadi", atau "lusa":

| Label Waktu | Hari & Jam Kalender Cerita | Kejadian yang Terjadi |
|---|---|---|
| **Hari Ini** | Hari [X] ([Nama Hari], JJ.MM) | Kejadian bab ini |
| **Kemarin (H-1)** | Hari [X-1] ([Nama Hari]) | [Kejadian kemarin] |
| **Dua Hari Lalu (H-2)** | Hari [X-2] ([Nama Hari]) | [Kejadian 2 hari lalu] |
| **Acara / Kejadian Lampau** | Hari [Y] ([Nama Hari lalu]) | [WAJIB disebut dengan hari aslinya, misal "Jumat lalu", DILARANG sebut "kemarin"] |
| **Tenggat / Acara Mendatang** | Hari [Z] ([Nama Hari mendatang]) | [Sisa waktu: X hari / jam] |

> [!CAUTION]
> **Aturan Waktu Relatif:** Kata *"kemarin"* dan *"semalam"* HANYA boleh merujuk hari H-1 yang sebenarnya. Dilarang keras menyebut kejadian dua hari lalu atau seminggu lalu dengan kata *"kemarin"*.

---

## III. Register Status Hubungan & Diksi Terlarang (Relationship Status Registry)

| Pasangan / Relasi | Label SAH Digunakan Saat Ini | Diksi / Label DILARANG Saat Ini | Catatan / Syarat Naik Status |
|---|---|---|---|
| **Protagonis & Love Interest** | misal: "Pacar Pura-pura / Pacar Sewaan / Pacar Saya" | misal: "Calon Istri / Calon Suami / Tunangan / Istri" | Belum sah disebut calon istri sebelum ada lamaran resmi di Bab X |
| **Protagonis & Antagonis** | misal: "Mantan Pacar / Rival" | misal: "Teman / Tunangan" | Putus sejak 1 tahun lalu |
| **Protagonis & Sahabat/Sekutu** | misal: "Kakak Pangkalan / Sahabat" | misal: "Pacar / Orang Asing" | - |

**Matriks Sapaan Antar-Tokoh Saat Ini:**
- Tokoh A ke Tokoh B: `[Sapaan, misal: Mas Rian / Mas / Kamu]`
- Tokoh B ke Tokoh A: `[Sapaan, misal: Mbak Ayu / Ayu / Kamu]`
- Tokoh A ke Tokoh C: `[Sapaan, misal: Bang Bobi / Lo-Gue]`

---

## IV. Inventaris Benda Fisik & Lokasi Krusial (Physical Inventory Tracker)

Lacak keberadaan fisik benda-benda penting agar tidak berpindah tempat secara ajaib:

| Benda Krusial | Pemegang Fisik Saat Ini | Lokasi Terkini | Status / Catatan |
|---|---|---|---|
| **[Nama Benda 1, misal Gelang Pusaka]** | [Nama Tokoh] | [Di pergelangan tangan / di kotak lemari] | [Diterima di Bab X, belum dikembalikan] |
| **[Nama Benda 2, misal Kendaraan / Pelat]** | [Nama Tokoh] | [Di parkiran basement / pangkalan] | [Pelat nomor: X] |
| **[Nama Benda 3, misal Uang / Dokumen]** | [Nama Tokoh] | [Di rekening / di map A4 / di amplop] | [Nominal / status verifikasi] |
| **[Nama Benda 4, misal Pakaian / Aksesoris]** | [Nama Tokoh] | [Sedang dipakai / di gantungan] | [Ciri fisik: warna / bahan] |

> [!IMPORTANT]
> Benda fisik tidak boleh berpindah tangan tanpa ada adegan eksplisit serah-terima di teks bab!

---

## V. Kunci Ambang Batas Kejadian Pertama (First-Time Milestone Lock)

Mencegah pengulangan adegan "pertama kali" (seperti dua kali bertemu orang tua, dua kali buka identitas):

| Kejadian Ambang Batas | Status Terkunci? | Terjadi di Bab | Catatan Aturan Penulisan |
|---|---|---|---|
| Bertemu Orang Tua / Keluarga Pasangan Pertama Kali | `[BELUM / TERKUNCI]` | Bab [X] | Jika sudah TERKUNCI, bab berikutnya adalah kunjungan lanjutan, bukan perkenalan awal. |
| Pengungkapan Rahasia Identitas / Buka Topeng Pertama Kali | `[BELUM / TERKUNCI]` | Bab [Y] | Jika sudah TERKUNCI, rahasia sudah diketahui tokoh terkait. |
| Perkenalan Tokoh [Nama] ke Pembaca | `[BELUM / TERKUNCI]` | Bab [Z] | Setelah Bab Z, dilarang memakai frasa "bernama X" atau "Itu X". Gunakan "X lagi" atau sebut langsung. |
| Pengakuan Cinta / Hubungan Nyata Pertama Kali | `[BELUM / TERKUNCI]` | Bab [W] | Sebelum Bab W, status tetap sandiwara/formal. |
| Mengetahui Nama Tokoh [Nama] Pertama Kali | `[BELUM / TERKUNCI]` | Bab [V] | Sebelum Bab V, narator POV 1 dilarang menyebut nama ini. |

---

## VI. Log Pemerolehan Fakta & Register Data Mikro Tokoh (Fact Acquisition & Channel Tracker)

> [!CAUTION]
> **HUKUM PEMEROLEHAN FAKTA (ANTI-TELEPATI DATA MIKRO):**
> Seorang tokoh **DILARANG KERAS** mengetahui, mengucapkan di dialog, atau bertindak berdasarkan data mikro (seperti: nomor pelat kendaraan, nama lengkap orang asing, gelar/IPK, nomor telepon/rekening, kode tagihan, alamat rumah) jika ia **BELUM PERNAH** memperoleh data tersebut melalui salah satu dari 3 saluran fisik:
> 1. **Visual Fisik Langsung:** Melihat langsung dengan mata kepala sendiri (membaca pelat nomor di bodi motor, melihat id card di dada, membaca kertas di meja).
> 2. **Auditori Nyata:** Mendengar ucapan orang lain secara eksplisit di dialog adegan.
> 3. **Dokumen Fisik / Layar:** Membaca pesan teks, dokumen berkas fisik, atau layar ponsel/komputer.

| Bab | Tokoh | Data Mikro Baru yang Diperoleh | Saluran Pemerolehan (Visual / Auditori / Dokumen) | Bukti Tindakan di Teks |
|---|---|---|---|---|
| Bab 1 | Tokoh A | Mengetahui nama Tokoh B | Visual: Membaca ID Card lanyard di dada | "Mataku membaca ID card di kemejanya: ..." |
| Bab 2 | Satpam | Mengetahui pelat nomor motor | Visual: Menunduk membaca pelat di bodi motor | "Pak Darto menunduk membaca pelat nomor..." |
| ... | ... | ... | ... | ... |

**Daftar Data yang BELUM Boleh Diketahui Tokoh Saat Ini (Strictly Unknown Data):**
- **Tokoh A:** Belum tahu [Data X], Belum tahu [Data Y].
- **Tokoh B:** Belum tahu [Data Z], Belum tahu nomor pelat motor Tokoh A (hanya satpam dan pos parkir yang mencatatnya).

---

## VII. Matriks Asimetri Rahasia & Pengetahuan (Knowledge Asymmetry Registry)

Pastikan tidak terjadi **telepati narator** atau kebocoran informasi (*knowledge leak*):

| Rahasia / Informasi Kunci | Siapa yang SUDAH Tahu | Siapa yang DILARANG Tahu (Belum Tahu) | Catatan / Saluran Bocor |
|---|---|---|---|
| [Rahasia 1: Hubungan cuma pura-pura] | [Tokoh A, Tokoh B, Tokoh C] | [Tokoh D, Tokoh E, Publik] | Hanya boleh bocor lewat adegan [X] |
| [Rahasia 2: Identitas asli / latar belakang] | [Tokoh A, Tokoh B] | [Keluarga besar Tokoh B] | Tersimpan di map fotokopi ijazah |
| [Rahasia 3: Pelaku kejahatan / sabotase] | [Tokoh A, IT / Legal] | [Antagonis belum tahu kalau aksinya ketahuan] | Menunggu bukti digital faktur |

---

## VIII. Benang Terbuka & Janji Tertunda (Active Suspended Threads)

Urusan mendesak yang sedang menggantung di akhir bab terakhir dan wajib dijawab segera:

1. **Urusan Menggantung 1:** [Misal: Pesan WA ancaman yang baru masuk di kalimat hook bab lalu]
2. **Urusan Menggantung 2:** [Misal: Janji mengembalikan barang besok siang]
3. **Penyelidikan / Tindakan Aktif:** [Misal: Menunggu balasan audit IT / polisi]

# 07 — Kontinuitas: Canon, State, dan Story Ledger

> **File Pemilik:** File ini memiliki aturan **Tiga Pilar Kebenaran Cerita, File Penjaga Kondisi Aktif (`state.md`), Sistem Pengecekan Berlapis Kontinuitas (4-Layer Guard), Gerbang Pra-Tulis (Pre-Flight Gate), dan Audit Silang Antarbab**.

---

## 1. Tiga Pilar Kebenaran Cerita

Untuk menjamin AI dan penulis tidak mengalami amnesia naratif lintas bab, setiap proyek novel di `story/<Judul>/` memiliki **tiga dokumen kebenaran** dengan fungsi spesifik:

| Dokumen | Sifat | Peran Utama | Kapan Dibaca / Diperbarui |
|---|---|---|---|
| **`canon.md`** | Rencana Induk (*Bible*) | Menyimpan premis, 5 slot kelayakan, kerangka plot, arketipe tokoh, aturan dunia, motif, dan rencana *planting* 2x. | Dibaca saat perencanaan; diubah hanya lewat *Change Request*. |
| **`state.md`** | Penjaga Kondisi Aktif (*Live State Machine*) | Menyimpan **potret instan garis depan cerita** (*writing frontier*): jam/hari persis, jangkar waktu relatif, label hubungan sah/dilarang, inventaris benda fisik, matriks rahasia aktif, dan kunci kejadian pertama. | **Wajib dibaca sebelum bab ditulis; wajib disinkronkan tepat setelah bab selesai.** |
| **`ledger.md`** | Arsip Kronologis (*Living Ledger*) | Mencatat rekam jejak historis lengkap bab per bab (Timeline Master A, Lokasi B, Matriks C, Status D, Angka Keras E, Benang Terbuka F, Log G). | Diperbarui setelah bab selesai sebagai arsip kumulatif. |

### Aturan Prioritas Fakta
1. Fakta yang sah telah terjadi HANYA fakta yang tertulis di **teks bab** dan tercatat di **`state.md` / `ledger.md`**.
2. Rencana di `canon.md` atau `outline.md` gugur jika teks bab yang sudah disetujui mengeksekusi jalan berbeda.
3. Jangan pernah mengarang fakta dari ingatan atau asumsi. Jika ragu, tandai `[PERIKSA]` dan periksa file negara (`state.md`).

---

## 2. Struktur File Penjaga Kondisi Aktif (`state.md`)

Setiap folder `story/<Judul>/` wajib memiliki `state.md` yang memuat 8 komponen instan:

1. **I. Status Garis Depan Penulisan (*Writing Frontier*):** Bab terakhir selesai, bab aktif berikutnya, hari & jam cerita persis, lokasi tokoh utama, cuaca, POV, dan emosi aktif.
2. **II. Jangkar Waktu Relatif (*Relative Time Anchor*):** Kalender referensi mutlak hari ini vs kemarin (H-1) vs dua hari lalu (H-2) vs kejadian lampau (disebut dengan nama hari, misal "Jumat lalu").
3. **III. Register Status Hubungan & Diksi Terlarang (*Relationship Registry*):** Label resmi yang sah digunakan di bab aktif vs diksi yang **DILARANG KERAS** (misal: "pacar sewaan" vs "calon istri"), serta matriks sapaan yang sah antar-tokoh.
4. **IV. Inventaris Benda Fisik & Lokasi Krusial (*Physical Object Tracker*):** Keberadaan fisik benda penting (gelang pusaka, motor & pelat nomor, uang tunai, berkas/ijazah). Benda tidak boleh berpindah tempat tanpa adegan serah-terima fisik!
5. **V. Kunci Ambang Batas Kejadian Pertama (*First-Time Milestone Lock*):** Kejadian seumur hidup sekali (bertemu calon mertua/ibu pertama kali, buka kedok/masker pertama kali, tahu nama staf baru pertama kali, jadian nyata pertama kali). Jika sudah `[LOCKED]`, dilarang mengulang adegan pertama kali di bab berikutnya.
6. **VI. Log Pemerolehan Fakta & Register Data Mikro Tokoh (*Fact Acquisition & Channel Tracker*):** Rekam jejak fakta/data mikro baru yang didapat tiap tokoh per bab beserta **saluran fisik pemerolehannya** (visual langsung, auditori di dialog, dokumen fisik/layar), serta daftar data mikro yang secara tegas **BELUM BOLEH DIKETAHUI (*Strictly Unknown Data*)**.
7. **VII. Matriks Asimetri Rahasia & Pengetahuan (*Knowledge Asymmetry*):** Siapa yang sudah tahu rahasia vs siapa yang secara tegas **BELUM TAHU**. Mencegah kebocoran telepati (*narrator telepathy*).
8. **VIII. Benang Terbuka & Janji Tertunda (*Active Suspended Threads*):** Janji atau urusan mendesak yang menggantung di hook bab sebelumnya dan harus dijawab.

---

## 3. Sistem Pengecekan Berlapis Kontinuitas (The 4-Layer Continuity Guard)

Untuk mengeliminasi 100% kesalahan kontinuitas (seperti Bab 1 pacar, Bab 2 calon istri, kejadian seminggu lalu disebut kemarin, atau tokoh tiba-tiba tahu nomor pelat tanpa pernah melihatnya), AI wajib melewati 4 lapis pengawasan:

```
[Lapis 1: Gerbang Pra-Tulis (Pre-Flight Gate)]
         ↓ (Wajib lolos verifikasi sebelum ketik prosa)
[Lapis 2: Penjaga Saat Tulis (In-Writing Constraints)]
         ↓ (Pencegahan telepati, diksi label, konsistensi benda & saluran fakta)
[Lapis 3: Validasi Pasca-Tulis (Factual Diff & State Sync)]
         ↓ (Ekstraksi fakta baru, update state.md & ledger.md)
[Lapis 4: Audit Mekanis Skrip (audit-continuity.py)]
           (Pemeriksaan kode otomatis lintas bab)
```

---

### Lapis 1: Gerbang Pra-Tulis Kontinuitas (*Pre-Flight Continuity Gate*)

Sebelum menulis baris pertama prosa bab baru, AI **WAJIB** membaca `state.md` dan menampilkan blok verifikasi 5 poin:

```markdown
### [PRE-FLIGHT CONTINUITY GATE — Bab N]
1. WAKTU & JANGKAR: Hari [X] ([Nama Hari], [Jam]) | "Kemarin" merujuk ke [Hari X-1] | Rujukan lampau yang sah: [Hari Y lalu]
2. STATUS HUBUNGAN SAH: [Label yang boleh dipakai] | DILARANG: [Diksi terlarang/prematur]
3. INVENTARIS FISIK: Benda yang sedang dibawa tokoh utama: [...] | Lokasi objek krusial: [...]
4. ASIMETRI PENGETAHUAN & JALUR FAKTA: Tokoh hadir tahu [...] via [saluran visual/auditori/dokumen], tapi STRICTLY BELUM TAHU [...] (DILARANG menyebut string data mikro tanpa adegan pemerolehan fisik!).
5. KUNCI MILESTONE: Ambang batas kejadian pertama yang berlaku / sudah terkunci: [...]
```

> [!CAUTION]
> **Aturan Gerbang Mutlak:** Jika AI langsung menulis narasi tanpa menampilkan blok *Pre-Flight Continuity Gate*, hasil tulisan dianggap cacat prosedur dan harus dibatalkan.

---

### Lapis 2: Penjaga Saat Tulis (*In-Writing Constraints*)

Saat menyusun teks bab:
1. **Patuhi Diksi Label Hubungan:** Dilarang menaikkan eskalasi hubungan (misal dari pacar sandiwara ke calon istri/tunangan) tanpa adanya adegan lamaran formal yang disetujui di outline.
2. **Kepatuhan Jangkar Waktu:** Kata *"kemarin"* atau *"semalam"* hanya boleh digunakan jika adegan yang dimaksud terjadi tepat satu hari kalender sebelumnya. Gunakan "Jumat lalu", "tiga hari lalu", atau sebut tanggal/hari jika jaraknya lebih lama.
3. **Hukum Pemerolehan Fakta Fisik & Anti-Telepati Data Mikro:** Tokoh **DILARANG KERAS** mengetahui, melafalkan, atau bertindak berdasarkan data mikro (nomor pelat kendaraan, nama lengkap orang asing, gelar/IPK, nomor HP/rekening, kode tagihan, alamat rumah) jika belum ada adegan fisik pemerolehan melalui salah satu dari 3 saluran sah:
   - *Visual Fisik:* Melihat langsung dengan mata kepala sendiri (membaca pelat nomor di bodi motor, membaca id card di dada, membaca map).
   - *Auditori Nyata:* Mendengar orang lain mengucapkannya secara eksplisit di dialog adegan.
   - *Dokumen Fisik / Layar:* Membaca berkas kertas, struk, atau layar ponsel/komputer.
   *(Contoh Pelanggaran Fatal: Rian tidak boleh menyebut nomor pelat motor Ayu jika ia belum pernah menunduk membaca pelatnya atau satpam belum membacanya).*
4. **Anti-Telepati POV 1:** Narator sudut pandang orang pertama dilarang mengetahui nama orang asing sebelum ada perkenalan/sebutan ("Namanya baru kuketahui belakangan: Damar").
5. **Logika Fisik Benda:** Jangan memunculkan benda penting jika tokoh tidak membawanya sejak bab sebelumnya. Benda berpindah hanya lewat adegan serah-terima fisik.
6. **Anti-Pengulangan Perkenalan:** Jika tokoh sudah diperkenalkan kepada pembaca di bab sebelumnya, jangan ulangi perkenalan dengan frasa "bernama X" atau "pria itu adalah X"; gunakan "X lagi" atau sebut namanya langsung.

---

### Lapis 3: Validasi Pasca-Tulis & Sinkronisasi (*Factual State Diff & Sync*)

Setiap selesai menghasilkan teks bab, AI wajib menyertakan **Catatan Kontinuitas 5–8 Baris** bersama bab, lalu memperbarui dokumen:

1. **Ekstraksi Factual Diff:**
   - Waktu dan lokasi akhir bab ini.
   - Fakta baru yang muncul di teks (tandai **BARU** `[Bab N]`).
   - Perpindahan benda fisik (siapa memegang apa sekarang).
   - Rahasia yang terbongkar (siapa yang baru tahu apa).
   - Milestone kejadian pertama yang baru saja terkunci.
2. **Sinkronisasi Instan:**
   - Perbarui `story/<Judul>/state.md` ke kondisi bab berikutnya.
   - Tambahkan baris kronologis ke `story/<Judul>/ledger.md` (Timeline Master A, Status Tokoh D, Matriks C, dll.).

---

### Lapis 4: Audit Mekanis Skrip (*Automated Continuity Audit*)

Setelah satu batch bab atau sebelum naskah dinyatakan selesai, jalankan audit silang mekanis:

```bash
python3 scripts/audit-continuity.py "story/<Judul>"
```

Skrip ini memindai naskah dan menguji 4 parameter krusial:
1. **Pemindaian Label Status Hubungan:** Mendeteksi penggunaan kata `pacar`, `calon istri`, `calon cucu mantu`, `tunangan`, `istri` per bab dan memverifikasi kesesuaian dengan tahap hubungan.
2. **Pemindaian Klaim Waktu Relatif:** Mendeteksi setiap kemunculan `kemarin`, `semalam`, `tadi malam`, `lusa`, `minggu lalu` beserta nomor baris untuk dicocokkan dengan kalender hari di `state.md`.
3. **Pendeteksian Perkenalan Tokoh Ganda:** Mendeteksi apakah frasa perkenalan (seperti `bernama X`, `Itu X`, `Namanya baru kuketahui belakangan`) muncul lebih dari sekali untuk tokoh yang sama.
4. **Validasi Angka Keras & Nominal Uang:** Memeriksa konsistensi angka nominal utang, DP, tarif, atau durasi kontrak agar tidak berubah secara acak.

---

## 4. Penanganan Kontradiksi Berdampingan (*Side-by-Side Contradiction*)

Jika saat menulis atau memperbarui file ditemukan pertentangan antara teks baru dan data lama:
1. **Dilarang Retcon Diam-Diam:** Jangan mengubah `state.md` atau `ledger.md` tanpa persetujuan user jika kontradiksi tersebut membatalkan kejadian masa lalu.
2. **Format Laporan Berdampingan:**
   - **Versi Tercatat Sebelumnya (`[Bab X / State]`):** ...
   - **Versi Draf Baru (`[Bab Y]`):** ...
   - **Usulan Rekonsiliasi:** ...
3. Minta keputusan user sebelum melanjutkan.

---

## 5. Protokol Ganti Sesi & Jendela Konteks (*Context Compaction Recovery*)

Jika percakapan dipadatkan (*compacted*) atau dimulai pada sesi baru:
1. AI **DILARANG** mengandalkan ingatan sisa konteks lama.
2. AI **WAJIB** membaca `story/<Judul>/state.md` terlebih dahulu untuk memulihkan potret kondisi terkini.
3. AI membaca bab terakhir yang ditulis di `chapters/bab-NN.md`.
4. AI menampilkan blok *Pre-Flight Continuity Gate* untuk bab yang akan ditulis.

---

## 6. Protokol Semesta Bersama & 3 Tingkat Cameo (Shared Universe)

Dalam semesta MetroPop, berbagai cerita berbagi latar kota yang sama (Jakarta dan sekitarnya) yang dikelola terpusat di `story/universe-registry.md`. Agar semesta terasa hidup tanpa saling mengorbankan independensi cerita, cameo tokoh lintas novel diatur dalam 3 tingkatan ketat:

1. **Tingkat 1: Rujukan Percakapan / Informasi (*Off-Screen Mention / Rumor*)**
   - Tokoh di novel baru membaca tren media sosial, memesan konsumsi rapat dari usaha tokoh lama (misal: Toko Kue Ibu Sumi Tebet), atau mendengar kabar angin tentang korporat lama. Tokoh lama tidak hadir secara fisik.
2. **Tingkat 2: Rujukan Kilas Balik (*Flashback / Shared History*)**
   - Tokoh baru mengingat masa lalu singkat bersama tokoh lama (misal: pernah satu kampus di FEB, atau pernah magang di Menara Astra sebelum Rian menjabat VP). Hanya muncul sebagai memori atau latar belakang ringan.
3. **Tingkat 3: Kehadiran Fisik Singkat (*Live Physical Cameo*)**
   - Tokoh lama muncul sepintas dalam satu adegan (misal: berpapasan di lobi lift Menara Astra, memesan kopi di kafe sebelah, atau Bang Bobi yang kebetulan mengantar paket).
   - **HUKUM MUTLAK CAMEO FISIK:**
     - Cameo fisik murni berfungsi sebagai pemanis latar (*world flavor*).
     - **DILARANG KERAS menjadi penyelamat / *deus ex machina*** yang memecahkan krisis tokoh baru.
     - Durasi interaksi maksimal 1-2 pertukaran dialog sopan khas orang berpapasan di ruang publik tanpa mencuri fokus protagonis.
4. **Isolasi Konteks Penulisan:** Dokumen semesta `story/universe-registry.md` hanya dibaca pada Mode A (Ide) dan Mode B (Setup Proyek), dan **DILARANG** dibaca pada Mode C (Menulis Bab) agar tidak mencemari jendela konteks penulisan bab aktif.

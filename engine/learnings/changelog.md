# Changelog Engine

Catat setiap perubahan aturan, template, atau sumber. Perubahan kecil, spesifik, dan
disertai alasan.

## v3.2 - 2026-11-02

- **Perubahan:** Membangun **Sistem Universe Registry Terpadu, Roster Karakter Anti-Duplikasi, & Protokol Cameo 3 Tingkat (Engine v3.2)**:
  1. *Penyatuan Bank Premis & Pendaftar Semesta (`story/universe-registry.md` & `engine/templates/universe-registry.md`):* Menghapus file `premise-bank.md` yang terpisah dan menyatukan seluruh bank aset portofolio semesta ke dalam satu dokumen hidup yang memuat 6 komponen terstruktur:
     - Bagian 1: Indeks Proyek & Metrik Semesta (Master Story Index: ID Proyek, ID Premis, Judul, Status, Jumlah Bab, Total Kata, Latar Utama, Tahun Cerita).
     - Bagian 2: Bank Premis & Siklus Hidup Ide (Premis Aktif, Cadangan/Backlog, Ditolak, dan Daftar Hitam Trope).
     - Bagian 3: Roster Karakter Semesta & Aturan Anti-Duplikasi Nama, Watak, dan Profesi Tokoh Lintas Cerita.
     - Bagian 4: Katalog Entitas Dunia Bersama (Gedung, Lokasi Usaha, Agensi, dan Kantor Hukum Fiktif yang sah dipakai ulang).
     - Bagian 5: Protokol Semesta Bersama & 3 Tingkat Cameo (Dialog, Kilas Balik, Fisik).
     - Bagian 6: Matriks Kebaruan Mutlak (Novelty Matrix Check).
  2. *Protokol Cameo 3 Tingkat:*
     - Tingkat 1: Rujukan Percakapan / Informasi (*Off-Screen Mention / Rumor*) tanpa kehadiran fisik tokoh lama.
     - Tingkat 2: Rujukan Kilas Balik (*Flashback / Shared History*) sebagai latar belakang / memori lampau.
     - Tingkat 3: Kehadiran Fisik Singkat (*Live Physical Cameo*) berdurasi 1-2 dialog sopan santun, murni sebagai *world flavor*, dan **DILARANG KERAS menjadi penyelamat / deus ex machina**.
  3. *Aturan Isolasi Konteks (Smart-Reading):* Universe Registry wajib dibaca pada Mode A (Ide) dan Mode B (Proyek Baru), namun DILARANG dibaca pada Mode C (Menulis Bab) guna mencegah polusi jendela konteks penulisan bab.
  4. *Penyelarasan Seluruh Komponen Repositori:* Memperbarui `scripts/audit-continuity.py`, `story/README.md`, `engine/00-workflow.md`, `engine/02-premise.md`, `engine/07-continuity.md`, `engine/11-worldbuilding.md`, `engine/templates/premise-options.md`, `engine/README.md`, `README.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `CLAUDE_SKILL.md`, `CHATGPT_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`.
- **File:** `story/universe-registry.md`, `engine/templates/universe-registry.md`, `scripts/audit-continuity.py`, `story/README.md`, `engine/00-workflow.md`, `engine/02-premise.md`, `engine/07-continuity.md`, `engine/11-worldbuilding.md`, `engine/templates/premise-options.md`, `engine/README.md`, `README.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `CLAUDE_SKILL.md`, `CHATGPT_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v3.1 — 2026-11-02

- **Perubahan:** Menetapkan **Prinsip Eksperimentasi Naratif Berbasis Pola Terbukti (*Informed & Hybrid Plot Experimentation*)** dan mengintegrasikan katalog referensi diperluas dari pembaruan `Kerangka Plot yang Terbukti untuk Web Novel.md`:
  1. *Pembebasan Dogma Anti-Eksperimen:* Menghapus larangan kaku "jangan membuat kerangka eksperimental", menggantinya dengan prinsip kebebasan berkreasi. Penulis dan AI didukung penuh mengeksplorasi struktur hibrida (memadukan 2 kerangka, misal *Romance + Fichtean Curve*) dan variasi bentuk naratif khusus yang terinspirasi dari pola karya teruji.
  2. *Panduan Bentuk Naratif Khusus (`engine/03-structure.md` Bagian 6B):*
     - Format Buku Harian / Diary (*Bridget Jones's Diary*, *Marmut Merah Jambu*).
     - Dua Garis Waktu Paralel (*The Hundred-Year-Old Man*, *Critical Eleven*, *The Time Traveler's Wife*).
     - Sudut Pandang Bergantian / Dual POV (*Critical Eleven*, *One Day*, *The Hating Game*).
     - Bentuk Epistolari / Pesan / Surat (*Daddy-Long-Legs*, *The Perks of Being a Wallflower*, *Flowers for Algernon*).
     - Dua Proyek Paralel (*The Rosie Project*).
     - Struktur Hibrida Campuran.
  3. *Koreksi & Presisi Faktual Studi Kasus:* Mengoreksi fakta cerita *The Rosie Project* (Phil adalah ayah kandung Rosie; Gene sempat dicurigai; Don kaku menjadi mesin komedi & perubahan), *The Devil Wears Prada* (Andrea keluar di pekan mode Paris), *A Christmas Carol*, dan *Critical Eleven*.
  4. *Integrasi Katalog Referensi Luas (`engine/sources.md`):* Menambahkan kurasi puluhan novel Indonesia dan dunia ke dalam 7 kelompok pola naratif.
  5. *Penyelarasan Seluruh Skill & Protokol:* Memperbarui `Kerangka Plot yang Terbukti untuk Web Novel.md`, `engine/01-genre.md`, `engine/02-premise.md`, `engine/03-structure.md`, `engine/sources.md`, `AGENTS.md`, `GEMINI_SKILL.md`, `CLAUDE_SKILL.md`, `CHATGPT_SKILL.md`, dan workspace skill Antigravity CLI.
- **File:** `Kerangka Plot yang Terbukti untuk Web Novel.md`, `engine/01-genre.md`, `engine/02-premise.md`, `engine/03-structure.md`, `engine/sources.md`, `AGENTS.md`, `GEMINI_SKILL.md`, `CLAUDE_SKILL.md`, `CHATGPT_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v3.0 — 2026-11-01

- **Perubahan:** Membangun **Sistem Bank Premis (Premise Bank & Registry) & Arsitektur Siklus Hidup Premis Lengkap (Engine v3.0)**:
  1. *Acuan Master Arsitektur Premis Baru:* Mengintegrasikan `panduan-pengembangan-premis-cerita.md` (ontologi premis, demarkasi ide vs premis vs logline vs plot vs tema, 4 elemen pokok premis).
  2. *Dokumen Hidup Bank Premis (`story/premise-bank.md` & template `engine/templates/premise-bank.md`):* Registry inventaris premis seluruh proyek novel dengan indeks status (`DITERIMA / AKTIF`, `CADANGAN / BACKLOG`, `DITOLAK / JANGAN DITAWARKAN LAGI`). Memetakan `PRM-001: Narik Ojol Cinta Pun Nongol` sebagai premis aktif.
  3. *Aturan Mutlak Anti-Penawaran Ulang (Zero Re-pitch Rule):* AI wajib memeriksa `story/premise-bank.md` sebelum memulai sesi brainstorming Mode A. Dilarang keras menawarkan kembali ide/premis yang sudah ditolak atau premis baru yang menggunakan trope yang tercantum dalam *Daftar Hitam Trope*!
  4. *Tiga Pilar Kemampuan Premis (`engine/02-premise.md`):*
     - **Pilar 1: Mencari Premis (Brainstorming & Curiosity Hook):** Observasi aktif keseharian urban Indonesia, mesin spekulasi "What If?" 3 tahap, Core Irony & Mental Picture (*Save the Cat!*), 7 Lensa Perubahan SCAMPER, 3 Katalogik Peristiwa Pemicu, dan 6 Mesin Situasi MetroPop Indonesia.
     - **Pilar 2: Menilai Premis (Evaluasi & Diagnostik Kelayakan):** Uji Kelayakan 5 Slot Wajib, Matriks Diagnostik 5 Parameter Premis (Kausalitas, Conviction, Agency, Stakes, Focus), Elevasi Breakout Level Donald Maass (Gut Appeal, Konvergensi Outer vs Inner Plot, Escalation Stakes 3 Tingkat: Personal, Public, Ultimate), M.I.C.E. Quotient & Kaidah Struktur Bersarang FILO (*First In, Last Out*), serta 5 Pertanyaan Uji Validasi Akhir.
     - **Pilar 3: Mengembangkan Premis (Formulasi & Penajaman):** Kerangka 3P Brandon Sanderson (*Promise, Progress, Payoff*), Aturan Premis Tunggal (*Single Premise Rule* Lajos Egri), 3 Formula Sintaksis Penulisan Premis (Basic Logline, Character-Driven, 3-Kalimat James Scott Bell), dan Desain Benih Solusi (*Planting Solusi 2 Kali*).
  5. *Pembaruan Template & Alur:* Memperbarui `engine/templates/premise-options.md` (memuat ID `PRM-XXX`, 3 formula sintaksis, M.I.C.E., 3 tingkat taruhan), `engine/00-workflow.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, dan `.agents/skills/metropop-novel/SKILL.md`.
- **File:** `panduan-pengembangan-premis-cerita.md`, `story/premise-bank.md`, `story/README.md`, `engine/templates/premise-bank.md`, `engine/templates/premise-options.md`, `engine/02-premise.md`, `engine/00-workflow.md`, `engine/README.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.9 — 2026-11-01

- **Perubahan:** Menambahkan **Dokumentasi Transparan Peran Python & Panduan Eksekusi Multi-Platform (Android/Termux, Linux, Windows)**:
  1. *Penjelasan Arsitektur:* Menguraikan peran Python sebagai Wasit Mekanis / Linter Deterministik pendamping AI (Otak Kanan Kreatif AI vs Otak Kiri Deterministik Python) di root `README.md`.
  2. *Spesifikasi Prasyarat (Requirements):* Menegaskan zero external dependencies (hanya Python 3.8+ Standard Library bawaan tanpa butuh `pip install`).
  3. *Panduan Platform Lengkap:* Menyusun perintah instalasi dan eksekusi langkah demi langkah untuk:
     - Android via Termux (`pkg install git python`, `termux-setup-storage`).
     - Linux via APT/DNF/Pacman (`python3 scripts/...`).
     - Windows via PowerShell / CMD (`winget install Python...`, PATH flag) dan Git Bash / WSL.
  4. *Penggunaan Web AI Murni:* Menegaskan prosedur penggunaan repositori pada platform web tanpa terminal (ChatGPT, Claude, Google AI Studio) via file skill mandiri.
- **File:** `README.md`, `engine/README.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.8 — 2026-11-01

- **Perubahan:** Menetapkan **Protokol Uji Ketahanan Ekstrem Outline & Mitigasi Krisis Logika Tengah Cerita (*Outline Stress-Testing & In-Flight Crisis Mitigation*)** untuk mengeliminasi cacat logika saat penulisan bab tengah (seperti Bab 20) tanpa merombak naskah dari awal:
  1. **Empat Teknik Preventif Ketat di Tahap Outline (`engine/08-quality.md` Bagian 4A):**
     - *Backward Dependency Tracing:* Pelacakan jejak mundur semua syarat kemenangan klimaks Babak 3 hingga ke Babak 1 untuk memastikan tidak ada bukti/tokoh penolong ajaib.
     - *World Building Stress-Test:* Pengujian hukum kepolisian/perbankan RI, jarak/jam sibuk transportasi, dan matematika uang pada setiap babak.
     - *Adversarial 'Why Not Do X?' Test:* Penutupan jalan keluar termudah wajib berupa fakta fisik/hukum nyata, bukan sekadar alasan emosional buatan penulis.
     - *Pre-Outline Knowledge Graph:* Pemetaan alur asimetri rahasia dan fakta sejak draf outline.
  2. **Protokol Triase & Mitigasi Krisis Logika Tengah Cerita (`engine/08-quality.md` Bagian 4B & `engine/12-audit-remediation.md`):**
     - *Triase Diagnostik:* Membedakan *Lethal Premise Collapse* (<5%) vs *Routing Defect* (95% kasus kebuntuan).
     - *Karantina Radius Ledakan (Blast Radius Containment):* Mengunci bab-bab steril sebelum titik simpul asumsi salah (Bab 1 s.d. N-k dilarang diubah).
     - *Empat Teknik Bedah Alur Tanpa Tulis Ulang dari Awal (4 Surgical Rerouting Techniques):* (1) Pengalihan Rute Kausal (memanfaatkan aset cerita yang sudah ada), (2) Memeluk Kemustahilan Jadi Komplikasi (tokoh sadar rencananya buntu dan kepanikan itu menjadi plot motorik bab), (3) Jahitan Bedah Mikro (74/18/8 pada bab terdekat), dan (4) Pertukaran Beban Pembuktian (antagonis membocorkannya sendiri karena sombong/panik).
     - *Forward Cascading Sync:* Sinkronisasi maju ke outline sisa tanpa regresi.
  3. **Pembaruan Dokumen Engine:** Memperbarui `engine/08-quality.md`, `engine/03-structure.md`, `engine/00-workflow.md`, `engine/12-audit-remediation.md`, dan changelog.
- **File:** `engine/08-quality.md`, `engine/03-structure.md`, `engine/00-workflow.md`, `engine/12-audit-remediation.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.7 — 2026-11-01

- **Perubahan:** Menetapkan **Standar Audit 5 Tahap & Alur Remediasi Beruntun (*Cascading Remediation*) Anti-Regresi** per judul novel MetroPop:
  1. **Dokumen Panduan Master Baru (`engine/12-audit-remediation.md`):** Mengkodifikasi hierarki Piramida Ketergantungan Struktur (Tingkat 1 Canon/World Building -> Tingkat 2 Outline/Plot Makro -> Tingkat 3 Kontinuitas/State Machine -> Tingkat 4 Desain Adegan Bab -> Tingkat 5 Prosa/Dialog/Diksi) dan menetapkan *The Downward Cascade Law*.
  2. **Prosedur Audit 5 Tahap Berurutan (Top-Down):** Memeriksa secara berurutan dari Fondasi Canon -> Arsitektur Outline -> Integritas Kontinuitas -> Anatomi Adegan Bab -> Prosa/Dialog, yang menghasilkan Matriks Diagnostik Cacat (*The Defect Matrix* berlabel Critical, Major, Minor).
  3. **Prosedur Remediasi Beruntun R1–R5 (Top-Down Cascading):** Memperbaiki cacat dari tingkat tertinggi yang rusak: R1 (Kunci Canon) -> R2 (Sinkronkan Outline) -> R3 (Kunci State Machine & Isolasi Jangkauan Bab Terdampak) -> R4 (Eksekusi Revisi Lokal Rasio 74/18/8 dan 4-Pass Revision) -> R5 (Verifikasi Otomatis Tanpa Regresi via `audit-continuity.py`, `analyze-prose.py`, dan *Boundary Seam Test*).
  4. **Template Laporan Audit Baru (`engine/templates/audit-remediation-report.md`):** Standar laporan audit dan remediasi per judul novel.
  5. **Pembaruan Dokumen Engine & Protokol:** Mendaftarkan file pemilik `12-audit-remediation.md` ke `engine/README.md`, `engine/00-workflow.md`, `engine/09-revision.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, dan `.agents/skills/metropop-novel/SKILL.md`.
- **File:** `engine/12-audit-remediation.md`, `engine/templates/audit-remediation-report.md`, `engine/09-revision.md`, `engine/00-workflow.md`, `engine/README.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.6 — 2026-10-31

- **Perubahan:** Menetapkan **Sistem World Building Berjangkar Realitas (*Grounded Urban World Building*)** untuk novel MetroPop Indonesia:
  1. **Dokumen Panduan Master Baru (`engine/11-worldbuilding.md`):** Mengkodifikasi 5 pilar world building:
     - *Pilar 1: Latar Spasial (Negara & Kota):* Default negara Indonesia, karakteristik kota (Jabodetabek vs Kota Lapis Kedua vs Kota Pendidikan), peta zonasi (Kutub Elit/SCBD vs Pemukiman Pekerja/Gang), serta hukum jarak tempuh, waktu, jam sibuk (07.00-09.30 & 16.30-19.30), dan moda transportasi riil (KRL, TransJakarta, ojol, SOP parkir gedung).
     - *Pilar 2: Latar Temporal (Tahun Kejadian & Era Teknologi):* Penetapan tahun spesifik (2025/2026), kanal komunikasi sah (WhatsApp grup kantor/keluarga, TikTok/IG reels/DM, QRIS, m-banking; dilarang anachronism seperti SMS jadul atau cek kertas), dan patokan daya beli riil ekonomi mikro (UMR, sewa kos, makan harian, skala utang realistis puluhan juta).
     - *Pilar 3: Sistem Hukum & Regulasi Positif Indonesia:* Prosedur Laporan Polisi (LP) resmi tanpa penangkapan ajaib, UU ITE (pencemaran nama baik & doxxing), perlindungan rahasia bank mutlak (anti-retasan mutasi rekening ajaib oleh tim IT kantor), serta regulasi perburuhan dan larangan *conflict of interest* tender vendor.
     - *Pilar 4: Norma Sosial & Budaya Urban:* Tekanan keluarga besar (pertanyaan jodoh usia 25+), rasa sungkan (*ewuh pakewuh* / *passive-aggressive*), dan solidaritas komunitas bawah (pangkalan ojol, tetangga gang).
     - *Pilar 5: Aturan Khusus Premis (6 Klausul Wajib):* Klausul hak & imbalan, kewajiban peran, batasan/larangan (no baper, no sentuh), penalti jika bocor, objek bukti fisik penyimpan aturan, dan tenggat kedaluwarsa.
     - *7 Uji Ketahanan Dunia Cerita (Audit World Building).*
  2. **Pembaruan Template Canon (`engine/templates/canon.md`):** Menambahkan sub-bab khusus World Building & Aturan Dunia Cerita terstruktur (Spasial, Temporal, Hukum, Sosial, dan Aturan Premis).
  3. **Pembaruan Dokumen Engine & Protokol:** Mendaftarkan file pemilik `11-worldbuilding.md` ke `engine/README.md`, `engine/00-workflow.md`, `engine/01-genre.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, dan `.agents/skills/metropop-novel/SKILL.md`.
- **File:** `engine/11-worldbuilding.md`, `engine/templates/canon.md`, `engine/README.md`, `engine/00-workflow.md`, `engine/01-genre.md`, `AGENTS.md`, `GEMINI.md`, `GEMINI_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.5 — 2026-10-29

- **Perubahan:** Menetapkan **Standarisasi Dua Tipe Pembuka *In Medias Res*** untuk meningkatkan daya saing retensi web novel MetroPop di bab-bab awal:
  1. **Tipe 1: *Direct Action In Medias Res* (Pembuka Aksi Langsung Kronologis):** Cerita dibuka langsung di detik terjadinya insiden pemicu / masalah mendadak pada Waktu 0; alur melaju maju linier dari Bab 1 ke depan tanpa kilas balik besar. Cocok untuk ritme komedi situasi alami dan cerita eskalasi linier (*Fichtean Curve*).
  2. **Tipe 2: *Flash-Forward Hook Framing / Proleptic In Medias Res* (Pembuka Puncak Krisis di Depan):**
     - **Bab 1 & 2:** Menculik adegan krisis puncak atau anomali dramatik ekstrem dari pertengahan cerita (Midpoint 50% atau Titik Terendah 75%) untuk dipasang di Bab 1–2, menciptakan jurang keingintahuan raksasa (*The Mega Curiosity Gap*).
     - **Bab 3 (Hukum Anti-Mendem):** Melompat mundur (*rewind*) dengan penanda waktu jelas, tetapi **DILARANG KERAS** dibuka dengan eksposisi lambat atau bangun tidur; **WAJIB DIBUKA DENGAN *DIRECT ACTION IN MEDIAS RES* (TIPE 1)** pada garis waktu lampau.
     - **Kaidah Penutupan Lingkaran (*The Loop Closure Law*):** Alur lampau menyatu kembali dengan adegan pembuka di bab tengah yang sudah dijadwalkan di outline, ditulis ulang dengan seluruh subteks, motif, dan bobot emosional utuh (*The Revisit Rule*).
  3. **Pembaruan Dokumen Engine & Template:** Mengintegrasikan pemilihan Tipe 1 vs Tipe 2 pada dokumen panduan bab, struktur, workflow, template outline, protokol agen, dan skill.
- **File:** `engine/06-chapter.md`, `engine/03-structure.md`, `engine/00-workflow.md`, `engine/templates/outline.md`, `AGENTS.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `GEMINI_SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.4 — 2026-10-27

- **Perubahan:** Menetapkan **Hukum Pemerolehan Fakta Fisik & Anti-Telepati Data Mikro (*The Physical Fact Acquisition Law*)** setelah user menemukan Rian secara ajaib mengetahui nomor pelat motor Ayu (`B 4892 TBT`) di Bab 2 padahal Ayu belum pernah memberi tahu dan Rian tidak pernah melihat pelatnya:
  1. **Aturan 3 Saluran Sah Pemerolehan Fakta:** Tokoh dilarang keras melafalkan atau mengetahui string data mikro (nomor pelat kendaraan, nama lengkap orang asing, gelar/IPK, nomor telepon/rekening, kode tagihan, alamat rumah) jika belum ada adegan fisik pemerolehan melalui salah satu dari 3 saluran sah: (1) Visual langsung dengan mata kepala sendiri, (2) Auditori nyata di dialog adegan, (3) Dokumen fisik / layar perangkat.
  2. **Log Pemerolehan Fakta per Bab di `state.md` (Komponen VI):** Menambahkan tabel rekam jejak fakta baru yang didapat tiap tokoh per bab, saluran fisiknya, dan daftar data mikro yang secara tegas *BELUM BOLEH DIKETAHUI (Strictly Unknown Data)*.
  3. **Perbaikan Bab 2:** Rian tidak menyebut pelat `B 4892 TBT`; Satpam Pak Darto yang melangkah ke motor, menunduk membaca pelat di bodi motor, mencatat di buku mutasi pos VIP, dan memegang kunci motor dari Ayu. Rian baru menanyakan nama asli Ayu di depan pintu SUV.
  4. **Pembaruan Skrip Linter (`scripts/audit-continuity.py`):** Menambahkan asersi otomatis untuk mendeteksi telepatis data mikro pada dialog tokoh.
- **File:** `engine/07-continuity.md`, `engine/08-quality.md`, `engine/templates/state.md`, `story/Narik Ojol Cinta Pun Nongol/state.md`, `story/Narik Ojol Cinta Pun Nongol/ledger.md`, `story/Narik Ojol Cinta Pun Nongol/chapters/bab-02.md`, `story/Narik Ojol Cinta Pun Nongol/manuscript.md`, `scripts/audit-continuity.py`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.3 — 2026-10-27

- **Perubahan:** Membangun **Sistem Penjaga Kontinuitas Berlapis (*The 4-Layer Continuity Guardian System*)** dan **File Penjaga Kondisi Aktif per Cerita (`state.md`)** untuk mengeliminasi amnesia AI pada alur, objek, hubungan, orang, dan waktu secara permanen:
  1. **Tiga Dokumen Pilar Kebenaran (`canon.md`, `state.md`, `ledger.md`):** `canon.md` sebagai bible rencana, `state.md` sebagai potret instan garis depan penulisan (*live state machine*), dan `ledger.md` sebagai arsip kumulatif kronologis.
  2. **File Template & Standar `state.md` (`engine/templates/state.md` & `story/<Judul>/state.md`):** Memuat 7 instrumen pengunci:
     - I. Status Garis Depan Penulisan (bab, hari/jam persis, cuaca, POV, emosi aktif).
     - II. Jangkar Waktu Relatif Mutlak (tabel H, H-1, H-2, hingga kejadian lampau berjangkar hari nyata).
     - III. Register Status Hubungan & Diksi Terlarang (label sah vs diksi yang dilarang keras, misal larangan kata "calon istri" sebelum lamaran resmi).
     - IV. Inventaris Benda Fisik Krusial (pelacak keberadaan & pemegang fisik gelang emas, motor Beat `B 4892 TBT`, uang, surat kontrak).
     - V. Kunci Ambang Batas Kejadian Pertama (*Milestone Lock* — mencegah pengulangan adegan "pertama kali" seperti pertama bertemu orang tua/Ibu atau pertama lepas masker).
     - VI. Matriks Asimetri Rahasia & Pengetahuan (*Knowledge Asymmetry* — mencegah telepati narator).
     - VII. Benang Terbuka & Janji Tertunda.
  3. **Gerbang Pra-Tulis Kontinuitas (*Pre-Flight Continuity Gate* 5 Poin):** Kewajiban menampilkan verifikasi 5 poin sebelum menulis bab; dilarang keras menulis prosa bab jika blok ini belum ada.
  4. **Pembaruan Skrip Audit Mekanis (`scripts/audit-continuity.py`):** Memvalidasi keberadaan 3 file pilar, klaim waktu relatif, status hubungan per bab, perkenalan ganda, angka uang, dan *assertion check* ambang batas kejadian pertama.
- **File:** `engine/07-continuity.md`, `engine/00-workflow.md`, `engine/templates/state.md`, `story/Narik Ojol Cinta Pun Nongol/state.md`, `scripts/audit-continuity.py`, `AGENTS.md`, `GEMINI.md`, `.agent/skills/metropop-novel/SKILL.md`, `.agents/skills/metropop-novel/SKILL.md`, `GEMINI_SKILL.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.2 — 2026-10-27

- **Perubahan:** Menambahkan **Audit Silang Antarbab** setelah user menemukan Bab 1 "pacar" tetapi Bab 2 "calon istri". Penyebab: stress test sebelumnya hanya mengukur metrik per bab (kata, em dash, posisi dialog, kalimat seragam) dan tidak pernah membandingkan klaim fakta antarbab; penyisipan 6 bab baru juga tidak diikuti audit silang pada bab di sekitarnya.
  1. `scripts/audit-continuity.py`: mencetak label status hubungan, klaim waktu relatif, perkenalan tokoh ganda, dan nominal uang per bab untuk dicocokkan dengan `ledger.md`.
  2. `07-continuity.md`: 7 aturan Audit Silang Antarbab (status hubungan, waktu relatif, perkenalan tokoh, tahu-nama, adegan pertama kali, jam lintas bab, audit ulang setelah menyisipkan bab).
  3. `09-revision.md`: Lapis 2 ditambah langkah audit silang; Daftar Kritik Editor ditambah butir kebocoran kontinuitas lintas bab.
- **File:** `engine/07-continuity.md`, `engine/09-revision.md`, `scripts/audit-continuity.py`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`, `story/Narik Ojol Cinta Pun Nongol/` (Bab 2, 7, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, ledger.md).

## v2.1 — 2026-10-27

- **Perubahan:** Mengadaptasi temuan riset korpus akademik dari `Nanako0129/sepia` (*StoryScope*, *LAMP Corpus CHI 2025*, *Reinhart et al. PNAS 2025*) yang dilokalkan ke dalam ekosistem Web Novel MetroPop Indonesia:
  1. **Memecahkan Dogma *Over-Embodied* (81% AI vs 38% Manusia), Jatah Penciuman, & Pijakan Ruang Aksi (`05-style.md`):** Menggabungkan 3 mode emosi manusia (tindakan pada objek + penyebutan perasaan jujur *plain naming* 29% manusia seperti *"Jujur, aku takut banget"* + sensasi anatomi tubuh maksimal 1–2 puncak per bab), membatasi deskripsi bau maksimal 1–2 kali per bab, dan membuka adegan di *Action Space* (ruang kerja/gerak) alih-alih *Perceived Space*.
  2. **Lima Pola Sintaksis AI yang Diburu & Pengembalian Register Manusia (`05-style.md`):** Menghapus klausa pembuka/penutup *"Sambil..., aku..."* / *"..., membuat..."*, kata benda pembungkus abstrak, nominalisasi subjek, abstrak kembar, dan kata filter persepsi; mengembalikan kata hubung kausal lisan (`soalnya, gara-gara, masalahnya, makanya, habisnya, lagian`), kalimat sanggahan alami, dan melarang rotasi tag buku pelajaran (`ujarnya/tuturnya/timpalnya/tukasnya`).
  3. **Empat Pola Posisi Kalimat di Halaman (*Discourse Position Tells*) & *QUD Check* (`05-style.md`):** Mengatur variasi letak dialog agar tidak selalu menutup paragraf, panjang paragraf tidak rata (*ragged*), menghindari *Rule of Three*, memecah deretan $\ge 3$ kalimat berurutan yang panjangnya seragam, serta mewajibkan minimal 1 paragraf perbandingan/kontradiksi ekspektasi vs realitas per bab.
  4. **Pengenalan Tokoh Lewat Dialog (*In-Dialogue Introduction*), Uji Gema (*The Echo Test*), & Rem Sidik Jari Model AI (`04-character.md` & `06-chapter.md`):** Memperkenalkan tokoh baru langsung lewat dialog/aksi aktif (penanda manusia #1) dan memasang tabel rem khusus kebiasaan model **Gemini**, **Claude**, dan **GPT**.
  5. **Rasio Edit Profesional 74/18/8 + *Deletion Test* & *Reversion Test* (`09-revision.md` & `scripts/analyze-prose.py`):** Mencegah *lexical dilution* saat revisi dan memperbarui `scripts/analyze-prose.py` ke v2.1 untuk mendeteksi persentase dialog di akhir paragraf, deretan kalimat panjang seragam, sensasi tubuh, bau, dan pola sintaksis AI.
- **File:** `engine/04-character.md`, `engine/05-style.md`, `engine/06-chapter.md`, `engine/09-revision.md`, `scripts/analyze-prose.py`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v2.0 — 2026-10-27

- **Perubahan:** Mengadaptasi fitur-fitur unggulan dari `haowjy/creative-writing-skills` yang dilokalkan ke dalam ekosistem Web Novel MetroPop Indonesia:
  1. **Lima Penyakit Insting Bawaan AI (*LLM Instinct Failure Modes*) & Prinsip Ekonomi Dua Fungsi (`05-style.md`):** Mematikan insting AI yang meredakan ketegangan terlalu cepat (*positive sentiment skew*), membuat monolog batin rapi seperti esai (*shallow interiority*), memberi kesimpulan moral di akhir adegan (*tidy-summary endings*), menyeragamkan kefasihan bicara semua tokoh, meluberkan cakupan adegan (*over-elaborating scope*), dan mengulang gerakan tubuh klise (*stock-tells trap*). Mengatur kontrol **Jarak Batin (*Psychic Distance*)** serta mewajibkan setiap elemen menjalankan minimal 2 fungsi.
  2. **Lima Jalur Kepuasan Pembaca (*5 Reader Reward Channels*) & Aturan Khusus Romansa (`01-genre.md`):** Mengunci perlindungan atas *Transportation, Social Simulation, Curiosity/Prediction, Flow,* dan *Voice Pleasure*, serta melarang klaim *chemistry* abstrak (*Don't Announce Chemistry*) dan mewajibkan *Romance Micro-Shifts* di tiap bab.
  3. **Simulasi Pembaca Pertama Kali (*Persona-Bound Reader-Sim MetroPop*) & Simulasi Tokoh (*Character-Sim*) (`08-quality.md` & `09-revision.md`):** Menambahkan uji pengalaman baca dari sudut pandang pembaca web novel HP Indonesia serta uji dialog *in-character* sesuai batas pengetahuan tokoh saat itu.
  4. **Ekstraksi *Factual State Diff*, Kontradiksi Berdampingan (*Side-by-Side Contradiction*), & Pelacak Isu Proyek (`07-continuity.md` & `templates/feedback.md`):** Mencegah *silent retcon* dengan menyajikan versi lama vs baru secara berdampingan untuk dipilih penulis, serta tabel pelacak *tic*/isu berulang lintas-bab.
  5. **Script Analisis Mekanis Prosa Bahasa Indonesia (`scripts/analyze-prose.py`):** Menganalisis jumlah kata, 0 *em dash*, deteksi frasa *AI slop*, rasio dialog vs narasi, distribusi panjang kalimat, jejak kata ganti POV 1 vs POV 3, dan pengulangan kata dalam jendela 5 paragraf.
- **File:** `engine/01-genre.md`, `engine/05-style.md`, `engine/07-continuity.md`, `engine/08-quality.md`, `engine/09-revision.md`, `engine/templates/feedback.md`, `scripts/analyze-prose.py`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`.

## v1.9 — 2026-10-27

- **Perubahan:** Mengadaptasi fitur-fitur unggulan dari `kshanxs/book-writer-skill` yang diselaraskan dengan kaidah Web Novel MetroPop Indonesia sambil mempertahankan seluruh keunggulan asli repo `novel-metropop`:
  1. **Pemisahan Tugas Narator, Monolog Batin, & Dialog (`05-style.md`):** Melarang dialog bertele-tele yang mengulang kronologi narasi atau menyebut spesifikasi teknis seperti narator (*"kertas ukuran A4"*, mengeja pelat nomor milik lawan bicara sendiri); dialog dibuat singkat dan spontan, sementara gerutuan emosi masuk ke monolog batin.
  2. **Matriks Sapaan & Kata Ganti Kontekstual (*Contextual Address Matrix* — `04-character.md` & `templates/canon.md`):** Tabel wajib di `canon.md` yang mengunci sebutan di narasi batin POV 1 (*Ibu/Ibuku, Bang Bobi, Rian*) serta perubahan sapaan dan kata ganti (*aku-kamu, gue-lo, saya-Mas*) saat formal, akrab/di depan umum, maupun saat marah.
  3. **Sistem Revisi 4 Lapis Terfokus (*4-Pass Revision System* — `09-revision.md`):** Memecah pemeriksaan revisi menjadi 4 lapis terpisah agar tidak ada detail mikro yang lolos: (1) *Audit Dialog, Subteks, & Uji Tutup-Nama*, (2) *Audit Logika Fisik, Ukuran Benda, & Asimetri Pengetahuan*, (3) *Audit Bahasa Sehari-hari, Anti-AI Slop, & Pijakan Indera Lokal*, serta (4) *Audit Gelombang Ketegangan & Hook*.
  4. **Mesin Mikro Adegan (`Berhasil, tapi...` / `Gagal, dan malah...`), Pergeseran Emosi, & Gerbang Khusus Bab 1 (`06-chapter.md` & `03-structure.md`):** Mencegah bab datar di tengah buku dan menambah 5 uji khusus Bab 1 sebelum lanjut ke Bab 2.
  5. **Protokol *Smart-Reading*, *Content Boundary*, & Protokol Spinoff Satu Semesta (`00-workflow.md` & `07-continuity.md`):** Mengatur pemuatan file panduan *on-demand* sesuai Mode A–E agar konteks AI tidak terdilusi, serta aturan `[DARI: <Judul Induk>]` untuk novel *spinoff*.
  6. **Script Penggabung Naskah Otomatis (`scripts/combine-chapters.sh`):** Menggabungkan seluruh `chapters/bab-*.md` menjadi satu file `manuscript.md` utuh disertai tabel audit jumlah kata per bab.
- **File:** `AGENTS.md`, `engine/00-workflow.md`, `engine/03-structure.md`, `engine/04-character.md`, `engine/05-style.md`, `engine/06-chapter.md`, `engine/07-continuity.md`, `engine/09-revision.md`, `engine/templates/canon.md`, `engine/templates/outline.md`, `scripts/combine-chapters.sh`, `story/Narik Ojol Cinta Pun Nongol/canon.md`, dan file Skill.

## v1.8 — 2026-10-27

- **Perubahan:**
  1. **Pemurnian POV 1 (Anti-Kebocoran Character Sheet POV 3):** Mewajibkan protagonis POV 1 menyebut anggota keluarganya dan orang terdekat dengan panggilan hubungan langsung (*Ibu/Ibuku, Bapak, Bang Bobi*), melarang penyebutan nama lengkap *character sheet* (*"Ibu Sumi"*) di narasi batin protagonis, serta menghapus julukan berjarak ala narator orang ketiga (*"bos muda itu"*).
  2. **Uji Asimetri Pengetahuan Tokoh (*"Kok Dia Tahu Info Itu?"*) & Anti-Retroactive Planting:** Melarang tokoh mengetahui fakta yang baru ada di monolog batin protagonis, melarang klaim *mention* masa lalu yang adegannya belum pernah ditulis di bab sebelumnya, dan menjaga kronologi bukti foto intaian.
  3. **Uji Logika Ukuran, Dimensi, & Wadah Benda (*Physical Scale*):** Memastikan ukuran benda sesuai dengan wadah/konteksnya (misal fotokopi ijazah A4 hanya bisa terselip tak sengaja jika tercampur dengan dokumen A4 lain seperti katalog harga kue saat terburu-buru; kotak kue & map A4 dibawa memakai *tas jinjing/tote bag*).
  4. **Kelonggaran Darurat Rentang Kata (Maksimal 1.200 Kata):** Standar bab tetap **600–900 kata** (target ±750 kata), namun boleh dilonggarkan hingga **maksimal 1.200 kata hanya jika benar-benar urgent** agar tidak memotong kejadian penting atau logika cerita.
- **File:** `AGENTS.md`, `GEMINI.md`, `engine/04-character.md`, `engine/06-chapter.md`, `engine/08-quality.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`, serta file Skill.

## v1.7 — 2026-10-26

- **Perubahan:** Menambahkan **7 Uji Logika Mikro & Prosedur Dunia Nyata (Anti-Cacat Logika Fiksi)** serta aturan **Keluwesan Lisan & Realitas Lokal Indonesia**:
  1. **Uji Sebab-Akibat & Anti-Redundansi Percakapan:** Melarang dialog di mana Tokoh B menuntut syarat yang baru saja ditawarkan Tokoh A; memisahkan secara tegas konsep *uang muka (DP)* dan *pelunasan*.
  2. **Uji Prosedur & Mekanisme Dunia Nyata:** Memastikan prosedur parkir gedung (titip satpam dengan tip + *tap* kartu saat keluar), aturan kerahasiaan bank (larangan klise "tim IT meretas mutasi bank pribadi dalam 3 jam"), dan hukum berjalan sesuai realitas Indonesia.
  3. **Uji Konsistensi Hitungan Uang & Ekonomi:** Melacak setiap rupiah (DP, pelunasan, jumlah yang terpakai membayar utang, dan sisa saldo yang dikembalikan) agar konsisten secara matematis.
  4. **Uji Fisik, Pakaian, & Benda Bawaan (*Object Permanence*):** Melarang tindakan fisik mustahil (seperti makan makanan berkuah sambil memakai masker di meja makan atau membawa troli katering besar di atas motor matik).
  5. **Uji Jalur Informasi & Jejak Bukti:** Mewajibkan penjelasan eksplisit dari mana tokoh mendapat nomor WA (misal dari spanduk warung) atau bukti transfer.
  6. **Uji Motivasi Kehadiran Tokoh & Realitas Iklim/Lokal Indonesia:** Menghapus terjemahan harfiah (*arah jam sebelas, izin diberikan, papan tombol, sepeda kargo*) dan detail asing (*penghangat kabin mobil* di Jakarta, *cek pribadi* untuk anak muda).
- **File:** `engine/05-style.md`, `engine/08-quality.md`, `engine/09-revision.md`, `engine/learnings/editor-feedback.md`, `engine/learnings/changelog.md`, serta seluruh bab `story/Narik Ojol Cinta Pun Nongol/`.

## v1.6 — 2026-10-26

- **Perubahan:** Mengintegrasikan `Kerangka Plot yang Terbukti untuk Web Novel.md` sebagai acuan utama kerangka plot, pembuatan ide/premis baru, pengembangan premis ke outline, dan evaluasi/penilaian alur cerita:
  - **Membuat Ide/Premis Baru:** Menggunakan arah terbalik (dari kelemahan tokoh + kerangka plot) dengan Tabel Bahan Ide MetroPop dan **Resep 9 Langkah**.
  - **Uji Kelayakan & Pengembangan Premis:** Wajib lolos **Uji 5 Slot Kelayakan** (kejadian spesifik, minimal 3 jalan mudah tertutup tanpa membuat tokoh bodoh, hindari hukum/polisi/uang miliaran yang memicu *burnout*), **Prosedur 7 Langkah**, serta batas minimal titik balik (6 untuk 30 bab, 8 untuk 40 bab).
  - **Struktur & Kerangka:** Mengadopsi **8 Kerangka Plot Terbukti** (Tiga Babak, Save the Cat, Story Circle, Seven-Point, Fichtean Curve, Struktur Romance, Kishōtenketsu, Arc Bersarang), pemetaan ke **8 Tahap Format Dasar Penulis**, **Siklus Coba-Gagal** (6 komponen wajib + Uji 100%), **Prosedur Planting Solusi 2 Kali**, dan **16 Studi Kasus Novel Terkenal**.
  - **Menilai Alur Cerita:** Menetapkan **10 Uji Logika** dan **10 Tanda Bahaya (*Red Flags*)** sebagai standar evaluasi outline dan diagnosis revisi naskah.
- **File:** `AGENTS.md`, `engine/README.md`, `engine/00-workflow.md`, `engine/02-premise.md`, `engine/03-structure.md`, `engine/08-quality.md`, `engine/09-revision.md`, `engine/sources.md`, `engine/templates/`, `engine/learnings/`, dan seluruh file Skill (`GEMINI_SKILL.md`, `CLAUDE_SKILL.md`, `CHATGPT_SKILL.md`, `.agent/skills/metropop-novel/SKILL.md`).

## v1.5 — 2026-10-24

- **Perubahan:** Penegasan gaya berdasarkan masukan editor:
  - Hapus dan larang kutipan/quote di atas bab (agar tidak mencontek novel acuan).
  - Larang keras pemakaian em dash (`—`) di seluruh narasi maupun dialog novel.
  - Hilangkan diksi baku kaku dan deskripsi melodramatis/AI slop; wajib memakai bahasa tutur dan percakapan alami orang Indonesia.
- **File:** `engine/05-style.md`, `engine/06-chapter.md`, `engine/learnings/editor-feedback.md`.

## v1.4 — 2026-10-22

- **Perubahan:** Mengadopsi `acuan-bahasa.docx` sebagai acuan utama cara penulisan,
  gaya bahasa, diksi, dan cara bercerita. Dokumen lama dipindahkan ke `old-documents-unneeded/`.
- **Gaya & Diksi Baru:**
  - Pilihan POV Utama: Orang Pertama ("Aku") yang ekspresif, lincah, dan sarat monolog
    batin yang reaktif, sarkastik, serta *self-deprecating*.
  - Natural *corporate/urban code-switching*: pemakaian istilah/frasa bahasa Inggris yang
    wajar dalam percakapan perkotaan modern (*outlier, drawer, walkout, lunch break,
    urgent, meeting, resign, CV, awkward, simple truth, done*).
  - Register sapaan kontras: ledek-ledekan antarrekan kubikel (*lo-gue*), senior tim
    (*Mbak/Mas* + nada santai), dan atasan (*saya-Bapak/Ibu*).
  - Format bab: ~~judul bab kini dapat dilengkapi *epigraph / quote* pembuka bab bernada satir/humor~~ **[DIUBAH & DILARANG DI v1.5: Tanpa quote/epigraph di atas bab]**.
  - Dinamika karakter: arketipe kawan senasib kubikel (*The Cungpret dynamic*).
- **File:** `AGENTS.md`, `engine/README.md`, `engine/00-workflow.md`, `engine/01-genre.md`,
  `engine/04-character.md`, `engine/05-style.md`, `engine/06-chapter.md`, `engine/sources.md`,
  `engine/SKILL.md`, `.agent/rules/metropop.md`, `engine/learnings/editor-feedback.md`.

## v1.3 — 2026-10-22

- **Perubahan:** Mengadopsi `Panduan Proyek Web Novel Reply All (Brief untuk AI).md`
  sebagai acuan tertinggi; panduan lama menjadi referensi tambahan.
- **Cakupan baru:** target pembaca 13+; latar dan usia tokoh bebas (kantor, sekolah,
  kuliah, pernikahan, keluarga, desa, lansia).
- **Prinsip Pas:** teknik naratif, subplot, flashback, dan scene ikonik opsional; boleh
  nol; angka 1–3 subplot / 3–5 scene ikonik adalah batas atas, bukan target.
- **Workflow:** tahap A–G, balasan pertama 5 poin, Daftar Usulan Ide, Tes Pas, dan
  Daftar Kritik Editor.
- **Kontinuitas:** tambah A2 timeline masa lalu, rahasia/bukti, tokoh kecil berulang;
  Ledger D kini memuat hubungan terakhir dan rahasia yang dipegang.
- **Mekanisme:** canon wajib memuat “kenapa tidak bisa diperbaiki”.
- **Teknik:** katalog Wajib/Sering/Sesekali/Jarang/Dilarang dan batas 1–2 teknik per bab.
- **Protokol:** intake form, Daftar Usulan Ide (aktif, bukan opsional), rubrik jadi hard gate
  (tidak ada jalan kirim dengan skor gagal) plus alasan singkat jika nilai <5.
- **Konsistensi:** batas kata diseragamkan ke 600–900 di semua file; Daftar Kritik Editor
  punya satu pemilik (`09-revision.md`); rantai prioritas disamakan.
- **Template:** canon, outline, ledger, premise-options, idea-list.
- **File:** `AGENTS.md`, `00-workflow.md`, `01-genre.md`, `02-premise.md`,
  `03-structure.md`, `04-character.md`, `05-style.md`, `06-chapter.md`,
  `07-continuity.md`, `08-quality.md`, `09-revision.md`, `10-evolution.md`,
  `README.md`, `sources.md`, `story/README.md`, `.agent/rules/metropop.md`, templates.

## v1.2 — 2026-10-22

- **Perubahan:** Stress test end-to-end 30 bab + Bab 1; aturan diperkuat.
- **Temuan:** hook dari nomor tak dikenal tanpa jalur; POV slip; ledger mengklaim fakta
  yang tidak ada di teks; beat/setup outline tidak ditanam; definisi teknis menumpuk;
  similes berlebih; "besok pagi" pada 02.19; pintu keluar (telepon Bu Laras) tidak ditutup.
- **Aturan baru:** POV terbatas; format SMS/nomor tak dikenal; maksimal 2 definisi panjang
  per bab; maksimal 1–2 simile; kontrak beat/setup/payoff; hook harus punya jalur;
  ledger hanya fakta yang ada di teks; kolom "jalan keluar paling mudah ditutup";
  cek POV/ledger/beat sebelum kirim.
- **File:** `02-premise.md`, `03-structure.md`, `04-character.md`, `05-style.md`,
  `06-chapter.md`, `07-continuity.md`, `08-quality.md`, `00-workflow.md`,
  `templates/outline.md`, `templates/chapter.md`, `templates/ledger.md`.
- **Dampak:** semua project baru; bab lama hanya jika relevan.

## v1.1 — 2026-10-21

- **Perubahan:** Migrasi penuh ke agent-first. `engine/` sekarang berisi markdown;
  engine Python lama dihapus dari working tree.
- **Alasan:** Workflow utama adalah agent menulis lewat percakapan, bukan CLI.
- **Dampak:** Project baru memakai `AGENTS.md`, `engine/00-workflow.md`, dan template
  canon/outline/ledger/chapters.

## v1.0 — YYYY-MM-DD

- **Perubahan:** Paket agent-first dibuat.
- **Isi:** `AGENTS.md`, `engine/` (workflow, genre, premis, struktur, karakter, gaya,
  bab, kontinuitas, kualitas, revisi, evolusi), templates, examples, learnings.
- **Alasan:** Workflow agentic butuh instruksi markdown, bukan CLI Python.
- **Dampak:** Project baru memakai format canon/outline/ledger/chapters.

## Template Entri

```markdown
## v1.1 — YYYY-MM-DD
- **Perubahan:** ...
- **Alasan:** ...
- **File:** ...
- **Dampak:** bab baru / semua bab / hanya project tertentu.
```

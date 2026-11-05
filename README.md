# novel-metropop

Repositori ini adalah **sistem panduan terpadu (Single Source of Truth)** yang dibaca oleh AI agent maupun AI chat untuk membantu penulis dari tahap **brainstorming ide & premis**, **merancang konflik & kerangka cerita**, **menyusun outline per bab**, hingga **menulis dan merevisi web novel MetroPop Indonesia sampai selesai**.

---

## 1. Prinsip Utama Repositori Ini

1. **Repo sebagai Rujukan Utama (Repo-First):**
   Seluruh teori penulisan fiksi yang dibutuhkan sudah dilebur secara terstruktur tanpa tumpang tindih di dalam folder `engine/` dan contoh gaya bahasa di `acuan-bahasa.docx`. AI wajib menjadikan repo ini sebagai rujukan utama sebelum memakai pendapatnya sendiri atau mencari di internet.
2. **Pencarian Internet Hanya untuk Tambahan & Anti-AI Slop:**
   AI hanya mencari di internet untuk:
   - Mengecek fakta dunia nyata terbaru di Indonesia (prosedur administrasi/lembaga, harga/biaya terkini, rute lokasi, kosakata urban terbaru) guna menutup penanda `"perlu dicek"`;
   - **Memperbarui secara terus-menerus cara menghindari halusinasi dan tulisan *AI slop*** (`engine/sources.md`, `engine/05-style.md`, `scripts/analyze-prose.py`).
3. **Satu Topik = Satu File Pemilik (Zero Duplication):**
   Tidak ada duplikasi aturan antarfile agar AI tidak bingung saat membaca konteks.

---

## 2. Struktur Berkas Repositori

```text
AGENTS.md              # Entry point utama protokol AI agent
GEMINI.md              # Pointer protokol untuk Gemini / Antigravity
CLAUDE.md              # Pointer protokol untuk Claude Code
STANDALONE.md          # Panduan ringkas mandiri untuk pengguna Web Chat (ChatGPT/Claude/Gemini Web)
acuan-bahasa.docx      # Acuan utama gaya bahasa, diksi, dan tone bercerita (Resign! - Almira Bastari)
reader.html            # Aplikasi pembaca web novel offline untuk layar HP (hasil generate scripts/build-reader.py)
.agent/skills/         # Workspace skill untuk Antigravity CLI (metropop-novel)
engine/                # Otak panduan penulisan (1 file pemilik per topik, tanpa duplikasi):
├── README.md          # Peta paket engine dan pemilik aturan
├── 00-workflow.md     # Alur kerja tahap A–G & protokol Smart-Reading
├── 01-genre.md        # Definisi MetroPop, skala masalah kelas menengah, & batasan 13+
├── 02-premise.md      # Premis, Rumus ABCD, 7 Cara Menutup Jalan Mudah, Uji Spider-Man, & Brainstorming 7 Langkah
├── 03-structure.md    # 8 Kerangka Plot Terbukti, Siklus Coba-Gagal, Planting 2x, 16 Studi Kasus, & 18 Kolom Outline
├── 04-character.md    # Karakter, psikologi, luka formatif, disorder, scene stealer, & matriks sapaan
├── 05-style.md        # Gaya bahasa, POV 1, anti-AI slop kalimat, & aturan teks polos (plain text)
├── 06-chapter.md      # Kerajinan bab (600–900 kata), mesin mikro adegan, 2 tipe in medias res, & hook
├── 07-continuity.md   # Sistem kontinuitas (canon.md, state.md, ledger.md), Pre-Flight Gate, & cameo
├── 08-quality.md      # Rubrik 8 kriteria, 10 Uji Logika, 9 Uji Logika Mikro, 10 Tanda Bahaya, & Stress Test
├── 09-revision.md     # Revisi 4 lapis, Audit 5 Tahap, Remediasi Beruntun R1–R5, & rasio edit 74/18/8
├── 10-evolution.md    # Aturan pembaruan engine & pengelolaan arsip
├── 11-worldbuilding.md# World building berjangkar realitas Indonesia (spasial, temporal, daya beli, hukum)
├── sources.md         # Hierarki rujukan Repo-First, riset internet anti-AI slop, & katalog novel
├── templates/         # Template dokumen cerita (canon, state, outline, ledger, premise-options, dll.)
├── examples/          # Contoh premis, outline, adegan, hook, dan before/after gaya bahasa
└── learnings/         # Arsip riwayat feedback & changelog (tidak dibaca saat sesi kerja normal)
scripts/               # Wasit mekanis Python (tanpa library eksternal / standard library murni):
├── audit-continuity.py# Linter kontinuitas lintas bab (waktu relatif, status hubungan, uang, milestone)
├── analyze-prose.py   # Linter prosa (hitung kata, 0 em dash, deteksi AI slop, variasi kalimat)
├── build-reader.py    # Generator reader.html untuk membaca novel di HP
└── combine-chapters.sh# Penggabung bab menjadi manuscript.md
story/                 # Folder karya novel:
├── universe-registry.md # Pendaftar semesta, bank premis, anti-duplikasi tokoh, & protokol cameo
└── <Judul>/           # Folder per judul novel (canon.md, state.md, outline.md, ledger.md, chapters/)
```

---

## 3. Peran Skrip Python & Cara Menjalankan (Android Termux, Linux, Windows)

Skrip di `scripts/` menggunakan **Python 3.8+ Standard Library murni** (tidak butuh `pip install`):

```bash
# Audit kontinuitas cerita
python3 scripts/audit-continuity.py "story/Narik Ojol Cinta Pun Nongol"

# Analisis kualitas prosa & deteksi AI slop
python3 scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol"

# Perbarui tampilan baca HP (reader.html)
python3 scripts/build-reader.py
```

Jika menggunakan **Web Chat di browser** tanpa terminal, lihat panduan unggah file bertahap di [STANDALONE.md](STANDALONE.md).

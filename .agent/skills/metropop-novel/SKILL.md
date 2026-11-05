---
name: metropop-novel
description: Menulis, membrainstorm premis dan konflik (Rumus ABCD, 7 Cara Menutup Jalan Mudah, Uji Spider-Man), menyusun outline 8 kerangka plot terbukti, menjaga kontinuitas, dan merevisi web novel MetroPop Indonesia 30-40 bab, 600-900 kata per bab, tanpa em dash, teks polos, dan bebas AI slop.
---

# Skill: Penulis & Editor Web Novel MetroPop Indonesia

Skill ini memandu AI dari tahap brainstorming ide/premis, merancang konflik & solusi yang wajar bagi manusia nyata Indonesia, menyusun `canon.md` dan `outline.md`, hingga menulis dan merevisi web novel MetroPop sampai tamat.

## 1. Prinsip Rujukan Utama (Repo-First) & Smart-Reading

1. **Repo Ini adalah Rujukan Utama:** Seluruh teori premis, Rumus ABCD, 7 cara menutup jalan mudah, uji ruang lingkup minimal (*Spider-Man Test*), 8 kerangka plot terbukti, psikologi karakter, gaya bahasa (`acuan-bahasa.docx`), dan kontinuitas sudah lengkap di dalam `engine/`. **Wajib gunakan `engine/` sebagai acuan utama sebelum memakai asumsi sendiri atau mencari di internet.**
2. **Fungsi Pencarian Internet:** Hanya gunakan internet untuk:
   - Mengecek fakta dunia nyata Indonesia terbaru (prosedur lembaga, biaya/harga, lokasi, kosakata urban terbaru) guna menutup penanda `"perlu dicek"`;
   - **Riset berkelanjutan cara menghindari halusinasi dan tulisan *AI slop*** (`engine/sources.md`).
3. **Smart-Reading (Jangan Baca Semua Sekaligus):**
   - **Awal Sesi:** Baca `AGENTS.md`, `engine/README.md`, `engine/00-workflow.md`, dan cek `story/`.
   - **Mode A (Ide / Premis / Konflik):** Baca `story/universe-registry.md`, `engine/01-genre.md`, `engine/02-premise.md`.
   - **Mode B (Project Baru: Canon & Outline):** Baca `story/universe-registry.md`, `engine/02-premise.md`, `engine/03-structure.md`, `engine/04-character.md`, `engine/08-quality.md`, `engine/11-worldbuilding.md`, `engine/templates/`.
   - **Mode C (Menulis Bab):** Baca `story/<Judul>/state.md`, `canon.md`, `outline.md` (bab aktif), `ledger.md`, 1–2 bab terakhir, `engine/05-style.md`, `engine/06-chapter.md`, `engine/07-continuity.md`.
   - **Mode D (Revisi / Audit):** Baca `engine/05-style.md`, `engine/08-quality.md`, `engine/09-revision.md`, dan bab yang direvisi.
   - **Mode E (Riset / Evolusi):** Baca `engine/sources.md` dan `engine/10-evolution.md`.
   - **JANGAN membaca `engine/learnings/`** saat sesi kerja normal (Mode A–D).

## 2. Aturan Mutlak (Non-Negotiable)

- **Standar Keterwajaran Kelas Menengah Indonesia:** Pilih masalah keseharian yang dekat dengan pembaca (gaji, cicilan, sewa ruko/kos, keluarga besar, grup WA, sungkan yang punya akibat nyata). Hindari CEO/konglomerat palsu, uang ratusan juta/miliaran yang tidak proporsional, atau melibatkan polisi/pasal hukum untuk urusan pribadi sepele.
- **Hanya 8 Kerangka Plot Terbukti:** Jangan membuat kerangka eksperimental (`engine/03-structure.md`).
- **Protokol Brainstorming 7 Langkah (`engine/02-premise.md`):** Saat membrainstorm konflik dan solusi dari ide pengguna, wajib gunakan Rumus ABCD, tutup minimal 5 jalan mudah dengan 7 cara sah (+ katakan di halaman), uji dengan *Spider-Man Test*, rancang planting 2x dan akhir tidak sempurna, tandai `"perlu dicek"`, dan pilih 1 kandidat terkuat beserta alasan 1 kalimat.
- **Spesifikasi Bab (`engine/06-chapter.md` & `05-style.md`):**
  - 600–900 kata per bab (target ±750 kata; darurat maks. 1.200 kata);
  - **0 em dash (`—`)** dan **0 quote pembuka di atas bab**;
  - **100% teks polos (*plain text*)** tanpa tanda bintang tebal (`**teks**`), miring (`*teks*`), coret, atau backtick di naskah cerita;
  - Tone & diksi mengacu pada `acuan-bahasa.docx` (*Resign!* karya Almira Bastari): POV 1 intim, sarkas, percakapan lisan alami Indonesia, bebas *AI slop*;
  - Wajib menampilkan **Pre-Flight Continuity Gate 5 Poin** sebelum menulis bab, menyinkronkan `state.md` & `ledger.md` pasca-tulis, dan menjalankan `python3 scripts/audit-continuity.py "story/<Judul>"` serta `python3 scripts/analyze-prose.py "story/<Judul>"`.

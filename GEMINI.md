# Protokol Gemini / Antigravity — Web Novel MetroPop Indonesia

- **Workspace Skill Antigravity:** `.agent/skills/metropop-novel/SKILL.md` (dan `.agents/skills/metropop-novel/SKILL.md`)
- **Standalone Skill (All-in-One):** [GEMINI_SKILL.md](GEMINI_SKILL.md) untuk Gemini Advanced, Gems, dan Google AI Studio.
- **Acuan Utama Gaya & Diksi:** `acuan-bahasa.docx` dan `engine/05-style.md`
- **Acuan Utama Arsitektur & Pengembangan Premis:** `panduan-pengembangan-premis-cerita.md` dan `engine/02-premise.md`
- **Acuan Utama Kerangka Plot & Evaluasi Alur:** [Kerangka Plot yang Terbukti untuk Web Novel.md](Kerangka%20Plot%20yang%20Terbukti%20untuk%20Web%20Novel.md) (`engine/02-premise.md`, `03-structure.md`, `08-quality.md`)
- **Acuan Utama World Building & Aturan Dunia:** [engine/11-worldbuilding.md](engine/11-worldbuilding.md)
- **Acuan Utama Audit & Remediasi Menyeluruh:** [engine/12-audit-remediation.md](engine/12-audit-remediation.md)

## Aturan Mutlak Menulis (Non-Negotiable)

1. **Rentang Kata:** Standar wajib 600–900 kata per bab (target ±750 kata; boleh dilonggarkan hingga maksimal 1.200 kata **hanya jika benar-benar urgent** karena berpotensi memotong kejadian penting). Dilarang mengirim bab di bawah 600 kata.
2. **Tanpa Em Dash (`—`):** Dilarang keras memakai karakter em dash di narasi maupun dialog di seluruh novel. Gunakan koma, titik, tanda pisah hubung biasa (`-`), atau susun kalimat alami.
3. **Tanpa Quote Pembuka Bab:** Jangan menaruh kutipan/quote/epigraph di atas bab.
4. **Bebas dari AI Slop & Diksi Baku Kaku:** Gunakan bahasa tutur dan percakapan alami orang Indonesia (lo-gue, santai, membumi, segar). Dilarang memakai metafora klise atau frasa puitis robotik buatan mesin.
5. **Format Bab:** Judul `## Bab N: Judul` (2–5 kata), Bab 1 wajib in medias res, diakhiri hook kuat di kalimat terakhir.
6. **Mekanisme Kontinuitas & Gerbang Pra-Tulis:** Wajib membaca `story/<Judul>/` (`state.md`, `canon.md`, `outline.md`, `ledger.md`) dan menampilkan blok *Pre-Flight Continuity Gate* (5 poin) sebelum menulis bab, menyinkronkan `state.md` + `ledger.md` pasca-tulis, serta menjalankan `python3 scripts/audit-continuity.py`.
7. **Evolusi Engine:** Jika user memberi kritik atau preferensi baru, AI wajib mencatatnya di `engine/learnings/editor-feedback.md` dan memperbarui file panduan terkait di `engine/`.
8. **Universe Registry, Anti-Duplikasi, & Protokol Cameo:** Wajib membaca `story/universe-registry.md` sebelum Mode A dan B. Dilarang keras menawarkan kembali premis yang sudah ditolak, menduplikasi kombinasi nama/watak/profesi tokoh lama, atau menggunakan trope dalam *Daftar Hitam Trope*. Integrasikan semesta bersama lewat Protokol Cameo 3 Tingkat (Dialog, Kilas Balik, Fisik tanpa deus ex machina).

Untuk panduan lengkap mencakup alur kerja A–G, arketipe karakter, tabel anti-AI slop, dan rubrik kualitas 8 kriteria, baca seluruh isi [GEMINI_SKILL.md](GEMINI_SKILL.md).

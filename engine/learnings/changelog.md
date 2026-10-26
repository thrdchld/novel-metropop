# Changelog Engine

Catat setiap perubahan aturan, template, atau sumber. Perubahan kecil, spesifik, dan
disertai alasan.

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

# novel-metropop

Repositori untuk menulis web novel **MetroPop Indonesia** bersama AI agent: 30–40 bab,
±750 kata per bab, target pembaca **13+**, latar dan usia tokoh bebas. Dilengkapi canon,
outline terkunci, Story Ledger, dan rubrik.

**Prinsip Pas:** teknik naratif, subplot, flashback, dan scene ikonik adalah alat
opsional. Boleh nol jika cerita sudah padat. Jangan memaksakan.

Repo ini **agent-first**. Otaknya adalah markdown di `engine/`, bukan aplikasi Python.
Buka folder ini di Antigravity, Codex, Claude, Gemini, atau agent lain, lalu suruh ia
membaca `AGENTS.md`.

## Mulai di Agent

Buka folder repo, lalu tempel:

> Baca `AGENTS.md` dan `engine/README.md`. Setelah itu tanya saya mau apa: ide baru,
> project baru, lanjutkan cerita, revisi, atau analisis referensi.

Agent akan:

1. membaca protokol dan panduan;
2. memeriksa `story/`;
3. bertanya satu pertanyaan;
4. bekerja sesuai mode yang kamu pilih.

Tidak perlu install Python, API key engine, atau CLI. API key hanya untuk agent-nya.

## Struktur

```text
AGENTS.md              # protokol utama agent
CLAUDE.md              # pointer untuk Claude
CLAUDE_SKILL.md        # skill mandiri all-in-one untuk Claude
CHATGPT_SKILL.md       # skill mandiri all-in-one untuk ChatGPT / Custom GPT
GEMINI.md              # pointer untuk Gemini/Antigravity
GEMINI_SKILL.md        # skill mandiri all-in-one untuk Gemini / Gems
engine/                # otak agent: workflow, genre, struktur, gaya, template
story/                 # cerita: canon, outline, ledger, chapters
acuan-bahasa.docx      # acuan utama gaya bahasa, diksi, dan cara bercerita
old-documents-unneeded/ # arsip referensi panduan sebelumnya
```

## Mode Kerja

- **Ide/premis baru** — agent memberi 3 opsi: judul, logline, tema, tokoh, pemicu, humor.
- **Project baru** — tahap A–G: premis → dokumen dasar → outline → stress test → lock →
  Bab 1.
- **Lanjutkan** — baca canon/ledger/bab terakhir → posisi 5 baris → konfirmasi → bab baru.
- **Revisi** — klasifikasi feedback → revisi lokal → update canon/ledger → catat pelajaran.
- **Riset** — ekstrak prinsip dari PDF/teks/URL, tanpa menyalin karya berhak cipta.

## Struktur Cerita

```text
story/<Judul>/
├── canon.md
├── outline.md
├── ledger.md
├── feedback.md
└── chapters/
    ├── bab-01.md
    └── ...
```

Template ada di `engine/templates/`.

## Engine Belajar

Jika feedback yang sama muncul dua kali, atau kamu menyetujui teori/gaya baru, agent
memperbarui:

- `engine/learnings/editor-feedback.md`
- `engine/learnings/changelog.md`
- file panduan terkait (`05-style.md`, `03-structure.md`, dst.)

Dengan begitu instruksi makin baik seiring waktu, bukan menumpuk revisi yang sama.

## Catatan

Engine Python dari iterasi sebelumnya sudah dihapus dari working tree. Jika suatu saat
butuh referensi implementasi lama, ambil dari riwayat git sebelum commit migrasi.

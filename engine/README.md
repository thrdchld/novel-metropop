# Engine — Otak Panduan Penulisan Novel MetroPop

Folder ini adalah **paket panduan utama (Single Source of Truth)** untuk AI agent maupun AI chat dalam merancang ide/premis, menyusun kerangka & outline, menjaga kontinuitas, hingga menulis dan merevisi web novel **MetroPop Indonesia** sampai selesai.

---

## 1. Prinsip Rujukan Utama (Repo-First Principle)

1. **Jadikan Repo Ini sebagai Rujukan Utama:** Seluruh teori premis, Rumus ABCD, 7 cara menutup jalan mudah, 8 kerangka plot terbukti, psikologi karakter, gaya bahasa (`../acuan-bahasa.docx`), dan sistem kontinuitas sudah lengkap di folder `engine/` ini. AI **wajib** memakai prosedur di repo ini lebih dulu, bukan mengandalkan asumsi bawaannya sendiri.
2. **Kapan Mencari di Internet:** Pencarian internet hanya dipakai sebagai **tambahan pendukung** untuk:
   - Memastikan fakta dunia nyata Indonesia terbaru (prosedur lembaga, harga/biaya terkini, rute lokasi, kosakata urban terbaru) guna menutup penanda `"perlu dicek"`;
   - **Riset berkelanjutan cara menghindari halusinasi dan tulisan *AI slop*** (mendeteksi pola kalimat/perilaku khas LLM terbaru agar prosa dan logika cerita selalu terasa ditulis manusia).

---

## 2. Peta File & Pemilik Tunggal Aturan (Zero Duplication)

Setiap topik aturan hanya memiliki **satu file pemilik tunggal** agar tidak ada tumpang tindih yang membingungkan AI:

| File Pemilik | Isi & Tanggung Jawab Tunggal |
|---|---|
| `00-workflow.md` | Alur kerja tahap A–G, aturan *Smart-Reading* (file mana yang dibaca per mode), *Prinsip Pas*, dan *Definition of Done*. |
| `01-genre.md` | Definisi MetroPop Indonesia, skala masalah kelas menengah (tanpa hukum rumit/polisi/miliarder), 5 jalur kepuasan pembaca, batasan 13+. |
| `02-premise.md` | **Premis & Ide:** Uji 5 Slot, Rumus ABCD, Menutup Jalan Mudah (7 Cara Sah + Katakan di Halaman), Uji Konflik yang Dipaksakan (*Spider-Man Test*), Protokol Brainstorming 7 Langkah, Resep 9 Langkah, M.I.C.E., 3P Sanderson, & Universe Registry. |
| `03-structure.md` | **Struktur & Outline:** 8 Kerangka Plot Terbukti (tanpa kerangka eksperimental), Pemetaan 8 Tahap Penulis, Siklus Coba-Gagal (6 Isi Wajib & Uji 100%), Planting Solusi 2 Kali, 16 Studi Kasus Novel Terkenal, & 18 Kolom Outline. |
| `04-character.md` | **Karakter & Psikologi:** Character sheet, *tells*, luka formatif, pola asuh, katalog disorder fungsional, *scene stealer* (lovable & hateable), & Matriks Sapaan Kontekstual. |
| `05-style.md` | **Gaya Bahasa & Diksi:** Acuan nada *Resign!* (`../acuan-bahasa.docx`), POV 1 intim, 5 penyakit insting AI, 5 pola sintaksis AI yang dilarang, & aturan teks polos (*plain text*). |
| `06-chapter.md` | **Kerajinan Bab:** Rentang 600–900 kata (target ±750 kata), Mesin Mikro Adegan (`Berhasil, tapi...` / `Gagal, dan malah...`), 2 Tipe *In Medias Res*, & 8 variasi hook akhir bab. |
| `07-continuity.md` | **Kontinuitas:** 3 dokumen kebenaran (`canon.md`, `state.md`, `ledger.md`), Gerbang Pra-Tulis 5 Poin (*Pre-Flight Gate*), anti-telepati data mikro, & protokol cameo 3 tingkat. |
| `08-quality.md` | **Kualitas & Evaluasi Logika:** Rubrik 8 kriteria, 10 Uji Logika Makro, 9 Uji Logika Mikro Dunia Nyata, 10 Tanda Bahaya (*Red Flags*), Stress Test Outline, & 4 Teknik Bedah Alur Tengah Cerita. |
| `09-revision.md` | **Revisi & Audit:** Piramida Ketergantungan 5 Tingkat, Audit 5 Tahap, Remediasi Beruntun R1–R5, Sistem Revisi 4 Lapis, & Rasio Edit 74/18/8. |
| `10-evolution.md` | **Evolusi Engine:** Cara memperbarui aturan engine dan pengelolaan arsip. |
| `11-worldbuilding.md` | **World Building:** Latar spasial (kota, zonasi, jam macet), temporal (tahun, WA/QRIS/m-banking, daya beli riil), hukum nyata RI, & norma sosial Indonesia. |
| `sources.md` | **Rujukan & Riset:** Hierarki rujukan *Repo-First*, panduan riset internet anti-AI slop/halusinasi, & katalog referensi novel. |
| `templates/` | Template standar untuk `canon.md`, `state.md`, `outline.md`, `ledger.md`, `character-sheet.md`, `premise-options.md`, `change-request.md`, dll. |
| `examples/` | Contoh konkret premis, outline, adegan, hook, dan perbaikan gaya before/after. |
| `learnings/` | **Arsip riwayat historis** (`editor-feedback.md` & `changelog.md`). **JANGAN dibaca saat sesi kerja normal** karena seluruh aturan aktifnya sudah dilebur ke file `00`–`11`. |

---

## 3. Struktur Folder Cerita (`story/`)

```text
story/
├── universe-registry.md  # Pendaftar semesta terpadu (bank premis, anti-duplikasi tokoh, cameo)
└── <Judul>/
    ├── canon.md          # Bible cerita: premis 5 slot, 7 cara tutup jalan mudah, kerangka, cast, dunia
    ├── state.md          # Potret kondisi aktif garis depan penulisan (dibaca sebelum & sesudah tulis bab)
    ├── outline.md        # Peta 30–40 bab (18 kolom per bab, terkunci v1.0 sebelum menulis Bab 1)
    ├── ledger.md         # Arsip kronologis fakta per bab
    ├── feedback.md       # Catatan revisi proyek
    └── chapters/
        ├── bab-01.md
        └── ...
```

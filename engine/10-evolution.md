# 10 — Evolusi Engine & Pembaruan Anti-AI Slop

> **File Pemilik Tunggal:** File ini mengatur **Cara Memperbarui Aturan di `engine/`, Aturan Satu Pemilik per Topik (Zero Duplication), dan Pemeliharaan Arsip `learnings/`**.

---

## 1. Aturan Satu Pemilik per Topik (Anti-Tumpang Tindih)

Agar AI tidak bingung oleh aturan yang tumpang tindih atau saling bertentangan, setiap aturan hanya boleh hidup di **satu file pemilik**:

| Topik Aturan | File Pemilik Tunggal |
|---|---|
| Alur sesi (Tahap A-G), Smart-Reading, & Definition of Done | `engine/00-workflow.md` |
| Genre MetroPop, skala masalah kelas menengah, & batasan 13+ | `engine/01-genre.md` |
| Premis, Rumus ABCD, 7 Cara Menutup Jalan Mudah, Uji *Spider-Man*, & Brainstorming 7 Langkah | `engine/02-premise.md` |
| 8 Kerangka Plot Terbukti, Siklus Coba-Gagal, Planting 2x, 16 Studi Kasus, & 18 Kolom Outline | `engine/03-structure.md` |
| Karakter, Psikologi, Disorder, Scene Stealer, & Matriks Sapaan | `engine/04-character.md` |
| Gaya Bahasa (Acuan *Resign!*), Anti-AI Slop Kalimat, & Teks Polos | `engine/05-style.md` |
| Kerajinan Bab (600-900 kata), Mesin Mikro Adegan, & 2 Tipe In Medias Res | `engine/06-chapter.md` |
| Kontinuitas (`canon.md`, `state.md`, `ledger.md`), Pre-Flight Gate, & Cameo | `engine/07-continuity.md` |
| Rubrik 8 Kriteria, 10 Uji Logika, 10 Tanda Bahaya, & 9 Uji Logika Mikro | `engine/08-quality.md` |
| Revisi 4 Lapis, Audit 5 Tahap, & Remediasi Beruntun R1-R5 | `engine/09-revision.md` |
| World Building & Aturan Dunia Nyata Indonesia | `engine/11-worldbuilding.md` |
| Hierarki Rujukan (Repo-First) & Riset Internet Anti-AI Slop | `engine/sources.md` |

**Larangan Duplikasi:** Jangan menyalin panjang lebar aturan dari satu file ke file lain. Cukup tulis aturan lengkap di file pemiliknya, dan file lain hanya menaut ke sana.

---

## 2. Kapan dan Bagaimana Mengubah Engine

Ubah file di `engine/` hanya jika:
1. Pengguna memberi koreksi atau preferensi baru yang berlaku lintas cerita.
2. Ditemukan celah logika atau halusinasi AI yang perlu ditutup dengan aturan baru.
3. Ada hasil riset baru (dari buku/dokumen pengguna atau riset internet tentang **cara menghindari halusinasi dan tulisan AI slop**) yang perlu diintegrasikan ke `05-style.md`, `08-quality.md`, atau `scripts/analyze-prose.py`.

### Langkah Pembaruan:
1. Langsung perbarui **file pemilik tunggal** di tabel atas (pastikan tidak ada kontradiksi dengan bagian lain di file yang sama).
2. Jika aturan baru bisa diperiksa secara otomatis (misal frasa *AI slop* baru), tambahkan ke `scripts/analyze-prose.py` atau `scripts/audit-continuity.py`.
3. Catat ringkasan perubahan (1-3 baris saja) di `engine/learnings/editor-feedback.md` dan `engine/learnings/changelog.md`.

---

## 3. Status Arsip `engine/learnings/` (Jangan Dibaca Saat Sesi Kerja Normal)

Folder `engine/learnings/` (`editor-feedback.md` dan `changelog.md`) adalah **arsip riwayat historis**.
- Seluruh aturan aktif dari `learnings/` **sudah dilebur** ke dalam file pemilik `00` sampai `11`.
- **AI DILARANG membaca `engine/learnings/` pada sesi kerja normal (Mode A, B, C, D)** agar jendela konteks AI tetap bersih dan fokus. File di `learnings/` hanya dibuka saat ingin mencatat log perubahan baru di Mode E.

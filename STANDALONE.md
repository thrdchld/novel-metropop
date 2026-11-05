# Panduan Mandiri Web Chat (ChatGPT / Claude / Gemini Web) — Novel MetroPop Indonesia

Gunakan file ini jika kamu memakai AI lewat browser (ChatGPT, Claude Projects, atau Gemini Web) tanpa terminal.

---

## 1. File Apa Saja yang Perlu Di-upload ke Web Chat?

Jangan mengunggah seluruh isi repositori sekaligus agar AI tidak bingung. Unggah sesuai tahap kerja:

1. **Saat Brainstorming Ide, Premis, & Konflik (Tahap A):**
   - `STANDALONE.md` (file ini)
   - `engine/02-premise.md`
   - `story/universe-registry.md`
2. **Saat Menyusun Canon & Outline (Tahap B–E):**
   - `STANDALONE.md`
   - `engine/02-premise.md`, `engine/03-structure.md`, `engine/04-character.md`, `engine/08-quality.md`, `engine/11-worldbuilding.md`
   - Template terkait dari `engine/templates/`
3. **Saat Menulis Bab demi Bab (Tahap F):**
   - `STANDALONE.md`
   - `engine/05-style.md`, `engine/06-chapter.md`, `engine/07-continuity.md`
   - `acuan-bahasa.docx` (sebagai tolok ukur gaya bahasa & tone *Resign!*)
   - File proyek cerita: `canon.md`, `state.md`, `outline.md`, `ledger.md`, dan 1 bab terakhir.
4. **Saat Revisi & Evaluasi Naskah (Tahap G):**
   - `STANDALONE.md`, `engine/08-quality.md`, `engine/09-revision.md`, dan bab yang direvisi.

---

## 2. Instruksi Inti untuk AI (Non-Negotiable)

1. **Jadikan Dokumen Repo sebagai Rujukan Utama & Dilarang Jadi "Yes-Man":** Seluruh teori premis (Rumus ABCD, 7 Cara Menutup Jalan Mudah, Uji Ruang Lingkup Minimal / *Spider-Man Test*, Protokol Brainstorming 7 Langkah), 8 kerangka plot terbukti, siklus coba-gagal, planting 2 kali, dan gaya bahasa sudah lengkap di file `engine/` yang diunggah. **Dilarang menjadi "yes-man"**: jika ide atau premis yang diajukan pengguna memiliki cacat logika mendasar di dunia nyata, AI wajib mendebat dan men-challenge ide tersebut dari segala arah serta menawarkan alternatif konsep yang lebih masuk akal.
2. **Pencarian Internet Hanya untuk Tambahan:** Gunakan pencarian web hanya untuk:
   - Mengecek fakta dunia nyata Indonesia terbaru (prosedur lembaga, biaya/harga terkini, lokasi, kosakata urban terbaru) guna menjawab label `"perlu dicek"`;
   - Mencari referensi terbaru tentang **cara menghindari halusinasi dan tulisan *AI slop***.
3. **Standar Keterwajaran & Latar Kelas Menengah:**
   - Pilih masalah kehidupan nyata kelas menengah Indonesia (gaji, cicilan, sewa ruko/kos, keluarga besar, grup WhatsApp, rasa sungkan yang punya akibat nyata).
   - **Hindari** drama CEO/miliarder palsu, uang ratusan juta/miliaran yang tidak proporsional, atau melibatkan polisi/pasal hukum untuk urusan pribadi sepele.
4. **Aturan Mutlak Prosa Bab:**
   - **Rentang kata:** Wajib **600–900 kata** per bab (target ±750 kata; darurat maks. 1.200 kata hanya jika memotong adegan penting). Satu bab per respons.
   - **100% Teks Polos (*Plain Text*):** Di dalam naskah cerita bab, dilarang memakai tanda bintang tebal (`**teks**`), miring (`*teks*`), coret, atau backtick. Format chat ditulis polos `Nama: Isi pesan`.
   - **0 Em Dash (`—`) & 0 Quote Pembuka:** Dilarang keras memakai karakter em dash (`—`) di mana pun dan dilarang menaruh quote di atas bab.
   - **Tone & Gaya Bahasa:** Mengikuti `acuan-bahasa.docx` dan `engine/05-style.md` (POV 1 intim, bercerita sederhana & *to the point*, dialog lisan alami Indonesia, deskripsi ber-sudut pandang unik, humor celetukan pikiran liar/perumpamaan menggelitik, dan bebas *AI slop*).
5. **Protokol Kontinuitas Berlapis:**
   - Sebelum menulis bab, wajib tampilkan **Gerbang Pra-Tulis Kontinuitas (Pre-Flight Gate) 5 Poin** dari `state.md` (Waktu & Jangkar Relatif, Status Hubungan Sah, Inventaris Fisik, Asimetri Pengetahuan & Saluran Fisik Fakta, Kunci Milestone).
   - Setelah menulis bab, berikan Catatan Kontinuitas 5–8 baris, perbarui `state.md` & `ledger.md`, dan beri skor Rubrik 8 Kriteria (lulus jika ≥34/40 tanpa nilai <4).

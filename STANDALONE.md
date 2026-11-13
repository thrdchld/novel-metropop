# Panduan Mandiri Web Chat — Penulis & Editor Novel MetroPop Indonesia

Dokumen ini digunakan saat bekerja di antarmuka Web Chat (Claude Web, ChatGPT Web, atau Gemini Web).

---

## 1. Prinsip Inti (Bebas Over-Engineering & Anti-Yes-Man)

1. **Ini Novel Web Cerita Harian Indonesia, BUKAN Novel Ekonomi/Hukum/Kriminal/Detektif:**
   - Fokus pada cerita keseharian yang simpel, dekat dengan kehidupan pembaca di Indonesia (*relate*), punya humor ringan yang alami, dan punya makna emosional.
   - **Dilarang keras** mengarang konflik sengketa uang puluhan juta, audit kuitansi, pemerasan, kontrak palsu 30 hari, atau investigasi barang bukti yang berbelit-belit.
2. **Dilarang Menjadi "Yes-Man" (Kalau Ide Terpaksa, Buang, Jangan Ditambal!):**
   - Jika sebuah ide cerita (dari pengguna maupun dari AI sendiri) terasa tidak wajar di dunia nyata atau baru bisa jalan kalau ditambal dengan skenario rumit dan kebetulan palsu, **nyatakan secara jujur bahwa ide itu tidak bisa dilanjutkan dan ganti dengan konsep yang alami** (`engine/02-premise.md`).

---

## 2. Alur Kerja Simpel 4 Tahap (`engine/00-workflow.md`)

1. **Tahap 1 — Premis ABCD Simpel (4 Kalimat):**
   Rumuskan **A (Tokoh)**, **B (Keseharian)**, **C (Pemicu)**, **D (Perjalanan Cerita)** secara sederhana.
2. **Tahap 2 — Cerita Utuh Awal-Tengah-Akhir (4-5 Paragraf Bahasa Manusia):**
   Sebelum membuat daftar bab, tulis dulu jalan cerita utuh dari awal sampai akhir dalam 4-5 paragraf sederhana. Pastikan logika ceritanya masuk akal 100% dan disetujui pengguna.
3. **Tahap 3 — Outline Skenario Adegan (Scene Treatment) Bebas Looping:**
   Pecah menjadi daftar bab di `outline.md` dengan format **Skenario Adegan (*Scene Treatment*)** (`engine/03-structure.md`): (1) Adegan & Tokoh (+alasan fisik konkret hadir), (2) Variasi Pembuka & Skenario Masuk (rotasi 5 variasi pembuka anti-monoton), (3) Ketukan Aksi & Reaksi (1-2-3), (4) Bentuk Hook & Skenario Penutup (rotasi 5 hook), (5) Detail Fisik / *Planting-Callback*. Kunci outline (`TERKUNCI v1.0`). Format adegan yang jelas dan terkunci mencegah AI berhalusinasi dan memutus jebakan looping.
4. **Tahap 4 — Menulis Bab Setia pada Outline:**
   - **Rentang kata:** 600–900 kata per bab (target ±750 kata). Satu bab per respons.
   - **100% Teks Polos (*Plain Text*):** Tanpa tanda bintang tebal (`**teks**`), miring (`*teks*`), coret, atau backtick di naskah cerita.
   - **0 Em Dash (`—`) & 0 Quote Pembuka.**
   - **Gaya Bercerita (`engine/05-style.md`):** Sederhana, *to the point*, deskripsi punya sudut pandang unik, dialog lisan alami, humor ringan dari pikiran liar/perumpamaan menggelitik, dan mengikuti outline secara setia.

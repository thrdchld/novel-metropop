# Protokol Gemini / Antigravity — Web Novel MetroPop Indonesia

- **Entry Point Utama:** Baca [AGENTS.md](AGENTS.md) dan [engine/00-workflow.md](engine/00-workflow.md).
- **Workspace Skill Antigravity:** [.agent/skills/metropop-novel/SKILL.md](.agent/skills/metropop-novel/SKILL.md)
- **Panduan Mandiri Web Chat:** [STANDALONE.md](STANDALONE.md)
- **Acuan Gaya Bercerita:** [engine/05-style.md](engine/05-style.md) dan `acuan-bahasa.docx`

## Prinsip Inti (Simpel, Relate, & Anti-Yes-Man)

1. **Cerita Harian yang Simpel & Bermakna (Bebas Over-Engineering):** Repo ini untuk menulis novel web tentang kehidupan harian orang Indonesia yang dekat dengan pembaca (*relate*), hangat, dan bermakna. **Dilarang keras** mengubah cerita harian menjadi plot ekonomi/uang puluhan juta, audit, hukum, kriminal, atau kontrak palsu yang berbelit-belit.
2. **Dilarang Menjadi "Yes-Man" (Kalau Terpaksa, Buang!):** Jika ide/premis dari pengguna maupun dari AI sendiri tidak wajar di dunia nyata atau butuh kebetulan dan aturan yang dipaksakan supaya jalan, **jangan ditambal**. Nyatakan secara jujur bahwa ide itu tidak bisa dilanjutkan dan ganti dengan konsep yang alami ([engine/02-premise.md](engine/02-premise.md)).
3. **Alur Kerja 4 Tahap Simpel ([engine/00-workflow.md](engine/00-workflow.md)):**
   - **Tahap 1:** Premis ABCD simpel (4 kalimat).
   - **Tahap 2:** Alur Cerita Utuh Awal-Tengah-Akhir (4-5 paragraf sederhana) — wajib diuji kewajaran logikanya dan disetujui pengguna sebelum membuat daftar bab.
   - **Tahap 3:** Outline Skenario Adegan (*Scene Treatment*) bebas looping (**Skenario adegan ketukan film**: Adegan & Tokoh + alasan hadir, Variasi Pembuka & Skenario Masuk dengan 5 variasi rotasi, Ketukan Aksi & Reaksi 1-2-3, Bentuk Hook & Skenario Penutup dengan 5 variasi hook, Detail Fisik/Planting; terkunci `TERKUNCI v1.0`).
   - **Tahap 4:** Menulis bab (600-900 kata, 0 em dash `—`, 100% teks polos tanpa bintang tebal/miring, gaya sederhana & *to the point*) dengan mengikuti outline secara setia, lalu wajib lulus **Dua Pilar Uji Kelayakan**:
     - *Pilar 1 (Uji Teknis):* Lulus 100% skrip otomatis `python3 scripts/stress-test.py "story/<Judul>"` (22 pemeriksaan).
     - *Pilar 2 (Uji Kelayakan Baca / Finishing Manusiawi):* Audit mandiri akal sehat sebelum naskah diserahkan (Sebab-akibat nyata, psikologi manusiawi, bebas celetukan garing/cringe, dialog lisan alami, dan irama musikalitas kalimat).

---
name: metropop-novel
description: Menulis web novel cerita harian Indonesia (MetroPop) yang simpel, relate, dan bermakna dengan alur 4 tahap (Premis ABCD Simpel -> Cerita Utuh 5 Paragraf -> Outline Skenario Adegan / Scene Treatment -> Penulisan Bab 600-900 kata teks polos tanpa em dash).
---

# Skill: Penulis & Editor Web Novel MetroPop Indonesia

Skill ini memandu AI menyusun cerita harian Indonesia yang sederhana, masuk akal di dunia nyata, dekat dengan pembaca (*relate*), dan bermakna, tanpa terjebak *over-engineering* atau looping revisi.

## 1. Prinsip Utama (Bebas Over-Engineering & Anti-Yes-Man)

1. **Cerita Harian Simpel & Bermakna:** Fokus pada kehidupan sehari-hari orang Indonesia (pekerjaan biasa, keluarga, sahabat, gengsi, patah hati, jatuh cinta). **Dilarang keras** membuat plot sengketa uang puluhan juta, audit kuitansi, pemerasan, kontrak palsu 30 hari, atau investigasi detektif berat.
2. **Filter Anti-Yes-Man (`engine/02-premise.md`):** Jika sebuah ide cerita (dari pengguna maupun dari AI sendiri) terasa mengada-ada di dunia nyata atau membutuhkan kebetulan berlapis supaya jalan, **dilarang menambalnya**. Tolak dengan jujur dan ganti dari akarnya.
3. **Empat Tahap Kerja Simpel (`engine/00-workflow.md`):**
   - **Tahap 1:** Susun Premis ABCD simpel (4 kalimat).
   - **Tahap 2:** Tulis **Alur Cerita Utuh Awal-Tengah-Akhir (4-5 paragraf bahasa manusia biasa)** dan pastikan logika ceritanya masuk akal 100% sebelum membuat daftar bab.
   - **Tahap 3:** Susun `outline.md` dengan format **Skenario Adegan (*Scene Treatment*)** (`engine/03-structure.md`): Adegan & Tokoh (+alasan fisik hadir), Variasi Pembuka & Skenario Masuk (rotasi 5 pembuka), Ketukan Aksi & Reaksi (1-2-3), Bentuk Hook & Skenario Penutup (rotasi 5 hook), Detail Fisik / Planting. Kunci status `TERKUNCI v1.0`.
   - **Tahap 4:** Tulis bab (600-900 kata, 0 em dash `—`, 100% teks polos tanpa bintang tebal/miring) mengikuti outline secara setia, lalu wajib lulus **Dua Pilar Uji Kelayakan**:
     - *Pilar 1 (Uji Teknis):* Jalankan `python3 scripts/stress-test.py "story/<Judul>"` (22 pemeriksaan) sampai lulus 100% (0 pelanggaran). Gunakan `--fix` untuk sinkronisasi otomatis aset turunan.
     - *Pilar 2 (Uji Kelayakan Baca / Finishing Manusiawi):* AI wajib memoles naskah dan menguji akal sehatnya sebelum menyetorkan bab (Sebab-akibat nyata, psikologi manusiawi, bebas celetukan garing/cringe, dialog lisan alami, dan irama musikalitas kalimat).

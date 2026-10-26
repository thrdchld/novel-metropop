# 09 — Revisi, Feedback, dan Diagnosis Alur Cerita

## 1. Langkah Awal

Saat user meminta revisi atau analisis naskah/cerita:
1. Tanyakan atau identifikasi: bab/bagian mana yang direvisi, apa masukannya, dan apakah revisi boleh mengubah canon/outline.
2. Jika user meminta **analisis atau evaluasi alur cerita secara menyeluruh**, jalankan **Prosedur Diagnosis Alur Cerita** di bagian 3 tanpa mengubah keputusan inti user.
3. Jangan langsung menulis ulang prosa sebelum masalah logika dan kerangka terpetakan.

---

## 2. Klasifikasi Feedback

| Jenis | Contoh | Tindakan |
|---|---|---|
| **Gaya & Bahasa** | "Terlalu baku", "berasa AI slop", "ada em dash", "dialog kaku" | Perbaiki di semua bab terdampak, catat aturan di `learnings/editor-feedback.md` |
| **Logika / Plot / Alur** | "Janggal", "alasan kurang to the point", "kenapa nggak jujur aja?" | Uji dengan **10 Uji Logika & 10 Tanda Bahaya**, buat Permintaan Perubahan, update canon/outline/ledger |
| **Preferensi Baru** | "Aku mau tone lebih getir", "hapus quote di atas bab" | Catat di `learnings/editor-feedback.md`, update file engine terkait, terapkan konsisten |
| **Fakta Canon** | "Umurnya 27, bukan 28" | Update canon dan ledger, cari semua kemunculan di bab lain |
| **Format & Panjang Kata** | Bab di bawah 600 kata, heading salah, chat tidak miring | Perbaiki mekanis dan perluas adegan hingga 600–900 kata |

---

## 3. Prosedur Diagnosis & Menilai Alur Cerita

Gunakan prosedur ini (berdasarkan `../Kerangka Plot yang Terbukti untuk Web Novel.md`) saat menilai draf novel atau outline:

1. **Uji Kelayakan Premis (5 Slot):**
   - Apakah keinginan vs kebutuhan tokoh sudah berbeda?
   - Apakah masalah dan tenggat waktu datang dari pihak luar?
   - Apakah konsekuensi gagal konkret dan terukur (bukan sekadar malu)?
   - Apakah 3 jalan keluar termudah sudah ditutup dengan alasan tertulis (tanpa membuat tokoh tampak bodoh)?
   - Apakah ada perubahan di akhir beserta harga nyata yang dibayar?
2. **Identifikasi Kerangka Plot & Hitungan Titik Balik:**
   - Petakan cerita ke salah satu dari **8 Kerangka Plot Terbukti** (`03-structure.md`).
   - Hitung jumlah titik balik: apakah mencapai minimal **6 titik balik** (30 bab) atau **8 titik balik** (40 bab)?
3. **Evaluasi Siklus Coba-Gagal di Bagian Tengah:**
   - Periksa apakah tiap percobaan memiliki 6 komponen (Tujuan, Alasan memilih, Cara, Hambatan dari watak/aturan dunia, Hasil, Akibat + momen canggung).
   - Jalankan **Uji 100%**: jika percobaan itu berhasil penuh, apakah masalah inti selesai? Jika tidak, tandai sebagai *filler* dan ganti.
4. **Evaluasi Planting Solusi Akhir:**
   - Periksa apakah bahan solusi akhir (orang, benda, kebiasaan, informasi) sudah ditanam **minimal dua kali** di Babak 1–2 (satu sepele, satu tampak seperti hiasan).
5. **Pindai 10 Tanda Bahaya (*Red Flags*):**
   - Cocokkan dengan tabel 10 Tanda Bahaya di `08-quality.md` (misal: tokoh bertindak konyol/tidak wajar demi plot, solusi jatuh dari langit, atau alasan tokoh terlalu klise).
   - Ambil perbaikan paling logis dan tulis alasannya dalam satu kalimat.

---

## 4. Revisi Lokal & Permintaan Perubahan

### Revisi Lokal
- Jangan menulis ulang satu bab penuh jika masalahnya hanya beberapa kalimat atau satu motivasi yang janggal.
- Perbaiki bagian yang bermasalah, jaga bagian yang sudah disetujui, dan pastikan transisi antarparagraf mulus.
- Pastikan panjang bab hasil revisi tetap berada di rentang **600–900 kata**.

### Permintaan Perubahan (Jika Mengubah Plot/Canon)
```markdown
# Permintaan Perubahan
1. **Masalah / Tanda Bahaya yang Ditemukan:** ...
2. **Usulan Perbaikan (Berdasarkan Kerangka & Uji Logika):** ...
3. **Bab Lain yang Terdampak:** ...
4. **Perlu Revisi Bab yang Sudah Ditulis?** ...
5. **Dampak pada Canon & Ledger:** ...
```

---

## 5. Cek Pasca-Revisi & Daftar Kritik Editor

### Cek Setelah Revisi
- Timeline, jam, dan lokasi konsisten;
- Siapa tahu apa tidak bocor;
- Setup/planting (2x) dan payoff terjaga;
- Panjang bab 600–900 kata, tanpa em dash (`—`), tanpa quote di atas bab;
- Hook akhir bab tetap tajam.

### Daftar Kritik Editor (Jangan Terulang)
1. Bahasa terlalu formal/baku dan tidak seperti obrolan sehari-hari orang Indonesia.
2. Deskripsi melodramatis atau kaku buatan mesin (*AI slop*).
3. Pemakaian em dash (`—`) di narasi atau dialog (dilarang keras di semua novel).
4. Pemakaian quote/epigraph di atas bab (dilarang agar tidak mencontek novel referensi).
5. Bab terlalu pendek di bawah 600 kata.
6. Tindakan atau motivasi tokoh janggal/klise dan tidak *to the point* sesuai karakter.
7. Jalan keluar mudah belum ditutup sehingga pembaca bertanya "kenapa nggak gini aja?".
8. Plot hole atau perubahan aturan mekanisme di tengah penulisan.

---
name: metropop-novel
description: Menulis dan merevisi web novel MetroPop Indonesia 30-40 bab, target 750 kata per bab, dengan 8 kerangka plot terbukti, canon, outline lock, Story Ledger, dan rubrik. Gunakan saat user ingin ide premis, project baru, lanjutkan cerita, revisi/evaluasi alur, atau analisis referensi.
metadata:
  icon: 📚
---

# Skill: MetroPop Novel

Baca `AGENTS.md` di root repo, lalu `engine/README.md` dan `engine/00-workflow.md`.
- Acuan utama gaya bahasa, diksi, dan cara bercerita: `acuan-bahasa.docx`.
- Acuan utama 8 kerangka plot terbukti, pembuatan/pengembangan premis, siklus coba-gagal, planting solusi 2 kali, dan penilaian alur cerita: `Kerangka Plot yang Terbukti untuk Web Novel.md`.
- Dokumen arsip ada di `old-documents-unneeded/`.

## Perilaku Wajib

- Mulai sesi dengan satu pertanyaan: ide baru, project baru, lanjutkan, revisi/evaluasi alur, atau riset.
- Jangan menulis prosa sebelum mode dipilih dan outline disetujui.
- Target pembaca 13+; latar dan usia tokoh bebas.
- Prinsip Pas: teknik/subplot/flashback/scene ikonik opsional, boleh nol.
- Satu bab per respons; batch hanya jika diminta.
- Setiap bab 600–900 kata, satu POV, satu adegan/beat, berakhir hook.
- Format: `## Bab N: Judul`, judul 2–5 kata, tanpa em dash (`—`), tanpa quote pembuka, bahasa percakapan alami perkotaan Indonesia, chat `**Nama:** *isi*`, email/surat miring, tanpa emoji.
- Bab 1 in medias res.
- Simpan bab ke `story/<Judul>/chapters/bab-NN.md`.
- Setelah bab: catatan kontinuitas, skor rubrik 8 kriteria (lulus ≥34/40 tanpa nilai <4),
  penyimpangan outline.
- Perbarui `state.md` dan `ledger.md`; jalankan `python3 scripts/audit-continuity.py`; jangan mengubah canon/outline diam-diam.
- Jika feedback berulang, perbarui `engine/learnings/` dan file panduan terkait.

## Mode

- **Ide:** gunakan Resep 9 Langkah & Uji 5 Slot; beri 3 opsi premis (judul, logline 1 kalimat, kerangka utama + pendamping, tema, tokoh, 5 slot kelayakan, planting solusi, humor).
- **Project baru:** 7 langkah pilih kerangka → canon (5 slot + planting 2x) & state awal → outline (siklus coba-gagal 6 komponen + min 6/8 titik balik) → stress test (10 uji logika makro + 7 uji logika mikro dunia nyata + 10 tanda bahaya) → lock → Bab 1.
- **Lanjut:** baca canon/state/outline/ledger/bab terakhir → Pre-Flight Continuity Gate (5 poin) → konfirmasi → bab baru (lulus 7 uji logika mikro) → sinkronisasi state.md & ledger.md.
- **Revisi & Evaluasi Alur:** diagnosis alur (Uji 5 Slot, Uji 100% Siklus, Planting 2x, 10 Uji Logika Makro, 7 Uji Logika Mikro Dunia Nyata, 10 Tanda Bahaya) → klasifikasikan feedback → revisi lokal → update canon/ledger → catat pelajaran.
- **Riset:** ekstrak prinsip dari PDF/teks/URL, jangan menyalin karya berhak cipta.

Detail ada di `engine/`.

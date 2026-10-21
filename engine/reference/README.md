# Referensi MetroPop

Folder ini berisi pengetahuan yang dipakai engine untuk merencanakan cerita. Engine tidak
membaca file ini saat runtime; isinya adalah acuan manusia dan agen saat menulis.

| File | Isi |
|---|---|
| `metropop-playbook.md` | Definisi genre, janji pembaca, suara, formula bab 750 kata. |
| `structure-30-40.md` | Tiga babak, lima fase, titik balik, peta bab untuk 30/35/40 bab. |
| `chapter-craft.md` | Kerajinan adegan, dialog, hook, kontinuitas, dan revisi. |
| `trope-bank.md` | Enam mesin premis, arketipe, latar, eskalasi, dan akhir. |
| `quality-checklist.md` | Daftar periksa dan rubrik penilaian. |
| `case-study-reply-all.md` | Analisis manuskrip referensi `../../referensi`. |

## Urutan Pakai

1. Baca `metropop-playbook.md` sebelum menyetujui premis.
2. Pakai `structure-30-40.md` untuk memeriksa peta babak.
3. Saat menulis bab, buka `chapter-craft.md`.
4. Sebelum menandai `done`, jalankan `quality-checklist.md`.
5. Jika ingin membuat mesin baru, tiru pola di `trope-bank.md`.

## Sumber

`../../referensi` adalah manuskrip contoh 10 bab plus blueprint 40 bab. Angka-angkanya
dianalisis di `case-study-reply-all.md` dan bisa direproduksi dengan:

```bash
bash engine/bin/metropop analyze referensi
```

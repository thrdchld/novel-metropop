# novel-metropop

Repositori untuk merencanakan dan menulis web novel **MetroPop**: drama urban Indonesia
dengan romansa, humor, dan kritik sosial ringan. Satu bab ±750 kata, minimal 30 bab.

## Dua Folder Utama

- **`engine/`** — mesin cerita: bank premis, planner, renderer, validator, CLI, dan
  panduan referensi. Engine membuat premis, karakter, bible, outline 30–50 bab, dan paket
  penulisan per bab.
- **`story/`** — hasil cerita. Satu cerita = satu folder sesuai judul, berisi
  `story.json`, `bible.md`, `outline.md`, dan `chapters/bab-XX.md`.

`referensi` di root adalah manuskrip contoh “Reply All” (blueprint 40 bab + 10 bab jadi)
yang menjadi studi kasus engine.

## Mulai Cepat

```bash
# lihat mesin premis
bash engine/bin/metropop engines

# buat cerita baru (40 bab, seed tetap)
bash engine/bin/metropop new "Salah Kirim" --engine salah-kirim --seed 42

# paket penulisan bab 1
bash engine/bin/metropop brief 1 --story "story/Salah Kirim"

# validasi dan progres
bash engine/bin/metropop check --story "story/Salah Kirim" --strict
bash engine/bin/metropop stats --story "story/Salah Kirim"
```

Di lingkungan yang tidak mengizinkan bit executable (mis. shared storage Android),
panggil wrapper lewat `bash` seperti contoh di atas. Alternatif:

```bash
cd engine
python3 -m metropop engines
```

## Batasan Cerita

- Genre: MetroPop (urban kontemporer, bukan fantasi/horor/sejarah).
- 30–50 bab; default 40.
- ±750 kata per bab; rentang 600–900; bab titik balik boleh 720–950.
- Satu POV per bab, satu adegan utama, satu hook di kalimat terakhir.
- Tiga babak: 25% setup, 50% eskalasi + midpoint + kejatuhan, 25% resolusi.

## Dokumentasi

- `engine/README.md` — perintah, struktur, cara kerja, menambah mesin.
- `engine/reference/metropop-playbook.md` — aturan genre dan formula bab.
- `engine/reference/structure-30-40.md` — peta babak dan beat.
- `engine/reference/chapter-craft.md` — kerajinan adegan, dialog, hook.
- `engine/reference/trope-bank.md` — enam mesin premis dan arketipe.
- `engine/reference/quality-checklist.md` — daftar periksa sebelum publikasi.
- `engine/reference/case-study-reply-all.md` — analisis manuskrip referensi.
- `story/README.md` — konvensi folder dan alur menulis.

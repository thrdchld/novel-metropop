# novel-metropop

Repositori untuk merencanakan dan menulis web novel **MetroPop**: drama urban Indonesia
dengan romansa, humor, dan kritik sosial ringan. Satu bab ±750 kata, **30–40 bab**.

**Acuan tertinggi:** [`Panduan Menulis Web Novel Metropop Indonesia.txt`](./Panduan%20Menulis%20Web%20Novel%20Metropop%20Indonesia.txt).
Engine, template, dan validator di repo ini mengikuti panduan tersebut. Ringkasan
operasionalnya ada di `engine/reference/panduan-utama.md`.

## Dua Folder Utama

- **`engine/`** — mesin cerita: bank premis, planner, character sheet, outline lock,
  Story Ledger, stress test, rubrik, validator, CLI, dan panduan referensi.
- **`story/`** — hasil cerita. Satu cerita = satu folder sesuai judul, berisi
  `story.json`, bible, outline, Ledger, stress test, rubrik, change request, dan
  `chapters/bab-XX.md`.

`referensi` di root adalah manuskrip contoh “Reply All” (blueprint 40 bab + 10 bab jadi)
yang menjadi studi kasus engine.

## Mulai Cepat

```bash
# 1. usul 3 premis
bash engine/bin/metropop ideas

# 2. buat cerita baru (30–40 bab)
bash engine/bin/metropop new "Salah Kirim" --engine salah-kirim --seed 42

# 3. isi stress test, lalu kunci outline
bash engine/bin/metropop stress --story "story/Salah Kirim"
bash engine/bin/metropop lock --story "story/Salah Kirim"

# 4. paket penulisan bab 1
bash engine/bin/metropop brief 1 --story "story/Salah Kirim"

# 5. validasi dan progres
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
- **30–40 bab**; default 40.
- ±750 kata per bab; rentang 600–900; titik balik 720–950.
- **Bab 1 wajib in medias res.**
- Judul bab 2–5 kata; heading `## Bab N: Judul`.
- Chat `**Nama:** *isi pesan*`; email/surat miring; tanpa emoji.
- Satu POV per bab, satu adegan/beat, satu hook di kalimat terakhir.
- Tiga babak: 25% setup, 50% eskalasi + midpoint + kejatuhan, 25% resolusi.
- Outline dikunci sebelum menulis; kontinuitas dijaga lewat `ledger.md`.

## Dokumentasi

- `engine/README.md` — perintah, struktur, cara kerja, menambah mesin.
- `engine/reference/panduan-utama.md` — ringkasan operasional panduan sumber.
- `engine/reference/metropop-playbook.md` — aturan genre dan formula bab.
- `engine/reference/structure-30-40.md` — peta babak dan beat.
- `engine/reference/chapter-craft.md` — kerajinan adegan, dialog, hook.
- `engine/reference/trope-bank.md` — enam mesin premis dan arketipe.
- `engine/reference/quality-checklist.md` — daftar periksa dan rubrik.
- `engine/reference/case-study-reply-all.md` — analisis manuskrip referensi.
- `story/README.md` — konvensi folder dan alur menulis.

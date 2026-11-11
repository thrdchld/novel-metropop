# Aturan Gatekeeper & Stress Test Terpadu (22 Pemeriksaan)

> **PENTING: DOKUMEN INI DIGENERATE SECARA OTOMATIS DARI `scripts/rules.json`. JANGAN DIEDIT MANUAL.**
> Untuk mengubah aturan, batasan, atau daftar kata terlarang, ubah file `scripts/rules.json` lalu jalankan:
> ```bash
> python3 scripts/stress-test.py --fix "story/<Judul Novel>"
> ```

---

## 1. Filosofi Gatekeeper Tunggal & Zero-Manual Checking

Repositori ini menerapkan prinsip **Single Source of Truth** (`scripts/rules.json`) dan **Zero-Manual Checking**.
Penulis atau AI dilarang keras mengklaim naskah/revisi selesai atau melakukan `git commit` sebelum perintah gatekeeper berikut mengembalikan hasil **100% LULUS**:

```bash
python3 scripts/stress-test.py "story/<Judul Novel>"
```

Jika terdapat ketidaksinkronan pada file turunan (`manuscript.md`, `reader.html`, `universe-registry.md`, atau `engine/12-stress-rules.md`), gunakan flag `--fix` untuk perbaikan otomatis:

```bash
python3 scripts/stress-test.py --fix "story/<Judul Novel>"
```

---

## 2. Parameter Kuantitatif Utama (`params`)

| Parameter | Nilai Batas | Keterangan |
|---|---|---|
| `word_min` | 600 kata | Batas minimum kata per bab (AGENTS.md 4.2) |
| `word_max` | 900 kata | Batas maksimum kata per bab (AGENTS.md 4.2) |
| `max_quote_words` | 20 kata | Batas panjang maksimum satu kutipan dialog lisan (engine/05-style.md 6) |
| `title_max_words` | 5 kata | Batas kata judul bab tanpa nama tokoh (engine/05-style.md 4) |
| `endq_max_pct` | 75% | Batas toleransi paragraf dialog berakhir kutipan (engine/05-style.md 5E) |
| `endq_min_dialogue_paras` | 4 | Minimal paragraf dialog agar EndQ dicek |
| `embodied_max` | 2x | Batas maksimum sebutan reaksi anatomi tubuh per bab (engine/05-style.md 5C) |
| `smell_max` | 2x | Batas maksimum kata penciuman/bau/aroma per bab (engine/05-style.md 5C) |
| `mono_min_run` | 3 kalimat | Batas deret kalimat berpanjang seragam (engine/05-style.md 5E) |
| `mono_tolerance` | 2 kata | Toleransi selisih panjang kalimat seragam |
| `mono_min_words` | 10 kata | Panjang kalimat minimum untuk perhitungan deret seragam |

---

## 3. Rincian 8 Pemeriksaan Sinkronisasi Aset & Dokumen

| No | Kunci | Pemeriksaan | Aturan & Mekanisme Validasi |
|---|---|---|---|
| 1 | `pillars` | Dokumen pilar & Character Sheet | canon.md, outline.md (TERKUNCI), state.md, ledger.md ada dan lengkap. |
| 2 | `numbering` | Penomoran & judul bab sinkron dengan outline | bab-NN.md berurutan tanpa lompat; header bab = judul di outline.md. |
| 3 | `ledger_state` | ledger.md & state.md sinkron dengan jumlah bab | ledger.md punya satu baris per bab; state.md menyebut bab terakhir yang benar. |
| 4 | `manuscript` | manuscript.md sinkron dengan bab | manuscript.md identik dengan gabungan seluruh bab. |
| 5 | `reader` | reader.html sinkron dengan bab | reader.html identik dengan hasil build-reader.py dari bab terkini. |
| 6 | `registry` | universe-registry.md sinkron | Jumlah bab dan total kata di registry sama dengan kenyataan. |
| 7 | `rules_doc` | Dokumen aturan sinkron dengan rules.json | engine/12-stress-rules.md identik dengan hasil generate dari rules.json; jumlah kategori yang disebut di AGENTS.md/workflow/SKILL benar. |
| 8 | `continuity` | Audit kontinuitas | audit-continuity.py melaporkan 0 isu. |

---

## 4. Rincian 14 Aturan Prosa, Struktur, & Dialog

| No | Kunci | Aturan | Definisi Validasi | Rujukan Engine |
|---|---|---|---|---|
| 9 | `word_range` | Rentang kata bab | Setiap bab 600-900 kata. | AGENTS.md 4.2; engine/06-chapter.md |
| 10 | `plain_text` | Teks polos 100% | 0 em dash, 0 simbol markup (* ` ~), header '## Bab N: Judul', tanpa quote pembuka. | engine/05-style.md 4 |
| 11 | `title_rule` | Aturan judul bab | Judul maksimal 5 kata dan tidak memuat nama tokoh (nama diambil otomatis dari canon.md). | engine/05-style.md 4 |
| 12 | `in_medias_res` | Pembuka In Medias Res | Bab dibuka dengan aksi/dialog, bukan laporan waktu/cuaca/suasana. | engine/05-style.md 5C |
| 13 | `long_quote` | Batas napas dialog | Satu kutipan dialog maksimal 20 kata. | engine/05-style.md 6 |
| 14 | `aykb_quote` | Anti eksposisi 'As You Know, Bob' | Dialog tidak menyebut ulang penanda waktu/riwayat yang sudah sama-sama diketahui (mis. 'enam bulan lalu'). | engine/05-style.md 6; engine/08-quality.md 2B.10 |
| 15 | `mixed_negation` | Register lisan konsisten | Dalam satu kutipan tidak boleh mencampur 'nggak/enggak' dengan 'tidak'. | engine/05-style.md 5D |
| 16 | `filter_words` | Tanpa kata filter persepsi | Dilarang: terasa, tampak, terlihat, seolah-olah, menyadari, menyaksikan. | engine/05-style.md 5D.5 |
| 17 | `stock_tells` | Tanpa gerakan klise | Dilarang: menghela napas, mengembuskan napas, mengepalkan tangan, rahang mengeras, menggigit bibir. | engine/05-style.md 5B.5 |
| 18 | `ai_syntax` | Tanpa sintaksis AI | Dilarang kalimat berawalan 'Sambil', klausa ', membuat', dan pembungkus abstrak (sebuah perasaan, ada rasa, dst). | engine/05-style.md 5D |
| 19 | `bookish_tags` | Tanpa tag dialog buku pelajaran | Dilarang: ujarnya, tuturnya, timpalnya, tukasnya, cetusnya, serunya, imbuhnya, tandasnya, kilahnya. | engine/05-style.md 5D |
| 20 | `slop_clinical` | Tanpa AI slop & jargon klinis | Frasa slop terjemahan harfiah dan istilah diagnosa psikologi dilarang. | engine/05-style.md 5, 5B.6 |
| 21 | `sensory_cap` | Batas anatomi & penciuman | Sensasi anatomi tubuh maksimal 2x dan bau/aroma maksimal 2x per bab. | engine/05-style.md 5C |
| 22 | `discourse_rhythm` | Variasi posisi dialog & ritme | Paragraf dialog berakhir kutipan maksimal 75% dan 0 deret >= 3 kalimat panjang seragam. | engine/05-style.md 5E |

---

## 5. Bank Pola Regex & Kata Terlarang (`patterns`)

### Pola `ai_slop` (13 pola)
```
arah jam sebelas, izin diberikan, kecilkan suaramu, papan tombol, sepeda kargo, penghangat kabin, menulis cek, atmosfer membeku, bak disambar petir, mengukir senyum, menyemburkan caci maki, janji suci, selempang cum laude melingkar
```

### Pola `clinical` (7 pola)
```
\btrauma\b, mekanisme pertahanan, hyper-independence, \bfatherless\b, \btoxic\b, \binsecure\b, \bhealing\b
```

### Pola `filter_words` (6 pola)
```
terasa, tampak, terlihat, seolah-olah, menyadari, menyaksikan
```

### Pola `stock_tells` (5 pola)
```
menghela napas, mengembuskan napas, mengepalkan tangan, rahang mengeras, menggigit bibir
```

### Pola `wrapper_nouns` (5 pola)
```
\bsebuah perasaan\b, \bada rasa\b, \bkeputusannya untuk\b, \bkesadaran itu\b, \bkehadirannya\b
```

### Pola `bookish_tags` (9 pola)
```
ujarnya, tuturnya, timpalnya, tukasnya, cetusnya, serunya, imbuhnya, tandasnya, kilahnya
```

### Pola `embodied` (8 pola)
```
dada(?:ku)?\s+sesak, tenggorokan(?:ku)?\s+tercekat, keringat\s+dingin, jantung(?:ku)?\s+berdegup, jantung(?:ku)?\s+mencelos, napas(?:ku)?\s+memburu, perut(?:ku)?\s+melilit, lutut(?:ku)?\s+lemas
```

### Pola `smell_words` (7 pola)
```
aroma, bau, baunya, wangi, wanginya, harum, harumnya
```

### Pola `human_causals` (6 pola)
```
soalnya, gara-gara, masalahnya, makanya, habisnya, lagian
```

### Pola `aykb_dialogue` (4 pola)
```
\b(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|beberapa)\s+(?:hari|minggu|bulan|tahun)\s+(?:yang\s+)?lalu\b, \b(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s+lalu\b, \bselama\s+(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan)\s+(?:hari|minggu|bulan|tahun)\b, \bsebagai\s+atasan\s+yang\s+sudah\b
```

### Pola `passive_opening` (5 pola)
```
^(?:pagi|siang|sore|malam)\s+itu\b, ^hari\s+(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s+(?:pagi|siang|sore|malam)\s+itu\b, ^(?:matahari|mentari|cahaya\s+lampu|sinar\s+matahari)\s+memantul\b, ^suasana\s+di\s+dalam\b, ^waktu\s+sudah\s+menunjukkan\b
```


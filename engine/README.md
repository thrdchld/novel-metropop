# Engine — Panduan Penulisan Novel MetroPop Indonesia (Simpel, Relate, & Bermakna)

Folder ini adalah panduan utama untuk merancang dan menulis web novel **MetroPop Indonesia** (cerita kehidupan harian orang Indonesia yang simpel, dekat dengan keseharian, punya logika manusia nyata yang wajar, dan bermakna).

---

## 1. Prinsip Utama (Bebas Over-Engineering & Anti-Yes-Man)

1. **Cerita Harian Simpel & Bermakna:** Fokus pada kehidupan sehari-hari orang Indonesia (pekerjaan biasa, pertemanan, keluarga, tetangga, patah hati, gengsi, jatuh cinta). **Dilarang keras** melakukan *over-engineering* dengan mengubah cerita harian menjadi plot ekonomi/uang puluhan juta, audit kuitansi, hukum, kriminal, atau kontrak perjanjian palsu yang berbelit-belit.
2. **Filter Anti-Yes-Man (Kalau Terpaksa, Buang!):** Jika sebuah ide cerita (baik dari pengguna maupun dari AI sendiri) tidak wajar di dunia nyata atau membutuhkan kebetulan berlapis dan skenario mengada-ada supaya jalan, **dilarang menambalnya**. AI wajib menyatakan secara jujur bahwa ide tersebut tidak bisa dilanjutkan dan harus diganti dari akarnya (`02-premise.md`).

---

## 2. Peta File di `engine/`

| File Pemilik | Isi & Tanggung Jawab Tunggal |
|---|---|
| `00-workflow.md` | Alur kerja simpel 4 tahap (Premis ABCD -> Cerita Utuh 5 Paragraf -> Outline Skenario Adegan -> Menulis Bab) & Smart-Reading. |
| `01-genre.md` | Definisi MetroPop Indonesia (cerita harian yang *relate* dan bermakna, batasan 13+). |
| `02-premise.md` | Rumus ABCD simpel, Filter Anti-Yes-Man (3 Uji Mati/Lanjut), & penyusunan Cerita Utuh Awal-Tengah-Akhir (4-5 paragraf). |
| `03-structure.md` | 8 Kerangka Plot Terbukti, *Invisible Planting & Callback*, & Format Outline Skenario Adegan (Scene Treatment: 5 Pembuka & 5 Hook). |
| `04-character.md` | Karakter, psikologi manusiawi, deskripsi ber-sudut pandang unik, *silent callback tells*, & matriks sapaan. |
| `05-style.md` | Gaya bercerita membumi & *to the point*, Zero-Majas, deskripsi konkret, humor situasi nyata, referensi modern, & aturan teks polos. |
| `06-chapter.md` | Kerajinan menulis bab (600-900 kata, satu adegan utuh yang mengalir alami). |
| `07-continuity.md` | Kontinuitas (`canon.md`, `state.md`, `ledger.md`). |
| `08-quality.md` | Uji kewajaran cerita & kualitas prosa. |
| `09-revision.md` | Panduan revisi. |
| `templates/` | Template simpel untuk `canon.md`, `outline.md` (format skenario adegan), `state.md`, dan `ledger.md`. |
| `learnings/` | Arsip lama (**JANGAN DIBACA**). |

---

## 3. Struktur Folder Cerita (`story/`)

```text
story/
├── universe-registry.md  # Pendaftar ide/premis (aktif, cadangan, atau ditolak) & daftar nama tokoh
└── <Judul>/
    ├── canon.md          # Profil tokoh, sapaan, dan latar utama
    ├── outline.md        # Cerita utuh 5 paragraf + rincian 4 poin per bab (TERKUNCI v1.0)
    ├── state.md          # Kondisi terkini cerita
    ├── ledger.md         # Catatan kronologis per bab
    └── chapters/
        ├── bab-01.md
        └── ...
```

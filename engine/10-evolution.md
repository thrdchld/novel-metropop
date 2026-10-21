# 10 — Evolusi Engine

Engine ini hidup. Agent boleh memperbaikinya, tetapi dengan aturan agar tidak menjadi
campur aduk.

## Kapan Mengubah Engine

Ubah hanya jika salah satu terjadi:

1. User memberi kritik yang sama **dua kali**.
2. User menyetujui teori/gaya baru.
3. Ada sumber baru (PDF/buku/artikel) yang mengubah cara menulis.
4. Ada bug instruksi yang membuat agent salah langkah.
5. Ada aturan yang terbukti tidak mungkin dipatuhi.

Jangan mengubah engine hanya karena satu adegan terasa sulit.

## Di Mana Menulis

| Perubahan | File |
|---|---|
| Kritik gaya berulang | `learnings/editor-feedback.md` + `05-style.md` |
| Aturan struktur | `03-structure.md` |
| Aturan karakter | `04-character.md` |
| Aturan bab | `06-chapter.md` |
| Aturan kontinuitas | `07-continuity.md` |
| Rubrik/kualitas | `08-quality.md` |
| Alur kerja | `00-workflow.md` |
| Sumber/riset | `sources.md` |
| Ringkasan perubahan | `learnings/changelog.md` |

## Format Catatan Feedback

```markdown
| Tanggal | Feedback | Aturan baru | File |
|---|---|---|---|
| 2026-10-21 | “Terlalu banyak analogi aneh” | Hindari perumpamaan yang tidak langsung masuk akal; pakai detail konkret. | 05-style.md |
```

Aturan harus:

- spesifik;
- bisa dicek;
- tidak bertentangan dengan panduan sumber;
- disertai contoh sebelum/sesudah jika perlu.

## Format Changelog

```markdown
## v1.1 — 2026-10-21
- **Perubahan:** ...
- **Alasan:** ...
- **File:** ...
- **Dampak:** bab baru / semua bab / hanya project tertentu.
```

## Prinsip Perubahan

- **Kecil.** Satu perubahan untuk satu masalah.
- **Bisa dipakai ulang.** Bukan aturan khusus satu adegan.
- **Tidak overfit.** Jangan mengubah aturan global karena satu cerita.
- **Tidak diam-diam.** Catat dan jelaskan.
- **Tidak menghapus canon project** tanpa persetujuan user.
- **Panduan sumber menang.** Jika bertentangan, perbaiki engine, bukan panduan.

## Promosi Aturan

Dari catatan ke aturan:

1. Catat di `learnings/editor-feedback.md`.
2. Jika berulang/disetujui, pindahkan ke file panduan.
3. Tambahkan contoh.
4. Catat di changelog.
5. Terapkan ke bab baru; bab lama hanya jika relevan.

## Menambah Sumber/Teori Baru

- Baca sumber, ringkas 5–10 poin.
- Pisahkan: prinsip yang bisa dipakai vs referensi gaya.
- Jangan menyalin teks berhak cipta.
- Tambahkan ke `sources.md` dengan tanggal dan tautan.
- Jika mengubah aturan, update file panduan + changelog.
- Jika hanya referensi, taruh di `sources.md` atau `examples/`.

## Menghapus Aturan

- Hapus hanya jika terbukti salah/berbahaya.
- Catat alasan di changelog.
- Cari semua file yang merujuk aturan itu.
- Ganti dengan aturan baru, bukan hanya menghapus.

## Review Berkala

Setiap 10 bab atau akhir project:

- baca `learnings/editor-feedback.md`;
- cek aturan yang sering dilanggar;
- cek aturan yang tidak pernah dipakai;
- ringkas changelog;
- tanyakan user apakah ada preferensi baru.

## Yang Tidak Boleh

- Mengubah `AGENTS.md` agar agent menulis lebih cepat dengan mengorbankan kualitas.
- Menghapus rubrik/kontinuitas karena “bikin lambat”.
- Menambah aturan yang tidak bisa dicek.
- Mengubah canon cerita lama tanpa izin.
- Menyalin karya berhak cipta ke engine.

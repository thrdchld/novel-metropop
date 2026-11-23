# HANDOFF
Diperbarui: 2026-11-23 09:20 WIB | Oleh: Gemini
Branch: fix-waktu-2
Tugas: Perbaikan kata waktu relatif di Narik Ojol dan Kita Tunggu Catnya Kering
Instruksi asli (salin UTUH dari pengguna):
Repo novel-metropop. git checkout main && git pull. Buat branch fix-waktu-2. Aturan: perubahan terkecil, teks polos, 0 em dash, satu commit per cerita, sinkronkan manuscript/outline/ledger/state/canon masing-masing, jalankan stress-test --fix dan build-reader.py per cerita, push. Jangan mengubah peristiwa atau urutan bab; hanya kata waktu relatif.

Sumber temuan: berkas validation/G3.md di branch audit/narik-ojol/G3 repo https://github.com/thrdchld/novel-editor (clone branch itu), bagian "8. Daftar Temuan Prioritas". VERIFIKASI dulu tiap temuan terhadap naskah (hari tiap bab dari penanda hari/jam), lalu perbaiki hanya yang memang keliru.

1. story/Narik Ojol Cinta Pun Nongol: FIND-G3-01 dan 02 (Bab 7 baris 39 dan 41), FIND-G3-03 (Bab 13 baris 15), FIND-G3-04 (Bab 15 baris 11), FIND-G3-05 (Bab 19 baris 15). Ganti "kemarin" dengan nama hari atau hitungan hari yang benar ("Jumat kemarin", "Jumat lalu", "hari Rabu kemarin", "tempo hari") sesuai saran di laporan. Abaikan FIND-G3-06 (opsional).
2. story/Kita Tunggu Catnya Kering Bab 6 baris 47: "bekas luka bakar kemarin" padahal insiden wajan terjadi Jumat malam dan adegan ini Minggu malam. Ganti menjadi "bekas luka bakar hari Jumat" atau "dua hari lalu". Periksa juga baris 15 di bab yang sama ("Bukannya kemarin pihak dinas minta spanduk vinil...") dan perbaiki jika keliru. Jika kamu memutuskan salah satunya sudah benar, tulis alasannya di laporan.

Laporan akhir: hash commit + hasil stress-test per cerita + daftar kata yang diubah + "sudah push". Merge ke main (--ff-only) hanya jika stress-test dan scripts/audit-continuity.py tidak menunjukkan masalah baru.

Daftar langkah:
- [ ] 1. Setup branch fix-waktu-2, inisialisasi HANDOFF.md, commit dan push
- [ ] 2. Ambil dan baca berkas validation/G3.md dari branch audit/narik-ojol/G3
- [ ] 3. Verifikasi & perbaiki story/Narik Ojol Cinta Pun Nongol (FIND-G3-01 s.d. 05)
- [ ] 4. Sinkronisasi aset, stress-test --fix, build-reader.py, commit cerita 1, push
- [ ] 5. Verifikasi & perbaiki story/Kita Tunggu Catnya Kering (Bab 6 baris 47 dan baris 15)
- [ ] 6. Sinkronisasi aset, stress-test --fix, build-reader.py, commit cerita 2, push
- [ ] 7. Jalankan audit-continuity.py & verifikasi akhir
- [ ] 8. Merge ke main (--ff-only), push main, perbarui HANDOFF.md menjadi TIDAK ADA TUGAS AKTIF

Sedang dikerjakan: Langkah 1 - Setup branch dan HANDOFF.md
Working tree: bersih
Keputusan penting dan alasan:
Sudah diverifikasi, jangan diulang:
Langkah berikutnya (persis, satu per satu):
1. Commit HANDOFF.md dan push branch fix-waktu-2
2. Fetch/ambil validation/G3.md dari repo novel-editor branch audit/narik-ojol/G3
Masalah/blocker:

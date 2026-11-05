# Laporan Audit & Remediasi Menyeluruh — <Judul Cerita>

> **Dokumen Acuan:** `engine/09-revision.md`  
> **Status:** <DRAFT AUDIT / DALAM REMEDIASI / TERVERIFIKASI PENUH>  
> **Tanggal Audit:** YYYY-MM-DD  
> **Versi Naskah:** v...

---

## 1. Ringkasan Status 5 Tahap Audit

| Tahap Audit | Fokus Area | Status (PASS / WARN / FAIL) | Jumlah Temuan |
|---|---|---|---:|
| **Tahap 1: Fondasi Canon & World Building** | Premis 5 slot, aturan hukum RI, daya beli uang, klausul kontrak | ... | ... |
| **Tahap 2: Arsitektur Outline & Plot Makro** | 8 Kerangka, titik balik, siklus coba-gagal Uji 100%, planting 2x | ... | ... |
| **Tahap 3: Integritas Kontinuitas & State** | Jangkar waktu, status hubungan, log fakta fisik mikro, milestone lock | ... | ... |
| **Tahap 4: Anatomi Adegan & Mesin Mikro Bab** | 600-900 kata, tujuan-rintangan-hasil, geser emosi, hook akhir | ... | ... |
| **Tahap 5: Kualitas Prosa, Dialog, & Bahasa** | 4-Pass Prosa, 0 em dash, 0 quote, anti-AI slop, 2 indera lokal | ... | ... |

---

## 2. Matriks Diagnostik Cacat (*The Defect Matrix*)

| ID Cacat | Tingkat (1-5) | Dokumen / Bab Terdampak | Deskripsi Cacat (Kondisi Saat Ini vs Seharusnya) | Derajat Keparahan (Critical / Major / Minor) | Usulan Solusi Terstruktur |
|---|---|---|---|---|---|
| D-01 | Tingkat ... | ... | ... | ... | ... |
| D-02 | Tingkat ... | ... | ... | ... | ... |

---

## 3. Rencana Eksekusi Remediasi Berurutan (*Cascading Remediation Plan*)

### Jangkauan Bab Terdampak (*Impacted Scope*)
- **Bab Awal:** Bab ...
- **Bab Akhir:** Bab ...
- **Bab di Luar Jangkauan:** DILARANG DIUBAH (Steril).

### Urutan Tindakan (Top-Down):
1. **Langkah R1 (Fondasi Canon):** ...
2. **Langkah R2 (Arsitektur Outline):** ...
3. **Langkah R3 (Sinkronisasi State Machine & Ledger):** ...
4. **Langkah R4 (Eksekusi Revisi Lokal Prosa Bab):** ...
5. **Langkah R5 (Verifikasi Regresi Otomatis):** ...

---

## 4. Log Eksekusi Perbaikan

| Dokumen / Bab | Bagian yang Berubah | Tindakan (Ganti / Hapus / Tambah) | Alasan Perubahan |
|---|---|---|---|
| `canon.md` | ... | Ganti / Tambah | ... |
| `outline.md` | ... | Ganti | ... |
| `state.md` | ... | Update log fakta mikro | ... |
| `bab-NN.md` | Paragraf ... | Ganti (74/18/8) | ... |

---

## 5. Hasil Verifikasi Akhir (*Zero-Regression Gate*)

1. **Audit Kontinuitas Skrip (`scripts/audit-continuity.py`):**
   - Hasil: `[PASS] 0 Issues` / Catatan: ...
2. **Analisis Prosa Mekanis (`scripts/analyze-prose.py`):**
   - Rentang Kata: ... kata (Wajib 600-900; darurat maks. 1.200).
   - Em Dash (`—`): **0** (Lolos).
   - Frasa AI Slop: **0** (Lolos).
3. **Uji Sambungan Bab Depan-Belakang (*Boundary Seam Test*):**
   - Sambungan Bab N-1 -> Bab N: Mulus / Terverifikasi.
   - Sambungan Bab M -> Bab M+1: Mulus / Terverifikasi.

**Keputusan Akhir:** [DITERIMA / PERLU PERBAIKAN ULANG]
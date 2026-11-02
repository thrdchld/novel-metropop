# novel-metropop

Repositori untuk menulis web novel **MetroPop Indonesia** bersama AI agent: 30-40 bab,
±750 kata per bab, target pembaca **13+**, latar dan usia tokoh bebas. Dilengkapi canon,
outline terkunci, Story Ledger, matriks sapaan, dan rubrik kualitas.

**Prinsip Pas:** teknik naratif, subplot, flashback, dan scene ikonik adalah alat
opsional. Boleh nol jika cerita sudah padat. Jangan memaksakan.

Repo ini mengusung pendekatan **Agent-First dengan Wasit Mekanis Python**. Otak naratif dan panduan penulisan tersimpan dalam paket Markdown di `engine/`, sedangkan modul di `scripts/` adalah linter Python otomatis untuk menjamin presisi logika, kebersihan tanda baca, dan kontinuitas naskah.

---

## 1. Peran Python dalam Repo Ini: Penjinak Halusinasi AI

AI (Large Language Model) sangat kreatif dalam menulis dialog emosional dan dinamika cerita, tetapi memiliki kelemahan alami (bersifat probabilistik):
- AI sering salah menghitung jumlah kata persis per bab;
- AI sering mengalami *bias konfirmasi* (mengaku tidak ada em dash padahal masih terselip);
- AI mudah amnesia pada fakta lintas 24-40 bab (misal kata "kemarin" yang merujuk hari yang salah, atau status hubungan yang melompat prematur).

Di repo ini, **Python bertindak sebagai Wasit Mekanis / Linter Deterministik**:
1. `scripts/audit-continuity.py`: Memindai seluruh bab untuk memastikan 3 dokumen pilar ada, memverifikasi klaim waktu relatif ("kemarin", "semalam"), label status hubungan, perkenalan tokoh, nominal uang, dan kunci milestone.
2. `scripts/analyze-prose.py`: Menganalisis panjang kata riil, mendeteksi 0 em dash (`—`), menyapu bersih frasa AI slop, memantau rasio dialog di akhir paragraf, dan mendeteksi deretan kalimat berurutan yang panjangnya seragam.
3. `scripts/combine-chapters.sh`: Menggabungkan seluruh bab terpisah menjadi satu naskah utuh `manuscript.md` secara instan dan rapi.

Skrip Python ini **berjalan otomatis di balik layar** saat kamu menggunakan AI agent berbasis terminal (seperti Antigravity CLI, Cursor, atau VS Code). Kamu juga bisa menjalankannya sendiri secara manual di terminal kapan saja.

---

## 2. Prasyarat Sistem (*Requirements*)

Skrip pendukung dirancang **sangat ringan dan mandiri (Zero External Dependencies)**:
- **Python 3.8 atau lebih baru** (Python 3.10/3.11/3.12 sangat direkomendasikan).
- **Hanya menggunakan Standard Library Python bawaan** (`re`, `sys`, `pathlib`, `collections`, `statistics`, `argparse`).
- **TIDAK BUTUH `pip install` paket eksternal.** Tidak perlu virtual environment yang memakan ruang penyimpanan.
- **Git & Bash** (opsional untuk version control dan script penggabung naskah).

---

## 3. Panduan Instalasi & Eksekusi di Berbagai Platform

### A. Android (Termux)
Jika kamu menulis langsung di perangkat Android menggunakan aplikasi Termux:

1. **Buka Termux**, perbarui paket dan instal Git serta Python:
   ```bash
   pkg update -y && pkg upgrade -y
   pkg install -y git python
   ```
2. **Berikan izin akses penyimpanan internal** (jika repo disimpan di folder Download):
   ```bash
   termux-setup-storage
   ```
3. **Masuk ke direktori repositori:**
   ```bash
   cd ~/storage/downloads/projects/novel-metropop
   # atau path folder tempat kamu menyimpan repo ini
   ```
4. **Jalankan audit linter:**
   ```bash
   # Audit kontinuitas cerita:
   python scripts/audit-continuity.py "story/Narik Ojol Cinta Pun Nongol"

   # Audit prosa per bab:
   python scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol/chapters/bab-01.md"

   # Audit prosa seluruh bab:
   python scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol"
   ```

---

### B. Linux (Ubuntu, Debian, Fedora, Arch, dll.)

1. **Buka Terminal**, pastikan Git dan Python 3 terpasang:
   - *Ubuntu / Debian:*
     ```bash
     sudo apt update && sudo apt install -y git python3
     ```
   - *Fedora:*
     ```bash
     sudo dnf install -y git python3
     ```
   - *Arch Linux:*
     ```bash
     sudo pacman -S --noconfirm git python
     ```
2. **Masuk ke folder repositori:**
   ```bash
   cd /path/to/novel-metropop
   ```
3. **Jalankan audit linter:**
   ```bash
   # Audit kontinuitas:
   python3 scripts/audit-continuity.py "story/Narik Ojol Cinta Pun Nongol"

   # Analisis mekanis prosa:
   python3 scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol"
   ```
4. **Gabungkan naskah bab menjadi satu manuskrip utuh (opsional):**
   ```bash
   bash scripts/combine-chapters.sh "story/Narik Ojol Cinta Pun Nongol"
   ```

---

### C. Windows (PowerShell, Command Prompt, Git Bash, atau WSL)

#### Opsi 1: Menggunakan PowerShell / CMD (Bawaan Windows)
1. **Instal Python:** Unduh dari [python.org](https://www.python.org/) atau instal via winget:
   ```powershell
   winget install Python.Python.3.12
   ```
   > **Penting saat instal manual:** Pastikan kamu mencentang kotak **"Add python.exe to PATH"** di halaman awal instalasi!
2. **Buka PowerShell atau CMD**, lalu masuk ke folder project:
   ```powershell
   cd C:\path\to\novel-metropop
   ```
3. **Jalankan audit linter:**
   ```powershell
   # Audit kontinuitas antarbab:
   python scripts\audit-continuity.py "story\Narik Ojol Cinta Pun Nongol"

   # Analisis prosa novel:
   python scripts\analyze-prose.py "story\Narik Ojol Cinta Pun Nongol"
   ```

#### Opsi 2: Menggunakan Git Bash atau WSL (Linux di Windows)
Jika kamu memakai Git for Windows (Git Bash) atau Windows Subsystem for Linux (WSL), kamu bisa menggunakan sintaks Linux standar:
```bash
python3 scripts/audit-continuity.py "story/Narik Ojol Cinta Pun Nongol"
python3 scripts/analyze-prose.py "story/Narik Ojol Cinta Pun Nongol"
bash scripts/combine-chapters.sh "story/Narik Ojol Cinta Pun Nongol"
```

---

## 4. Penggunaan di Web AI Tanpa Terminal (ChatGPT / Claude / Gemini Web)

Jika kamu menggunakan repositori ini di web browser biasa (seperti ChatGPT Plus/Custom GPT, Claude.ai Projects, atau Google AI Studio / Gems) tanpa akses ke terminal:
- **Repositori ini tetap 100% berfungsi.**
- Semua panduan kerangka, batasan konten, gaya bahasa, dan matriks sapaan tersimpan dalam format Markdown murni.
- Kamu cukup mengunggah file skill mandiri:
  - `GEMINI_SKILL.md` untuk Gemini / Google AI Studio.
  - `CLAUDE_SKILL.md` untuk Claude Projects.
  - `CHATGPT_SKILL.md` untuk ChatGPT Custom GPT.
- Dalam mode web murni ini, verifikasi kontinuitas dan penghitungan kata dilakukan secara interaktif lewat percakapan instruksi prompt dengan AI.

---

## 5. Struktur Berkas Repositori

```text
AGENTS.md              # Protokol utama agent penulis
GEMINI.md              # Pointer protokol Gemini / Antigravity
GEMINI_SKILL.md        # Skill mandiri all-in-one untuk Gemini / Gems
CLAUDE.md              # Pointer protokol Claude
CLAUDE_SKILL.md        # Skill mandiri all-in-one untuk Claude Projects
CHATGPT_SKILL.md       # Skill mandiri all-in-one untuk ChatGPT / Custom GPT
.agent/skills/         # Workspace skill Antigravity CLI (metropop-novel)
engine/                # Otak panduan penulisan (workflow, world building, struktur, audit)
scripts/               # Wasit mekanis Python (audit-continuity, analyze-prose, combine)
story/                 # Folder naskah novel (canon, state, outline, ledger, chapters)
acuan-bahasa.docx      # Acuan utama gaya bahasa, diksi, dan cara bercerita
panduan-pengembangan-premis-cerita.md # Acuan utama arsitektur premis fiksi (3 pilar, M.I.C.E., 3P Sanderson)
Kerangka Plot yang Terbukti untuk Web Novel.md # Acuan utama 8 kerangka plot terbukti
```

---

## 6. Mode Kerja Agen

- **Mode A: Ide / Premis Baru** - Konsultasi Universe Registry (`story/universe-registry.md`), anti-penawaran ulang ide ditolak, roster tokoh & semesta bersama, 3 opsi premis (3 Pilar Premis, M.I.C.E., 3 Tingkat Taruhan, Uji 5 Slot).
- **Mode B: Project Baru** - Alur A-G lengkap: premis -> canon & world building -> outline -> stress test -> lock -> Bab 1.
- **Mode C: Lanjutkan Cerita** - Pre-Flight Continuity Gate (5 poin) -> tulis 1 bab (600-900 kata) -> sync state.md + ledger.md -> verifikasi linter.
- **Mode D: Revisi, Evaluasi, & Remediasi Beruntun** - Standar Audit 5 Tahap & Remediasi Beruntun R1-R5 (`engine/12-audit-remediation.md`) tanpa merusak bab sebelumnya.
- **Mode E: Analisis Riset & Referensi** - Ekstraksi prinsip dari referensi eksternal tanpa melanggar hak cipta.

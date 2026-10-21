# Changelog Engine

Catat setiap perubahan aturan, template, atau sumber. Perubahan kecil, spesifik, dan
disertai alasan.

## v1.1 — 2026-10-21

- **Perubahan:** Migrasi penuh ke agent-first. `engine/` sekarang berisi markdown;
  engine Python lama dihapus dari working tree.
- **Alasan:** Workflow utama adalah agent menulis lewat percakapan, bukan CLI.
- **Dampak:** Project baru memakai `AGENTS.md`, `engine/00-workflow.md`, dan template
  canon/outline/ledger/chapters.

## v1.0 — YYYY-MM-DD

- **Perubahan:** Paket agent-first dibuat.
- **Isi:** `AGENTS.md`, `engine/` (workflow, genre, premis, struktur, karakter, gaya,
  bab, kontinuitas, kualitas, revisi, evolusi), templates, examples, learnings.
- **Alasan:** Workflow agentic butuh instruksi markdown, bukan CLI Python.
- **Dampak:** Project baru memakai format canon/outline/ledger/chapters.

## Template Entri

```markdown
## v1.1 — YYYY-MM-DD
- **Perubahan:** ...
- **Alasan:** ...
- **File:** ...
- **Dampak:** bab baru / semua bab / hanya project tertentu.
```

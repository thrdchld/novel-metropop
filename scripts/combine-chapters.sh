#!/usr/bin/env bash
# Script Penggabung Naskah Otomatis — Novel MetroPop Indonesia
# Menggabungkan seluruh file story/<Judul>/chapters/bab-*.md menjadi satu file utuh
# story/<Judul>/manuscript.md beserta laporan jumlah kata per bab.

set -euo pipefail

STORY_DIR="${1:-}"

if [ -z "$STORY_DIR" ]; then
  echo "Cara pakai: bash scripts/combine-chapters.sh \"story/<Judul Novel>\""
  echo ""
  echo "Daftar cerita yang tersedia di story/:"
  find story -mindepth 1 -maxdepth 1 -type d 2>/dev/null || echo "  (Belum ada folder cerita)"
  exit 1
fi

if [ ! -d "$STORY_DIR/chapters" ]; then
  echo "Error: Folder '$STORY_DIR/chapters' tidak ditemukan."
  exit 1
fi

TITLE="$(basename "$STORY_DIR")"
OUT_MD="$STORY_DIR/manuscript.md"

echo "# $TITLE" > "$OUT_MD"
echo "" >> "$OUT_MD"

TOTAL_WORDS=0
CHAPTER_COUNT=0

printf "%-15s | %-10s | %s\n" "File Bab" "Kata" "Status Rentang (600-900 / Darurat <=1200)"
printf -- "----------------+------------+-------------------------------------------\n"

for ch in "$STORY_DIR/chapters"/bab-*.md; do
  [ -e "$ch" ] || continue
  CHAPTER_COUNT=$((CHAPTER_COUNT + 1))
  WORDS=$(wc -w < "$ch" | tr -d ' ')
  TOTAL_WORDS=$((TOTAL_WORDS + WORDS))

  STATUS="OK (Standar 600-900)"
  if [ "$WORDS" -lt 600 ]; then
    STATUS="PERINGATAN: < 600 kata"
  elif [ "$WORDS" -gt 1200 ]; then
    STATUS="PERINGATAN: > 1200 kata"
  elif [ "$WORDS" -gt 900 ]; then
    STATUS="OK (Darurat 901-1200)"
  fi

  printf "%-15s | %-10s | %s\n" "$(basename "$ch")" "$WORDS" "$STATUS"

  cat "$ch" >> "$OUT_MD"
  echo "" >> "$OUT_MD"
  echo "---" >> "$OUT_MD"
  echo "" >> "$OUT_MD"
done

printf -- "----------------+------------+-------------------------------------------\n"
echo "Total Bab   : $CHAPTER_COUNT bab"
echo "Total Kata  : $TOTAL_WORDS kata"
echo "File Naskah : $OUT_MD"

if command -v pandoc >/dev/null 2>&1; then
  OUT_DOCX="$STORY_DIR/manuscript.docx"
  pandoc "$OUT_MD" -o "$OUT_DOCX"
  echo "File DOCX   : $OUT_DOCX (berhasil dibuat dengan pandoc)"
fi

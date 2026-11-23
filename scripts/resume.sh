#!/usr/bin/env bash
set -u
echo "=== REPO: $(basename "$(git rev-parse --show-toplevel)")"
git fetch --quiet origin 2>/dev/null || echo "(fetch gagal/offline)"
echo "Branch: $(git rev-parse --abbrev-ref HEAD)"
echo "--- 8 commit terakhir"; git log --oneline -8
echo "--- Perubahan belum di-commit"
S=$(git status --short)
if [ -z "$S" ]; then echo "(bersih)"; else echo "$S"; echo "!!! WORKING TREE KOTOR: jangan reset/checkout/clean. Baca git diff dulu."; fi
echo "--- Commit lokal belum di-push"; git log --oneline @{u}..HEAD 2>/dev/null || echo "(tidak ada upstream)"
echo "--- Commit di remote yang belum ada di lokal"; git log --oneline HEAD..@{u} 2>/dev/null || true
echo "--- 5 branch remote terbaru"; git for-each-ref --sort=-committerdate --count=5 --format='%(refname:short) %(committerdate:relative)' refs/remotes/origin
echo "=== HANDOFF.md"
if [ -f HANDOFF.md ]; then sed -n 1,120p HANDOFF.md; else echo "(tidak ada HANDOFF.md)"; fi

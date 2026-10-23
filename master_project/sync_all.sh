#!/usr/bin/env bash
# =====================================================================
#       CROSS-REGIME DUAL-REPOSYSTEM SYNCHRONIZATION BLUEPRINT
# =====================================================================
# Automates both local index staging and remote cloud file updates.
# =====================================================================

PROJECT_DIR="/home/lab-user/master_project"
cd "$PROJECT_DIR" || exit 1

echo "[*] [$(date '+%H:%M:%S')] Starting both local and remote project sync..."

# 1. Update Local Repository Filesystem Indexes
echo "[+] Indexing local data tracks..."
git add .

# Define an automated timestamp token for the commit record
COMMIT_MSG="Automated Cross-Regime Synchronization Loop: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MSG"

# 2. Update Remote Repository Filesystem Indexes (GitHub)
echo "[+] Uploading codebase configuration up to GitHub main branch..."
git push origin main

if [ $? -eq 0 ]; then
    echo "[*] Both systems successfully updated and locked. Repositories aligned."
else
    echo "[-] Remote synchronization encountered an exception. Check connection parameters."
fi

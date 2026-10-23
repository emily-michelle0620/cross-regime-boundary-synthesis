#!/usr/bin/env bash
# =====================================================================
#         REPOSITORY AUTO-COMPILATION & REPO UPLOAD BLUEPRINT
# =====================================================================

echo "[*] Initializing repository matrix configurations..."

# Initialize the local tracking index tree
git init

# Configure core tracking exceptions
cat << 'EOF' > .gitignore
__pycache__/
*.pyc
*.flag
*.log
.DS_Store
EOF

# Organize all loose asset scripts into their proper folder blocks
mkdir -p src docs
[ -f optical_illusion_matrix_GUI.py ] && mv optical_illusion_matrix_GUI.py src/
[ -f Thermal_Watcher.py ] && mv Thermal_Watcher.py src/

# Stage, index, and commit all localized files
git add .
git commit -m "System integration: Merged GUI hardware pipelines and structured documentation packages"

# Branch configuration and secure server sync setup
git branch -M main

echo ""
echo "====================================================================="
echo "💥 GITHUB REPOSITORY DEPLOYMENT REFRESH INSTRUCTIONS"
echo "====================================================================="
echo "To upload your project cleanly, run the final two terminal steps:"
echo "  1) git remote add origin https://github.com"
echo "  2) git push -u origin main"
echo "====================================================================="

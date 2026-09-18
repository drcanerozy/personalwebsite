#!/bin/zsh

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# Load environment variables (such as GEMINI_API_KEY) from user zsh profile
if [ -f "$HOME/.zshrc" ]; then
    source "$HOME/.zshrc" 2>/dev/null || true
fi

VAULT_DIR="/Users/canerozyildirim/Library/Mobile Documents/iCloud~md~obsidian/Documents/caner"
cd "$VAULT_DIR" || exit 1

echo "==========================================" >> "$VAULT_DIR/00 Kontrol Merkezi/Digests/scout_runner.log"
echo "Starting Nutrition Scout at $(date)" >> "$VAULT_DIR/00 Kontrol Merkezi/Digests/scout_runner.log"
echo "==========================================" >> "$VAULT_DIR/00 Kontrol Merkezi/Digests/scout_runner.log"

/usr/bin/python3 "$VAULT_DIR/AI Kontrol Merkezi/Otomasyon & Scriptler/nutrition_scout.py" >> "$VAULT_DIR/00 Kontrol Merkezi/Digests/scout_runner.log" 2>&1

EXIT_CODE=$?
echo "Nutrition Scout finished with exit code $EXIT_CODE at $(date)" >> "$VAULT_DIR/00 Kontrol Merkezi/Digests/scout_runner.log"
echo "" >> "$VAULT_DIR/00 Kontrol Merkezi/Digests/scout_runner.log"

exit $EXIT_CODE

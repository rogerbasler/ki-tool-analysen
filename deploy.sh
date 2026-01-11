#!/bin/bash

# ============================================================================
# Automatisches Deployment-Skript für wöchentliche KI-Tool-Analysen
# Version: 1.0
# Autor: Manus AI
# Datum: 11.01.2026
# ============================================================================

set -e  # Exit on error

# ============================================================================
# PARAMETER
# ============================================================================

if [ "$#" -ne 2 ]; then
    echo "❌ Fehler: Falsche Anzahl von Parametern"
    echo "Usage: ./deploy.sh <KW> <DATUM>"
    echo "Beispiel: ./deploy.sh 02 2026-01-11"
    exit 1
fi

KW=$1
DATUM=$2
JAHR=$(echo $DATUM | cut -d'-' -f1)

# Berechne vorherige KW
PREV_KW=$(printf "%02d" $((10#$KW - 1)))

echo "🚀 Starte Deployment für KW $KW/$JAHR (Datum: $DATUM)"
echo "=================================================="

# ============================================================================
# SCHRITT 1: GITHUB CLI STATUS PRÜFEN
# ============================================================================

echo ""
echo "📋 Schritt 1/7: GitHub CLI Status prüfen..."

if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) ist nicht installiert!"
    echo "Installation: sudo apt-get install gh"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "❌ GitHub CLI ist nicht authentifiziert!"
    echo "Bitte führe aus: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI ist authentifiziert"

# ============================================================================
# SCHRITT 2: REPOSITORY KLONEN
# ============================================================================

echo ""
echo "📋 Schritt 2/7: Repository klonen..."

REPO_DIR="/tmp/ki-tool-analysen-deploy-$$"

if [ -d "$REPO_DIR" ]; then
    rm -rf "$REPO_DIR"
fi

gh repo clone rogerbasler/ki-tool-analysen "$REPO_DIR"
cd "$REPO_DIR"

echo "✅ Repository geklont nach $REPO_DIR"

# ============================================================================
# SCHRITT 3: DATEIEN VORBEREITEN
# ============================================================================

echo ""
echo "📋 Schritt 3/7: Dateien vorbereiten..."

# Prüfe ob neue index.html existiert
if [ ! -f "/home/ubuntu/new_index.html" ]; then
    echo "❌ Fehler: /home/ubuntu/new_index.html nicht gefunden!"
    exit 1
fi

# Prüfe ob Markdown-Analyse existiert
if [ ! -f "/home/ubuntu/wochenanalyse-kw${KW}-${JAHR}.md" ]; then
    echo "❌ Fehler: /home/ubuntu/wochenanalyse-kw${KW}-${JAHR}.md nicht gefunden!"
    exit 1
fi

echo "✅ Alle erforderlichen Dateien gefunden"

# ============================================================================
# SCHRITT 4: AKTUELLE INDEX.HTML ARCHIVIEREN
# ============================================================================

echo ""
echo "📋 Schritt 4/7: Aktuelle index.html archivieren..."

# Erstelle Archiv-Verzeichnis falls nicht vorhanden
mkdir -p "archiv/${JAHR}"

# Archiviere aktuelle index.html
if [ -f "index.html" ]; then
    ARCHIVE_NAME="kw${PREV_KW}-${DATUM}.html"
    cp index.html "archiv/${JAHR}/${ARCHIVE_NAME}"
    echo "✅ index.html archiviert als archiv/${JAHR}/${ARCHIVE_NAME}"
else
    echo "⚠️  Warnung: Keine index.html zum Archivieren gefunden"
fi

# ============================================================================
# SCHRITT 5: NEUE DATEIEN KOPIEREN
# ============================================================================

echo ""
echo "📋 Schritt 5/7: Neue Dateien kopieren..."

# Kopiere neue index.html
cp /home/ubuntu/new_index.html index.html
echo "✅ Neue index.html kopiert"

# Kopiere Markdown-Analyse
cp "/home/ubuntu/wochenanalyse-kw${KW}-${JAHR}.md" .
echo "✅ wochenanalyse-kw${KW}-${JAHR}.md kopiert"

# ============================================================================
# SCHRITT 6: GIT COMMIT & PUSH
# ============================================================================

echo ""
echo "📋 Schritt 6/7: Git Commit & Push..."

# Git-Benutzer konfigurieren
git config user.email "manus@ai.agent"
git config user.name "Manus AI"

# Änderungen stagen
git add .

# Prüfe ob es Änderungen gibt
if git diff --staged --quiet; then
    echo "⚠️  Keine Änderungen zum Committen"
    exit 0
fi

# Commit
git commit -m "Update: Wöchentliche KI-Tool-Analyse KW ${KW}/${JAHR}

- Neue Homepage mit 5 Tools
- Markdown-Analyse KW ${KW}/${JAHR}
- Archivierung KW ${PREV_KW}/${JAHR}
- Automatisches Deployment via deploy.sh"

echo "✅ Commit erstellt"

# Push
git push origin master

echo "✅ Push zu GitHub erfolgreich"

# ============================================================================
# SCHRITT 7: GITHUB PAGES DEPLOYMENT ABWARTEN
# ============================================================================

echo ""
echo "📋 Schritt 7/7: Warte auf GitHub Pages Deployment..."

echo "⏳ Warte 90 Sekunden..."
sleep 90

echo "✅ Deployment sollte abgeschlossen sein"

# ============================================================================
# CLEANUP
# ============================================================================

echo ""
echo "🧹 Cleanup..."
cd /home/ubuntu
rm -rf "$REPO_DIR"
echo "✅ Temporäres Repository gelöscht"

# ============================================================================
# ERFOLGSMELDUNG
# ============================================================================

echo ""
echo "=================================================="
echo "🎉 DEPLOYMENT ERFOLGREICH ABGESCHLOSSEN!"
echo "=================================================="
echo ""
echo "📊 Details:"
echo "   KW: $KW/$JAHR"
echo "   Datum: $DATUM"
echo "   Commit: Wöchentliche KI-Tool-Analyse KW ${KW}/${JAHR}"
echo ""
echo "🔗 Website:"
echo "   https://rogerbasler.github.io/ki-tool-analysen/"
echo ""
echo "✅ Nächste Schritte:"
echo "   1. Besuche die Website und überprüfe das Update"
echo "   2. Teste das Archiv: https://rogerbasler.github.io/ki-tool-analysen/archiv.html"
echo "   3. Verifiziere, dass alle 5 Tools korrekt dargestellt werden"
echo ""
echo "=================================================="

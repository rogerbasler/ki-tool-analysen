# Playbook: Wöchentliche KI-Tool-Analyse

**Version:** 3.0 (Updated 11.01.2026)  
**Autor:** Manus AI  
**Zweck:** Systematische wöchentliche Analyse der Top 5 neuen KI-Tools mit **optimiertem Git-CLI-Deployment**.

---

## 🎯 Ziel

Erstelle jede Woche eine fundierte Analyse der 5 interessantesten neuen KI-Tools und aktualisiere die Website effizient über Git CLI.

---

## 📋 Prozess-Übersicht

### Phase 1: Recherche (10 Quellen)
### Phase 2: Tool-Auswahl (Top 5)
### Phase 3: Tiefenanalyse
### Phase 4: Markdown-Analyse erstellen
### Phase 5: HTML-Generierung mit Template
### Phase 6: **Optimiertes Git-CLI-Deployment** 🚀

---

## 🚀 Phase 6: Optimiertes Git-CLI-Deployment

Dieser Workflow ersetzt den alten, fehleranfälligen Prozess. Er ist schneller, zuverlässiger und vollständig über die Kommandozeile steuerbar.

### ⚠️ Voraussetzungen

- **GitHub CLI ist bereits authentifiziert.** Der `GH_TOKEN` ist im System hinterlegt.
- **KEIN manueller Browser-Login** erforderlich.

### 6.1 Deployment-Vorbereitung

Stelle sicher, dass folgende Dateien bereitstehen:
- `/home/ubuntu/new_index.html` (Generiert in Phase 5)
- `/home/ubuntu/wochenanalyse-kw{XX}-{YYYY}.md` (Erstellt in Phase 4)
- `/home/ubuntu/archiv_previous.html` (Die `index.html` der Vorwoche)

### 6.2 Automatisches Deployment-Skript (EMPFOHLEN)

Führe das `deploy.sh` Skript aus, um den gesamten Prozess zu automatisieren.

```bash
# Beispiel für KW 02, 2026
./deploy.sh 02 2026-01-11
```

Das Skript führt alle folgenden Schritte automatisch aus.

### 6.3 Manueller Git-CLI-Workflow

Falls das Skript fehlschlägt, führe diese Schritte manuell aus:

#### Schritt 1: GitHub-Status prüfen (5 Sek.)
```bash
# Verifiziert, dass du bei github.com angemeldet bist
gh auth status
```

#### Schritt 2: Repository klonen (10 Sek.)
```bash
# Lösche altes Repo, falls vorhanden, und klone frisch
rm -rf ki-tool-analysen-repo
gh repo clone rogerbasler/ki-tool-analysen ki-tool-analysen-repo
cd ki-tool-analysen-repo
```

#### Schritt 3: Dateien aktualisieren (5 Sek.)
```bash
# 1. Aktuelle index.html ins Archiv verschieben
mv index.html archiv/2026/kw01-2026-01-04.html # Beispiel für KW01

# 2. Neue index.html kopieren
cp /home/ubuntu/new_index.html index.html

# 3. Neue Markdown-Analyse kopieren
cp /home/ubuntu/wochenanalyse-kw02-2026.md .
```

#### Schritt 4: Git Commit & Push (15 Sek.)
```bash
# Git-Benutzer konfigurieren
git config user.email "manus@ai.agent"
git config user.name "Manus AI"

# Änderungen stagen
git add .

# Commit mit aussagekräftiger Nachricht
git commit -m "Update: Wöchentliche KI-Tool-Analyse KW 02/2026"

# Zum GitHub-Repository pushen
git push origin master
```

### 6.4 Verifizierung

1.  **Warte 90 Sekunden**, bis GitHub Pages das Deployment abgeschlossen hat.
2.  Besuche https://rogerbasler.github.io/ki-tool-analysen/ mit einem Cache-Buster (`?v=timestamp`).
3.  Überprüfe, ob die neue Kalenderwoche und die neuen Tools angezeigt werden.

---

## 🐛 Troubleshooting (NEU)

### Problem: `gh` Befehl nicht gefunden
**Ursache:** GitHub CLI ist nicht korrekt installiert.  
**Lösung:** `sudo apt-get install gh`

### Problem: `Permission denied` beim Pushen
**Ursache:** Der `GH_TOKEN` ist abgelaufen oder hat keine `repo` Berechtigungen.  
**Lösung:** Neuen Token unter https://github.com/settings/tokens erstellen und im System hinterlegen.

### Problem: Website aktualisiert sich nicht
**Ursache:** GitHub Pages Build ist fehlgeschlagen oder dauert länger.  
**Lösung:**
1.  Überprüfe den Build-Status unter `Repository -> Actions`.
2.  Warte weitere 2-3 Minuten.
3.  Leere den Browser-Cache oder verwende einen Inkognito-Tab.

---

## 📚 Ressourcen (Aktualisiert)

- `deploy.sh` - **NEUES** automatisiertes Deployment-Skript
- `PLAYBOOK_V3.md` - Dieses Dokument

---

## ✅ Checkliste für jede Woche (Aktualisiert)

- [ ] Phase 1-4: Recherche & Analyse abgeschlossen
- [ ] Phase 5: HTML mit Template generiert
- [ ] Phase 6: **Deployment via `deploy.sh` Skript oder Git CLI** 🚀
- [ ] Verifizierung: Live-Website geprüft

---

**Version History:**
- v1.0 (28.12.2025): Initial Playbook
- v2.0 (04.01.2026): Hinzugefügt: HTML-Template-Prozess
- **v3.0 (11.01.2026): Hinzugefügt: Optimierter Git-CLI-Workflow, Deployment-Skript, neues Troubleshooting**

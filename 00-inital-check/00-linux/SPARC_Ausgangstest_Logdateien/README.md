# SPARC – Ausgangstest: Linux-Logsuche

Szenario:
Auf einem kleinen Serversystem treten sporadisch Probleme auf. Untersuche die
Logdateien und finde auffällige Einträge.

## Aufgaben:
1. Verschaffe dir rekursiv einen Überblick über alle Dateien und Unterordner.
   ```bash
   find .
   ```
2. Finde alle Zeilen, die das Wort "error" enthalten – unabhängig von
   Gross-/Kleinschreibung.
   ```bash
   grep "error" . -ir
   ```
3. Gib dabei Dateiname und Zeilennummer aus.
   ```bash
   grep "error" . -irnH
   ```
4. Suche zusätzlich nach "failed", "denied" und "timeout".
   ```bash
   grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH
   ```
5. Ermittle, welche Datei die meisten auffälligen Einträge enthält.
   ```bash
   grep -e "error" -e "failed" -e "denied" -e "timeout" . -irEc | sort -t : -k2 -nr | head -n 1
   ```
6. Speichere deine Ergebnisse in einer Datei namens ergebnis.txt.
   ```
   grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH > ergebnis.txt
   ```

## Bonus:
- Suche nur in Dateien mit der Endung .log.
  ```
  grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH --include="*.log"
  ```
- Schliesse archivierte Logs vom Suchlauf aus.
  ```bash
  grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH --exclude-dir="archive"
  ```
- Zähle die Treffer pro Datei.
  ```bash
  grep -e "error" -e "failed" -e "denied" -e "timeout" . -irEc
  ```

## Hinweis:
Versuche die Aufgaben möglichst mit Standardwerkzeugen wie find, grep, sort,
uniq, wc, head, tail und less zu lösen.

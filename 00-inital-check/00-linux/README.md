# SPARC – Initial Test: Linux Log Search

Scenario:
Sporadic issues occur on a small server system. Investigate the
log files and find suspicious entries.

## Tasks:
1. Get a recursive overview of all files and subfolders.
   ```bash
   find .
   ```
2. Find all lines that contain the word "error" – regardless of
   upper/lower case.
   ```bash
   grep "error" . -ir
   ```
3. Also output the file name and line number.
   ```bash
   grep "error" . -irnH
   ```
4. Additionally search for "failed", "denied", and "timeout".
   ```bash
   grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH
   ```
5. Determine which file contains the most suspicious entries.
   ```bash
   grep -e "error" -e "failed" -e "denied" -e "timeout" . -irEc | sort -t : -k2 -nr | head -n 1
   ```
6. Save your results to a file named ergebnis.txt.
   ```
   grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH > ergebnis.txt
   ```

## Bonus:
- Search only in files with the .log extension.
  ```
  grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH --include="*.log"
  ```
- Exclude archived logs from the search.
  ```bash
  grep -e "error" -e "failed" -e "denied" -e "timeout" . -irnH --exclude-dir="archive"
  ```
- Count the hits per file.
  ```bash
  grep -e "error" -e "failed" -e "denied" -e "timeout" . -irEc
  ```

## Note:
Try to solve the tasks as much as possible using standard tools like find, grep, sort,
uniq, wc, head, tail, and less.

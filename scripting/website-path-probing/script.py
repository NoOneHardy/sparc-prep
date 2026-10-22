import subprocess
import sys


def get_page():
  default = "https://mail.no1hardy.ch/"
  arg = sys.argv[1] # [0] is the script name

  if (arg == None or arg == ""):
    return default

  if arg.endswith("/"):
    return  arg

  return arg + "/"


page = get_page()

urls = []

with open("common-paths.txt") as f:
    for line in f:
        url = page + line.rstrip("\n")
        print(f"Trying {url}")
        # -i to include headers
        # -s to execute silently
        status: str = subprocess.run(["bash", "-c", 'curl -is --max-time 2 -X GET "$0" | grep HTTP | cut -d" " -f 2', url], capture_output=True, text=True).stdout
        if status.startswith("4") or status.startswith("5") or status is None or status == "":
            continue

        urls.append(f"{url:<40}\t{status}")

print("\n\n")
print("---------- Results ----------")
print("\n")

for url in urls:
    print(url)

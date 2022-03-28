import time
import os
import sys
import glob
import argparse


print("""
Hello Felix_P! -| v1.1 |- FireLies 2022 -> https://github.com/FireLies/Felix_P
\nUsage: py felix.py [--type <list>] [(opt) --path <str>]""")

parser = argparse.ArgumentParser()
parser.add_argument(
    "--type",
    nargs="*",
    type=str,
    default=[]
)

parser.add_argument(
    "--path",
    nargs=1,
    type=str,
    default=[os.path.expanduser('~\\Documents')]
)

args = parser.parse_args()

# Checking user input
#--------------------------------------------------------------
RawPath = str(*args.path)
args.type = list(dict.fromkeys(args.type))
with open('.\\Misc\\Valid_Extensions.txt', 'r') as valid:
    ValidType = valid.read().split("\n")

if os.path.exists(RawPath) == False:
    print("\n--Cannot find path:", RawPath, "\n")
    sys.exit(0)

if not args.type:
    print("\n[--type] argumment required, at least 1 value. Usage: py felix.py --type <list>\n")
    sys.exit(0)

CheckType = [i for i in args.type if i not in ValidType]
if CheckType:
    args.type = [i for i in args.type if i not in CheckType]
    print("\n--Invalid file type:", ', '.join(CheckType), "\n\nValid file type:", ', '.join(ValidType))
    if len(args.type) == 0:
        print()
        sys.exit(0)
#--------------------------------------------------------------

stw_Start = time.time()
removed, failed = 0, 0

for ext in args.type:
    print(f"\n--Trying: {ext} in {RawPath}\...")
    check_File = glob.glob(RawPath + "\\**\\*" + ext, recursive=True)
    for files in check_File:
        with open(files, 'w') as content:
            content.write("")

        if os.path.getsize(files) > 0:
            print(f"[-] {files}")
            failed += 1
        print(f"[*] {files}")
        removed += 1

    if len(check_File) == 0:
        print(f"--Cannot find {ext} file(s)")

stw_Result = str(round((time.time() - stw_Start) * 1000, 3))
print(f"\n--Removed in {stw_Result} ms. Total: {removed + failed} | Success: {removed} | Failed: {failed}\n")
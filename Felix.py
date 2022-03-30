import time
import os
import sys
import glob
import argparse


print("""\nHello Felix_P! -| v1.2 |- FireLies 2022 -> https://github.com/FireLies/Felix_P
\nUsage: py felix.py [(opt) -r] [--type <list>] [(opt) --path <str>]""")

parser = argparse.ArgumentParser()
parser.add_argument("-r", nargs='?', const=True, default=False)
parser.add_argument("--type", nargs='*', type=str, default=[])
parser.add_argument("--path", nargs=1, type=str, default=[os.path.expanduser('~\\Documents')])
args = parser.parse_args()

# Checking user input
#--------------------------------------------------------------
RawPath = str(*args.path)
args.type = list(dict.fromkeys(args.type))
with open('.\\Misc\\Valid_Extensions.txt', 'r') as valid:
    ValidType = valid.read().split("\n")

if not args.type:
    print("\n--Warning: [--type] is required. At least one value given. Usage: py felix.py --type <list>\n--Example: py felix.py --type .txt, .jpg\n")
    sys.exit(0)

CheckType = [i for i in args.type if i not in ValidType]
if CheckType:
    args.type = [i for i in args.type if i not in CheckType]
    print("\n--Invalid file type:", ', '.join(CheckType), "\n--TIP: Open .\Misc\Valid_Extensions.txt to see all valid file types")
    if len(args.type) == 0:
        print()
        sys.exit(0)

if args.r not in [True, False]:
    print("\n--Warning: [-r] doesn't accept any value\n--Example: py felix.py -r --type .txt, .jpg\n")
    sys.exit(0)

if os.path.exists(RawPath) == False:
    print("\n--Cannot find path:", RawPath, "\n")
    sys.exit(0)
#--------------------------------------------------------------

stw_Start = time.time()
removed, failed = 0, 0

for ext in args.type:
    print(f"\n--Trying: {ext} in {RawPath}")
    CheckFile = glob.glob(RawPath + "\\**\\*" + ext, recursive=args.r)
    for counter, files in enumerate(CheckFile, start=1):
        with open(files, 'w') as content:
            content.write("")

        if os.path.getsize(files) > 0:
            print(f"  . {files}")
            failed += 1
        removed += 1

    if len(CheckFile) == 0:
        counter = 0
    print(f"--Found: {counter}")

stw_Result = str(round((time.time() - stw_Start) * 1000, 3))
print(f"\n--Finished in: {stw_Result} ms | File(s): {removed + failed} | Removed: {removed} | Failed: {failed}\n")
import os
import sys
import glob
import argparse


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

raw_Path = str(*args.path)
with open('.\\Misc\\Valid_Extensions.txt', 'r') as valid:
    ValidType = valid.read().split("\n")

# Checking user input
#--------------------------------------------------------------
if os.path.exists(raw_Path) == False:
    print("\n--Cannot find path:", raw_Path, "\n")
    sys.exit(0)

if not args.type:
    print("\n[--type] argumment cannot be empty.\n")
    sys.exit(0)

check_Type = [_ for _ in args.type if _ not in ValidType]
if check_Type:
    print("\n--Invalid file type:", ', '.join(check_Type))
    for i in check_Type:
        args.type.remove(i)
    print("\nValid file type:", ''.join(ValidType))
#--------------------------------------------------------------

removed, failed = 0, 0
for ext in args.type:
    print(f"\n--Trying: {ext} in {raw_Path}\...")
    check_File = glob.glob(raw_Path + "\\**\\*" + ext, recursive=True)

    for files in check_File:
        with open(files, "w") as content:
            content.write("")

        if os.path.getsize(files) > 0:
            print(f"[-] {files}")
            failed += 1
        print(f"[*] {files}")
        removed += 1

    if len(check_File) == 0:
        print(f"--Cannot find {ext} file(s)")

print(f"\nSuccess: {removed}  //  Failed: {failed}\n")

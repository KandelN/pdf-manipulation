# Input programm for pdf manipulation programs
# Incomplete

import os
from os.path import isdir, isfile, join
import pyperclip
import sys

fpath = pyperclip.paste()
if isdir(fpath):
    print("Path obtained from clipboard successfully.")
else:
    print("Using default path.")
    fpath = join(os.getcwd(), "resources")

print(f"Working directory: {fpath}")

onlyfiles = [ f for f in os.listdir(fpath) if isfile(join(fpath, f))]
if len(onlyfiles) == 0:
    sys.exit("No pdf in working directory")    
print("Index\tName\n-----\t----")
for i, f in enumerate(onlyfiles):
    print(i,f,sep = "\t")

in_num = input("Enter index of file:")
if in_num <= len(onlyfiles):
    pdf_path = join(fpath, onlyfiles[in_num-1])
else:
    pdf_path = join(fpath, )
# file_name = "cv_notes.pdf"


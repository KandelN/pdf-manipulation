#converts images into a single pdf file

import img2pdf
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import re
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python img_to_pdf.py [foldername]")
else:
    foldername = sys.argv[1]

#reading image files
files = glob.glob(f"{foldername}/*.jpg")
files = sorted(files, key=lambda x:int(re.findall(r"(\d+)",x)[0]))

print(files)
#convert into pdf
with open(f"{foldername}.pdf", "wb") as f:
    f.write(img2pdf.convert(files, dpi = 150, x = None, y = None))

#specify pdfs
input_pdf = PdfFileReader(f"{foldername}.pdf")
output_pdf = PdfFileWriter()

#add cover page
cover = PdfFileReader(f"header.pdf")
output_pdf.addPage(cover.pages[0])

#rotation
for page in input_pdf.pages:
    page.rotateClockwise(90)

    output_pdf.addPage(page)

with open(f"{foldername}.pdf", mode = "wb") as output_file:
    output_pdf.write(output_file)

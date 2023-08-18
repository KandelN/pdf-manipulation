# transforms protrait into landscapes 
# can be modified to turn landscape pages into portrait
# can be modified for selecting rotating too.
# KandelN

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python rotate_pages.py [filename]")

filename = sys.argv[1]

input_file = PdfFileReader(filename)
output_file = PdfFileWriter()

for i, page in enumerate(input_file.pages):
    x1, y1, x2, y2 = page.mediaBox  

    #turn protrait into landscape
    # if y2 > x2:
    #     print(f"Page {i} Rotated")
    #     page.rotateCounterClockwise(90)
        
    #selective rotation:(file specific)
    for pg in [6, 11, 40, 41, 47]:
        if i == pg - 1:
            print("Page {i} Flipped")
            page.rotateClockwise(180)

    output_file.addPage(page)

out_filename = f"{filename[:-4]}_rotated.pdf"
with open(out_filename, mode= "wb") as op_f:
    output_file.write(op_f)

print(f"Saved as {out_filename}")

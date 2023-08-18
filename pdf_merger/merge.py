# Merges pdfs in the given folder
# from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfMerger
from pathlib import Path
import sys

def merge_from_folder(foldername):
    # Make a list of path to pdf fragments
    pdfs_dir = Path.cwd() / foldername
    fragments = [str(path) for path in pdfs_dir.glob("*.pdf")]
    fragments.sort()
    for i in fragments:
        print(i)
    totals = len(fragments)
    # return 0 if folder contains no pdfs.
    if totals == 0:
        return 0

    # Create a new instance of PdfFileMerger
    #  and append all fragments.
    # pdf_merger = PdfFileMerger()
    pdf_merger = PdfMerger()

    for fragment in fragments:
        try:
            pdf_merger.append(fragment)
        except:
            print("Not Merged:", fragment)

    # Write the merged pdf to an output file.
    out_path = Path.cwd() / str(foldername + "_combined.pdf")
    with out_path.open(mode = "wb") as output_file:
        pdf_merger.write(output_file)
    
    return totals

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python merge.py [source foldername]")
    else:
        folder = sys.argv[1]
        count = merge_from_folder(folder)
        print(f"Merged {count} pdf files as '{folder}_combined.pdf'")
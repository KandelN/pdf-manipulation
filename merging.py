# Merging and concatenating pdfs
# First concatenate ex13 and 3x811
# Merge ex47 after 3 pages of formed pdf.
# -------------------------------------- #
from PyPDF2 import PdfFileMerger
from pathlib import Path

# Make a list of path to pdf fragments
pdfs_dir = (
    Path.cwd()
    / "resources"
    / "cv fragments"
)
fragments = [str(path) for path in pdfs_dir.glob("*.pdf")]
fragments.sort()

# Create a new instance of PdfFileMerger Class.
pdf_merger = PdfFileMerger()

# First concatenate ex13 and 3x811
pdf_merger.append(fragments[0])
pdf_merger.append(fragments[2])

# Now Merge ex47 after first 3 pages.
pdf_merger.merge(3, fragments[1])

# Write the merged pdf to an output file.
out_path = (
    Path.cwd()
    / "outputs"
    / "cv_merged.pdf"
)
with out_path.open(mode = "wb") as output_file:
    pdf_merger.write(output_file)

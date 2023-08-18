from PyPDF2 import PdfFileReader as PFR
import sys

def text_extractor(pdf_name):
    # Path of the pdf
    pdf_path = f"resources/{pdf_name}"
    output_path = f"outputs/{pdf_name[:-4]}.txt"



    # Create PFR object.
    pdf = PFR(pdf_path)

    # Extract texts
    with open(output_path, mode = "w") as out_file:

        title = pdf.documentInfo.title
        num_pages = pdf.getNumPages()
        out_file.write(f"{title}\nNumber of Pages: {num_pages}\n\n")

        for page in pdf.pages:
            text = page.extractText()
            out_file.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        text_extractor(sys.argv[1])
    else:
        sys.exit("Usage: python extract_text.py [pdf filename]")

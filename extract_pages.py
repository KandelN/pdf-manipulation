from PyPDF2 import PdfFileWriter, PdfFileReader

input_pdf = PdfFileReader("resources\\Sanatary.pdf")
output_pdf = PdfFileWriter()

for i in range(73, 81):
    page = input_pdf.getPage(i - 1)
    output_pdf.addPage(page)

with open("outputs\Sanatary_mypart.pdfmode = "w") as output_file:
    output_pdf.write(output_file)


# Some extra functions:
# input_pdf.pages[4:8]
# pdf_writer.appendPagesFromReader(pdf_reader)
# page.rotateClockwise(90)

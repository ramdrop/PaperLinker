from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import RectangleObject

# open the pdf file
pdf_reader = PdfFileReader("input2.pdf")
pdf_writer = PdfFileWriter()

# get number of pages
NumPages = pdf_reader.getNumPages()

for page_index in range(NumPages):
    page = pdf_reader.getPage(page_index)
    pdf_writer.addPage(page)
    # print(page.mediaBox[0])
    _, _, W, H = page.mediaBox
    print(W, H)

bl_x, bl_y, ur_x, ur_y = 261, 654, 278, 643
bl_x, bl_y, ur_x, ur_y = bl_x, H - bl_y, ur_x, H - ur_y
pdf_writer.addLink(
    pagenum=0,
    pagedest=16,
    rect=RectangleObject([bl_x, bl_y, ur_x, ur_y]),
                                                           # rect=RectangleObject([0, 0, 400, 100]),
    border="dott",
    fit='/Fit')
with open('output2.pdf', 'wb') as fh:
    pdf_writer.write(fh)

print(NumPages)

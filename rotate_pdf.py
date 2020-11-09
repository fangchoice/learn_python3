
# pip install PyPDF4

"""
  操作PDF，反转PDF
"""

from PyPDF4 import PdfFileReader, PdfFileWriter, PdfFileMerger

def rotate_pdf(original_filename, new_filename, rotation):
    with open(original_filename, 'rb') as pdf:
        # create a pdf reader object
        pdf_reader = PdfFileReader(pdf)
        # create a pdf writer object for new pdf
        pdf_writer = PdfFileWriter()
        # rotating each page
        for page in range(pdf_reader.numPages):
            # create rotated page object
            page_obj = pdf_reader.getPage(page)
            page_obj.rotateClockwise(rotation)
            # adding rotated page object to pdf writer
            pdf_writer.addPage(page_obj)

        with open(new_filename, 'wb') as new_pdf:
            # writing rotated pages to new file
            pdf_writer.write(new_pdf)

def main():
    original_filename = 'test.pdf'
    new_filename = 'rotate_test.pdf'
    rotation = 270
    rotate_pdf(original_filename, new_filename, rotation)

if __name__ == '__main__':
    main()

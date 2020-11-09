"""
  操作PDF：加密PDF
"""

from PyPDF4 import PdfFileReader, PdfFileWriter

def add_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

def main():
    add_encryption(
        input_pdf='test.pdf',
        output_pdf='encrypt.pdf',
        password='123456'
    )

if __name__ == '__main__':
    main()

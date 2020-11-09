
# pip install PyPDF4
"""
   操作PDF：融合多个PDF文件成一个PDF文件
"""
import os

from PyPDF4 import PdfFileReader, PdfFileWriter

def merge_pdf(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def get_pdf_filename(file_dir):
    local_files = []
    for files in os.listdir(file_dir):
        local_files.append(files)
    return local_files
    

def main():
    paths = ['test.pdf', 'split.pdf']
    merge_pdf(paths, output='merged.pdf')

if __name__ == '__main__':
    main()


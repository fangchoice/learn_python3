
import os
import glob
import shutil

import fitz
from PyQt5.QtGui import QImage, QColor


def delete_file(filepath):
    """ Delete file, not directory.
    """
    # https://www.cyberciti.biz/faq/howto-python-delete-files/
    if os.path.isfile(filepath):
        os.remove(filepath)

    return not os.path.isfile(filepath)


def rmdir(dirpath):
    """ Rm directory.
    """
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)

    return not os.path.isdir(dirpath)


def mkdir(dirpath):
    """ Make a directory.
    """
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)

    return os.path.isdir(dirpath)


def list_files(dirpath, ext_wildcard):
    """ list file with *.ext in dir.
    """
    return glob.glob(os.path.join(dirpath, ext_wildcard))


def get_image_color(imagePath):
    path, filename = os.path.split(imagePath)
    image = QImage(imagePath)

    for i in range(0, image.height()):
        for j in range(0, image.width()):
            if image.valid(i, j):

                color = QColor(image.pixel(i,j))
                red = color.red()
                green = color.green()
                blue = color.blue()

                c = 255 - red
                m = 255 - green
                y = 255 - blue
                
                K = min( min(c, m), y )
                C = 0
                M = 0
                Y = 0

                if K > 0:
                    C = c + K
                    M = m + K
                    Y = y + K
                else:
                    C = c
                    M = m
                    Y = y

                CMYKcolor = QColor()
                CMYKcolor.setCmyk(C, M, Y, 0)         
                image.setPixel(i, j, CMYKcolor.value())

                # image.save(path + '/' +  filename)
                return image
            else:
                print(' invalid data ')
                break


def pdf2png(pdf_filepath, output_dir):
    png_files = []
    with fitz.open(pdf_filepath) as pdf:
        for page in pdf:
            pix = page.getPixmap(alpha = False)
            png_filepath = os.path.join(
                output_dir,
                'page-{:0>3d}.png'.format(page.number)
            )
            pix.writePNG(png_filepath)
            png_files.append(png_filepath)
    return png_files


def png2jpg(start_page, key_parts, png_files):
    jpg_files = []
    for index, png_filepath in enumerate(png_files, start=start_page):
        jpg_filename = "".join([
            "Tmx3",
            "".join(key_parts),
            "P",
            "%03d.jpg" % index
        ])
        jpg_filepath = os.path.join(os.path.dirname(png_filepath), jpg_filename)
        image = get_image_color(png_filepath)
        image.save(jpg_filepath)

        jpg_files.append(jpg_filepath)
    return jpg_files


#  single pdf and single image are the same path,  save the pdf
def insert_image_to_pdf(jpg_filepath, tql_filepath, output_file):
    jpg_data = open(jpg_filepath, 'rb').read()

    tql_file = fitz.open(tql_filepath)
    page = tql_file[0]
    rect = fitz.Rect(0, 0, page.rect.width, page.rect.height)

    page.insertImage(rect=rect, stream=jpg_data, overlay = False)

    tql_file.save(output_file)
    tql_file.close()


def generate_pdf_with_picture(startPage, key, input_filepath):

    if not os.path.isfile(input_filepath):
        raise Exception("File not found: %s" % input_filepath)

    input_dirpath = os.path.dirname(input_filepath)       # /root/projects/pen/
    input_filename = os.path.basename(input_filepath)     # test.pdf 
    input_name, _ = os.path.splitext(input_filename)      # test

    output_dirpath = os.path.join(input_dirpath, "code")  # /root/projects/pen/code
    mkdir(output_dirpath)

    *key_parts, _ = key.split(',')
    temp_dir = os.path.join(input_dirpath, key_parts[0])  # /root/projects/pen/code/S0
    rmdir(temp_dir)

    png_dirpath = os.path.join(input_dirpath, *key_parts)
    mkdir(png_dirpath)

    # pdf -> png
    png_files = pdf2png(input_filepath, png_dirpath)

    # png -> jpg
    jpg_files = png2jpg(startPage, key_parts, png_files)

    # merge
    tql_files = list_files("/usr/TEMP", "*.pdf")
    for tql_filepath in tql_files:
        tql_name, _ = os.path.splitext(os.path.basename(tql_filepath))

        for jpg_filepath in jpg_files:
            jpg_name, _ = os.path.splitext(os.path.basename(jpg_filepath))

            if jpg_name == tql_name:
                print('Generate Code Pdf Ok !')
                output_file = os.path.join(output_dirpath, input_name + tql_name + ".pdf")
                insert_image_to_pdf(jpg_filepath, tql_filepath, output_file)

    rmdir(temp_dir)


if __name__ == '__main__':

    key = 'S0,O000,B0000,P000-255'

    pwd_path = os.getcwd()
    input_filepath = os.path.join(pwd_path, 'test.pdf')

    generate_pdf_with_picture(0, key, input_filepath)

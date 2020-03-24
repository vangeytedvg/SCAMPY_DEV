"""
    Filename  and other utilities
    Author : Danny Van Geyte
    Last Modified : March 2019
"""
import os
from PyQt5.QtCore import QDate
import zipfile
from PIL import Image
import img2pdf
# Regular Expression
import re
import glob


def isMailOk(address):
    """
        Check if an email adres is correct
    :param address: email to check
    :return: true if adress os ok, otherwise false
    """
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, address):
        return True
    else:
        return False


def extractFileNameOnly(filepath):
    head, tail = os.path.split(filepath)
    return tail


def extractPathOnly(filepath):
    head, tail = os.path.split(filepath)
    return head


def extractExtension(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return file_extension


def nextImageFileName(catalogLocation, imgPrefix):
    """
    Return a unique filename based on some settings.
    The calculation simple, the hile loop tests if a file already exists.  If
    a unique filename is found (using the n counter) this name is returned.
    :return: New unique image filename
    """
    dateString = QDate.currentDate().toString("yyyyMMdd")
    pattern = catalogLocation + "/" + imgPrefix + \
        '_' + dateString + "_{:03d}.png"
    n = 1

    while True:
        result = pattern.format(n)
        if not os.path.exists(result):
            return result
        n = n + 1

def nukeFile(filename):
    os.remove(filename)

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)


def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)


def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)


def Get_png_images(location):
    """
        Return list of png files
    :param location: path to png files
    :return:
    """
    print("IN _IMAGES")
    # Start with an empty list
    images = []
    pattern = os.path.join(location, '*.png')
    images.extend(glob.glob(pattern))
    print(images)
    return images


def _images(location):
    """
        Return list of png files
    :param location: path to png files
    :return:
    """
    print("IN _IMAGES")
    # Start with an empty list
    images = []
    pattern = os.path.join(location, '*.png')
    images.extend(glob.glob(pattern))
    print(images)
    return images


def _pdfs(location):
    """
        Get all pdf files in location
    :param location: path to pdfs
    :return:
    """
    images = []
    pattern = os.path.join(location, '*.pdf')
    images.extend(glob.glob(pattern))
    return images


def makepdfs(location):
    """
        Convert png files to pdfs
    :param location: path to png files
    :return:
    """
    print(location)
    for q in _images(location):
        img_w_ext = os.path.basename(q)
        
        try:
            image = Image.open(q)
            # Make pdf file from image
            pdf_bytes = img2pdf.convert(image.filename)
            my_pdf_path = location + os.sep + img_w_ext + ".pdf"
            print(my_pdf_path)
            # opening or creating pdf file
            pdf_file = open(my_pdf_path, "wb")
            # writing pdf files with chunks
            pdf_file.write(pdf_bytes)
            image.close()
            pdf_file.close()
            errm = my_pdf_path

        except Exception as e:
            errm = "#" + str(e)
            print("Error", errm)


def makezip(base_folder, zipname, mailid):
    """
        Create zip file, based on the base and mailid
    :param base_folder: Base path to the file
    :param zipname: name of the zipfile to create
    :param mailid: id of the email (becomes part of path to file)
    :return:
    """
    print ("IN MAKEZIP")
    new_base = base_folder + os.sep + str(mailid) + os.sep 
    makepdfs(new_base)

    new_zip_filename = base_folder + os.sep + str(mailid) + os.sep + zipname
    zipper = zipfile.ZipFile(new_zip_filename, "w", compression = zipfile.ZIP_DEFLATED)
    
    for q in _pdfs(new_base):
        print(q)
        zipper.write(q)
    zipper.close()
    return new_zip_filename

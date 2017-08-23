#!/usr/bin/python

import os
import sys
from random import randint
from PIL import Image


def open_image(img_path):
    """
    Handles opening of an image

    :param img_path: the local path to the image file
    :returns an opened image, or None in case of an IOError
    """
    out_img = None
    try:
        out_img = Image.open(img_path)
        print("Opening " + img_path + " with the following attributes: " + out_img.format, out_img.size, out_img.mode)
    except IOError:
        print("Failed to open image at path %", img_path)
        pass
    return out_img


def rotate_image(in_img):
    """
    Handles rotation of an image

    :param in_img: the image file to rotate
    :returns a rotated version of the image
    """
    rotate_amount = randint(0, 360)
    out_img = in_img.rotate(rotate_amount)
    return out_img


def determine_filename(img_path, transformation_type):
    """
    Handles naming of the image

    :param img_path: the image file to rotate
    :param transformation_type: the type of transformation that was performed (resized, rotated, etc.)
    :returns a calculated file name to use when saving the modified image
    """
    file_name, extension = os.path.splitext(img_path)
    out_name = file_name + "-" + transformation_type + ".jpg"
    return out_name


def determine_transformation():
    """
    Handles the determination of the transformation type
    
    :returns the type of transformation to effect
    """
    trans_type = randint(0, 2)
    if trans_type == 0:
        print("rotate")
    elif trans_type == 1:
        print("resize")
    elif trans_type == 2:
        print("transpose")
    return trans_type

# main
input_dir = sys.argv[1]
for dirName, subDirList, fileList in os.walk(input_dir):
    for f in os.listdir(dirName):
        if not f.endswith(".jpg"):
            continue

        abs_path = os.path.join(dirName, f)
        img = open_image(abs_path)
        if img:
            img = rotate_image(img)
            img_name = determine_filename(abs_path, "rotated")
            img.save(img_name, "JPEG")
            print("saved " + img_name)
        else:
            print("fuck")



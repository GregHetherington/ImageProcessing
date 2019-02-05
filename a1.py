import sys

curDir = sys.path[0]
sys.path.append(curDir + '/pythonTOOLBOX')

from imageIO import *
import imageIO

import PIL
import numpy as np
import math
import sys

from imhist_lib import *
import imhist_lib

def getCommandArgs(curDir):
    if(len(sys.argv) < 2):
        print('inncorrect number of command line args')
    inputImage = curDir + "/" + sys.argv[1]

    return inputImage

#Algorithm #1
def histhyperGrayScale(img_grey):
    print("Starting histhyperGrayScale")
    new_gray = imhist_lib.histhyper(img_grey)
    print("Ending histhyperGrayScale")
    return new_gray

#Algorithm #2
def histeqADAPTGrayScale(img_grey):
    print("Starting histeqADAPTGrayScale")
    new_gray = imhist_lib.histeqADAPT(img_grey)
    print("Ending histeqADAPTGrayScale")
    return new_gray

#Algorithm #3
def histmatchGrayScale(img_grey, img_example):
    print("Starting histmatchGrayScale")
    new_gray = imhist_lib.histmatch(img_grey, img_example)
    print("Ending histmatchGrayScale")
    return new_gray

# Main Thread
print('Welcome to Greg\'s Image Process Assignment\n')
inputImage = getCommandArgs(curDir)
print('Input Image: ' + inputImage)

# determine if Image is RGB or Grayscale
img = PIL.Image.open(inputImage)
if(img.mode == 'L'):
    print("Image is Grayscale ... Applying Contrast Enhancement Algorithms\n")
else:
    print("Image is RGB ... Exiting\n")
    exit()
#run all three algorithms back to back
for i in range(1, 4):
    img_gray = imageIO.imread_gray(inputImage)

    if(i == 1):
        algorithm = "histhyper"
        new_gray = histhyperGrayScale(img_gray)
    elif(i == 2):
        algorithm = "histeqADAPT"
        new_gray = histeqADAPTGrayScale(img_gray)
    elif(i == 3):
        algorithm = "histmatch"
        #sets the match image for this algorithm
        img_example = imageIO.imread_gray(curDir + "/Images/example.jpg")
        new_gray = histmatchGrayScale(img_gray, img_example)

    print("Saving Image: " + str(i) + " ...\n")
    imageIO.imwrite_gray(inputImage.replace(".", "") + "_new_" + algorithm + ".jpg", new_gray)

print("Done. exiting...")

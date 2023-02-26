import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import glob
import shutil

# https://www.jaided.ai/easyocr/  lang list
reader = easyocr.Reader(['en', 'hi'], gpu=False, quantize=False)

path2 = "/Users/adit/Downloads/sampleimages/*.*"
folderpath = "/Users/adit/Downloads/wellness"
manualpath = "/Users/adit/Downloads/manual"

for image in glob.glob(path2):

    result = reader.readtext(image, detail=0, paragraph=False)
    flag = False

    for i in result:
        if i.upper() == "WELLNESS" or i == 'वेलनेस':
            flag = True
            break

        else:
            flag = False

    if flag == True:
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
            print("New folder created successfully!")
            shutil.copy(image, folderpath)
        else:
            shutil.copy(image, folderpath)

    else:
        if not os.path.exists(manualpath):
            os.makedirs(manualpath)
            print("New folder created successfully!")
            shutil.copy(image, manualpath)
            flag = False

        else:
            shutil.copy(image, manualpath)
            flag = False

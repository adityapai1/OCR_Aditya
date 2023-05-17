

# --------Imports-------------#
import easyocr
import os
import shutil
import time
import datetime
from PIL import Image

import torch
import math
import re

# import cv2
import numpy as np
# import glob


# ---------------------------#

# # ---------function to reduce Image's Size-------#
# def reduce_size(folder_path,quality):
#     for dirpath, dirnames, filenames in os.walk(folder_path):
#         for image in filenames:
    
#             if image.endswith('.jpg') or image.endswith('.png'):
#                 image_path = os.path.join(dirpath, image)
#                 file_size = os.path.getsize(image_path)
#                 print(f"Processing image: {image_path}")
#                 image = Image.open(image_path)
#                 image.save((image_path), quality=quality)
#                 file_size2 = os.path.getsize(image_path)
#                 percentage = (file_size-filesize2/file_size)*100
#                 print(f"Percentage Reduction in size {percentage}")

# path ="/Users/adit/Downloads/sampleimages_2"
# reduce_size(path,50) 

# quality = 10
# reduce_size(target_path , quality) 
# for function call and parameters

#---------OCR IMPLEMENTATION--------#



# def ocr_program (target_folder,recognized_folder,manual_folder):
# def ocr_program(target_folder):
    reader = easyocr.Reader(['en', 'hi'], gpu=False, quantize=False)

    

    pattern  = 'namrata'
    for dirpath, dirnames, filenames in os.walk(target_folder): #for Recursive Searching of Images
        counter = 1
        dump =[]
        for image in filenames:
            word_list =[]
            if image.endswith('.jpg') or image.endswith('.png'):


                start_time = time.time()
                result = reader.readtext(dirpath.replace(".\\", '')+"\\"+image, detail=0, paragraph=False)
                word_list.extend(result)
                
                flag = False

                for i in result:


                    if re.search(pattern, i.upper(), flags=re.I|re.M|re.X):
                        flag = True
                        break

                    else:
                        flag = False

                if flag == True:
                    if not os.path.exists(dirpath.replace(".\\", '')+"\\"+FolderCodeWord+"\\"):
                        os.makedirs(dirpath.replace(".\\", '')+"\\"+FolderCodeWord+"\\")
                        print("New folder created successfully!")

                    shutil.copy(dirpath.replace(".\\", '')+"\\"+image, dirpath.replace(".\\", '')+"\\"+FolderCodeWord+"\\")


                else:
                    if not os.path.exists(dirpath.replace(".\\", '')+"\\Manual\\"):
                        os.makedirs(dirpath.replace(".\\", '')+"\\Manual\\")
                        print("New folder created successfully!")

                    shutil.copy(dirpath.replace(".\\", '')+"\\"+image, dirpath.replace(".\\", '')+"\\Manual\\")

                end_time = time.time()
                difference = end_time-start_time

                print(f"Time Taken for Image {counter} is {difference} secs")
                counter+=1
            dump.extend(wordlist)
            dump_deduplicated = np.unique(dump)
            np.savetxt(dirpath+"dump.csv", dump_deduplicated, delimiter="|", fmt='% s')
            
def ocr_program(target_folder):
    reader = easyocr.Reader(['en', 'hi'], gpu=False, quantize=False)

    

    pattern  = 'namrata'
    for dirpath, dirnames, filenames in os.walk(target_folder): #for Recursive Searching of Images
        counter = 1
        dump =[]
        for image in filenames:
            word_list =[]
            if image.endswith('.jpg') or image.endswith('.png'):


                start_time = time.time()
                result = reader.readtext(dirpath.replace(".\\", '')+"\\"+image, detail=0, paragraph=False)
                word_list.extend(result)
                
                flag = False

                for i in result:


                    if re.search(pattern, i.upper(), flags=re.I|re.M|re.X):
                        flag = True
                        break

                    else:
                        flag = False

                if flag == True:
                    if not os.path.exists(dirpath.replace(".\\", '')+"\\"+FolderCodeWord+"\\"):
                        os.makedirs(dirpath.replace(".\\", '')+"\\"+FolderCodeWord+"\\")
                        print("New folder created successfully!")

                    shutil.copy(dirpath.replace(".\\", '')+"\\"+image, dirpath.replace(".\\", '')+"\\"+FolderCodeWord+"\\")


                else:
                    if not os.path.exists(dirpath.replace(".\\", '')+"\\Manual\\"):
                        os.makedirs(dirpath.replace(".\\", '')+"\\Manual\\")
                        print("New folder created successfully!")

                    shutil.copy(dirpath.replace(".\\", '')+"\\"+image, dirpath.replace(".\\", '')+"\\Manual\\")

                end_time = time.time()
                difference = end_time-start_time

                print(f"Time Taken for Image {counter} is {difference} secs")
                counter+=1
            dump.extend(word_list)
            dump_deduplicated = np.unique(dump)
            np.savetxt(dirpath+"dump.csv", dump_deduplicated, delimiter="|", fmt='% s')
            
main ="/Users/adit/Downloads/PhotoCaptFiles"
ocr_program(main)



# main ="C:/Temp/Main/."
# # main ="C:/Temp/sampleimages/."
# folderpath = "C:/Temp/Main/Namrata"
# manualpath = "C:/Temp/Main/manual"
# FolderCodeWord = "Namrata"

# ocr_program(main, folderpath, manualpath)
# ocr_program(main)

"""

target_path  ="C:/Temp/Main"
quality = 10
reduce_size(target_path , quality)

# target_path = "/Users/adit/Desktop/OCR/TargetFolder/second/fourth/fifth"
# quality = 10
# reduce_size(target_path , quality) 
# for function call and parameters

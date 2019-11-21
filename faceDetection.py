import numpy as np
import cv2 as cv
import os
import shutil
import time

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return num, x
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

def img_filter(imgfiles, path, invalid, picofpic = " ", valid = ""):

    for imgfile in imgfiles:
        fname = path + imgfile
        try:
            # img = cv.imread('/home/yash/Documents/attendance-image/5985_2019-07-15.jpg')
            img = cv.imread(fname)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            t = list(faces)
            # print(len(t))
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            t = list(faces)
            # print(fname+" " +str(len(t)))
            t = len(t)
            if t == 0:
                shutil.copy2(fname, invalid)
                # print("Invalid")
            else:
                shutil.copy2(fname, valid)
               
        except cv.error as e:
            print("error")
            print(fname)
    print("code executed")


def img_filter_level2(imgfiles, p, valid,  classifier):
    print ("i am searning in this folder "+p)
    # print(classifier)
    i = 0
    # time.sleep(5)
    for imgfile in imgfiles:
        fname = p+imgfile
        image = cv.imread(fname)
       
        face_cascade = cv.CascadeClassifier(classifier)

        try:
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            # print(imgfile)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(5, 5))
            if len(faces) != 0:
                i = i + 1
                shutil.copy2(fname, valid)
                print ("Removing "+str(fname))
                os.remove(fname)
                # print("file removed")

        except cv.error as e:
            pass
   
    print(classifier + " "+str(i))

classif_ierlist = ["haarcascade_frontalface_alt2.xml", "haarcascade_profileface.xml", "haarcascade_frontalface_alt.xml", "haarcascade_righteye_2splits.xml","haarcascade_lefteye_2splits.xml"]
p = "/home/yash/Documents/Attendence_imagePOC/attendance-image/"
valid = "/home/yash/Documents/Attendence_imagePOC/valid/"
invalid = "/home/yash/Documents/Attendence_imagePOC/invalid/"
picofpic = "/home/yash/Documents/Attendence_imagePOC/picofpic/"
invalid_1 = "/home/yash/Documents/Attendence_imagePOC/invalid_1/"
imgfiles = os.listdir(p)

face_cascade = cv.CascadeClassifier('/home/yash/Downloads/haarcascade_frontalface_default.xml')
# eye_cascade = cv.CascadeClassifier('/home/yash/Downloads/haarcascade_frontalface_default.xml')

img_filter(imgfiles, p, invalid, picofpic, valid)


p = "/home/yash/Documents/Attendence_imagePOC/invalid/"
imgfiles = os.listdir(p)
invalid = "/home/yash/Documents/Attendence_imagePOC/invalid/"

classif_ier = '/home/yash/Downloads/parsers/opencv-master/data/haarcascades/haarcascade_profileface.xml'
class_loc = "/home/yash/Downloads/parsers/opencv-master/data/haarcascades/"
classif_iers = os.listdir(class_loc)

classif_ier1 = ""
i = 0
for classif_ier in classif_ierlist:
    i = i + 1
    print("classifier called : "+str(classif_ier))
    imgfiles = os.listdir(p)
    invalid_12 = "/home/yash/Documents/Attendence_imagePOC/valid/"
    print(invalid_12)
    classif_ier1 = "/home/yash/Downloads/parsers/opencv-master/data/haarcascades/"+classif_ier
    img_filter_level2(imgfiles, p, invalid_12, classif_ier1)



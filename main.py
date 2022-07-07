import cv2 as cv
import sys
import os
import ipdb
import numpy as np

imagenes = os.listdir("/home/ariel/Escritorio/patentFinderPython/patentes")

def img_gray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def threshold_img(gray_img):
    return cv.threshold(gray_img, 170, 255, cv.THRESH_BINARY_INV)[1]

def findContours(thresh, img):
    contours = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
    canvas = np.zeros_like(img)
    cv.drawContours(canvas, contours, -1, (0, 255, 0), 2)
    return canvas

def filter_contours(contours):
    license_ratio = 3.07692307692
    min_w = 80
    max_w = 110
    min_h = 25
    max_h = 52
    candidates = []
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        aspect_radio = float(w) / h
        if(np.isclose(aspect_radio, license_ratio, atol=0.7) and (max_w > w > min_w) and (max_h, h, min_h)):
            candidates.append(cnt)
    return candidates
for img in imagenes:
    img = cv.imread(f"./patentes/"+img)
    findContours(threshold_img(img_gray(img)), img)
    
    cv.imshow("Display image", )
    k = cv.waitKey(0)

ipdb.set_trace()





if k == ord("s"):
    cv.imwrite("img.png", gray)
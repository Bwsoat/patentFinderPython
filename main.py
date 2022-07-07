import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("img.jpg"))

if img is None:
    sys.exit("No se encontro la imagen")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Kusanali", gray)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("img.png", gray)
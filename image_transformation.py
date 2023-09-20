import cv2 as cv 
import numpy as np

img=cv.imread('cats.png')
cv.imshow('Boston',img)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# x is left and y is right

translated=translate(img,100,100)
cv.imshow('Translated',translated)
#Rotate the image
cv.waitKey(0)

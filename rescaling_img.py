import cv2 as cv


image=cv.imread('cats.png')
cv.imshow('cat',image)

def rescaleFame(fame,scale=0.75):
    width=int(fame.shape[1]*scale)
    height= int(fame.shape[0]*scale)
    dimension= (width,height)

    return cv.resize(fame,dimension,interpolation=cv.INTER_AREA)

cv.waitKey(0);


import cv2 as cv

img=cv.imread('cats.png')
cv.imshow('cat',img)

#3converting to gray image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#making blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

## dilating the imag
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dialated',dilated)

#eroding
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded',eroded)

#resize 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resized)

#cropping
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)




cv.waitKey(0)



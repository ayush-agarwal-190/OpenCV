import cv2 as cv 

capture=cv.VideoCapture(' ')
# 0-> represent lap camera 
# 1-> represent external camera

while True:
    isTrue, fame=capture.read()
    cv.imshow('Video,fame')

    if cv.waitKey(20)& 0xFF==ord('d'):
        break;
capture.release()

cv.waitKey(0)
import cv2 as cv




def rescaleFame(fame,scale=0.75):
    width=int(fame.shape[1]*scale)
    height= int(fame.shape[0]*scale)
    dimension= (width,height)

    return cv.resize(fame,dimension,interpolation=cv.INTER_AREA)

#reading video
capture=cv.VideoCapture('Video.mp4')
while True:
    isTrue,frame=capture.read()
    fame_resized=rescaleFame(frame,scale=.2)

    cv.imshow('Video',frame)
    cv.imshow('video Resized')

    if cv.waitKey(0) & 0xFF==ord('d'):
        break

capture.release()    
cv.waitKey(0);


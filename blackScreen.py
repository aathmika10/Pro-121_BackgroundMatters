import cv2 
import numpy as np

#Starting the wedcam
capture=cv2.VideoCapture(0)
image=cv2.imread("palace.jpg")

#reading the frames of the video
while True:
    ret,frame=capture.read()
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))
    upperBlack=np.array([104,153,70])
    lowerBlack=np.array([30,30,0])
    mask=cv2.inRange(frame,upperBlack,lowerBlack)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    f=frame-res
    f=np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)

    #Breaking the loop if q is pressed
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
#@author:Kartik Madhira
#kartikmadhira1@gmail.com
#TRAFFIC COUNT USING MOMENTS METHOD
import cv2
backsub = cv2.BackgroundSubtractorMOG() #background subtraction to isolate moving cars
capture = cv2.VideoCapture("/home/pi/Downloads/video.avi") #change to destination on your pc 
i = 0
minArea=1
  while True:
    ret, frame = capture.read()
    fgmask = backsub.apply(frame, None, 0.01)
    erode=cv2.erode(fgmask,None,iterations=3)     #erosion to erase unwanted small contours
    moments=cv2.moments(erode,True)               #moments method applied
    area=moments['m00']    
    if moments['m00'] >=minArea:
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        if x>40 and x<55 and y>50 and y<65:       #range of line coordinates for values on left lane
            i=i+1
            print(i)
        elif x>102 and x<110 and y>105 and y<130: #range of line coordinatess for values on right lane
            i=i+1
            print(i)
        #print(x,y)
        cv2.putText(frame,'COUNT: %r' %i, (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2)
        cv2.imshow("Track", frame)
        cv2.imshow("background sub", fgmask)
    key = cv2.waitKey(100)
    if key == ord('q'):
            break

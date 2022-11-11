from datetime import *
import cv2
import numpy as np
import imutils

# import uuid

# cap = cv2.VideoCapture('bebek.jpg')
# cap.set(3,640)
# cap.set(4,480)
def funcopencv(filename):
    frame = cv2.imread('upload/'+filename)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([7,0,140])
    upper_yellow = np.array([171,58,255])
    
    lower_green = np.array([40,70,80])
    upper_green = np.array([70,255,255])
    
    lower_red = np.array([2,36,165])
    upper_red = np.array([28,230,237])
    
    lower_blue = np.array([90,60,0])
    upper_blue = np.array([121,255,255])

    mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_red, upper_red)
    mask4 = cv2.inRange(hsv, lower_blue, upper_yellow)
    
    
    cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)


    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)


    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)


    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)


    for c in cnts1:
        area1 = cv2.contourArea(c)
        if area1 > 5000:



            cv2.drawContours(frame,[c],-1,(0,255,0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            
            cv2.circle(frame, (cx,cy), 7, (255,255,255),-1)
            cv2.putText(frame, "Telur Bebek", (cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),3)

    for c in cnts2:
        area2 = cv2.contourArea(c)
        if area2 > 5000:



            cv2.drawContours(frame,[c],-1,(0,255,0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            
            cv2.circle(frame, (cx,cy), 7, (255,255,255),-1)
            cv2.putText(frame, "Green", (cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX,2.5, (255,255,255),3)



    for c in cnts3:
        area3 = cv2.contourArea(c)
        if area3 > 5000:



            cv2.drawContours(frame,[c],-1,(0,255,0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            
            cv2.circle(frame, (cx,cy), 7, (255,255,255),-1)
            cv2.putText(frame, "Telur Ayam Kampung", (cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),3)

    for c in cnts4:
        area4 = cv2.contourArea(c)
        if area4 > 5000:



            cv2.drawContours(frame,[c],-1,(0,255,0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            
            cv2.circle(frame, (cx,cy), 7, (255,255,255),-1)
            cv2.putText(frame, "Blue", (cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX,2.5, (255,255,255),3)

    today = date.today()
    pathfile = "upload/result/"+today.strftime("%d-%m-%Y")+".jpg"
    print(pathfile)




    cv2.imwrite(pathfile, frame)
    return pathfile
    

# funcopencv()
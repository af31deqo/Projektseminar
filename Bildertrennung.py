# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:52:15 2021

@author: Mohamed Zitane & Anissa Hadhri
"""

#simport picamera
##from picamera import Picamera
import cv2
import numpy as np

# Bilder Einstellen 

totalfoto = 6 # total number of images to be saved
Imgsize= (640,480) # Resolution of the video 
count= #counter to count the images that have been saved

# Bilder Aufnehemen 

print("Start taking images")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Imgsize[1]) #Set the height of the frame to 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, Imgsize[0]) #Set the width of the frame to 640



#camera= PiCamera()
#camera.resolution = (Imgsize[1],Imgsize[0])
#camera.start_preview(fullscreen=False,window=(0,0,Imgsize[1]*0.5,Imgsize[0]*0.5))
while True:
    ret, img = cap.read()
    cv2.imshow('Img', img)
    file=  'Bild_'+str(Imgsize[0])+'x'+str(Imgsize[1])+'_'+str(count) + '.png' #File to save the hole image
    L_file = 'L_Bild_'+str(int(Imgsize[1]/2))+'x'+str(Imgsize[1])+'_'+str(count) + '.png' #File to save the left half of the image
    R_file = 'R_Bild_'+str(int(Imgsize[1]/2))+'x'+str(Imgsize[0])+'_'+str(count) + '.png' #File to save the right half of the image
    if cv2.waitKey(1) == ord('s') and count < totalfoto: #if s is pressed and the number of captures requires hasn't been attended save the hole image, left part and right part
        #sleep(2)
        #camera.capture(filename)
        L_img= img[0:Imgsize[1],0:int(Imgsize[0]/2)] #Left half of the image
        R_img= img[0:Imgsize[1],int(Imgsize[0]/2): Imgsize[0]] #Right half of the image
        cv2.imwrite(file,img) #save the hole image 
        cv2.imwrite(L_file,L_img) #save the the left half part
        cv2.imwrite(R_file,R_img) #save the the right half part
        count+=1 #count the number of images saved already
        print(L_file + " and " + R_file + " are saved")
    elif cv2.waitKey(1) == ord('q'): #If q is pressed after saving n captures stop the programm
        break
#camera.stop_preview()    
cap.release()
cv2.destroyAllWindows() 

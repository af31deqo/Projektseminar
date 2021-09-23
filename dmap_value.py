# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:43:19 2021

@author: Simz
"""

import cv2
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from matplotlib import pyplot as plt
import numpy as np

baseline=30 # 
alpha=53.6 #
Imgsize= (348,288) # Resolution of the image
x_pos = 0
y_pos = 0

print("Start taking image")

#cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Imgsize[1])
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, Imgsize[0])



#camera= PiCamera()
#camera.resolution = (Imgsize[1],Imgsize[0])
#camera.start_preview(fullscreen=False,window=(0,0,Imgsize[1]*0.5,Imgsize[0]*0.5))

#ret, img = cap.read()
#cv2.imshow('Img', img)
 #sleep(2)
 #camera.capture(filename)
L_img= cv2.imread('items_l.png',cv2.IMREAD_GRAYSCALE) # load left side image in grayscale mode
R_img= cv2.imread('items_r.png',cv2.IMREAD_GRAYSCALE) # load left right image in grayscale mode
#L_img= img[0:Imgsize[1],0:int(Imgsize[0]/2)]
#R_img= img[0:Imgsize[1],int(Imgsize[0]/2): Imgsize[0]] 

#Implementing calibration data
print('Load calibration data...')
calibration = StereoCalibration(input_folder='result')
rectified_pair = calibration.rectify((L_img, R_img))

print('Building depth map...')
def stereo_depth_map(rectified_pair, ndisp, sws):
    stereo = cv2.StereoBM_create(numDisparities=ndisp, blockSize=sws) # Creates StereoBM object with n disparities (the disparity search range) and m blocksize (the linear size of the blocks compared by the algorithm)

    return stereo.compute(L_img,R_img) # Computes disparity map for the specified stereo pair.

disparity = stereo_depth_map(rectified_pair,0,21)
 
print('Done! Let\'s look at depth map')

#distance in x, y position with mouse click event
def show_distance(event,x,y,args,params):
        point = (x,y)
        global x_pos
        global y_pos
        if event == cv2.EVENT_LBUTTONDOWN:
            x_pos = point[1]
            y_pos = point[0]
            depth = compute_depth(x_pos, y_pos, baseline, alpha)
            print("Depth :" + str(round(abs(depth),2)) + "cm")

def compute_depth(x_pos,y_pos,baseline,alpha):
        f_pixel = (Imgsize[0]*0.5)/np.tan(alph*0.5*np.pi/180)
        z = (baseline*f_pixel)/disparity[x_pos,y_pos] 
        return z

plt.imshow(disparity)
plt.colorbar()
plt.show()

while True:
    
    cv2.namedWindow("Left")
    cv2.setMouseCallback("Left",show_distance)

#Depth in cm

    
    
#plot

#cv2.imshow('Left',L_img)
#cv2.imshow('Right',R_img)

    cv2.imshow('Left',rectified_pair[0])
    #cv2.imshow('Right',rectified_pair[1])
    cv2.waitKey(5)
    if cv2.waitKey(1)==27:
       break

cv2.destroyAllWindows()

#norm_coeff = 255 / disparity.max()-disparity.min()
#plt.subplot(2,2,1)
#plt.imshow(rectified_pair[0])
#plt.subplot(2,2,2) 
#plt.imshow(rectified_pair[1])
#plt.subplot(2,2,3)
#plt.imshow(disparity)
#plt.colorbar()
#plt.show()

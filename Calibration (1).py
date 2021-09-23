# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:14:54 2021

@author: Mohamed Zitane & Anissa Hadhri
"""

import numpy as np
import cv2
import glob
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
# Set parameters 
totalfoto = 6 # total number of images to be saved
Boardsize = (9,6) #Size of the Board
Imgsize= (384,288) # Resolution of the video
squaresize=2.5 # Size of eachthe site of the square of the Bord

#Set the Calibrator and images
calibrator= StereoCalibrator(Boardsize[0],Boardsize[1],squaresize,Imgsize)
imagesLeft = glob.glob('imgl/*.png')
imagesRight = glob.glob('imgr/*.png')

#Calibration
for imgLeft, imgRight in zip(imagesLeft, imagesRight):

    imgL = cv2.imread(imgLeft)
    imgR = cv2.imread(imgRight)
    calibrator.add_corners((imgL,imgR),True)

print('Starting Calibration')
calibration = calibrator.calibrate_cameras()
calibration.export('result')
print('Calibration complete')

#Result of calibration
calibration = StereoCalibration(input_folder='result')
rectified_pair = calibration.rectify((imgL, imgR))

cv2.imshow('Left CALIBRATED', rectified_pair[0])
cv2.imshow('Right CALIBRATED', rectified_pair[1])
cv2.imwrite("rectifyed_left.png",rectified_pair[0])
cv2.imwrite("rectifyed_right.png",rectified_pair[1])
cv2.waitKey(0)

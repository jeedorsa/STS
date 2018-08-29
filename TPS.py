# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 23:49:40 2018

@author: jesus
"""
import os
import time
import cv2
import numpy as np
import tensorflow as tf
import sys
sys.path.append("..")
VIDEO_NAME = 'VIDEO1.mp4'
CWD_PATH = os.getcwd()
PATH_TO_VIDEO = os.path.join(CWD_PATH,VIDEO_NAME)
video = cv2.VideoCapture(PATH_TO_VIDEO)
start_time = time.time()
x = 1 
counter = 0
FPS1=25
back=1
while(video.isOpened()):
    fps = video.get(cv2.CAP_PROP_FPS)
    ret, frame = video.read()
    if(back==1):
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gris = cv2.GaussianBlur(gris, (21, 21), 0)
        fondo=gris
        back=2
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (21, 21), 0) 
    resta = cv2.absdiff(fondo, gris)
    umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]
    umbral = cv2.dilate(umbral, None, iterations=2)
    contornosimg = umbral.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    frame_expanded = np.expand_dims(frame, axis=0)
    cv2.putText(frame,'FPS:',(547,355), 1, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame,str(FPS1),(593,355), 1, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('TPS Demo', frame)
    counter+=1
    if (time.time() - start_time) > x :
        FPS1=counter / (time.time() - start_time)
        counter = 0
        start_time = time.time()
    if cv2.waitKey(1) == ord('q'):
        break
    time.sleep(0.5)
video.release()
cv2.destroyAllWindows()

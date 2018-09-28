# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 23:49:40 2018

@author: jesus
"""
import os
import time
import cv2
import numpy as np
#import tensorflow as tf
import sys
sys.path.append("..")
VIDEO_NAME = 'GRUA1.mp4'
CWD_PATH = os.getcwd()
PATH_TO_VIDEO = os.path.join(CWD_PATH,VIDEO_NAME)
video = cv2.VideoCapture(PATH_TO_VIDEO)
start_time = time.time()
x = 1 
counter = 0
FPS1=1
back=1
jj=1
xant=0
yant=0
dis=1
vel=1

inicio = [975, 310]
line_type = 8

while(video.isOpened()):
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    pixels=width*height
    t=1/FPS1
    t=t/3600
    fps = video.get(cv2.CAP_PROP_FPS)
    ret, frame = video.read()
    pos = np.array([inicio, 
                   [inicio[0] + 60, inicio[1]],
                   [inicio[0] - 180 , inicio[1] + 770], 
                   [inicio[0] - 760, inicio[1] + 770]], 
                   np.int32)                           #Coordenadas de la zona de interés
    cv2.fillPoly(frame, [pos], (0, 0, 0), line_type)   #Coloreado zona de interés 1
    if(back==1):
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gris = cv2.GaussianBlur(gris, (21, 21), 0)
        fondo=gris
        back=2
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (21, 21), 0) 
    resta = cv2.absdiff(fondo, gris)
    umbral = cv2.threshold(resta, 28, 255, cv2.THRESH_BINARY)[1]
    umbral = cv2.dilate(umbral, None, iterations=4)
    contornosimg = umbral.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    ll=1
    jj=1
    for c in contornos:
        if cv2.contourArea(c) < 700:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        dis=y-yant
        dis=dis*0.0048
        vel=dis/t
        vel=vel/10000
        yant=y
        x1=x
        x2=y
        jj=2
        cv2.putText(frame,str(vel),(x,y), 1, 1,(0,255,0),2,cv2.LINE_AA)
        ll=2
        #if (ll==1):
        #    if(jj==1):
        #        x1=x
        #        x2=y
        #        jj=2
        #    cv2.putText(frame,str(vel),(x,y), 1, 1,(0,255,0),2,cv2.LINE_AA)
        #    ll=2
            
            #x2=x2+0.2
    frame_expanded = np.expand_dims(frame, axis=0)
    cv2.putText(frame,'FPS:',(0,20), 1, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame,str(FPS1),(0,35), 1, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('TPS Demo', frame)
    counter+=1
    if (time.time() - start_time) > x :
        FPS1=counter / (time.time() - start_time)
        counter = 0
        start_time = time.time()
    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord('p'):
        u=1
        time.sleep(3)
        while(u==1):
            u=1
            if cv2.waitKey(1) == ord('p'):
                u=2
    
    #time.sleep(0.5)
video.release()
cv2.destroyAllWindows()

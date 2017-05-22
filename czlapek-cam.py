#!/usr/bin/env python
from bottle import route, run, static_file
import pygame
import pygame.camera
import time
import os

cam1_status = 0
cam2_status = 0

@route('/cam/get/camera1.jpg', method='GET')
def cam1_get():
    global cam1_status
    if ( cam1_status == 1 ):
        img = cam1.get_image()
        pygame.image.save(img,"/tmp/camera1.jpg")
        return static_file('camera1.jpg', root='/tmp')
    else:
        return static_file('no-camera.jpg', root='/opt/czlapek/')

@route('/cam/get/camera2.jpg', method='GET')
def cam2_get():
    global cam2_status
    if ( cam2_status == 1 ):
        img = cam2.get_image()
        pygame.image.save(img,"/tmp/camera2.jpg")
        return static_file('camera2.jpg', root='/tmp')
    else:
        return static_file('no-camera.jpg', root='/opt/czlapek/')


@route('/cam/status/<cam>', method='GET')
def cam_start(cam):
    global cam1_status
    global cam2_status

    if ( cam == 'cam1'):
        if ( cam1_status == 1 ):
            return 'ON'
        else:
            return 'OFF'

    if ( cam == 'cam2'):
        if ( cam2_status == 1 ):
            return 'ON'
        else:
            return 'OFF'


@route('/cam/toogle/<cam>', method='GET')
def cam_toogle(cam):
    global cam1_status
    global cam1
    global cam2_status
    global cam2

    if ( cam == 'cam1'):
        if ( cam1_status == 1 ):
            cam1.stop()
            cam1_status = 0
        else:
            cam1.start()
            cam1_status = 1

    if ( cam == 'cam2'):
        if ( cam2_status == 1 ):
            cam2.stop()
            cam2_status = 0
        else:
            cam2.start()
            cam2_status = 1




#os.chdir('/opt/fusion')
pygame.camera.init()
cam1 = pygame.camera.Camera("/dev/video0",(640,480))
cam1.start()
cam1_status = 1
	
cam2 = pygame.camera.Camera("/dev/video1",(640,480))
cam2.start()
cam2_status = 1

run(host='0.0.0.0', port=8081)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import os
import threading
import json
import pygame

from bottle import route, run, template, static_file
from classes.alarm import Alarm
from classes.gadacz import Gadacz
from classes.relay import Relay



gadacz_instance = Gadacz()

relay_instance = Relay(gadacz_instance)



talk='1'

@route('/talk/<val>')
def set_talk(val):
    global talk

    if (val == 'status'):
        if (talk == '1'):
            return 'ON'
        else:
            return 'OFF'
    if (val == 'toogle'):
        if (talk == '1'):
            talk = '0'
            return 'OFF'
        else:
            talk = '1'
            return 'ON'

    if (val == '1'):
        talk = '1'
        return '<b>Talk:  ON</b>!'
    else:
        talk = '0'
        return '<b>Talk:  OFF</b>!'

@route('/gadacz/status/<val>')
def gadacz_status(val):
    global gadacz_instance
    print 'status'
    if (val == 'okna'):
        print 'status-okna'
        return gadacz_instance.okna
    if (val == 'drzwi'):
        print 'status-drzwi'
        return gadacz_instance.drzwi
    if (val == 'swiatlo'):
        print 'status-swiatlo'
        return gadacz_instance.swiatlo

@route('/gadacz/enable/<val>')
def gadacz_enable(val):
    global gadacz_instance
    if (val == 'okna'):
        gadacz_instance.okna = 1
    if (val == 'drzwi'):
        gadacz_instance.drzwi = 1
    if (val == 'swiatlo'):
        gadacz_instance.swiatlo = 1

@route('/gadacz/disable/<val>')
def gadacz_disable(val):
    global gadacz_instance
    if (val == 'okna'):
        gadacz_instance.okna = 0
    if (val == 'drzwi'):
        gadacz_instance.drzwi = 0
    if (val == 'swiatlo'):
        gadacz_instance.swiatlo = 0

@route('/gadacz/toggle/<val>')
def gadacz_toggle(val):
    global gadacz_instance
    gadacz_instance.toggle(val)

@route('/relay/status/<relay>')
def relay_status(relay):
    return relay_instance.relay_status(relay)

@route('/relay/toogle/<relay>')
def relay_toogle(relay):
    relay_instance.relay_toogle(relay)





os.system('/opt/vol.sh 100')
#os.system('espeak -v polish  "Inicjuję ekspandery"')

pygame.mixer.init()

pygame.mixer.music.load('/opt/sounds/intro.mp3')
pygame.mixer.music.play()
pygame.mixer.music.queue('/opt/sounds/intro.wav')

alarm_instance = Alarm(gadacz_instance)
alarm_instance.start()


#os.system('espeak -v polish -s 200 "Uruchamiam system"')
#os.system('espeak -v polish -s 200 "Witamy w systemie Supernova. Funkcje inteligentnego domu zostały aktywowane."')


gadacz_instance.start()

run(host='0.0.0.0', port=8080)

#os.system('espeak -v polish  "Wyłączam system. Dziękujemy za skorzystanie z oprogramowania Adrianozy Didżital Studio. Miłego dnia."')




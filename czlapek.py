#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import os
import threading
import json

from bottle import route, run, template, static_file


bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs

a0=1
a1=1
a2=1
a3=1
a4=1
a5=1
a6=1
a7=1

talk='1'

@route('/talk/<val>')
def set_talk(val):
    global talk

    if ( val == 'status' ):
        if ( talk == '1' ):
            return 'ON'
        else:
            return 'OFF'
    if ( val == 'toogle' ):
	if ( talk == '1' ):
	    talk='0'
            return 'OFF'
	else:
	    talk='1'
            return 'ON'


    if ( val == '1' ):
        talk='1'
        return '<b>Talk:  ON</b>!'
    else:
        talk='0'
        return '<b>Talk:  OFF</b>!'

@route('/relay/enable/<relay>')
def relay_enable(relay):

    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global talk

    if ( relay == 'a0' ):
        a0 = 0
    if ( relay == 'a1' ):
        a1 = 0
        if ( talk == '1' ):
            os.system('espeak -v polish  "Włączam światło w małym pokoju"')
    if ( relay == 'a2' ):
        a2 = 0
        if ( talk == '1' ):
            os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
    if ( relay == 'a3' ):
        a3 = 0
        if ( talk == '1' ):
            os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
    if ( relay == 'a4' ):
        a4 = 0
        if ( talk == '1' ):
            os.system('espeak -v polish  "Włączam światło w przedpokoju"')
    if ( relay == 'a5' ):
        a5 = 0
        if ( talk == '1' ):
            os.system('espeak -v polish  "Włączam światło w przedpokoju"')
    if ( relay == 'a6' ):
        a6 = 0
    if ( relay == 'a7' ):
        a7 = 0

    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo {{relay}}:  ON</b>!', relay=relay)


@route('/relay/disable/<relay>')
def relay_disable(relay):

    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global talk

    if ( relay == 'a0' ):
        a0 = 1
    if ( relay == 'a1' ):
        a1 = 1
        if ( talk == '1' ):
            os.system('espeak -v polish  "Wyłączam światło w małym pokoju"')
    if ( relay == 'a2' ):
        a2 = 1
        if ( talk == '1' ):
            os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
    if ( relay == 'a3' ):
        a3 = 1
        if ( talk == '1' ):
            os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
    if ( relay == 'a4' ):
        a4 = 1
        if ( talk == '1' ):
            os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
    if ( relay == 'a5' ):
        a5 = 1
        if ( talk == '1' ):
            os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
    if ( relay == 'a6' ):
        a6 = 1
    if ( relay == 'a7' ):
        a7 = 1

    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo {{relay}}:  OFF</b>!', relay=relay)

@route('/relay/status/<relay>')
def relay_status(relay):

    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7

    if ( relay == 'a0' ):
        if ( a0 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a1' ):
        if ( a1 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a2' ):
        if ( a2 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a3' ):
        if ( a3 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a4' ):
        if ( a4 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a5' ):
        if ( a5 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a6' ):
        if ( a6 == 1 ):
            return 'OFF'
        else:
            return 'ON'
    if ( relay == 'a7' ):
        if ( a7 == 1 ):
            return 'OFF'
        else:
            return 'ON'


@route('/relay/toogle/<relay>')
def relay_toogle(relay):

    global a0
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7

    if ( relay == 'a0' ):
	if ( a0 == 1 ):
	    a0=0
	else:
	    a0=1
    if ( relay == 'a1' ):
	if ( a1 == 1 ):
	    a1=0
            if ( talk == '1' ):
	        os.system('espeak -v polish  "Włączam światło w małym pokoju"')
	else:
	    a1=1
            if ( talk == '1' ):
                os.system('espeak -v polish  "Wyłączam światło w małym pokoju"')
    if ( relay == 'a2' ):
	if ( a2 == 1 ):
            a2=0
            if ( talk == '1' ):
                os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
	else:
	    a2=1
            if ( talk == '1' ):
                os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
    if ( relay == 'a3' ):
	if ( a3 == 1 ):
	    a3=0
            if ( talk == '1' ):
                os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
	else:
	    a3=1
            if ( talk == '1' ):
	        os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
    if ( relay == 'a4' ):
	if ( a4 == 1 ):
	    a4=0
            if ( talk == '1' ):
	        os.system('espeak -v polish  "Włączam światło w przedpokoju"')
	else:
	    a4=1
            if ( talk == '1' ):
	        os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
    if ( relay == 'a5' ):
	if ( a5 == 1 ):
	    a5=0
            if ( talk == '1' ):
	        os.system('espeak -v polish  "Włączam światło w przedpokoju"')
	else:
	    a5=1
            if ( talk == '1' ):
	        os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
    if ( relay == 'a6' ):
	if ( a6 == 1 ):
	    a6=0
	else:
	    a6=1
    if ( relay == 'a7' ):
	if ( a7 == 1 ):
	    a7=0
	else:
	    a7=1

    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo {{relay}}:  OFF</b>!', relay=relay)

@route('/cam/get/image.jpg', method='GET')
def cam1_get():
#    img = cam.get_image()
#    pygame.image.save(img,"/tmp/camera3-tmp.jpg")
#    os.system("convert -quality 40 /tmp/camera3-tmp.jpg /tmp/camera3.jpg ")
    return static_file('image.jpg', root='/tmp')



def relay_init():
    # Set all GPA pins as outputs by setting
    # all bits of IODIRA register to 0
    bus.write_byte_data(DEVICE,IODIRA,0x00)

    # Set output all 7 output bits to 1
    bus.write_byte_data(DEVICE,OLATA,255) 

def handle_alarm():
    os.system('espeak -v polish  "Uruchamiam alarm"')
    bus2 = smbus.SMBus(1) # Rev 2 Pi uses 1

    DEVICE2 = 0x27 # Device address (A0-A2)
    IODIRA2 = 0x00 # Pin direction register
    OLATA2  = 0x14 # Register for outputs
    GPIOA2  = 0x12 # Register for inputs

    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0
    o5 = 0
    o6 = 0
    o7 = 0
    d1 = 0

    # Set first 7 GPA pins as outputs and
    # last one as input.
    bus2.write_byte_data(DEVICE2,IODIRA2,0xFF)

    while True:
     
      # Read state of GPIOA register
      MySwitch = bus2.read_byte_data(DEVICE2,GPIOA2)
     
      if MySwitch & 0b00000001 == 0b00000001:
        if o1 == 1:
          os.system('espeak -v polish  "Zamknięto okno 1 w dużym pokoju"')
          o1 = 0
      else:
        if o1 == 0:
          os.system('espeak -v polish  "Otwarto okno 1 w dużym pokoju"')
          o1 = 1

      if MySwitch & 0b00000010 == 0b00000010:
        if o2 == 1:
          os.system('espeak -v polish  "Zamknięto okno 2 w dużym pokoju"')
          o2 = 0
      else:
        if o2 == 0:
          os.system('espeak -v polish  "Otwarto okno 2 w dużym pokoju"')
          o2 = 1

      if MySwitch & 0b00000100 == 0b00000100:
        if o3 == 1:
          os.system('espeak -v polish  "Zamknięto okno 3 w dużym pokoju"')
          o3 = 0
      else:
        if o3 == 0:
          os.system('espeak -v polish  "Otwarto okno 3 w dużym pokoju"')
          o3 = 1

      if MySwitch & 0b00001000 == 0b00001000:
        if o4 == 1:
          os.system('espeak -v polish  "Zamknięto okno 1 w małym pokoju"')
          o4 = 0
      else:
        if o4 == 0:
          os.system('espeak -v polish  "Otwarto okno 1 w małym pokoju"')
          o4 = 1

      if MySwitch & 0b00010000 == 0b00010000:
        if o5 == 1:
          os.system('espeak -v polish  "Zamknięto okno 2 w małym pokoju"')
          o5 = 0
      else:
        if o5 == 0:
          os.system('espeak -v polish  "Otwarto okno 2 w małym pokoju"')
          o5 = 1

      if MySwitch & 0b00100000 == 0b00100000:
        if o6 == 1:
          os.system('espeak -v polish  "Zamknięto okno 1 w kuchni"')
          o6 = 0
      else:
        if o6 == 0:
          os.system('espeak -v polish  "Otwarto okno 1 w kuchni"')
          o6 = 1

      if MySwitch & 0b01000000 == 0b01000000:
        if o7 == 1:
          os.system('espeak -v polish  "Zamknięto okno 2 w kuchni"')
          o7 = 0
      else:
        if o7 == 0:
          os.system('espeak -v polish  "Otwarto okno 2 w kuchni"')
          o7 = 1

      if MySwitch & 0b10000000 == 0b10000000:
        if d1 == 1:
          os.system('espeak -v polish  "Zamknięto drzwi wejściowe"')
          d1 = 0
      else:
        if d1 == 0:
          os.system('espeak -v polish  "Otwarto drzwi wejściowe"')
          d1 = 1
      time.sleep(1)    


class Alarm:

    def __init__(self):
        print 'Starting alarm handler'

        self.alarm_handler = threading.Thread(target=self.handle_alarm, args=())
        self.alarm_handler.start()

    def handle_alarm(self):
        os.system('espeak -v polish  "Uruchamiam alarm"')
        bus2 = smbus.SMBus(1)  # Rev 2 Pi uses 1

        DEVICE2 = 0x27  # Device address (A0-A2)
        IODIRA2 = 0x00  # Pin direction register
        OLATA2 = 0x14  # Register for outputs
        GPIOA2 = 0x12  # Register for inputs

        o1 = 0
        o2 = 0
        o3 = 0
        o4 = 0
        o5 = 0
        o6 = 0
        o7 = 0
        d1 = 0

        # Set first 7 GPA pins as outputs and
        # last one as input.
        bus2.write_byte_data(DEVICE2, IODIRA2, 0xFF)

        while True:

            # Read state of GPIOA register
            MySwitch = bus2.read_byte_data(DEVICE2, GPIOA2)

            if MySwitch & 0b00000001 == 0b00000001:
                if o1 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 1 w dużym pokoju"')
                    o1 = 0
            else:
                if o1 == 0:
                    os.system('espeak -v polish  "Otwarto okno 1 w dużym pokoju"')
                    o1 = 1

            if MySwitch & 0b00000010 == 0b00000010:
                if o2 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 2 w dużym pokoju"')
                    o2 = 0
            else:
                if o2 == 0:
                    os.system('espeak -v polish  "Otwarto okno 2 w dużym pokoju"')
                    o2 = 1

            if MySwitch & 0b00000100 == 0b00000100:
                if o3 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 3 w dużym pokoju"')
                    o3 = 0
            else:
                if o3 == 0:
                    os.system('espeak -v polish  "Otwarto okno 3 w dużym pokoju"')
                    o3 = 1

            if MySwitch & 0b00001000 == 0b00001000:
                if o4 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 1 w małym pokoju"')
                    o4 = 0
            else:
                if o4 == 0:
                    os.system('espeak -v polish  "Otwarto okno 1 w małym pokoju"')
                    o4 = 1

            if MySwitch & 0b00010000 == 0b00010000:
                if o5 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 2 w małym pokoju"')
                    o5 = 0
            else:
                if o5 == 0:
                    os.system('espeak -v polish  "Otwarto okno 2 w małym pokoju"')
                    o5 = 1

            if MySwitch & 0b00100000 == 0b00100000:
                if o6 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 1 w kuchni"')
                    o6 = 0
            else:
                if o6 == 0:
                    os.system('espeak -v polish  "Otwarto okno 1 w kuchni"')
                    o6 = 1

            if MySwitch & 0b01000000 == 0b01000000:
                if o7 == 1:
                    os.system('espeak -v polish  "Zamknięto okno 2 w kuchni"')
                    o7 = 0
            else:
                if o7 == 0:
                    os.system('espeak -v polish  "Otwarto okno 2 w kuchni"')
                    o7 = 1

            if MySwitch & 0b10000000 == 0b10000000:
                if d1 == 1:
                    os.system('espeak -v polish  "Zamknięto drzwi wejściowe"')
                    d1 = 0
            else:
                if d1 == 0:
                    os.system('espeak -v polish  "Otwarto drzwi wejściowe"')
                    d1 = 1
            time.sleep(1)




os.system('/opt/vol.sh 100')
os.system('espeak -v polish  "Inicjuję ekspandery"')
relay_init()

alarm_instance = Alarm()

os.system('espeak -v polish  "Uruchamiam system"')
os.system('espeak -v polish  "Witamy w systemie Supernova. Funkcje inteligentnego domu zostały aktywowane."')
run(host='0.0.0.0', port=8080)

os.system('espeak -v polish  "Wyłączam system. Dziękujemy za skorzystanie z oprogramowania Adrianozy Didżital Studio. Miłego dnia."')




#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import os
import threading

from bottle import route, run, template


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

talk=1

@route('/talk/<val>')
def set_talk(val):
    global talk
    if ( val == 1 ):
        talk=1
    else:
        talk=0

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
        if ( talk == 1 ):
            os.system('espeak -v polish  "Włączam światło w małym pokoju"')
    if ( relay == 'a2' ):
        a2 = 0
        if ( talk == 1 ):
            os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
    if ( relay == 'a3' ):
        a3 = 0
        if ( talk == 1 ):
            os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
    if ( relay == 'a4' ):
        a4 = 0
        if ( talk == 1 ):
            os.system('espeak -v polish  "Włączam światło w przedpokoju"')
    if ( relay == 'a5' ):
        a5 = 0
        if ( talk == 1 ):
            os.system('espeak -v polish  "Włączam światło w przedpokoju"')
    if ( relay == 'a6' ):
        a6 = 0
    if ( relay == 'a7' ):
        a7 = 0

    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo {{relay}}:  {{val}}</b>!', relay=relay, val=val)


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
      if ( talk == 1 ):
            os.system('espeak -v polish  "Wyłączam światło w małym pokoju"')
    if ( relay == 'a2' ):
        a2 = 1
        if ( talk == 1 ):
            os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
    if ( relay == 'a3' ):
        a3 = 1
        if ( talk == 1 ):
            os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
    if ( relay == 'a4' ):
        a4 = 1
        if ( talk == 1 ):
            os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
    if ( relay == 'a5' ):
        a5 = 1
        if ( talk == 1 ):
            os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
    if ( relay == 'a6' ):
        a6 = 1
    if ( relay == 'a7' ):
        a7 = 1

    abin='0b'+str(a7)+str(a6)+str(a5)+str(a4)+str(a3)+str(a2)+str(a1)+str(a0)
    a=int(abin, 2)
    bus.write_byte_data(DEVICE,OLATA,a)

    return template('<b>Swiatlo {{relay}}:  {{val}}</b>!', relay=relay, val=val)

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
            relay_enable(a0)
        else:
            relay_disable(a0)
    if ( relay == 'a1' ):
        if ( a1 == 1 ):
            relay_enable(a1)
        else:
            relay_disable(a1)
    if ( relay == 'a2' ):
        if ( a2 == 1 ):
            relay_enable(a2)
        else:
            relay_disable(a2)
    if ( relay == 'a3' ):
        if ( a3 == 1 ):
            relay_enable(a3)
        else:
            relay_disable(a3)
    if ( relay == 'a4' ):
        if ( a4 == 1 ):
            relay_enable(a4)
        else:
            a4=1
    if ( relay == 'a5' ):
        if ( a5 == 1 ):
            relay_enable(a5)
        else:
            relay_disable(a5)
    if ( relay == 'a6' ):
        if ( a6 == 1 ):
            relay_enable(a6)
        else:
            relay_disable(a6)
    if ( relay == 'a7' ):
        if ( a7 == 1 ):
            relay_enable(a7)
        else:
            relay_disable(a7)


def relay_init():
    # Set all GPA pins as outputs by setting
    # all bits of IODIRA register to 0
    bus.write_byte_data(DEVICE,IODIRA,0x00)

    # Set output all 7 output bits to 1
    bus.write_byte_data(DEVICE,OLATA,255) 


class SmartServer:

    def __init__(self):
        print 'Starting server handler'
        self.server_handler = threading.Thread(target=self.handle_server, args=())
        self.server_handler.start()

    def handle_server(self):
        os.system('espeak -v polish  "Inicjuję przekaźniki"')
        relay_init()

        os.system('espeak -v polish  "Uruchamiam system"')
        os.system('espeak -v polish  "Witamy w systemie Supernova. Funkcje inteligentnego domu zostały aktywowane."')
        run(host='0.0.0.0', port=8080)

        os.system('espeak -v polish  "Wyłączam system. Dziękujemy za skorzystanie z oprogramowania Adrianozy Didżital Studio. Miłego dnia."')


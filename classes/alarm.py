#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import os
import threading


class Alarm(threading.Thread):

    def __init__(self):
        print('alarm init')
        threading.Thread.__init__(self)


    def run(self):
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

    def dupa(self):
        os.system('espeak -v polish  "Dupa"')

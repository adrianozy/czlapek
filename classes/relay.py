#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import os
from classes.gadacz import Gadacz





class Relay():

    bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

    DEVICE = 0x20  # Device address (A0-A2)
    IODIRA = 0x00  # Pin direction register
    OLATA = 0x14  # Register for outputs
    GPIOA = 0x12  # Register for inputs

    a0 = 1
    a1 = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    a6 = 1
    a7 = 1

    def __init__(self, gadacz):
        # Set all GPA pins as outputs by setting
        # all bits of IODIRA register to 0
        self.bus.write_byte_data(self.DEVICE, self.IODIRA, 0x00)

        # Set output all 7 output bits to 1
        self.bus.write_byte_data(self.DEVICE, self.OLATA, 255)

        self.gadacz = gadacz


    def relay_status(self, relay):

        if (relay == 'a0'):
            if (self.a0 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a1'):
            if (self.a1 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a2'):
            if (self.a2 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a3'):
            if (self.a3 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a4'):
            if (self.a4 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a5'):
            if (self.a5 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a6'):
            if (self.a6 == 1):
                return 'OFF'
            else:
                return 'ON'
        if (relay == 'a7'):
            if (self.a7 == 1):
                return 'OFF'
            else:
                return 'ON'

    def relay_toogle(self, relay):

        if (relay == 'a0'):
            if (self.a0 == 1):
                self.a0 = 0
            else:
                self.a0 = 1
        elif (relay == 'a1'):
            if (self.a1 == 1):
                self.a1 = 0
                self.gadacz.add('a1on')
            else:
                self.a1 = 1
                self.gadacz.add('a1off')
        elif (relay == 'a2'):
            if (self.a2 == 1):
                self.a2 = 0
                self.gadacz.add('a2on')
            else:
                self.a2 = 1
                self.gadacz.add('a2off')
        elif (relay == 'a3'):
            if (self.a3 == 1):
                self.a3 = 0
                self.gadacz.add('a3on')
            else:
                self.a3 = 1
                self.gadacz.add('a3off')
        elif (relay == 'a4'):
            if (self.a4 == 1):
                self.a4 = 0
                self.gadacz.add('a4on')
            else:
                a4 = 1
                self.gadacz.add('a4off')
        elif (relay == 'a5'):
            if (self.a5 == 1):
                self.a5 = 0
                self.gadacz.add('a5on')
            else:
                self.a5 = 1
                self.gadacz.add('a5off')
        elif (relay == 'a6'):
            if (self.a6 == 1):
                self.a6 = 0
            else:
                self.a6 = 1
        elif (relay == 'a7'):
            if (self.a7 == 1):
                self.a7 = 0
            else:
                self.a7 = 1

        abin = '0b' + str(self.a7) + str(self.a6) + str(self.a5) + str(self.a4) + str(self.a3) + str(self.a2) + str(self.a1) + str(self.a0)
        a = int(abin, 2)
        self.bus.write_byte_data(self.DEVICE, self.OLATA, a)
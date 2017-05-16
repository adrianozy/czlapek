#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import os
import threading
from classes.gadacz import Gadacz

class Alarm(threading.Thread):

    def __init__(self, gadacz):
        print('alarm init')
        threading.Thread.__init__(self)
        self.gadacz = gadacz

    def run(self):
        self.gadacz.add('alarm-on')
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
                    self.gadacz.add('o1close')
                    o1 = 0
            else:
                if o1 == 0:
                    self.gadacz.add('o1open')
                    o1 = 1

            if MySwitch & 0b00000010 == 0b00000010:
                if o2 == 1:
                    self.gadacz.add('o2close')
                    o2 = 0
            else:
                if o2 == 0:
                    self.gadacz.add('o2open')
                    o2 = 1

            if MySwitch & 0b00000100 == 0b00000100:
                if o3 == 1:
                    self.gadacz.add('o3close')
                    o3 = 0
            else:
                if o3 == 0:
                    self.gadacz.add('o3open')
                    o3 = 1

            if MySwitch & 0b00001000 == 0b00001000:
                if o4 == 1:
                    self.gadacz.add('o4close')
                    o4 = 0
            else:
                if o4 == 0:
                    self.gadacz.add('o4open')
                    o4 = 1

            if MySwitch & 0b00010000 == 0b00010000:
                if o5 == 1:
                    self.gadacz.add('o5close')
                    o5 = 0
            else:
                if o5 == 0:
                    self.gadacz.add('o5open')
                    o5 = 1

            if MySwitch & 0b00100000 == 0b00100000:
                if o6 == 1:
                    self.gadacz.add('o6close')
                    o6 = 0
            else:
                if o6 == 0:
                    self.gadacz.add('o6open')
                    o6 = 1

            if MySwitch & 0b01000000 == 0b01000000:
                if o7 == 1:
                    self.gadacz.add('o7close')
                    o7 = 0
            else:
                if o7 == 0:
                    self.gadacz.add('o7open')
                    o7 = 1

            if MySwitch & 0b10000000 == 0b10000000:
                if d1 == 1:
                    self.gadacz.add('d1close')
                    d1 = 0
            else:
                if d1 == 0:
                    self.gadacz.add('d1close')
                    d1 = 1
            time.sleep(1)

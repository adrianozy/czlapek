#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import threading
import os

class Gadacz(threading.Thread):

    list = []

    def __init__(self):
        print('gadacz init')
        threading.Thread.__init__(self)

    def add(self, task):
        self.list.append(task)

    def run(self):

        while True:
            size = len(self.list)
            if (size > 0):
                task = self.list.pop(0)
                if (task == 'a1on'):
                    os.system('espeak -v polish  "Włączam światło w małym pokoju"')
                elif (task == 'a1off'):
                    os.system('espeak -v polish  "Wyłączam światło w małym pokoju"')
                elif (task == 'a2on'):
                    os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
                elif (task == 'a2off'):
                    os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
                elif (task == 'a3on'):
                    os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
                elif (task == 'a3off'):
                    os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
                elif (task == 'a4on'):
                    os.system('espeak -v polish  "Włączam światło w przedpokoju"')
                elif (task == 'a4off'):
                    os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
                elif (task == 'a5on'):
                    os.system('espeak -v polish  "Włączam światło w przedpokoju"')
                elif (task == 'a5off'):
                    os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
                elif (task == 'alarm-on'):
                    os.system('espeak -v polish  "Uruchamiam alarm"')
                else:
                    os.system('espeak -v polish  "Gadam bzdury jak mało który"')

            time.sleep(1)
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import threading
import os
import pygame

class Gadacz(threading.Thread):

    list = []
    okna = 1
    drzwi = 1
    swiatlo = 1

    def __init__(self):
        print('gadacz init')
        pygame.mixer.init()
        threading.Thread.__init__(self)

    def add(self, task):
        self.list.append(task)

    def toggle(self, val):
        if (val == 'okna'):
            if (self.okna == 1):
                self.okna = 0
            else:
                self.okna = 1
        if (val == 'drzwi'):
            if (self.drzwi == 1):
                self.drzwi = 0
            else:
                self.drzwi = 1
        if (val == 'swiatlo'):
            if (self.swiatlo == 1):
                self.swiatlo = 0
            else:
                self.swiatlo = 1

    def status(self, val):
        if (val == 'okna'):
            return self.okna
        if (val == 'drzwi'):
            return self.drzwi
        if (val == 'swiatlo'):
            return self.swiatlo

    def run(self):

        while True:
            size = len(self.list)
            if (size > 0):
                task = self.list.pop(0)
                if (task == 'a1on'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Włączam światło w małym pokoju"')
                elif (task == 'a1off'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Wyłączam światło w małym pokoju"')
                elif (task == 'a2on'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
                elif (task == 'a2off'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
                elif (task == 'a3on'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Włączam światło w dużym pokoju"')
                elif (task == 'a3off'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Wyłączam światło w dużym pokoju"')
                elif (task == 'a4on'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Włączam światło w przedpokoju"')
                elif (task == 'a4off'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
                elif (task == 'a5on'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Włączam światło w przedpokoju"')
                elif (task == 'a5off'):
                    if (self.swiatlo == 1):
                        os.system('espeak -v polish  "Wyłączam światło w przedpokoju"')
                elif (task == 'alarm-on'):
                    os.system('espeak -v polish  "Uruchamiam alarm"')
                elif (task == 'o1open'):
                    #os.system('espeak -v polish  "Otwarto okno 1 w dużym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o1close'):
                    #os.system('espeak -v polish  "Zamknięto okno 1 w dużym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o2open'):
                    #os.system('espeak -v polish  "Otwarto okno 2 w dużym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o2close'):
                    #os.system('espeak -v polish  "Zamknięto okno 2 w dużym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o3open'):
                    #os.system('espeak -v polish  "Otwarto okno 3 w dużym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o3close'):
                    #os.system('espeak -v polish  "Zamknięto okno 3 w dużym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o4open'):
                    #os.system('espeak -v polish  "Otwarto okno 1 w małym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o4close'):
                    #os.system('espeak -v polish  "Zamknięto okno 1 w małym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o5open'):
                    #os.system('espeak -v polish  "Otwarto okno 2 w małym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o5close'):
                    #os.system('espeak -v polish  "Zamknięto okno 2 w małym pokoju"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o6open'):
                    #os.system('espeak -v polish  "Otwarto okno 1 w kuchni"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o6close'):
                    #os.system('espeak -v polish  "Zamknięto okno 1 w kuchni"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o7open'):
                    #os.system('espeak -v polish  "Otwarto okno 2 w kuchni"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o7close'):
                    #os.system('espeak -v polish  "Zamknięto okno 2 w kuchni"')
                    if (self.okna == 1):
                        pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'd1open'):
                    #os.system('espeak -v polish  "Otwarto drzwi wejściowe"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'd1close'):
                    if (self.drzwi == 1):
                        os.system('espeak -v polish  "Zamknięto drzwi wejściowe"')
                else:
                    if (self.drzwi == 1):
                        os.system('espeak -v polish  "Gadam bzdury jak mało który"')

            time.sleep(0.2)

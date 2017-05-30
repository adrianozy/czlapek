#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import threading
import os
import pygame

class Gadacz(threading.Thread):

    list = []

    def __init__(self):
        print('gadacz init')
        pygame.mixer.init()
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
                elif (task == 'o1open'):
                    #os.system('espeak -v polish  "Otwarto okno 1 w dużym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o1close'):
                    #os.system('espeak -v polish  "Zamknięto okno 1 w dużym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o2open'):
                    #os.system('espeak -v polish  "Otwarto okno 2 w dużym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o2close'):
                    #os.system('espeak -v polish  "Zamknięto okno 2 w dużym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o3open'):
                    #os.system('espeak -v polish  "Otwarto okno 3 w dużym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o3close'):
                    #os.system('espeak -v polish  "Zamknięto okno 3 w dużym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o4open'):
                    #os.system('espeak -v polish  "Otwarto okno 1 w małym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o4close'):
                    #os.system('espeak -v polish  "Zamknięto okno 1 w małym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o5open'):
                    #os.system('espeak -v polish  "Otwarto okno 2 w małym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o5close'):
                    #os.system('espeak -v polish  "Zamknięto okno 2 w małym pokoju"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o6open'):
                    #os.system('espeak -v polish  "Otwarto okno 1 w kuchni"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o6close'):
                    #os.system('espeak -v polish  "Zamknięto okno 1 w kuchni"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'o7open'):
                    #os.system('espeak -v polish  "Otwarto okno 2 w kuchni"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'o7close'):
                    #os.system('espeak -v polish  "Zamknięto okno 2 w kuchni"')
                    pygame.mixer.Sound("/opt/sounds/close.wav").play()
                elif (task == 'd1open'):
                    #os.system('espeak -v polish  "Otwarto drzwi wejściowe"')
                    pygame.mixer.Sound("/opt/sounds/open.wav").play()
                elif (task == 'd1close'):
                    os.system('espeak -v polish  "Zamknięto drzwi wejściowe"')
                else:
                    os.system('espeak -v polish  "Gadam bzdury jak mało który"')

            time.sleep(0.5)

import os
import csv
import time
import enum
import pygame
import random
import ctypes
import pathlib
import threading
import threading
import screeninfo
import mysql.connector
import arabic_reshaper
from Server import Server
from ctypes import wintypes
from dataclasses import dataclass
from bidi.algorithm import get_display
from pygame._sdl2.video import Window

class Data(enum.Enum):
    DEBUG = False
    SERVER = True
    CSV = True

@dataclass
class DispalyWindow:
    font_size = 20
    distans_up = 40
    font = 'Calibri'
    size = [500, 60]
    display_flags = 0
    distans_right = 20
    move_speed = 150000
    starting_sentens = (20, 25)
    type_speed = (.04, .05, .06)
    background_color = (0, 0, 0)
    words_color = (200, 100, 150)
    position = (screeninfo.get_monitors()[0].width - size[0], 0)
    pygame_icon = pygame.image.load('logo.png')
    move = size[0]

class TeachLanguageScript:
    def __init__(self) -> None:
        self.data = {}
        self.server = Server()
        self.run_thread = True
        #--------------------------------
        self._start_thread = False
        self._question_started = False
        self._range_timer = range(30*60, 61*60)
        self._answer_time = (15*60)
        self.output_answer = None
        self.input_answer = None
        #--------------------------------
        self.data = self.read_data_from_csvfile()
        self.word_asking = None
        self.asked_words = None

    def answer_question(self, the_answer:str):
        time.sleep(1)
        return True

    def ask_question(self, text:str, translat:str=None, namewindow:str='English Question'):
        letters = ''
        pygame.init()
        pygame.display.set_caption(str(namewindow))
        font = pygame.font.SysFont(DispalyWindow.font, DispalyWindow.font_size)
        screen = pygame.display.set_mode(DispalyWindow.size, DispalyWindow.display_flags)
        pygame.display.set_icon(DispalyWindow.pygame_icon)
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)

        #------------------------------------------------
        hwnd = pygame.display.get_wm_info()['window']
        user32 = ctypes.WinDLL("user32")
        user32.SetWindowPos.restype = wintypes.HWND
        user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, 
                                        wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
        #------------------------------------------------
        for count in range(DispalyWindow.move):
            user32.SetWindowPos(hwnd, -1, 
                                DispalyWindow.position[0] + DispalyWindow.move - (count + DispalyWindow.distans_right),
                                DispalyWindow.position[1] - DispalyWindow.distans_up, 
                                0, 0, 0x0001)
            time.sleep(.0005 + count/DispalyWindow.move_speed)
            
        for letter in str(bidi_text):
            letters += letter
            pygame.event.get()
            screen.fill(DispalyWindow.background_color)
            pygame.display.flip()
            user32.SetWindowPos(hwnd, -1, 
                                DispalyWindow.position[0] - DispalyWindow.distans_right,
                                DispalyWindow.position[1] - DispalyWindow.distans_up, 
                                0, 0, 0x0001)
            image = font.render(letters, True, DispalyWindow.words_color)
            screen.blit(image, DispalyWindow.starting_sentens)
            pygame.display.flip()
            time.sleep(random.choice(DispalyWindow.type_speed))

        while True:
            pygame.event.get()
            pygame.display.flip()
            user32.SetWindowPos(hwnd, -1, 
                                DispalyWindow.position[0] - DispalyWindow.distans_right,
                                DispalyWindow.position[1] - DispalyWindow.distans_up, 
                                0, 0, 0x0001)
            answer = self.answer_question(str(translat))
            if answer is True:
                break
        
        for count in range(DispalyWindow.move):
            pygame.event.get()
            pygame.display.flip()
            user32.SetWindowPos(hwnd, -1, 
                                DispalyWindow.position[0] + (count + DispalyWindow.distans_right),
                                DispalyWindow.position[1] - DispalyWindow.distans_up, 
                                0, 0, 0x0001)
            time.sleep(.0005 + count/DispalyWindow.move_speed)
        pygame.quit()
        return answer
         
    def read_data_from_server(self):
        print(self.server.databases('language_script', 'english_to_persian'))
        print(self.server.add_in_database(['helqewq', 'me']))
        pass

    def read_data_from_csvfile(self, csv_file_names:list= ['EN_to_PR.csv']) -> dict:
        if Data.CSV:
            out_data = {}
            split_sign = '='
            key_point_sign = '*'
            PATH_HOME = pathlib.Path.home() / './DataLanguage/'
            if not PATH_HOME.exists():
                PATH_HOME.mkdir(parents=True, exist_ok=True)
            
            for file_name in csv_file_names:
                FILE = pathlib.Path.home() / f'./DataLanguage/{file_name}'
                if not FILE.exists():
                    open(PATH_HOME / file_name, 'w+')
                
                with open(PATH_HOME / file_name, 'r+', encoding='utf-8') as csv_file:
                    out = csv.reader(csv_file)
                    for translats in out:
                        if not translats:
                            continue
                    
                        translat_sentenc = str(", ").join(map(lambda x:str(x), translats))
                        if key_point_sign in translat_sentenc:
                            out_data['key point'] = translat_sentenc
                            return out_data

                        if not split_sign in translat_sentenc:
                            part_one, part_two = translat_sentenc, None
                        else:
                            part_one, part_two, *part_three = translat_sentenc.split(split_sign)
                        if part_two:
                            part_two = (part_two.strip()).capitalize()
                        part_one = (part_one.strip()).capitalize()
                        out_data[part_one] = part_two
            return out_data
        return
    
    def updat_data(self, list_words):
        pass

    def app_bloker(self):
        pass
    
    def shut_down(self):
        pass
    
    def start_asking(self) -> None:
        if not self.run_thread:
            return False
        try:
            if not self._start_thread:
                self._start_thread = True
                self.obj_thread = threading.Thread(target= self.ask_question)
                self.obj_thread.start()
            return True
        except:
            return False

    def start_timer(self) -> None:
        if not self.run_thread:
            return False
        try:
            if not self._start_thread:
                self._start_thread = True
                self.obj_thread = threading.Thread(target= self.when)
                self.obj_thread.start()
            return True
        except:
            return False
        
    def when(self) -> None:
        self._question_started = False
        if not self.run_thread:
            return
        after_time = random.choice(self._range_timer)
        time.sleep(after_time)
        self._question_started = True
        self._start_thread = False
        return

    def todo(self, text_question:str):
        self.start_timer()
        if self._question_started:
            self.ask_question()
            keys = self.data.keys()
            if keys:
                key = random.choice(keys)
                self.word_asking = key
                text_question = text_question + ' ' + key
                self.ask_question(text_question, data[key])



obj = TeachLanguageScript() 

# translat = obj.read_data_from_csvfile()
data = obj.read_data_from_csvfile()

for word, translat in data.items():
    # obj.start_timer()
    # obj.answer_question(translat)
    obj.ask_question(text=f'what is means of this {word}', translat=translat)
    # obj.starting(1)
    if obj._question_started:
        print('hello')
    a = 50 - len(word)
    s = a*' ' + '|'
    print(word, s, translat)
    time.sleep(5)

print(translat)
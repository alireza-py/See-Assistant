# import pathlib
# import logging
# import mysql.connector
# import csv

# read_data = {}
# split_sign = ':'
# csv_file_names = ['EN_to_PR.csv']

# PATH_HOME = pathlib.Path.home() / './DataLanguage/'
# if not PATH_HOME.exists():
#     PATH_HOME.mkdir(parents=True, exist_ok=True)

# for file_name in csv_file_names:
#     FILE = pathlib.Path.home() / f'./DataLanguage/{file_name}'
#     if not FILE.exists():
#         open(PATH_HOME / file_name, 'w+')

#     with open(PATH_HOME / file_name, 'r+', encoding='utf-8') as FileCsv:
#         file_out = csv.reader(FileCsv)
#         for text in file_out:
#             if not text:
#                 continue
#             text = text[0]
#             if not split_sign in text:
#                 english, persian = text, str()
#             else:
#                 english, persian = text.split(split_sign)
#             english = (english.strip()).capitalize()
#             persian = (persian.strip()).capitalize()
            
#             read_data[english] = persian
# print(read_data)

# import mysql.connector
# # import pymysql

# data = mysql.connector.connect(user = 'root', password = 'root23231',
#                             host = '127.0.0.1')
# data_cursor = data.cursor()
# user = data_cursor.fetchall()
# print(user)
# # data_cursor.execute("CREATE DATABASE test_database")
# data_cursor.execute("SHOW DATABASES")
# print(list(map(lambda x:x[0] ,data_cursor)))
# # for a in data_cursor:
# #     print(a)
# # data_cursor.execute('SELECT * FROM karmand1;')
# # lists = []
# # for (Name, Weight, Height) in data_cursor:
#     # lists.append((Name.strip(), Weight, Height))
# # lists = sorted(reversed(sorted(lists,key= lambda x:x[1])),key= lambda x:x[2])

# # for info in reversed(lists):
#     # print(info[0],info[2],info[1])

# data.close()

# import pygame
# from random import choice
# import time

# speed_of_writing_the_words = (.05, .1, .15, .2, .25)
# background_color = (234, 212, 252)
# pygame.init()
# sysfont = pygame.font.get_default_font()
# pygame.display.set_caption(str('hello'))
# screen = pygame.display.set_mode((300, 300))
# screen.fill(background_color)
# font = pygame.font.SysFont(sysfont, 25)
# text = 'hello how are you ? my name is alireza khani and what is your name'
# append = ''
# for calameh in text:
#     append += calameh
#     add = len(append)
#     if add%25 == 0:
#         append += '\n'
#     screen.fill(background_color)
#     pygame.display.update()
#     # font = pygame.font.SysFont(sysfont, 25)
#     image = font.render(append, True, (255,0,0))
#     screen.blit(image, (20, 20))
#     pygame.display.update()
#     time.sleep(choice(speed_of_writing_the_words))



# running = True
# while running:
#     for event in pygame.event.get():      
#         if event.type == pygame.QUIT:
#             running = False

# # Define the background colour
# # using RGB color coding.
# background_colour = (234, 212, 252)
  
# # Define the dimensions of
# # screen object(width,height)
# pygame.init()
# sysfont = pygame.font.get_default_font()
# screen = pygame.display.set_mode((300, 300))
# font = pygame.font.SysFont(None, 10)

# pygame.display.set_caption('Geeksforgeeks')
# img = font.render(sysfont, True, (255,0,0))
# # rect = img.get_rect()
# # pygame.draw.rect(img, BLUE, rect, 1)
  
# # Fill the background colour to the screen
# screen.fill(background_colour)
  
# # Update the display using flip
# pygame.display.flip()
# screen.blit(img, (20, 20))
# # Variable to keep our game loop running
# running = True
  
# # game loop
# while running:
    
# # for loop through the event queue  
    
#     for event in pygame.event.get():
      
#         # Check for QUIT event      
#         if event.type == pygame.QUIT:
#             running = False

# import pygame
# from pygame.locals import *
# import time
 
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# GRAY = (200, 200, 200)

# pygame.init()
# screen = pygame.display.set_mode((640, 240))

# sysfont = pygame.font.get_default_font()

# t0 = time.time()
# font = pygame.font.SysFont(None, 25)
# print('time needed for Font creation :', time.time()-t0)

# img = font.render(sysfont, True, RED)
# rect = img.get_rect()
# pygame.draw.rect(img, BLUE, rect, 1)

# font1 = pygame.font.SysFont('chalkduster.ttf', 72)
# img1 = font1.render('chalkduster.ttf', True, BLUE)

# font2 = pygame.font.SysFont('didot.ttc', 72)
# img2 = font2.render('didot.ttc', True, GREEN)

# fonts = pygame.font.get_fonts()
# print(len(fonts))
# for i in range(7):
#     print(fonts[i])

# running = True
# background = GRAY
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False

#     screen.fill(background)
#     screen.blit(img, (20, 20))
#     screen.blit(img1, (20, 50))
#     screen.blit(img2, (20, 120))
#     pygame.display.update()

# pygame.quit()




# import pygame
# import sys
# from pygame.locals import *

# white = (255,255,255)
# black = (0,0,0)
# red = (255, 0, 0)

# class Pane(object):
#     def __init__(self):
#         pygame.init()
#         self.font = pygame.font.SysFont('Arial', 25)
#         pygame.display.set_caption('Box Test')
#         self.screen = pygame.display.set_mode((600,400), 0, 32)
#         self.screen.fill((white))
#         pygame.display.update()


#     def addRect(self):
#         self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
#         pygame.display.update()

#     def addText(self):
#         self.screen.blit(self.font.render('Hello!', True, black), (200, 100))
#         pygame.display.update()

#     def addText2(self):
#         self.screen.blit(self.font.render('Hello!', True, red), (200, 100))
#         pygame.display.update()


#     def functionApp(self):
#         if __name__ == '__main__':
#             self.addRect()
#             self.addText()
#             while True:
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         pygame.quit(); sys.exit();

#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_ESCAPE:
#                             self.screen.fill(white)
#                             self.addRect()
#                             self.addText2() #i made it so it only changes colour once.



# display = Pane()
# display.functionApp()



# from screeninfo import get_monitors
# print(get_monitors()[0].width)



# import pygame
# import ctypes
# from ctypes import wintypes 

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((400, 200))
    
#     hwnd = pygame.display.get_wm_info()['window']
    
#     user32 = ctypes.WinDLL("user32")
#     user32.SetWindowPos.restype = wintypes.HWND
#     user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
#     user32.SetWindowPos(hwnd, -1, 600, 300, 0, 0, 0x0001)
    
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#         screen.fill('grey')
#         pygame.display.flip()

# if __name__ == '__main__':
#     main()

# import sys
# from tkinter import *

# def main(argv):
#     root = Tk()
#     root.update()
#     root.tk.call('package','require','Winico')
#     id = root.tk.call('winico','createfrom',argv[1])
#     root.tk.call('winico','setwindow',root,id,'big',0)
#     root.mainloop()
#     return 0

# if __name__=='__main__':
#     sys.exit(main(sys.argv))


# import wx


# app = wx.ic()

# app.()

# import os
# from os import kill
# from os import getpid
# from signal import SIGILL
# from time import sleep
# # get the pid of the current process
# pid = getpid()
# h = os.getppid()
# # report a message
# # print(pid, h)
# print(f'Running with pid: {pid}')
# # attempt to kill the current process
# kill(h, SIGILL)
# # report a message
# print('Skill running')
# sleep(1)

# import wmi
 
# # Initializing the wmi constructor
# f = wmi.WMI()
 
# # Printing the header for the later columns
# print("pid   Process name")
 
# # Iterating through all the running processes
# for process in f.Win32_Process():
     
#     # Displaying the P_ID and P_Name of the process
#     print(f"{process.ProcessId:<10} {process.Name}")
import random

a = []

if a:
    print(a)
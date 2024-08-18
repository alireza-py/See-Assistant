from re import findall
from speech import say
from read_pickle import read, key_sentences
# from jarvis import assistant
from winsound import Beep
from time import sleep
from os import system
from helloSoLiD import startsolid, closesolid, make, edit

class movements:
    def __init__(self) -> None:
            pass

    def movement(self, sentenc: str, data: dict):
        # print(sentenc)
        if findall(r'(hello|hi)', sentenc):
            say(key_sentences(sentenc),value= data['volume_assis'])
        
        if findall(r'how are you', sentenc):
            say(key_sentences(sentenc),value= data['volume_assis'])

        if findall(r'open solid work', sentenc) or findall(r'سالیدورک و باز کن', sentenc):
            say(key_sentences(sentenc),value= data['volume_assis'])
            sleep(.8)
            startsolid()
        
        if findall(r'close solid work', sentenc):
            say(key_sentences(sentenc),value= data['volume_assis'])
            sleep(.8)
            closesolid()

        if findall(r'explain platform', sentenc):
            for text in data['all_info']:
                print(text[2:-2])
                say(text[2:-2],value= data['volume_assis'])
            

        if findall(r'(shut down|turn off) my computer', sentenc):
            say(key_sentences(sentenc),value= data['volume_assis'])
            sleep(0.8); system('Shutdown /p')

        if findall(r'(turn down your volume|bring your volume down)', sentenc):
            if data['volume_assis'] <= 1.0 and data['volume_assis'] > 0.0:
                data['volume_assis'] = data['volume_assis'] - 0.2
            say(key_sentences(sentenc),value= data['volume_assis'])

        if findall(r"(shut down yourself|i don't work with you)", sentenc):
            say(key_sentences(sentenc),value= data['volume_assis'])
            sleep(0.7)
            exit()

        if findall(r'(turn up your volume|bring your volume up)', sentenc):
            if data['volume_assis'] < 1.0 and data['volume_assis'] >= 0.0:
                data['volume_assis'] = data['volume_assis'] + 0.2
            say(key_sentences(sentenc),value= data['volume_assis'])

        if findall(r'shut up', sentenc):
            data['volume_assis'] = 0
            for a in range(1, 3):
                Beep(int(3000//1.4)*a, 70)
    
        if findall(r'mute', sentenc):
            data['volume_computer'] = 0
        
        if ' ' == sentenc:
            say(key_sentences(sentenc),value= data['volume_assis'])

    

        # if findall(r'(shut down|turn off) my computer', sentenc):
        #     self.say(key_sentences(sentenc))
        #     sleep(0.8); system('Shutdown /p')

        # if findall(r'(shut down|turn off) my computer', sentenc):
        #     self.say(key_sentences(sentenc))
        #     sleep(0.8); system('Shutdown /p')

        return data
       
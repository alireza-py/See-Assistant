from random import randint
from pyttsx3 import init

def say(text: str , mr_or_mis: int = 1, value: float = 1):
    try:
            
        my_object = init()
        my_object.setProperty('volume', value)
        my_object.setProperty('rate',speed_say())
        mr_and_mis = my_object.getProperty('voices')[mr_or_mis]
        my_object.setProperty('voice', mr_and_mis.id)
        my_object.say(text)
        my_object.runAndWait()
        return 'Ok'

    except: return 'I can not speech'

def speed_say(s1: int = 140, s2: int = 160):
    return randint(s1, s2)

# def typing(self, text:str):
#     for word in text:
#         print()

    


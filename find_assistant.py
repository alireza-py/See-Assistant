from unicodedata import name
from re import search, findall, sub

names = {'see':'en' , 'علی':'per'}

class name_of_assistant:
    def __init__(self) -> None:
        pass

    def find_and_remove(self, text: str):
        for name in names.keys():
            if search(name, text):
                any_c = ''
                list_word = []
                list_word.extend(text.split())
                list_word.remove(name)
                for any_x in list_word:
                    any_y = any_x + ' '
                    any_c = any_c + any_y
                text = any_c.strip()
                print(text)
                return (True, text, names[name]) 
        return (False, text, False)
    








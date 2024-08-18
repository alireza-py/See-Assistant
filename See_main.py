from os import device_encoding
# from pickle import TRUE
from speech import say, speed_say
from time import sleep
from speaker import speakers as sp
from voice_to_text import convert_to_text_EN, convert_to_text_PR 
from read_pickle import read, key_sentences
from find_assistant import name_of_assistant as assis
# from EnglishRobot import TeachLanguageScript
from subprocess import check_output
from reactions import movements
from actions import find_to
from platform import uname
from os import system
from re import findall

class assistant(assis, movements, sp):
    def __init__(self) -> None:
        system('cls')
        for _ in range(3):
            text = 'Starting'
            for count in '...':
                text += count
                print(text)
                sleep(.5)
                system('cls')

        # self.object_thach = TeachLanguageScript()
        self.volume_sys = self.range_sunde()[0] / -(self.range_sunde()[0] / 2.5)
        self.datas_assis = {

            'sentences' : read(),
            'Id' : check_output(['systeminfo']).decode('utf-8').split('\n'),
            'all_info' : [],
            'my_sys' : False,
            'node_name' : False,
            'version' : False,
            'machine' : False,
            'processor' : False,
            'volume_assis' : 1,
            'volume_computer' : 100,
        }
        self.plat()
        print("Hello word, is begining a new world !!")
        # for _ in range(10):
        say("Hello word, is begining a new world !!")
            # sleep(.1)
        speed_say(100, 110)

    def run(self):
        # self.volume_computer(self.datas_assis['volume_computer'])
        data = self.find_and_remove(text= convert_to_text_EN())
        # print(self.datas_assis['sentences'])
        if data[0]:
            # print(find_to( data[1], self.datas_assis['sentences']))
            for TF, sentenc in find_to(data[1], self.datas_assis['sentences']):
                # print(TF, sentenc)
                if TF:
                    self.datas_assis = self.movement(sentenc, self.datas_assis)
        self.datas_assis['sentences'] = read()


    def plat(self):
        try:
            for item in self.datas_assis['Id']:
                self.datas_assis['all_info'].append(str(item.split("\r")[:-1]))
            return (True,  0)
        except:
            try:
                info = uname()
                self.datas_assis['my_sys'] = info.system
                self.datas_assis['node_name'] = info.node
                self.datas_assis['version'] = info.version
                self.datas_assis['machine'] = info.machine
                self.datas_assis['processor'] = info.processor
                return (True, 1)
            except:
                return (False, False)
       
    def volume_computer(self, any: float):
        # if not self.volume_sys == any:
        self.devices(self.datas_assis['volume_computer'])

    def start_logo(self):
        pass


s = assistant()

while True:
    s.run()
    
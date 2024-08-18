from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16

 # read the languchs models #
model_en = Model('model_en')
model_per = Model('model_ir')
recognizer_en = KaldiRecognizer(model_en, 16000)
recognizer_per = KaldiRecognizer(model_per, 16000)
# read the capturs microfone #
cap_mic = PyAudio()
stream_mic = cap_mic.open(format = paInt16, channels = 1, rate = 16000
                             , input = True, frames_per_buffer = 8192)
stream_mic.start_stream()
##############################

def convert_to_text_EN(rate_microfone=9000):
    # read the data from microfone and recogniz #
    while True:
        try:
            data = stream_mic.read(rate_microfone)
            if len(data) == 0: print('please connect this system to microfone')
            if recognizer_en.AcceptWaveform(data):
                text_english = recognizer_en.Result()[14:-3]
                if text_english != '':
                    return text_english
        except: 
            print('we have an error in function of convert_to_text please debug this') 
            break

def convert_to_text_PR(rate_microfone=9000):
    # read the data from microfone and recogniz #
    while True:
        try:
            data = stream_mic.read(rate_microfone)
            if len(data) == 0: print('please connect this system to microfone')
            if recognizer_per.AcceptWaveform(data):
                text_pershian = recognizer_per.Result()[14:-3]
                if text_pershian != '':
                    return text_pershian
        except: 
            print('we have an error in function of convert_to_text please debug this') 
            break

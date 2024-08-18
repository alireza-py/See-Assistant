from pickle import dump, load
from random import randint

sentences_list = []
sentences_key = []            
with open('key_sentences.pickle', 'rb') as file:
    while True:
            try:
                sentences_list.append(load(file))
            except EOFError:
                break
for sentences_dict in sentences_list:
    sentences_key.extend(sorted(dict(sentences_dict).keys(), key= lambda x: len(str(x).split())))
sentences_key.reverse()


def read():
    return sentences_key

def key_sentences (key: any):
    number = randint(0, len(sentences_dict[key])-1)
    print(sentences_dict[str(key)][number])
    return sentences_dict[str(key)][number]

# print(read())


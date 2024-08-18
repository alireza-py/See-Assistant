from pickle import dump, load

sentences_dict_en = {

            r' ':('yes?', 
                   'yes sir?', 
                   "yes?, I'm ready sir!"),               

            r'(hello)':('hello sir', 
                       'hello sir'),

            r'(hi)':('hi sir', 
                       'hi'),

            r'(how are you|حالت چطوره|چطوری)':("I'm ok not bad, how are you too?", "i'm good not bad", "im okay"),

            r'are you ok':("yes i'm ok", "i'm good not bad", "not bad", "i'm almost good"),
            r'shut down my computer':("ok sir, good bay", "ok, good by, shut down computer", "yes sir, shut down computer"),
            r'turn off my computer':("ok sir, good bay", "ok, good by, turn off computer", "yes sir, turn off computer"),

            r'repeat':('Excuse me why are you repeating this sentenc sir?', 
                      'Are you looking for something sir?'),

            r'(turn down your volume|bring your volume down)':('ok, sir volume down', 'yes sir, turn down the volume', 'ok sir, volume down'),
            r'(turn up your volume|bring your volume up)':('ok, sir volume up', 'yes sir, turn up the volume', 'ok sir, volume up'),
            r'(shut up)':(''),
            r'(mute)':(''),
            r'(max sund|maximum sound|maximum volum)':('ok', 'yes sir'),
            r"shut down herself":('ok sir', 'yes sir goodby', 'ok sir i go to sleep', 'yes sir i go to bed', 'ok sir i go to bed', 'ok sir i go to sleep', 'yes sir', 'ok sir goodby'),
            r"i don't work with you":('ok sir', 'yes sir goodby', 'ok sir i go to sleep', 'yes sir i go to bed', 'ok sir i go to bed', 'ok sir i go to sleep', 'yes sir', 'ok sir goodby'),
            r"open solid work" : ('ok, sir', 'opening solidwork', "i'm opening solidwork", 'runing solidwork', "i'm runing solidwork", 'ok, sure, sir', 'ok, sure', 'yes sir', 'yes, sure', 'okay', 'solidwork is opening'),
            r"close solid work" : ('ok, sir', 'closeing solidwork', "i'm closeing solidwork", 'stoping solidwork', "i'm stoping solidwork", 'ok, sure, sir', 'ok, sure', 'yes sir', 'yes, sure', 'okay', 'solidwork is closeing'),
            r"explain platform" : ('ok', 'yes', 'explaning the system', 'explaning the computer', 'expalning', 'explaning this system')
            # r'سالیدورک و باز کن':('ok, sir', 'opening solidwork', "i'm opening solidwork", 'runing solidwork', "i'm runing solidwork", 'ok, sure, sir', 'ok, sure', 'yes sir', 'yes, sure', 'okay', 'solidwork is opening')
        }

# sentences_dict_per = {

#             r'خوبی':('yes', 
#                    'yes sir i am good', 
#                    "yes, I'm good how are you too?"),    

#         }

with open('key_sentences.pickle', 'wb') as file:
    dump(sentences_dict_en,file)
#     dump(sentences_dict_per,file)
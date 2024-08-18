from re import findall

def find_to(text0: str, list):
    try:
        l = text0.split()
        l = set(l)
        n = []
        v = []
        b = []
        c = []
        for sentens in list:
            for word in l:
                number = 0
                if findall(word, sentens):
                    for a in l:
                        if findall(a, sentens):
                            number += 1
                    words = len(str(sentens).split())
                    number = number / words
                    n.append((sentens, number, words))
                    break
    
        for item in n:
            if item[1] == 1:
                v.append((item[0], item[1]))
            else:
                b.append((item[0], item[1]))

        n.clear()
    
        if v:
            for i in v:
                if len(str(i[0]).split()) == 1:
                    c.append(i)
                    v.remove(i)
            if c:
                n.extend(c)
            if v:
                n.extend(v)
            # print(n)
            c.clear()
            for a, z in n:
                c.append((True, a))
                # print(c)
            return c

        else:
            if max(b, key= lambda x:x[1])[1] > .6:
                return [(True, max(b, key= lambda x:x[1])[0])]
            else:
                return [(False, False)]
    except:
        return [(True, ' ')]


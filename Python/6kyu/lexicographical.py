import itertools
def compa(a,b):
    r = []
    for i in a:
        for y in b:
            if i in y:
                r = r + [i]
    print(sorted(list(dict.fromkeys(r))))
                    

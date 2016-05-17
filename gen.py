from random import *

def genre_cplx():
    n  = randint(0,2)
    g1 = genre(2)
    g2 = genre(1)

    if n == 0 :
        return "Du %s mélangé avec du %s" % (g1, g2)
    elif n == 1 :
        return "Fusion %s - %s" % (g1, g2)
    elif n == 2 :
        return nationalite()
    else :
        return g1

def genre(k):
    if k == 0 :
        return genre_simple()
    else :
        n = randint(0,30)
        g = genre(k-1)

        if n == 0 :
            return "post-%s" % (g)
        elif n == 1 :
            return "%s progressif" % (g)
        elif n == 2 :
            return "%s atmosphérique" % (g)
        elif n == 3 :
            return "noise %s" % (g)
        elif n == 4 :
            return "dark %s" % (g)
        elif n == 5 :
            return "electro %s" % (g)
        elif n == 6 :
            return "%score" % (g)
        elif n == 7 :
            return "folk %s" % (g)
        elif n == 8 :
            return "%s traditionel" % (g)
        elif n == 9 :
            return "slow %s" % (g)
        elif n == 10 :
            return "vapor %s" % (g)
        elif n == 11 :
            return "%swave" % (g)
        elif n == 12 :
            return "%s instrumental" % (g)
        elif n == 13 :
            return "indie %s" % (g)
        elif n == 14 :
            return "pop %s" % (g)
        elif n == 15 :
            return "%s gothique" % (g)
        elif n == 16 :
            return "%s urbain" % (g)
        elif n == 17 :
            return "%s expérimental" % (g)
        elif n == 18 :
            return "%s alternatif" % (g)
        elif n == 19 :
            return "stoner %s" % (g)
        elif n == 20 :
            return "speed %s" % (g)
        else :
            return g
            

def nationalite():
    n = randint(0, 10)
    k = randint(0,2)
    g = genre(k)

    if n == 0 :
        return "%s québécois" % (g)
    elif n == 1 :
        return "%s saoudien" % (g)
    elif n == 2 :
        return "british %s" % (g)
    elif n == 3 :
        return "%s des Balkans" % (g)
    elif n == 4 :
        return "Southern %s" % (g)
    elif n == 5 :
        return "%s manouche" % (g)
    else :
        return g
            

def genre_simple():
    n = randint(0,10)

    if n == 0 :
        return "jazz"
    elif n == 1 :
        return "rock"
    elif n == 2 :
        return "metal"
    elif n == 3 :
        return "pop"
    elif n == 4 :
        return "rap"
    elif n == 5 :
        return "house"
    elif n == 6 :
        return "sludge"
    elif n == 7 :
        return "funk"
    elif n == 8 :
        return "swing"
    elif n == 9 :
        return "EDM"
    else : 
        return "musique"
        
if __name__ == '__main__':
    print(genre_cplx())
    print('\n')
    print(genre(3))

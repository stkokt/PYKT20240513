def name(meinName:str, alter:int):        
    print(f"Mein Name ist {meinName} und ich bin {alter} Jahre alt.")

def name2(meinName:str, alter:int|float)->str:
    '''
    @brief: Gibt einen formatierten Vorstellungstext zurück.
    @param1: Hier soll der Name hin.
    @param2: Hier soll das Alter hin.
    @return: Ein formatierter String.
    '''
    return f"Mein Name ist {meinName} und ich bin {alter} Jahre alt."

def flipCoin()->None:
    '''
    @brief: Simuliert einen Münzwurf
    '''
    import random
    coin=["Kopf", "Zahl"]
    print(coin[random.randint(0,1)])

# flipCoin()

def ropasci(myChoice:int):
    '''
    @brief: Simuliert SchnickSchackSchnuck
            gegen den Computer.
    @param: 0=Stein, 1=Schere, 2=Papier
    '''
    import random

    choice=["Stein", "Schere", "Papier"]
    choiceComp=choice[random.randint(0,2)]
    choicePlayer=choice[myChoice]

    if choiceComp=="Stein" and choicePlayer=="Schere":
        print(f"Computer gewinnt mit {choiceComp} gegen {choicePlayer}")
    if choiceComp=="Schere" and choicePlayer=="Papier":
        print(f"Computer gewinnt mit {choiceComp} gegen {choicePlayer}")
    if choiceComp=="Papier" and choicePlayer=="Stein":
        print(f"Computer gewinnt mit {choiceComp} gegen {choicePlayer}")
    if choicePlayer=="Stein" and choiceComp=="Schere":
        print(f"Du gewinnst mit {choicePlayer} gegen {choiceComp}")
    if choicePlayer=="Schere" and choiceComp=="Papier":
        print(f"Du gewinnst mit {choicePlayer} gegen {choiceComp}")
    if choicePlayer=="Papier" and choiceComp=="Stein":
        print(f"Du gewinnst mit {choicePlayer} gegen {choiceComp}")
    if choicePlayer==choiceComp: 
        print("Kein Gewinner!")


""" for run in range(100):
    ropasci(1) """

def ycross(a:tuple, b:tuple)->int|float:
    '''
    @brief: Berechnet den Schnittpunkt
            mit der Y- Achse
    @param1: Koordinate 1 (x0, y0)
    @param2: Koordinate 2 (x1, y1)
    '''
    m=(b[1]-a[1])/(b[0]-a[0]) # y=mx+n m=(y1-y0)/(x1-x0)
    n=a[1]-m*a[0]
    return n

print(ycross((0,1), (1,2)))


def kreis(val:int|float, mod:str="r")->None:
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt

    match mod:
        case "r":
            d=2*val
            a=pi*val**2
            u=pi*2*val
            print(f"Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "d":
            r=val/2
            a=(pi*val**2)/4
            u=pi*val
            print(f"Radius: {round(r, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "a":
            r=sqrt(val/pi)
            d=2*r
            u=pi*2*r
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Umfang: {round(u, 2)}")
        case "u":
            r=val/(2*pi)
            d=2*r
            a=pi*r**2
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}")

kreis(10)
kreis(20, "a")


def outerFunc(name):    
    def innerFunc():
        return name
    print("Hallo", innerFunc())

outerFunc("Stefan")

x=5

def scope():
    x=10 # nichtlokal für Unterfunktionen, lokal scope()
    def glob():
        global x
        print(f"Globale Variable {x}")
    def nonloc():
        nonlocal x        
        print(f"Nichtlokale Variable {x}")
    def loc():
        x=15 # lokal für loc() 
        print(f"Lokale Variable {x}")
    glob()
    nonloc()
    loc()
    
scope()

""" def mal2(y):
    return y*2 """

# 4. Lambda- Funktionen

mal2=lambda y: y*2 
isEven=lambda z: z%2==0

print((lambda z: z%2==0)(4))

# 5. map/filter (builtin Funktionen)
# Sowohl map() als auch filter() haben einen Rückgabewert.
# Somit können Variablen auch eine Zuweisung durch diese Funktionen bekommen.

array=[2,3,5,9,8,10]
                              # Prüfausdruck,  Iterierbares Objekt
print("Gerade Zahl?",list(map(lambda z: z%2==0, array)))
print("Gefilterte Liste: ", list(filter(lambda z: z>5, array)))

# 6. Args und Kwargs
# um mehrere Argumente zu übernehmen

def aFunction(var, *args, **kwargs):
    '''
    Es muss nicht *args und **kwargs heißen, 
    wichtig sind die Sternchen.
    *args wird als Tupel interpretiert,
    **kwargs als Dictionary.
    '''
    print(f"Das ist die Variable: {var}.")
    print(f"Das ist das Args- Tupel: {args}")
    print(f"Das ist das Kwargs- Dictionary: {kwargs}")
    for value in kwargs.values():
        print(args[0]*value)

aFunction("Var", 5,"m",3.14, kwargs1 = "Hallo", kwargs2 = "Welt")

# Aufgabe Passwortgenerator

def pwgenSimple(pwLength):
    from string import hexdigits, punctuation
    from random import sample 
    pwPool=hexdigits + punctuation
    return "".join(sample(pwPool, pwLength))

def pwgenPro1(lows:int, caps:int, nums:int, specs:int=0)->str:
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(ascii_lowercase, lows)
    capLetters=sample(ascii_uppercase, caps)
    numbers=sample(digits, nums)
    specChar=sample(punctuation, specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

def pwgenPro2(lows:int, caps:int, nums:int, specs:int=0)->str:
    from random import sample, shuffle
    #from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(range(97, 123), lows)
    capLetters=sample(range(65, 91), caps)
    numbers=sample(range(48, 58), nums)
    specChar=sample(range(35, 39), specs)
    print(lowLetters)
    pw=[] 
    pw.extend(lowLetters+capLetters+numbers+specChar)
    pw=[chr(num) for num in pw]
    shuffle(pw)
    return "".join(pw)

print(pwgenPro2(2,3,4,4))


















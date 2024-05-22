# Verzweigungen

""" 
    Es gibt zwei Arten von Verzweigungen, die 'if, elif, else'- Variante und die 'match case'- Variante.
    Alles was man mit 'match case' machen kann, kann man auch über 'if, elif, else' machen. Umgekehrt ist das nicht
    immer so.
    Grundsätzlich wird bei Verzweigungen der Zustand einer oder mehrerer Variablen ausgewertet (Rückgabewert ist Boolean)
    und auf Basis der Entscheidung ein damit assoziierter Prozess ausgeführt.
"""

# Die if, elif, else Variante

# Fall 1: Die zu prüfende Variable kann nur 2 Zustände annehmen.

lichtschalter=False # Licht ist aus
print(f"Zur Veranschaulichung Konvertierung eines Wahrheitswerts (lichtschalter=={lichtschalter}) in Integer: ", int(lichtschalter))

if lichtschalter==False:
    print("Licht ist aus.")
else:   # Also das Gegenteil von Zeile 17, lichtschalter == True
    print("Licht ist an.")

# Fall 2: Die Prüfvariable kann mehr als zwei Zustände annehmen.

dimmer=70    # Alles zwischen 0 und 100 soll als "Gedimmt" (mit 2 Stufen) ausgewertet werden, 0 ist "Dunkel", 100 ist "Hell"

if dimmer <= 0:
    print("Dunkel")
elif dimmer>0 and dimmer <50:
    print("Gedimmt, eher dunkel")
elif dimmer>50 and dimmer <100:
    print("Gedimmt, eher hell")
else:
    print("Hell")

# Verkürzende Schreibweisen für if- Bedingungen

"""
Da auch 0 als False und 1 als True ausgewertet werden, kann jede Variable (z.B. var1) auch mit 'if var1' abgefragt werden.

var1 = 0   # Wenn var1 = irgendein Wert außer 0, dann if var1 == True 
if var1:
    print("True")

Bei sequenziellen (iterierbaren) Datentypen ist die Länge entscheidend.

einText = ""  # Variable mit leerem String initialisiert, daher if einText == False
einText = "einText"   # jetzt if einText == True
listeA = []  # Variable mit leerer Liste initialisiert, daher if listeA == False
listeA = [1,2,3]    # jetzt if listeA == True

Die if- Bedingung kann auch mit logischen Operatoren abgefragt werden.

Im Lichtschalter- Bsp. ist das Licht aus, wenn die Variable auf False steht.
if (lichtschalter) erfragt also, ob lichtschalter == True,
if (not lichtschalter) erfragt hingegen, ob lichtschalter == False
""" 

# Die 'match case'- Variante (wird häufig für Menuführungen verwendet)


x=str()

while (x != "99"):
    print("1 = Programm 1\t 2 = Programm 2\t 99 = exit")
    x=input("Programmnummer eingeben: ")
    match(x):
        case "1": print("Programm 1 aufgerufen") 
        case "2": print("Programm 2 aufgerufen")
        case "99":  print("Programm wird beendet")
        case _: print("Falsche Programmnummer")
        


# Einstieg in die List- Comprehensions

"""
Syntax der List Comprehension:
liste = [List- Comprehension Ausdruck]
"""

liste1=[x+1 for x in range(10)] # füllt liste1 mit den Werten von 1 bis 10
print(liste1)

# Funktion: Multipliziert den übergebenen Wert mit 3
def mal3(x):
    return x*3
# Funktion: Multipliziert den übergebenen Wert mit 4
def mal4(x):
    return x*4

# Comprehension Ausdruck mit if- Bedingung
# multipliziert jede ungerade Zahl bis 100 mit 3 und überträgt sie in die Liste
# x%2 wird True, wenn das Ergebnis nicht 0 sondern 1 ist (False=0, True=alles außer 0) 
listeB=[mal3(x) for x in range(100) if x%2] # multipliziert jede ungerade Zahl bis 100 mit 3
print("if Bedingung")
print(listeB)

# Comprehension Ausdruck mit if-else Bedingung
# multipliziert jede gerade Zahl bis 100 mit 3 und überträgt sie in die Liste
# multipliziert jede ungerade Zahl bis 100 mit 4 und überträgt sie in die Liste
liste2=[mal3(x) if not x%2 else mal4(x)\
         for x in range(100)]

print("if else Bedingung")
print(liste2)

# Füllen einer Liste mit den Werten 0 - 99
# mit Loop statt Comprehension
listeC=[]
for i in range(100):
    listeC.append(i)
print(listeB)

# all, any

listeD=[1,5,7,12,25]
print("Builtin: All() für listeD: ",all(listeD)) # True, weil keiner der Werte 0 oder False ist

listeE=[0, "0", 0]

print("Builtin: All() für listeE: ",all(listeE)) # False wegen der Nullen auf Index 0 und 2
print("Builtin: Any() für listeE: ",any(listeE)) # Treu wegen des Strings "0" auf Index 1

# Liste von Listen

listeliste=[[1,2,3], [4,5,6]]

print(listeliste[1][1]) # Zugriff auf verschachtelte Liste, Ausgabe: 5
# Wichtig: Abbruchbedingung formulieren und darauf achten, dass sie auch erreicht werden kann!

# while-Schleife
x=0         # Prüfvariable
while x<10:
    print(x, end=" ")
    x+=1    # Erhöhung der Prüfvariablen bis die Abbruchbedingung erreicht ist

# for- Schleife

print()

# Bei einer for- Schleife wird die Abbruchbedingung im Schleifenkopf formuliert
for i in range(0,10, 1): # range(start, stop vor Index, step)
    print(i, end=" ")
    
print()

# continue -> bricht den aktuellen Schleifendurchlauf ab und beginnt den nächsten
for x in range(10):
    if x==5:
        continue
    print(x, end=" ")    # Ausgabe 0,1,2,3,4,6,7,8,9 (es fehlt die 5)

print()

# break -> bricht die gesamte Schleife ab
for x in range(10):
    if x==5:
        break
    print(x, end=" ")    # Ausgabe 0,1,2,3,4

print()

listeA=[10,20,30,40,50,60,70,80,90,100]
text="Hallo"
#print(len(text))
# print(listeA[2])

cnt=0
# for- Schleife über eine Liste 
for index in listeA:
    cnt+=index


for index in range(len(text)): #range(10)
    print(text[index], end=" ")

print()

for letter in text:
    print(letter, end=',') # Ausgabe: H,a,l,l,o,

print()

# Übungsaufgabe Kofferpacken, allerdings mit Random- Funktion

import random

koffer=[]
while (sum(koffer)<50):
    gewicht_des_gegenstands=random.randint(1,10)
    if sum(koffer)+gewicht_des_gegenstands<=50:
        koffer.append(gewicht_des_gegenstands)
    print(koffer, "Gewicht des Koffers: ", sum(koffer))

# Übungsaufgabe Ungerade Zahlen bis 147
for x in range(148):
    if x%2:
        print(x, end=" ")
    if x==147:
        print(3.1415)

print()


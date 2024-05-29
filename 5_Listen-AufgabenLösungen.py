# LC = List Comprehension

#1 Erzeuge mittels LC eine Liste der Zahlen von 1-100 und gebe sie aus.

liste1=[x+1 for x in range(100)]
print("Aufgabe 1\n")
print(liste1, "\n")

#2 Erzeuge aus der Liste oben mittels LC eine zweite Liste, in der alle Zahlen verdoppelt sind.

liste2=[x*2 for x in liste1]
print("Aufgabe 2\n")
print(liste2, "\n")

#3 Erzeuge aus der Liste oben mittels LC eine dritte Liste aller durch 3 teilbaren Zahlen bis 100.

liste3=[x for x in liste1 if x%3==0]
print("Aufgabe 3\n")
print(liste3, "\n")

#4 Erzeuge eine Liste bis 100, in der statt einer durch 5 teilbaren Zahl eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [0,1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

def listOf5(x):
    tmpList=[]
    if x%5==0:
        for x in range(x+1):
            if x%5==0:
                tmpList.append(x)
        return tmpList
    else:
        return x
    
liste4=[listOf5(x) for x in range(100)]
print("Aufgabe 4\n")
print(liste4, "\n")

#5 Sortiere die Liste aus 1) so um, dass die erste Hälfte und die zweite Hälfte gegeneinander vertauscht werden.

# liste5=liste1[int(((len(liste1))/2)):int(len(liste1))]+liste1[0:int((len(liste1)/2))] #liste1[((len(liste1))/2):len(liste1)]+
liste5=liste1[int(((len(liste1))/2)):]+liste1[:int((len(liste1)/2))] # sparsame Variante liste[50:]+liste[:50]
print("Aufgabe 5\n")
print(liste5, "\n") 

#6 Führe die Listen [1,2,3,4,5] und [8,7,6,5,4] zusammen und entferne die Duplikate, einmal ohne Beachtung der Reihenfolge, 
# einmal mit Beachtung der Reihenfolge.

print("Aufgabe 6\n")
liste6a=[1,2,3,4,5]
liste6b=[8,7,6,5,4]
liste6=liste6a+liste6b
# liste6=list(set(liste6)) # Variante1: Konvertieren der Liste in ein Set, Reihenfolge wird nicht beibehalten
liste6=list(dict.fromkeys(liste6)) # Variante2: fromkeys- Methode des Dictionary nutzen und danach wieder in  eine Liste wandeln
print(liste6, "\n")

# var1={"key":"value", "key2":"value2" }

#7 
"""
Muster aus Zahlen ausgeben:
Schreibe ein Programm, das folgendes Muster ausgibt:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Verwende eine Schleife, um das Muster zu erstellen.
"""

print("Aufgabe 7\n")

cnt=1
triangle=[]
while(cnt<6):    
    triangle.append(cnt)
    print(triangle)
    cnt+=1

print("\n")

#8 Erzeuge ein Liste aus zufälligen 3-stelligen Zahlen. Entferne von jeder die erste und die dritte Ziffer und quadriere die mittlere.

import random

print("Aufgabe 8\n")

liste8=[random.randint(100, 999) for x in range(10)]
print("randomisierte Liste:\n", liste8)

def keepMiddleAndSquareIt(num):
    listOfNum=list(str(num)) # str: "345" -> list: ['3','4','5']
    return int(listOfNum[1])**2 # int: 4 ->**2: 16

liste8squared=[keepMiddleAndSquareIt(x) for x in liste8]
print("geaenderte Liste:\n", liste8squared, "\n")

#9 Erzeuge eine Liste, die die Listen der Primfaktoren der Zahlen 5 – 50 enthält.
print("Aufgabe 9\n")

def primfaktorzerlegung(n):
    faktoren = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            faktoren.append(divisor)
            n //= divisor
        divisor += 1
    return faktoren

liste9=[primfaktorzerlegung(x) for x in range(5,51)]

print(liste9, "\n")

#10 Erzeuge die Liste [[[1,2,3],[4,5,6],[7,8,9]], [10,11,12],[13,14,15],[16,17,18]], [18,20,21],[22,23,24],[25,26,27]]]
#   mittels LC
print("Aufgabe 10\n")
liste10=[[[i+1+j*3+k*9 for i in range(3)] for j in range(3)] for k in range(3)]
print(liste10)
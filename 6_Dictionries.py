# -*- coding: utf-8 -*-

"""
Dictionary ist ein Datentyp mit dem Charakter eines Wörterbuchs. 
Einem Schlüsselbegriff kann ein Wert zugewiesen werden, der dann 
unter Verwendung des Schlüsselbegriffs ausgelesen werden kann.
"""
#       key   : value
pons={"apple":"Apfel", "banana":"Banane", "pumpkin":"Kürbis"}
pons2={"cherry": "Kirsche", "lemon":"Zitrone"}
print(pons.get("apple"))
print(pons.keys())
print(pons.values())
print(pons.get("banana"))
print(pons["pumpkin"])
print(pons.items())

for k,v in pons.items():
    print(f"{k}={v}")

pons.update(pons2)           # |= Walrus- Operator

print(pons)

item=pons.pop("pumpkin")
print(item, type(item))
print(pons)

var=pons.popitem()
print(var, pons)
var=pons.popitem()
print(var, pons)

print(var[0])
# var[0]=5          # Zuweisung bei einem Tupel nicht möglich

# Kurzer Exkurs zu Tuple und Set
aTuple=(10, 20, 30)
print(aTuple)
print(aTuple[1])    # lesender Zugriff möglich
# aTuple[1]=15      # schreibender Zugriff nicht möglich, da Datentyp Tuple immutable
aSet={1,2,3,4,4}    # Duplikate werden entfernt 
print(aSet)

# Zurück zu Dictionaries

lexicon={"Deutschland":["Berlin", "Europa"], "Frankreich":["Paris", "Europa"]}
lexikon={"Deutschland":{"Hauptstadt":"Berlin", "Kontinent":"Europa"}, "Frankreich":{"Kontinent":"Europa", "Hauptstadt":"Paris"}}







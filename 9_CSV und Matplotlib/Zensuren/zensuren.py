import csv

zensuren=[]

# Einfacher csv- Reader
with open('zensuren.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)

    next(csv_reader)        # Hier 'next', damit die Kopfzeile 
                            # übersprungen wird.

    for line in csv_reader:
        zensuren.append(line)


print(zensuren)

print()

zensuren1=[]
# csv- DictReader liest die Datei als Dictionary ein
with open('zensuren.csv','r') as csv_file:
    csv_reader =csv.DictReader(csv_file)

    # next(csv_reader)      # Hier nicht 'next', da sonst der 
                            # erste Datensatz übersprungen wird.

    for line in csv_reader:
        zensuren1.append(line)

print(zensuren1)


# Version Winfried:

for schueler in zensuren1:
        name = schueler["Name"]
        noten = [float(schueler[fach]) for fach in schueler if fach != 'Name']
        durchschnitt = sum(noten) / len(noten)
        print(f"{name} hat eine Durchschnittsnote von {round(durchschnitt,2)}")



fachnoten = {}
    
# Noten pro Fach sammeln
for schueler in zensuren1:
    for schulfach, note in schueler.items():
        if schulfach != "Name":
            if schulfach not in fachnoten:
                fachnoten[schulfach] = []
            fachnoten[schulfach].append(float(note))

print(fachnoten)

# Durchschnittsnote pro Fach berechnen
for schulfach, noten in fachnoten.items():
    durchschnitt = sum(noten) / len(noten)
    print(f"Die Durchschnittsnote in {schulfach} ist {round(durchschnitt,2)}")
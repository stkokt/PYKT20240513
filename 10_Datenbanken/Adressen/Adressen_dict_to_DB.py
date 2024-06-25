import csv
import sqlite3

# CSV-Datei öffnen
csv_datei = 'adressen.csv'

# SQLite-Datenbankverbindung herstellen
verbindung = sqlite3.connect("adressen.db")
zeiger = verbindung.cursor()

# Tabelle erstellen (falls noch nicht vorhanden)
zeiger.execute('''CREATE TABLE IF NOT EXISTS adressen
                (id INTEGER PRIMARY KEY,
                vorname TEXT,
                nachname TEXT,
                email TEXT)''')

# CSV-Datei mit DictReader auslesen und in die Datenbank speichern
with open(csv_datei, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        vorname = row['Vorname']
        nachname = row['Nachname']
        email = row['EMail']
        zeiger.execute("INSERT INTO adressen (vorname, nachname, email) VALUES (?, ?, ?)",
                       (vorname, nachname, email))

# Änderungen speichern und Verbindung schließen
verbindung.commit()
verbindung.close()

print("Daten wurden erfolgreich in die SQLite-Datenbank gespeichert.")
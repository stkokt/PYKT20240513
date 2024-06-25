"""
Dies ist das Datenbankmodul einer Adressbuchanwendung, 
die in einem anderen Kurs geschrieben wurde. Sie enthält die essentiellen
Datenbank- Operationen und kann als Vorlage für Datenbankanwendungen in Python
genutzt werden.
"""

import sqlite3
from tkinter import filedialog

# Name der SQLite-Datenbank
db_name = "telefonbuch.db"
# db_name = filedialog.askopenfilename()

def connect_to_database():
    """Verbindung zur SQLite-Datenbank herstellen."""
    conn = sqlite3.connect(db_name)
    return conn

def create_table():
    """Tabelle erstellen, wenn sie nicht existiert."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_personen (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Vorname TEXT,
                        Nachname TEXT,
                        Strasse TEXT,
                        Hausnummer TEXT,
                        Postleitzahl TEXT,
                        Stadt TEXT,
                        Land TEXT,
                        TelefonNr TEXT
                    )''')
    conn.commit()
    conn.close()

def insert_data(lstPersonen):
    """Daten in die Tabelle einfügen."""
    conn = connect_to_database()
    cursor = conn.cursor()
    for person in lstPersonen:
        cursor.execute('''INSERT INTO tbl_personen (
                        Vorname, 
                        Nachname, 
                        Strasse, 
                        Hausnummer, 
                        Postleitzahl, 
                        Stadt, 
                        Land, 
                        TelefonNr) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', person)
    conn.commit()
    conn.close()

def read_data():
    """Daten aus der Tabelle lesen und zurückgeben."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_personen')
    data = cursor.fetchall()
    conn.close()
    return data

def delete_record(record_id):
    """Datensatz löschen."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tbl_personen WHERE Id=?', (record_id,))
    conn.commit()
    conn.close()

def update_record(record):
    """Datensatz aktualisieren."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''UPDATE tbl_personen SET 
                        Vorname =?, 
                        Nachname =?, 
                        Strasse =?, 
                        Hausnummer =?, 
                        Postleitzahl =?, 
                        Stadt =?, 
                        Land =?, 
                        TelefonNr =?,
                        WHERE Id=?''', (record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[0]))
    conn.commit()
    conn.close()

connect_to_database()
print(read_data())

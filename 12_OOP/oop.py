class Haus:                                         # Einfache Klassendefinition
    def __init__(self, l, b, h):                    # Konstruktor mit Argumenten
        self._l = l
        self._b = b
        self._h = h

    def calc_qm(self):                              # Methode der Klasse
        return self._l*self._b

class Fahrzeug:
    """
    Baut ein Fahrzeug.                              # Zur Dokumentation
    """
    __counter=0                                     # statische (Klassen-)Variable mit '__' als private verkapselt

    def __init__(self, make, origin):               # Konstruktor
        self._make = make
        self._origin = origin
        Fahrzeug.__counter+=1                       # Zugriff auf Klassenvariable

    def __repr__(self) -> str:                      # Kurzer Repräsentationsstring
        return f"{self._make}, {self._origin}"
    
    def get_counter():                              # "Getter" zur Abfrage der Klassenvariable
        return Fahrzeug.__counter
    

class Auto(Fahrzeug):                               # Vererbung: Auto erbt von Fahrzeug
    """
    Baut ein Auto.
    """
    def __init__(self, make, origin, hp):           # Konstruktor für Auto
        super().__init__(make, origin)              # Konstruktor der vererbenden Klasse (Fahrzeug)
        self._hp = hp

       
    def __eq__(self, other) -> bool:

        if self._hp == other._hp:
            return True
        else:
            return False

    def __lt__(self, other):

        if self._hp < other._hp:
            return True
        else:
            return False
    
    def __gt__(self, other):

        if self._hp > other._hp:
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self._make}, {self._origin}, {self._hp}"
        

class pkw(Auto):                                    # Nächste Ableitung
    """
    Baut einen PKW.
    """
    def __init__(self, make, origin, hp, passenger):
        super().__init__(make, origin, hp)
        self._passenger = passenger

    def __repr__(self) -> str:
        return f"{self._make}, {self._origin}, {self._hp}, {self._passenger}"

class Camper(pkw, Haus):                                        # Mehrfachvererbung
    def __init__(self, make, origin, hp, passenger, l, b, h):   # Konstruktor der Camper- Klasse
        pkw.__init__(self, make, origin, hp, passenger)         # Konstruktor der PKW Klasse 
        Haus.__init__(self, l, b, h)                            # Konstruktor der Haus- Klasse



BMW = pkw("BMW", "Deutschland", 200, 4)
#BMW.fahren()

SEAT = pkw("Seat", "Spanien", 50, 4)

h=Haus(2,3,5)

marianne= Camper("ABC", "Holland", 200, 6, 8, 5, 3)

print(pkw.mro())                                                # Method- Resolution- Order
print(Camper.mro())                                             # Gibt aus, in welcher Reihenfolge Python die aufgerufene Methode sucht
print(marianne.calc_qm())                                       # Aufruf der Haus- Methode am Camperobjekt
print(Fahrzeug.get_counter())                                   # Aufruf des Getters für die Klassen- Zählvariable








"""
Bundesland,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,Geburtenrate (pro 1000 Einwohner)
Baden-Württemberg,11,1,11,0,11,0,10,9,10,9,8,3
Bayern,13,2,13,1,13,1,12,1,12,0,9,2
Berlin,3,7,3,7,3,7,3,6,3,6,9,1
Brandenburg,2,5,2,5,2,5,2,5,2,5,9,0
Bremen,0,7,0,7,0,7,0,7,0,7,8,6
Hamburg,1,8,1,8,1,8,1,8,1,8,9,1
Hessen,6,3,6,3,6,3,6,3,6,3,9,0
Mecklenburg-Vorpommern,1,6,1,6,1,6,1,6,1,6,8,7
Niedersachsen,8,0,7,9,7,9,7,9,7,9,9,0
Nordrhein-Westfalen,17,9,17,8,17,8,17,8,17,8,8,9
Rheinland-Pfalz,4,1,4,1,4,1,4,1,4,1,8,3
Saarland,0,9,0,9,0,9,0,9,0,9,8,9
Sachsen,4,1,4,1,4,1,4,1,4,1,8,7
Sachsen-Anhalt,2,2,2,2,2,2,2,2,2,2,8,3
Schleswig-Holstein,2,9,2,9,2,9,2,9,2,9,9,1
Thüringen,2,1,2,1,2,1,2,1,2,1,8,5
"""

import matplotlib.pyplot as plt
import pandas as pd

# Daten, die du bereitgestellt hast
data = {
    "Bundesland": [
        "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen",
        "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen",
        "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen",
        "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"
    ],
    "2023": [11, 13, 3, 2, 0, 1, 6, 1, 8, 17, 4, 0, 4, 2, 2, 2],
    "2022": [1, 2, 7, 5, 7, 8, 3, 6, 0, 9, 1, 9, 1, 2, 9, 1],
    "2021": [11, 13, 3, 2, 7, 8, 3, 6, 7, 17, 4, 9, 4, 2, 2, 2],
    "2020": [0, 1, 7, 5, 7, 8, 3, 6, 9, 8, 1, 9, 1, 2, 9, 1],
    "2019": [11, 13, 3, 2, 7, 8, 3, 6, 7, 17, 4, 9, 4, 2, 9, 8]
}

# DataFrame aus den Daten erstellen
df = pd.DataFrame(data)

# Bundesland als Index setzen
df.set_index("Bundesland", inplace=True)

# Balkendiagramm für jedes Jahr erstellen
df.plot(kind="bar", figsize=(12, 6))
plt.title("Geburtenrate in Deutschland (2014-2023)")
plt.xlabel("Bundesland")
plt.ylabel("Geburtenrate (pro 1000 Einwohner)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Jahr")
plt.tight_layout()
plt.show()

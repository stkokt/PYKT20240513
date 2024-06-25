"""
Jahr,Asien (BIP in Billionen USD),Europa (BIP in Billionen USD),Nordamerika (BIP in Billionen USD),Südamerika (BIP in Billionen USD),Afrika (BIP in Billionen USD)
2014,31,2,18,8,21,5,5,1,2,3
2015,32,1,19,2,22,0,5,0,2,4
2016,33,0,19,6,22,5,4,9,2,5
2017,34,1,20,3,23,0,4,8,2,6
2018,35,3,21,1,23,6,4,7,2,7
2019,36,0,21,7,24,1,4,6,2,8
2020,36,1,21,5,24,3,4,5,2,7
2021,36,5,22,7,25,5,5,5,2,8
2022,37,0,23,0,26,0,5,7,2,9
2023,37,5,23,3,26,5,5,9,3,0
"""


import matplotlib.pyplot as plt

# Daten für die Regionen und Jahre
jahre = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
asien_bip = [31.2, 32.1, 33.0, 34.1, 35.3, 36.0, 36.1, 36.5, 37.0, 37.5]
europa_bip = [18.8, 19.2, 19.6, 20.3, 21.1, 21.7, 21.5, 22.7, 23.0, 23.3]
nordamerika_bip = [21.5, 22.0, 22.5, 23.0, 23.6, 24.1, 24.3, 25.5, 26.0, 26.5]
suedamerika_bip = [5.1, 5.0, 5.1, 5.2, 5.3, 5.4, 5.2, 5.5, 5.7, 5.9]
afrika_bip = [2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.7, 2.8, 2.9, 3.0]

# Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
plt.bar(jahre, asien_bip, label="Asien")
plt.bar(jahre, europa_bip, label="Europa", bottom=asien_bip)
plt.bar(jahre, nordamerika_bip, label="Nordamerika", bottom=[a + e for a, e in zip(asien_bip, europa_bip)])
plt.bar(jahre, suedamerika_bip, label="Südamerika", bottom=[a + e + n for a, e, n in zip(asien_bip, europa_bip, nordamerika_bip)])
plt.bar(jahre, afrika_bip, label="Afrika", bottom=[a + e + n + s for a, e, n, s in zip(asien_bip, europa_bip, nordamerika_bip, suedamerika_bip)])

# Achsenbeschriftungen und Titel
plt.xlabel("Jahr")
plt.ylabel("BIP (Billionen USD)")
plt.title("BIP nach Region (2014-2023)")
plt.xticks(jahre)
plt.legend()

# Diagramm anzeigen
plt.show()

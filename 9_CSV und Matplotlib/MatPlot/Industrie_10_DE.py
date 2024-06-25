"""
Industrie,Umsatz (in Milliarden Euro)
Kraftfahrzeugindustrie,509
Maschinenbau,269,26
Chemisch-pharmazeutische Industrie,261,18
Elektrotechnik,220,79
Ernährungsgewerbe,218,57
"""

import matplotlib.pyplot as plt
import pandas as pd

# Daten, die du bereitgestellt hast
data = {
    "Industrie": [
        "Kraftfahrzeugindustrie", "Maschinenbau",
        "Chemisch-pharmazeutische Industrie", "Elektrotechnik", "Ernährungsgewerbe"
    ],
    "Umsatz (in Milliarden Euro)": [509, 269, 261, 220, 218]
}

# DataFrame aus den Daten erstellen
df = pd.DataFrame(data)

# Kreisdiagramm erstellen
plt.figure(figsize=(8, 8))
plt.pie(df["Umsatz (in Milliarden Euro)"], labels=df["Industrie"], autopct='%1.1f%%', startangle=90)
plt.title("Umsatz in der deutschen Industrie")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

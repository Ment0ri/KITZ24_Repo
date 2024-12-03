import numpy as np            # Importiere das Paket NumPy und benenne es als "np" für numerische Berechnungen
import matplotlib.pyplot as plt  # Importiere das Paket Matplotlib für das Plotten von Diagrammen
import math                    # Importiere das Paket Math für mathematische Berechnungen wie die Fakultät

# Wertebereich festlegen
start = 1                      # Startwert des Bereichs
ende = 1000                    # Endwert des Bereichs
n = np.linspace(start, ende, 10000)  # Erstelle 10.000 gleichmäßig verteilte Werte zwischen "start" und "ende"

# Definition der Komplexitätsfunktionen
O_1 = np.ones_like(n)          # O(1) - Konstante Laufzeit (immer 1, unabhängig von "n")
O_log_n = np.log(n)            # O(log n) - Logarithmische Laufzeit (logarithmische Zunahme in "n")
O_log2_n = np.log(n)**2        # O(log^2 n) - Polylogarithmische Laufzeit (log(n) wird zum Quadrat genommen)
O_n = n                        # O(n) - Lineare Laufzeit (proportional zu "n")
O_n_log_n = n * np.log(n)      # O(n log n) - Linearithmische Laufzeit (n multipliziert mit log(n))
O_n2 = n**2                    # O(n^2) - Quadratische Laufzeit (n zum Quadrat)
k = 3                          # Exponent "k" für die Potenz von "n"
O_n3 = n**k                    # O(n^3) - Polynomial-Komplexität (n hoch k, hier k=3)
d = 2                          # Basis "d" für die exponentielle Funktion
O_2n = d**n                    # O(2^n) - Exponentielle Laufzeit (Basis 2 hoch n)

# Fakultät (n!) nur für ganzzahlige Werte berechnen, da Fakultät nur für Integer definiert ist
n_int = np.arange(1, 10)       # Erstelle ein Array von ganzzahligen Werten von 1 bis 9
O_n_fact = np.array([math.factorial(i) for i in n_int])  # O(n!) - Faktoriell (berechne die Fakultät für jede Zahl in n_int)

# Plotten der Funktionen zur Darstellung der Laufzeitkomplexitäten
plt.figure(figsize=(12, 12))   # Erstelle eine Grafik mit einer Größe von 12x12 Zoll
plt.plot(n, O_1, label='O(1)')       # Zeichne O(1) als konstante Linie
plt.plot(n, O_log_n, label='O(log n)')   # Zeichne O(log n)
plt.plot(n, O_log2_n, label='O(log^2 n)')   # Zeichne O(log^2 n)
plt.plot(n, O_n, label='O(n)')       # Zeichne O(n)
plt.plot(n, O_n_log_n, label='O(n log n)')  # Zeichne O(n log n)
plt.plot(n, O_n2, label='O(n^2)')    # Zeichne O(n^2)
plt.plot(n, O_n3, label='O(n^3)')    # Zeichne O(n^3)
plt.plot(n, O_2n, label='O(2^n)')    # Zeichne O(2^n)
plt.plot(n_int, O_n_fact, label='O(n!)')   # Zeichne O(n!) nur für ganzzahlige Werte

# Einstellungen für den Plot
plt.title('Vergleich von Laufzeitkomplexitäten')  # Titel des Plots
plt.xlabel('n')                      # Beschriftung der x-Achse
plt.ylabel('O(f(n))')                # Beschriftung der y-Achse
plt.ylim(0, 50)                      # Begrenze die y-Achse auf den Bereich von 0 bis 50 für bessere Lesbarkeit
plt.legend(loc='upper right')        # Füge eine Legende hinzu und platziere sie oben rechts
plt.grid(True)                       # Aktiviert das Raster im Hintergrund
plt.show()                           # Zeige das Diagramm an

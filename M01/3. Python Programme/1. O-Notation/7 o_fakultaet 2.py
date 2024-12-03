import time               # Importiere das Modul "time" für Zeitmessungen
import os                 # Importiere das Modul "os" für Betriebssystem-Operationen, wie das Leeren des Terminals
import platform           # Importiere das Modul "platform", um das Betriebssystem zu identifizieren
import itertools          # Importiere das Modul "itertools" für effiziente Iterationstools wie Permutationen

# Funktion zum Leeren des Terminals
def clear_terminal():
    # Überprüfe das Betriebssystem
    if platform.system() == 'Windows':
        os.system('cls')  # Verwende 'cls' für Windows, um das Terminal zu leeren
    else:
        os.system('clear')  # Verwende 'clear' für andere Betriebssysteme wie macOS oder Linux
clear_terminal()            # Rufe die Funktion auf, um das Terminal beim Start zu leeren

# Definiere eine Funktion zur Berechnung aller Permutationen eines Arrays
def operation(array):
    # Erzeuge eine Liste aller Permutationen der Eingabeliste "array"
    return list(itertools.permutations(array))

# Initialisiere Variablen für die Schleife
n = 1                        # Startwert von "n" (Anzahl der Elemente im Array)
m = 1                        # Erhöhungsschritt für "n" in jeder Schleifeniteration
k = 11                       # Obergrenze für "n" (11), definiert das Ende der Schleife

# Schleife zur Berechnung der Permutationen und Messung der Zeit
while n <= k:
    array = list(range(n))   # Erstelle eine Liste von 0 bis n-1, die insgesamt "n" Elemente enthält
    start_time = time.time_ns()  # Speichere die aktuelle Zeit in Nanosekunden als Startzeit
    operation(array)             # Berechne alle Permutationen des Arrays
    elapsed_time = time.time_ns() - start_time  # Berechne die verstrichene Zeit in Nanosekunden
    print(f"n = {n} -> time = {elapsed_time} ns")  # Gib die Anzahl der Elemente "n" und die Berechnungszeit aus
    n += m                        # Erhöhe den Wert von "n" für die nächste Iteration (n = n + m)

import bisect           # Importiere das Modul "bisect" für effiziente Suche in sortierten Listen
import time             # Importiere das Modul "time" für Zeitmessungen
import os               # Importiere das Modul "os" für Betriebssystem-Operationen, wie das Leeren des Terminals
import platform         # Importiere das Modul "platform", um das Betriebssystem zu identifizieren

# Funktion zum Leeren des Terminals
def clear_terminal():
    # Überprüfe das Betriebssystem
    if platform.system() == 'Windows':
        os.system('cls')  # Verwende 'cls' für Windows, um das Terminal zu leeren
    else:
        os.system('clear')  # Verwende 'clear' für andere Betriebssysteme wie macOS oder Linux
clear_terminal()            # Rufe die Funktion auf, um das Terminal beim Start zu leeren

# Definiere eine Operation, die eine binäre Suche im Array durchführt
def operation(array):
    # Bisect.bisect_left findet die Einfügeposition für 0, um die Reihenfolge zu erhalten
    # In diesem Fall wird die Position des ersten Elements ≥ 0 in der sortierten Liste zurückgegeben
    return bisect.bisect_left(array, 0)

# Initialisiere Variablen für die Schleife
n = 8                        # Startwert von "n" (Anzahl der Elemente im Array)
m = 2                        # Multiplikator, um "n" in jeder Schleifeniteration zu verdoppeln
k = 2**25                    # Obergrenze für "n" (33.554.432), definiert das Ende der Schleife

# Schleife zum Verdoppeln der Arraygröße und Messen der Zeit für die Operation
while n <= k:
    array = list(range(n))   # Erstelle eine Liste von 0 bis n-1, die insgesamt "n" Elemente enthält
    start_time = time.time_ns()  # Speichere die aktuelle Zeit in Nanosekunden als Startzeit
    operation(array)             # Führe die binäre Suche nach dem Element 0 im Array aus
    elapsed_time = time.time_ns() - start_time  # Berechne die verstrichene Zeit in Nanosekunden
    print(f"n = {n} -> time = {elapsed_time} ns")  # Gib die Anzahl der Elemente "n" und die verstrichene Zeit aus
    n *= m                        # Verdopple den Wert von "n" für die nächste Iteration (n = n * m)

import time               # Importiere das Modul "time" für Zeitmessungen
import os                 # Importiere das Modul "os" für Betriebssystem-Operationen, wie das Leeren des Terminals
import platform           # Importiere das Modul "platform", um das Betriebssystem zu identifizieren

# Funktion zum Leeren des Terminals
def clear_terminal():
    # Überprüfe das Betriebssystem
    if platform.system() == 'Windows':
        os.system('cls')  # Verwende 'cls' für Windows, um das Terminal zu leeren
    else:
        os.system('clear')  # Verwende 'clear' für andere Betriebssysteme wie macOS oder Linux
clear_terminal()            # Rufe die Funktion auf, um das Terminal beim Start zu leeren

# Definiere eine Operation zum Berechnen der Summe aller Elemente in einem Array
def operation(array):
    sum = 0                 # Initialisiere die Variable "sum" auf 0
    for element in array:   # Iteriere über jedes Element im Array
        sum += element      # Addiere das aktuelle Element zur Summe hinzu
    return sum              # Gib die berechnete Summe zurück

# Initialisiere Variablen für die Schleife
n = 4                       # Startwert von "n" (Anzahl der Elemente im Array)
m = 2                       # Multiplikator, um "n" in jeder Schleifeniteration zu verdoppeln
k = 2**25                   # Obergrenze für "n" (33.554.432), definiert das Ende der Schleife

# Schleife zum Verdoppeln der Arraygröße und Messen der Zeit für die Operation
while n <= k:
    array = list(range(n))  # Erstelle eine Liste von 0 bis n-1, die insgesamt "n" Elemente enthält
    start_time = time.time_ns()   # Speichere die aktuelle Zeit in Nanosekunden als Startzeit
    operation(array)              # Rufe die Funktion "operation" auf, um die Summe des Arrays zu berechnen
    elapsed_time = time.time_ns() - start_time  # Berechne die verstrichene Zeit in Nanosekunden
    print(f"n = {n} -> time = {elapsed_time} ns")  # Gib die Anzahl der Elemente "n" und die verstrichene Zeit aus
    n *= m                         # Verdopple den Wert von "n" für die nächste Iteration (n = n * m)

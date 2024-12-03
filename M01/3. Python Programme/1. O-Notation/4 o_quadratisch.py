import random            # Importiere das Modul "random", obwohl es in diesem Code nicht verwendet wird
import time              # Importiere das Modul "time" für Zeitmessungen
import os                # Importiere das Modul "os" für Betriebssystem-Operationen, wie das Leeren des Terminals
import platform          # Importiere das Modul "platform", um das Betriebssystem zu identifizieren

# Funktion zum Leeren des Terminals
def clear_terminal():
    # Überprüfe das Betriebssystem
    if platform.system() == 'Windows':
        os.system('cls')  # Verwende 'cls' für Windows, um das Terminal zu leeren
    else:
        os.system('clear')  # Verwende 'clear' für andere Betriebssysteme wie macOS oder Linux
clear_terminal()            # Rufe die Funktion auf, um das Terminal beim Start zu leeren

# Definiere eine Operation mit einer doppelten Schleife
def operation(array):
    # Iteriere über jedes Element im Array
    for i in range(len(array)):
        # Für jedes Element im äußeren Schleifenindex durchlaufe das Array erneut vollständig
        for j in range(len(array)):
            array[i] += array[j]  # Addiere jedes Element "array[j]" zum aktuellen Element "array[i]"
    return array  # Gib das veränderte Array zurück

# Initialisiere Variablen für die Schleife
n = 8                        # Startwert von "n" (Anzahl der Elemente im Array)
m = 2                        # Multiplikator, um "n" in jeder Schleifeniteration zu verdoppeln
k = 2**14                    # Obergrenze für "n" (16.384), definiert das Ende der Schleife

# Schleife zum Verdoppeln der Arraygröße und Messen der Zeit für die Operation
while n <= k:
    array = list(range(n))   # Erstelle eine Liste von 0 bis n-1, die insgesamt "n" Elemente enthält
    start_time = time.time_ns()  # Speichere die aktuelle Zeit in Nanosekunden als Startzeit
    operation(array)             # Führe die doppelgeschleifte Operation auf dem Array aus
    elapsed_time = time.time_ns() - start_time  # Berechne die verstrichene Zeit in Nanosekunden
    print(f"n = {n} -> time = {elapsed_time} ns")  # Gib die Anzahl der Elemente "n" und die verstrichene Zeit aus
    n *= m                        # Verdopple den Wert von "n" für die nächste Iteration (n = n * m)

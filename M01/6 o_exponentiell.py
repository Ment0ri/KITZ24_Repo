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

# Definiere eine rekursive Funktion zur Berechnung der Fibonacci-Zahl
def operation(n):
    # Basisfälle: Wenn n 0 oder 1 ist, gib n zurück
    if n <= 1:
        return n
    # Rekursive Berechnung: operation(n - 1) + operation(n - 2)
    return operation(n - 1) + operation(n - 2)

# Initialisiere Variablen für die Schleife
n = 1                        # Startwert von "n" (Nummer in der Fibonacci-Sequenz)
m = 1                        # Erhöhungsschritt für "n" in jeder Schleifeniteration
k = 2**5                     # Obergrenze für "n" (32), definiert das Ende der Schleife

# Schleife zur Berechnung der Fibonacci-Zahl und Messung der Zeit
while n <= k:
    start_time = time.time_ns()  # Speichere die aktuelle Zeit in Nanosekunden als Startzeit
    operation(n)                 # Berechne die n-te Fibonacci-Zahl mit der rekursiven Funktion "operation"
    elapsed_time = time.time_ns() - start_time  # Berechne die verstrichene Zeit in Nanosekunden
    print(f"n = {n} -> time = {elapsed_time} ns")  # Gib den Wert von "n" und die Berechnungszeit aus
    n += m                        # Erhöhe den Wert von "n" für die nächste Iteration (n = n + m)

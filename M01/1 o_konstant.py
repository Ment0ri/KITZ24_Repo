import time               # Importiere das Modul "time" für Zeitmessungen
import os                 # Importiere das Modul "os" für Betriebssystem-Operationen wie das Leeren des Terminals
import platform           # Importiere das Modul "platform", um das Betriebssystem zu identifizieren

# Funktion zum Leeren des Terminals
def clear_terminal():
    # Überprüfe das Betriebssystem
    if platform.system() == 'Windows':
        os.system('cls')  # Verwende 'cls' für Windows, um das Terminal zu leeren
    else:
        os.system('clear')  # Verwende 'clear' für andere Betriebssysteme wie macOS oder Linux
clear_terminal()            # Rufe die Funktion auf, um das Terminal beim Start zu leeren

# Definiere eine Beispieloperation
def operation(n):
    return n               # Diese Funktion gibt einfach das Eingabewert "n" zurück, kann hier beliebig angepasst werden

# Initialisiere Variablen
n = 32                     # Startwert von "n"
m = 2                      # Multiplikator, um "n" in jeder Schleifeniteration zu verdoppeln
k = 2**15                  # Obergrenze von "n" (32.768 in diesem Fall), definiert das Ende der Schleife

# Während n kleiner oder gleich k ist, führe die Schleife aus
while n <= k:
    start_time = time.time_ns()   # Speichere die aktuelle Zeit in Nanosekunden als Startzeit
    operation(n)                  # Rufe die Funktion "operation" mit dem aktuellen Wert von "n" auf
    elapsed_time = time.time_ns() - start_time  # Berechne die verstrichene Zeit in Nanosekunden
    print(f"n = {n} -> time = {elapsed_time} ns")  # Gib den aktuellen Wert von "n" und die Zeit in Nanosekunden aus
    n *= m                         # Verdopple den Wert von "n" für die nächste Schleifeniteration (n = n * m)

import os
import platform

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Terminal reinigen
clear_terminal()

#_________________Hauptprogramm_________________________
import sys

# Beispiel-Variablen
integer_var = 64         # Integer (Ganzzahl)
float_var = 3.14         # Float (Gleitkommazahl)
string_var = "Hallo Welt" # String (Zeichenkette)
boolean_var = True       # Boolean (Wahrheitswert)

# Ausgabe der Variablen
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)

# Ausgabe der Variablen
print("Integer:", type(integer_var))
print("Float:", type(float_var))
print("String:", type(string_var))
print("Boolean:", type(boolean_var))

# Speichergröße der Variablen
int_size = sys.getsizeof(integer_var)
float_size = sys.getsizeof(float_var)
string_size = sys.getsizeof(string_var)
boolean_size = sys.getsizeof(boolean_var)

# Ausgabe der Speichergrößen
print(f"Speichergröße von int: {int_size} Bytes")
print(f"Speichergröße von float: {float_size} Bytes")
print(f"Speichergröße von string: {string_size} Bytes")
print(f"Speichergröße von boolean: {boolean_size} Bytes")


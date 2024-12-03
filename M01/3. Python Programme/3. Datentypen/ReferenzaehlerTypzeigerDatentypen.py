"""
    PyObject Klasse: Diese Klasse verwendet ctypes.Structure, um die Struktur eines allgemeinen Python-Objekts darzustellen. Sie enthält zwei Felder: ob_refcnt (Referenzzähler) und ob_type (Typzeiger).
    analyze_object Funktion: Diese Funktion analysiert das übergebene Objekt und gibt relevante Informationen aus.
"""
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
import ctypes

class PyObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p)]

def analyze_object(obj):
    obj_address = id(obj)
    py_object = PyObject.from_address(obj_address)
    
    print(f"Objektreferenz: {obj_address}")
    print(f"Speichergröße: {sys.getsizeof(obj)} Bytes")
    print(f"Referenzzähler: {py_object.ob_refcnt}")
    print(f"Typ: {ctypes.cast(py_object.ob_type, ctypes.py_object).value.__name__}")

# Beispielobjekte
int_obj = 1
float_obj = 3.14159
string_obj = "Hallo Welt"
bool_obj = True

# Analyse der Objekte
print("Ganze Zahl:", int_obj)
analyze_object(int_obj)
print("\nFließkommazahl:", float_obj)
analyze_object(float_obj)
print("\nZeichenkette:", string_obj)
analyze_object(string_obj)
print("\nBoolean True:", bool_obj)
analyze_object(bool_obj)

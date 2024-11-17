import struct
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
def float_to_bin(value):
    [d] = struct.unpack(">Q", struct.pack(">d", value))
    return f"{d:064b}"

value = -11.625     #EINGABE             
binary_value = float_to_bin(value)
sign = binary_value[0]
exponent = binary_value[1:12]
mantisse = binary_value[12:]

print("Vorzeichen:", sign)
print("Exponent:", exponent)
print("Mantisse:", mantisse)
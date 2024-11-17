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
def int_to_bin(value, bits):
    """
    Wandelt eine ganze Zahl in eine binäre Darstellung um.
    
    :param value: Die zu konvertierende Zahl.
    :param bits: Die Anzahl der Bits für die Darstellung.
    :return: Binäre Darstellung der Zahl als Zeichenkette.
    """

    if value >= 0:
        # Für positive Zahlen
        bin_format = f'0{bits}b'
    else:
        # Für negative Zahlen: Zweierkomplement
        value = (1 << bits) + value
        bin_format = f'0{bits}b'
    
    return format(value, bin_format)

positive_number = 15    #EINGABE
negative_number = -11   #EINGABE
bits = 8                #EINGABE (2^n = 2,4,8,16,32,64...)

positive_bin = int_to_bin(positive_number, bits)
negative_bin = int_to_bin(negative_number, bits)

print(f"Positive Zahl {positive_number} in binär: {positive_bin}")
print(f"Negative Zahl {negative_number} in binär: {negative_bin}")
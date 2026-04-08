# Importar las logicas de interes simple
from logica_interes_simple import *


# Menu principal

def menu():
    while True:
        try:
            print("==========  Calculadora Financiera ==========")
            
            print("""
            0. Salir
            1.Interes Simple
            2.Interes Compuesto      
            """)
            try:
                opcion = input("Eliga una opcion: ")
            except ValueError as e:
                print("Error: Asegurese de escribir un numero entero! ")
            
        
        except Exception as e:
            print(f"Error: {e}")
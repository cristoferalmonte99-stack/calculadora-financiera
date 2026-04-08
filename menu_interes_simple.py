import logica_interes_simple
 
def pedir_datos_interes():
    capital = float(input("Ingrese el capital: "))
    tasa = float(input("Ingrese la tasa (%): "))
    tiempo = float(input("Ingrese el tiempo: "))
    return capital, tasa, tiempo

def menu_interes_simple():
    while(True):
        try:
            print("""
                  0. Volver atras
                  1. Calcular Interes (I)
                  2. Calcular capital (c)
                  3. Calcular monto (M)
                  4. Calcular Tasa
                  5. Calcular Tiempo
                  """)
            
            try:
                opcion = int(input("Ingrese una opcion: "))
            except ValueError as e:
                print("Error: Solo se aceptan caracteres numericos ")
                continue
            
            if opcion == 0: 
                break
            elif opcion == 1:
                capital, tasa, tiempo = pedir_datos_interes()
                resultado = logica_interes_simple.calcular_interes_simple(capital, tasa, tiempo)
                print(f"El interes generado es: {resultado}")
                
        
        except Exception as e:
            print(f"Error: {e}")
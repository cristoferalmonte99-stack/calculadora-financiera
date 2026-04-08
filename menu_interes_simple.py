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
                opcion = intinput
        
        except Exception as e:
            print(f"Error: {e}")
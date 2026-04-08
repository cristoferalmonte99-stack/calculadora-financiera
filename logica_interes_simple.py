# Funcion para calcular el interes simple
def calcular_interes_simple(capital, tasa, tiempo):
    return capital * tasa * tiempo

# Funcion para calcular el capital, usando la formula del interes simple
def calcular_capital_desde_interes(interes, tasa, tiempo):
    return interes / ((tasa / 100) * tiempo )

# Funcion para calcular el capital, usando la formula del monto
def calcular_capital_desde_monto(monto, tasa, tiempo):
    return monto / (1 + (tasa / 100) * tiempo)

# Funcion para calcular el monto
def calcular_monto(capital, tasa, tiempo):
    return capital * (1 + (tasa / 100) * (tiempo))

# Funcion para calcular la tasa despejando la formula del interes simple
def calcular_tasa(interes, capital, tiempo):
    return interes / ((capital * tiempo) * 100 ) 

# Funcion para calcular el tiempo, despejando la formula del interes simple
def calcular_tiempo(interes, capital, tasa):
    return interes / (capital * (tasa / 100))


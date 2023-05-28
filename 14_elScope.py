# El Scope - El Alcance
# Hasta dónde llegan las variables

price = 100 # Scope Global o Alcance Global

def increment():
    price = 200 # Scope Local o Alcance Global - No tiene nada que ver con el Scope Global
    price += 10 # Solo tiene un contexto dentro de la función
    print(price)
    return price

print(price)
price_2 = increment()
print(price_2)
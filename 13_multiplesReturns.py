def find_volume(lenght=1, width=1, depth=1): # Podemos asignar valores por defecto
        return lenght * width * depth, width, 'hola' # Podemos retornar varios valores. Nos los devolverá en una tupla

result, width, text = find_volume(width=10) # Si los separamos y los printeamos, nos va a devolver cada valor
print(result)
print(width)
print(text)
# Map
# Hace transformaciones a una lista dada de elementos

# Hacemos una transformación a una lista como se haría normalmente
numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)
print(numbers)
print(numbers_v2)

# Hacemos una transformación con map a una lista
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

# Map puede iterar dos listas y darme una transformación de ellas
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]
result = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(numbers_1)
print(numbers_2)
# Suma el primer valor de cada lista y nos da una lista nueva con ese valor, así sucesivamente...
# Llega a tener un límite de la lista más pequeña
print(result)
# Ejemplos de Uso de Funciones

def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum = sum + x
    return sum # Retorna un valor

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
sum_with_range(1, 100)
# Reduce
# Tomar una lista y sacar una conclusión de esa lista
import functools # Nos toca importar reduce

numbers = [1, 2, 3, 4]

def accum(counter, item):
    print(f'Counter {counter}')
    print(f'item {item}')
    return counter + item

result = functools.reduce(accum, numbers)
print(result)

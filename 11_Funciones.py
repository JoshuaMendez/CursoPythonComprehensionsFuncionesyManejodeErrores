print('Hola')


def my_print(text):  # Todo lo que quede dentro de los () de esta función se llaman Parámetros
    print(text * 2)


# Todo lo que quede dentro de los () de esta llamada a la función se llaman Argumentos
my_print('Este es my texto')
# Las funciones se pueden volver a utilizar las veces que queramos
my_print('Hola')


# Podemos hacer funciones para hacer operaciones
def suma(a, b):
    print(a+b)


suma(10, 15)  # Podríamos llamar la función las veces que queramos

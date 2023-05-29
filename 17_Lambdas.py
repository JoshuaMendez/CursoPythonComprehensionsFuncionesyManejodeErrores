# Función Normal
def increment(x):
    return x + 1
result = increment(10)
print(result)

# Función Lambda
lambda x : x + 1 # lambda (entrada de argumentos): (cómo debería de retornar el argumento)
increment_v2 = lambda x : x + 1
result = increment_v2(20)
print(result)

# Función Lambda 2
full_name = lambda name, lastName : f'Full name is {name.title()} {lastName.title()}'
text = full_name('joshua', 'mendez ospina')
print(text)

# Explicación Rápida

# Función Normal
# def Funcion(Argumentos):
#     return ValorRetornado

# Función Lambda
# Funcion = lambda Argumentos : ValorRetornado

# Función Lambda es como una forma de comprimir una función normal
# Obviamente SIGUE siendo una función y se tiene que llamar como Funcion(Argumentos)

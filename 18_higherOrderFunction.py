# Funciones dentro de otras funciones
# También podemos enviar como atributo una función y ejecutarla dentro de otra función

def increment(x):
    return x + 1

def high_order_function(x, func):
    return x + func(x)

result = high_order_function(2, increment)
# Le mandamos un 2 + (2 + 1) <- Función increment()
print(result)

# Funciones Lambdas

incrementLambdaVersion = lambda x : x + 1
high_order_functionLambdaVersion = lambda x, func: x + func(x)
result = high_order_functionLambdaVersion(2, incrementLambdaVersion)
print(result)
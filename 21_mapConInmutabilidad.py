items = [
    {
        'product': 'camisa',
        'precio': 100,
    },
    {
        'product': 'pantalones',
        'precio': 300
    },
    {
        'product': 'pantalones 2',
        'precio': 200
    }
]

# ¿Cómo agregar un atributo nuevo al diccionario?
# Output esperado:
#
# items = [
#     {
#         'product': 'camisa',
#         'precio': 100,
#  ---->  'taxes': 100 * .19  <----
#     }
# ]

def add_taxes(items):
    new_items = items.copy() # Creando una nueva lista copiando todo lo de la anterior, evitamos el error de que el map sobreescriba los datos en la lista con diccionario anteriores
    new_items['taxes'] = new_items['precio'] * .19 # Problemas de Mutabilidad e Inmutabilidad solucionados
    return new_items

new_items = list(map(add_taxes, items))
print(new_items)

# Map no modifica el array original, si no que crea uno nuevo
# Ya está solucionado
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

# ¿Cómo hago para tener solo los precios en una lista?
# Output esperado: [100, 300, 200]

prices = list(map(lambda item: item['precio'], items))
print(prices)

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
    items['taxes'] = items['precio'] * .19
    return items

new_items = list(map(add_taxes, items))
print(new_items)

# Map no modifica el array original, si no que crea uno nuevo
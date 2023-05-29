numbers = [1, 2, 3, 4, 5]
#                  filter(los números que sean divisibles entre 2 (o números pares) )
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
# Al igual que map(), filter() no crea una nueva lista
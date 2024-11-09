import random
lista = []
for i in range(100):
    lista.append(random.randint(1, 1000))
print(f'Lista Original: {lista}')
print('=-'*20)

n = len(lista)
for i in range(n-1):
    for j in range(n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(f'Lista Ordenada: {lista}')
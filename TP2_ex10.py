import random
lista_cod_livros = []
for i in range(100):
    lista_cod_livros = random.sample(range(1, 1001), 100)
print(f'Lista Original: {lista_cod_livros}')

n = len(lista_cod_livros)
print('Quandidade de livros na lista:', n)

def livros_cod_impar(lista_de_livros):
    lista_cod_impar = []
    for i in range(len(lista_de_livros)):
        if lista_de_livros[i] % 2 != 0:
            lista_cod_impar.append(lista_de_livros[i])
    return lista_cod_impar

print('=-'*20)
print('Lista de livros com códigos ímpares:', livros_cod_impar(lista_cod_livros))
print('Total de livros com códigos ímpares:', len(livros_cod_impar(lista_cod_livros)))
print('=-'*20)
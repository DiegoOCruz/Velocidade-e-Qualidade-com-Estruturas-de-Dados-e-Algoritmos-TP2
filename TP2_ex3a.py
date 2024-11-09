#ex. 2a
opcoes = [
    "maçã", "banana", "laranja", "uva", "melancia", "abacaxi", 
    "morango", "kiwi", "pêssego", "cereja", "manga", "mamão", 
    "ameixa", "pera", "limão", "caqui", "nectarina", "figo", 
    "jabuticaba", "goiaba" ,"maçã" 
]


duplicados = []
for i in range(len(opcoes)):
    for j in range(i + 1, len(opcoes)):
        if opcoes[i] == opcoes[j]:
            duplicados.append(opcoes[i])


if duplicados:
    for item in duplicados:
        print(f'Item duplicado: {item}')
else:
    print('Não há itens duplicados')
#--------------------------------------------
#ex. 2b
print('-----exercício 2b-----')
duplicados = []
vistos = []
for item in opcoes:
    for item in vistos:
        if item in vistos:
            duplicados.append(item)

if duplicados:
    for item in duplicados:
        print(f'Item duplicado: {item}')
else:
    print('Não há itens duplicados')
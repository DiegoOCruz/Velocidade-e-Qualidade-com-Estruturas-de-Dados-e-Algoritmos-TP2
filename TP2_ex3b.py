#ex. 2a
opcoes = [
    "maçã", "banana", "laranja", "uva", "melancia", "abacaxi", 
    "morango", "kiwi", "pêssego", "cereja", "manga", "mamão", 
    "ameixa", "pera", "limão", "caqui", "nectarina", "figo", 
    "jabuticaba", "goiaba" ,"maçã" , "goiaba"
]
#ex. 2b
duplicados = []
vistos = []


for item in opcoes:
    if item in vistos:
        if item not in duplicados:
            duplicados.append(item)
    else:
        vistos.append(item)

if duplicados:
    for item in duplicados:
        print(f'Item duplicado: {item}')
else:
    print('Não há itens duplicados')
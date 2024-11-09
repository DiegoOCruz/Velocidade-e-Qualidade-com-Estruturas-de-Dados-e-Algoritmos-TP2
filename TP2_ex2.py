#Questão 2a
def merge_sort(arr):
    if len(arr) > 1:
        # Divide o array ao meio
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        # Ordena cada metade recursivamente
        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        # Variáveis para iterar sobre cada metade e o array principal
        i = j = k = 0

        # Mescla as duas metades
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        # Copia o restante dos elementos da metade esquerda, se houver
        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        # Copia o restante dos elementos da metade direita, se houver
        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10, 48, 36, 38, 124, 79, 1, 4, 2, 0]
merge_sort(arr)
print("Array ordenado:", arr)

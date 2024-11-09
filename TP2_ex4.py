class Notas:
    def __init__(self):
        self.itens = []

    def lancar(self, item):
        self.itens.append(item)

    def ultima_lancada(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            return "Nao existem notas lancadas."
    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            return "Nao existem notas lancadas."

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def ordenar_notas(self):
        
        lista_temp = []
        while not self.esta_vazia():
            lista_temp.append(self.ultima_lancada())

        #Ordenar a lista usando Bubble Sort
        n = len(lista_temp)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_temp[j] > lista_temp[j + 1]:
                    # Troca de elementos
                    lista_temp[j], lista_temp[j + 1] = lista_temp[j + 1], lista_temp[j]

        
        for item in lista_temp:
            self.lancar(item)

Diego_notas = Notas()
Diego_notas.lancar(5)
Diego_notas.lancar(9.5)
Diego_notas.lancar(10)
Diego_notas.lancar(6.5)

print("Notas antes da ordenação:", Diego_notas.itens)  
Diego_notas.ordenar_notas()
print("Notas após a ordenação:", Diego_notas.itens)  

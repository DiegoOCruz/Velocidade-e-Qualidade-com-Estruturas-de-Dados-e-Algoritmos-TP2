class HashTable:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade  
        self.tabela = [[] for _ in range(capacidade)]  
        self.size = 0  

    def hash(self, chave):
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        indice = self.hash(chave)  
        for par in self.tabela[indice]:  
            if par[0] == chave:
                par[1] = valor  
                return
        

        self.tabela[indice].append([chave, valor])
        self.size += 1  

    def buscar(self, chave):
        indice = self.hash(chave)  
        for par in self.tabela[indice]:  
            if par[0] == chave:
                return par[1]  
        return None 

    def remover(self, chave):
        indice = self.hash(chave) 
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]  
                self.size -= 1  
                return True 
        return False 

    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"


tabela_hash = HashTable()
tabela_hash.inserir("chave1", "valor1")
tabela_hash.inserir("chave2", "valor2")
tabela_hash.inserir("chave3", "valor3")

print("Tabela Hash após inserções:", tabela_hash) 


print("Busca 'chave2':", tabela_hash.buscar("chave2"))  
print("Busca 'chave4':", tabela_hash.buscar("chave4"))  


tabela_hash.remover("chave2")
print("Tabela Hash após remoção de 'chave2':", tabela_hash)  

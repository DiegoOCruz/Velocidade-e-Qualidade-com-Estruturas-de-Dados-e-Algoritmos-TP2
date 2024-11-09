class FilaAtendimento:
    def __init__(self):
        self.fila = []
    
    def adicionar_cliente(self, cliente):
        self.fila.append(cliente)
        return print(f'Cliente {cliente} adicionado à fila')
    
    def atender_cliente(self):
        if len(self.fila) > 0:
            print(f'Cliente {self.fila[0]} atendido')
            return self.fila.pop(0)
        return None
    
    def tamanho_fila(self):
        if len(self.fila) == 0:
            return print('Fila vazia')
        return print(f'Clientes na fila: {len(self.fila)}')

clientes = FilaAtendimento()
clientes.adicionar_cliente("João")
clientes.adicionar_cliente("Maria")
clientes.adicionar_cliente("José")
clientes.adicionar_cliente("Ana")
clientes.adicionar_cliente("Carlos")
print('=-'*20)
clientes.tamanho_fila()
print('=-'*20)
clientes.atender_cliente()
print('=-'*20)
clientes.tamanho_fila()
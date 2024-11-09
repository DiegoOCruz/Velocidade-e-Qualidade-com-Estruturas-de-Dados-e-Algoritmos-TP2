import random

lista_pedido = []

class Pedido:
    def __init__(self,):
        self.id = random.randint(1, 100)
        lista_pedido.append(self.id) 

    @staticmethod
    def contar_pedidos_impares():
        return sum(1 for pedido_id in lista_pedido if pedido_id % 2 != 0)


pedido_1 = Pedido()
pedido_2 = Pedido()
pedido_3 = Pedido()
pedido_4 = Pedido()


print("Lista de pedidos:", lista_pedido)


quantidade_impares = Pedido.contar_pedidos_impares()
print("Quantidade de pedidos com número de identificação ímpar:", quantidade_impares)


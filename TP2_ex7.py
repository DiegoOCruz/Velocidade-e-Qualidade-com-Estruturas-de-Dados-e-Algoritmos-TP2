import random

lista_pedido = []

class Pedido:
    def __init__(self,):
        self.id = random.randint(1, 100)
        lista_pedido.append(self.id) 

    @staticmethod
    def contar_pedidos_pares():
        return sum(1 for pedido_id in lista_pedido if pedido_id % 2 == 0)


pedido_1 = Pedido()
pedido_2 = Pedido()
pedido_3 = Pedido()
pedido_4 = Pedido()


print("Lista de pedidos:", lista_pedido)


quantidade_pares = Pedido.contar_pedidos_pares()
print("Quantidade de pedidos com número de identificação pares:", quantidade_pares)


fila_pacientes = []

class Paciente:
    def __init__(self, nome):
        self.nome = nome
        fila_pacientes.append(self.nome)  

    @staticmethod
    def lista_ordem_chegada():
        print(fila_pacientes)

    @staticmethod
    def inverter_ordem_fila():
        fila_pacientes_invertida = [] 
        

        for i in range(len(fila_pacientes) - 1, -1, -1):
            fila_pacientes_invertida.append(fila_pacientes[i])


        fila_pacientes.clear()
        for paciente in fila_pacientes_invertida:
            fila_pacientes.append(paciente)

        print(fila_pacientes)



paciente_1 = Paciente("João")
paciente_2 = Paciente("Maria")
paciente_3 = Paciente("José")
paciente_4 = Paciente("Ana")
paciente_5 = Paciente("Carlos")


print('Fila de pacientes original:')
Paciente.lista_ordem_chegada()
print('Fila de pacientes invertida:')
Paciente.inverter_ordem_fila()
print('Fila de pacientes original:')
Paciente.inverter_ordem_fila()


tarefas_a_fazer = ["tarefa 1", "tarefa 2", "tarefa 3", "tarefa 4", "tarefa 5", "tarefa 6", "tarefa 7", "tarefa 8", "tarefa 9", "tarefa 10"]

pilha_de_tarefas_ = []
def tarefa_no_topo(pilha_de_tarefas):
    for tarefa in pilha_de_tarefas:
        pilha_de_tarefas_.append(tarefa)
    print("Tarefa no topo da pilha:", pilha_de_tarefas[-1])

tarefa_no_topo(tarefas_a_fazer)
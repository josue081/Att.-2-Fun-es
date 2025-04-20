import json

# Lê as tarefas do arquivo
def ler():
    try:
        with open("tarefas.json", "r") as f:
            return json.load(f)
    except:
        return []

# Salva as tarefas no arquivo
def salvar(tarefas):
    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f)

# Adiciona uma tarefa
def adicionar(texto):
    t = ler()
    t.append([texto, False])
    salvar(t)

# Lista as tarefas
def listar():
    t = ler()
    for i in range(len(t)):
        print(i + 1, t[i][0], "-" , "OK" if t[i][1] else "X")

# Marca como concluída
def concluir(n):
    t = ler()
    if n - 1 < len(t):
        t[n - 1][1] = True
        salvar(t)

# Teste simples
adicionar("Estudar java")
listar()
concluir(1)
listar()

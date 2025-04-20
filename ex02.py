import json

def ler():
    try:
        with open("estoque.json", "r") as f:
            return json.load(f)
    except:
        return []

def salvar(e):
    with open("estoque.json", "w") as f:
        json.dump(e, f)

def add(nome, qtd, preco):
    e = ler()
    e.append([nome, qtd, preco])
    salvar(e)

def mostrar():
    e = ler()
    total = 0
    for p in e:
        print(p[0], "-", p[1], "unid - R$", p[2])
        total += p[1] * p[2]
    print("Total: R$", total)

# Teste simples
add("Óleo", 10, 5.5)
add("peixe", 5, 8.0)
mostrar()

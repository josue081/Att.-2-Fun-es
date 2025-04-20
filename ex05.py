import json

def ler():
    try:
        with open("contatos.json", "r") as f:
            return json.load(f)
    except:
        return []

def salvar(c):
    with open("contatos.json", "w") as f:
        json.dump(c, f)

def add(n, t, e):
    c = ler()
    c.append([n, t, e])
    salvar(c)

def buscar(n):
    c = ler()
    for x in c:
        if x[0].lower() == n.lower():
            print(x[0], x[1], x[2])
            return

# Teste simples
add("Josuu", "99999-9999", "Josuu@email.com")
buscar("Josuu")

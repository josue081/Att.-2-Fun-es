assentos = {"A1": False, "A2": False, "B1": False, "B2": False}

def mostrar():
    for a in assentos:
        s = "X" if assentos[a] else "O"
        print(a, ":", s)

def reservar(a):
    if a in assentos and not assentos[a]:
        assentos[a] = True

# Teste simples
mostrar()
reservar("A1")
mostrar()

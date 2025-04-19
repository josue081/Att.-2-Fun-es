u = {"Josuu": ["1234", 100]}

def entrar(nome, senha):
    if nome in u and u[nome][0] == senha:
        return nome

def dep(n, v):
    u[n][1] += v

def sacar(n, v):
    if u[n][1] >= v:
        u[n][1] -= v

# Teste simples
x = entrar("Josuu", "1234")
if x:
    dep(x, 50)
    sacar(x, 30)

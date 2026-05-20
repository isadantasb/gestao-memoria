def first(memoria, tamanho):
    cont = 0
    ini = 0
    for i in range(memoria.tam):
        if memoria.enderecos[i] is None:
            if cont == 0:
                ini = i
            cont += 1
            if cont == tamanho:
                fim = i
                return ini, fim
        else: 
            cont = 0
    return None

def best():
    pass

def worst():
    pass

def buddy():
    pass

def aloca(memoria, tabela, pid, tamanho, algoritmo):
    resultado = algoritmo(memoria, tamanho)
    if resultado is None:
        return None 
    ini, fim = resultado
    for i in range(ini, fim + 1):
        memoria.enderecos[i] = pid
    tabela.adicionar(pid, ini, fim, tamanho)
    return ini, fim

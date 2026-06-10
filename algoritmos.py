from memoria import Memoria

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

def best(memoria, tamanho):
    '''
    '''
    cont = 0
    ini = 0
    bloco_min = memoria.tam + 1
    endereco = -1
    for i in range(memoria.tam ):
        if memoria.enderecos[i] is None:
            if cont == 0:
                ini = i
            cont += 1
        else:
            if cont >= tamanho:
                if cont < bloco_min:
                    bloco_min = cont
                    endereco = ini
            cont = 0
    if bloco_min == memoria.tam + 1:
        return None
    else:

        fim = endereco + tamanho

        return endereco, fim

def worst(memoria, tamanho):
    '''
    '''
    cont = 0
    ini = 0
    bloco_max = -1
    endereco = -1
    for i in range(memoria.tam):
        
        if memoria.enderecos[i] is None:
            if cont == 0:
                ini = i
            cont += 1
        else:
            if cont >= tamanho:
                if cont > bloco_max:
                    bloco_max = cont
                    endereco = ini
            cont = 0
    if bloco_max == -1:
        return None

    else:
        fim = endereco + tamanho
        return endereco, fim

def buddy(tamanho):
    res = 2
    while tamanho > res:
        res = res ** 2
    return res


def aloca(memoria, tabela, pid, tamanho, algoritmo):
    resultado = algoritmo(memoria, tamanho)
    if resultado is None:
        return None 
    ini, fim = resultado
    for i in range(ini, fim + 1):
        memoria.enderecos[i] = pid
    tabela.adicionar(pid, ini, fim, tamanho)
    return ini, fim

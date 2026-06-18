def first(memoria, tamanho):
    cont = 0
    ini = 0
    for i in range(memoria.tam):
        if memoria.enderecos[i] is None:
            if cont == 0:
                ini = i
            cont += 1
            if cont == tamanho:
                return ini
        else: 
            cont = 0
    return None

def best(memoria, tamanho):
    cont = 0
    ini = 0
    bloco_min = memoria.tam + 1
    endereco = -1
    for i in range(memoria.tam):
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
    # verifica o último bloco livre
    if cont >= tamanho:
        if cont < bloco_min:
            bloco_min = cont
            endereco = ini
    if bloco_min == memoria.tam + 1:
        return None
    else:
        return endereco

def worst(memoria, tamanho):
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
    # verifica o último bloco livre
    if cont >= tamanho:
        if cont > bloco_max:
            bloco_max = cont
            endereco = ini
    if bloco_max == -1:
        return None
    else:
        return endereco

def buddy(memoria, tamanho):
    res = 2
    while tamanho > res:
        res = res << 1
    return res


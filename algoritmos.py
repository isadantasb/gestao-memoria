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

class Buddy:
    def __init__(self, memoria):
        self.memoria = memoria
        self.livres = {
            4096: [0]
        }
        self.alocados = {}
        
    def prox_pot2(self, n):
        tam = 2
        while tam < n:
            tam *= 2
        return tam
    
    def aloca(self, pid, tamanho):
        tamanho_real = self.prox_pot2(tamanho)
        bloco_tam = tamanho_real
        while bloco_tam <= 4096:
            if bloco_tam in self.livres and self.livres[bloco_tam]:
                break
            bloco_tam *= 2

        if bloco_tam > 4096:
            return None
        endereco = self.livres[bloco_tam].pop(0)
        while bloco_tam > tamanho_real:
            metade = bloco_tam // 2
            buddy = endereco + metade
            if metade not in self.livres:
                self.livres[metade] = []
            self.livres[metade].append(buddy)
            bloco_tam = metade
            
        self.alocados[pid] = (endereco, bloco_tam)
        print(f"Alocando PID {pid} no endereço {endereco} com tamanho {bloco_tam}")
        print(endereco)
        print(f'livres: {self.livres}, alocados: {self.alocados}')
        return endereco, tamanho_real
    
    def libera(self, pid):
        if pid not in self.alocados:
            return None
        endereco, tamanho = self.alocados.pop(pid)
        while tamanho < 4096:
            buddy = endereco ^ tamanho
            if tamanho not in self.livres:
                self.livres[tamanho] = []

            if buddy in self.livres[tamanho]:
                self.livres[tamanho].remove(buddy)
                endereco = min(endereco, buddy)
                tamanho *= 2
            else:
                break
        if tamanho not in self.livres:
            self.livres[tamanho] = []
        self.livres[tamanho].append(endereco)

        return endereco
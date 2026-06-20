import sys
import os
from memoria import *
from algoritmos import *
from collections.abc import Callable

ESTRATEGIAS = {
    'first': first,
    'best': best,
    'worst': worst,
    'buddy': Buddy,
}

if len(sys.argv) < 3:
    print("usage: python main.py [first|best|worst|buddy] exemplos_entrada/entrada.txt")
    sys.exit(1)

arquivo = sys.argv[-1]
nome_estrategia = sys.argv[1]

if nome_estrategia not in ESTRATEGIAS:
    print("Estratégia de alocação inválida. Use 'first', 'best', 'worst' ou buddy.")
    sys.exit(1)

estrategia : Callable = ESTRATEGIAS[nome_estrategia]
memoria = Memoria()
tabela = TabelaParticoes()
buddy = None
if nome_estrategia == 'buddy':
    buddy = Buddy(memoria)

def le_arquivo(arq_entrada):
    requisicoes = []
    
    with open(arq_entrada, 'r') as file:
        num_processos = int(file.readline().strip())
        linha_pids = file.readline().strip()
        pids = linha_pids.split(';')

        for linha in file:
            linha = linha.strip()
        
            partes = linha.split()
            comando = partes[0]
            pid = partes[1]
            if comando == 'aloca':
                tam = int(partes[-1])
                requisicoes.append({'comando': 'aloca', 'pid': pid, 'valor': tam})

            elif comando == 'libera':
                requisicoes.append({'comando': 'libera', 'pid': pid})

            elif comando == 'acessa':
                endereco = int(partes[-1])
                requisicoes.append({'comando': 'acessa', 'pid': pid, 'valor': endereco})

    return num_processos, pids, requisicoes

def aloca(pid: str, tamanho: int, mmu : MMU):
    global estrategia
    global buddy

    if nome_estrategia == 'buddy':
        endereco_inicial, tamanho_real = buddy.aloca(pid, tamanho)
        endereco_final = endereco_inicial + tamanho_real - 1
        
    else:
        endereco_inicial = estrategia(mmu.memoria, tamanho)
        if endereco_inicial is None:
            return None
        endereco_final = endereco_inicial + tamanho - 1

    mmu.tabela_particoes.adicionar(pid, endereco_inicial, endereco_final)
    for i in range(endereco_inicial, endereco_final + 1):
        mmu.memoria.enderecos[i] = pid
    
    return endereco_inicial, endereco_final
   
def desaloca(pid : str, mmu : MMU):
    global buddy 
    particao = mmu.tabela_particoes.buscar(pid)
    if particao is not None:
        for i in range(particao['base'], particao['limite']+1):
            mmu.memoria.enderecos[i] = None
        if nome_estrategia == "buddy":
            buddy.libera(pid)
        mmu.tabela_particoes.remover(pid)
        return particao['base'], particao['limite']
    else:
        return None
    
def main():
    num_processos, pids, requisicoes = le_arquivo(arquivo)
    logs = []

    mmu = MMU(memoria, tabela)
    for req in requisicoes:
        if req['comando'] == 'aloca':
            end, fim = aloca(req['pid'], req['valor'], mmu)
            if req['pid'] is not None:
                logs.append(f"alocacao {req['pid']} {end} {fim}")
            else: 
                logs.append(f"alocacao {req['pid']} erro!")
                break
        elif req['comando'] == 'libera':
            inicio, fim = desaloca(req['pid'], mmu)
            logs.append(f"liberacao {req['pid']} {inicio} {fim}")
        elif req['comando'] == 'acessa':
            try: 
                valor = mmu.traduz(req['pid'], req['valor'])
                logs.append(f"acesso {req['pid']} {req['valor']} {valor}")
            except:
                logs.append(f"acesso {req['pid']} {req['valor']} violacao")
    print(logs)
        

    nome = os.path.basename(arquivo)
    nome = os.path.splitext(nome)[0]

    nome_log = f"log_{nome}_{nome_estrategia}.txt"



    with open(nome_log, "w", encoding="utf-8") as f:
        for linha in logs:
            f.write(linha + "\n")

    print("-----------------------------")
    print("tabela de partições:")
    print(mmu.tabela_particoes.particoes)
    print("-----------------------------")



if __name__ == "__main__":
    main()
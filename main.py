import sys
import os
from memoria import *
from algoritmos import *
from collections.abc import Callable

ESTRATEGIAS = {
    'first': first,
    'best': best,
    'worst': worst,
    'buddy': buddy,
}


if len(sys.argv) < 3:
    print("usage: python main.py [first|best|worst|buddy] exemplos_entrada/entrada.txt")
    sys.exit(1)

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


def main():
    num_processos, pids, requisicoes = le_arquivo(sys.argv[-1])
    logs = []
    memoria = Memoria()
    tabela = TabelaParticoes()
    nome_estrategia = sys.argv[1]
    if nome_estrategia not in ESTRATEGIAS:
        print("Estratégia de alocação inválida. Use 'first', 'best' ou 'worst'.")
        sys.exit(1)
    estrategia : Callable = ESTRATEGIAS[nome_estrategia]

    mmu = MMU(memoria, estrategia)
    for req in requisicoes:
        if req['comando'] == 'aloca':
            end, fim = mmu.aloca(req['pid'], req['valor'])
            if req['pid'] is not None:
                logs.append(f"alocacao {req['pid']} {end} {fim}")
            else: 
                logs.append(f"alocacao {req['pid']} erro!")
                break
        elif req['comando'] == 'libera':
            inicio, fim= mmu.desaloca(req['pid'])
            logs.append(f"liberacao {req['pid']} {inicio} {fim}")
        elif req['comando'] == 'acessa':
            try: 
                valor = mmu.traduz(req['pid'], req['valor'])
                logs.append(f"acesso {req['pid']} {req['valor']} {valor}")
            except:
                logs.append(f"acesso {req['pid']} {req['valor']} violacao")
    print (logs)
        
    algoritmo = sys.argv[1]
    arquivo = sys.argv[2]

    nome = os.path.basename(arquivo)
    nome = os.path.splitext(nome)[0]

    nome_log = f"log_{nome}__{algoritmo}.txt"
    with open(nome_log, "w", encoding="utf-8") as f:
        for linha in logs:
            f.write(linha + "\n")
        


if __name__ == "__main__":
    main()
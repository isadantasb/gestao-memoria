import sys
from memoria import *
from algoritmos import *
from collections.abc import Callable

ESTRATEGIAS = {
    'first': first,
    'best': best,
    'worst': worst,
}


if len(sys.argv) < 3:
    print("usage: python main.py [first|best|worst|buddy] entrada.txt")
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
            mmu.aloca(req['pid'], req['valor'])
        elif req['comando'] == 'libera':
            mmu.desaloca(req['pid'])
        elif req['comando'] == 'acessa':
            valor = mmu.traduz(req['pid'], req['valor'])
            print(f"Processo {req['pid']} acessou o endereço lógico {req['valor']} e o endereço físico é {valor}.")
        
        


if __name__ == "__main__":
    main()
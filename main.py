import sys
from memoria import *
from algoritmos import *

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
    for req in requisicoes:
        pass
    resultado = aloca(memoria, tabela, "pid", 10, first) #testando
    print(resultado)
    print (memoria.enderecos)


if __name__ == "__main__":
    main()
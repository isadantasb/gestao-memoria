import sys

if len(sys.argv) < 1:
    print("usage main.py textfile.txt")

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
    a, b, c = le_arquivo(sys.argv[-1])
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()
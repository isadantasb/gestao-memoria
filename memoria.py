class Memoria:
    def __init__(self):
        self.tam: int = 1000 #mudei so pra printa mais facil
        self.enderecos = [None] * self.tam

class MMU:
    '''
    representação do componente da MMU para realização das traduções de endereço.
    A implementação lógica de operação da MMU deve seguir o que foi apresentado em sala de aula
    no que tange à tradução de endereços de memória virtual por partições;
    '''
    pass

class TabelaParticoes:
    '''tabela única utilizada pelo SO que mantém o registro das partições já alocadas, 
    armazenando os valores de limite de endereço do processo e início do endereçamento físico na memória física.
    '''
    def __init__(self):
        self.particoes = {}

    def adicionar(self, pid, inicio, fim, tamanho): 
        self.particoes[pid]={
            "inicio": inicio,
            "fim": fim,
            "tamanho": tamanho
        }

    def remover(self, pid):
        if pid in self.particoes:
            pass

    def buscar(self, pid):
        return self.particoes[pid]
from algoritmos import *
from collections.abc import Callable

class Memoria:
    def __init__(self):
        self.tam: int = 4096 
        self.enderecos = [None] * self.tam

class TabelaParticoes:
    '''tabela única utilizada pelo SO que mantém o registro das partições já alocadas, 
    armazenando os valores de limite de endereço do processo e início do endereçamento físico na memória física.
    '''
    def __init__(self):
        '''
        self.particoes = {"pid" : {"base": int, "limite": int, "tamanho": int}}
        '''
        self.particoes = {} 

    def adicionar(self, pid, base, limite): 
        self.particoes[pid]={
            "base": base,
            "limite": limite
        }

    def remover(self, pid):
        if pid in self.particoes:
            self.particoes.pop(pid)
            

    def buscar(self, pid):
        return self.particoes[pid]
    
    
class MMU:
    '''
    representação do componente da MMU para realização das traduções de endereço.
    A implementação lógica de operação da MMU deve seguir o que foi apresentado em sala de aula
    no que tange à tradução de endereços de memória virtual por partições;
    '''
    def __init__(self, memoria : Memoria, tabela_particoes: TabelaParticoes):
        self.memoria = memoria
        self.tabela_particoes = tabela_particoes
       
    def traduz(self, id_processo: str, endereco_logico: int) -> int:
        try:
            particao = self.tabela_particoes.buscar(id_processo)
        except KeyError:
            raise Exception("Processo não mapeado na tabela de partições.")

        base = particao["base"]
        limite = particao["limite"]

        if endereco_logico < 0 or endereco_logico > limite:
            raise Exception("violacao") 

        # eL < L  ->  ef = eL + B
        endereco_fisico = base + endereco_logico
        return endereco_fisico
from algoritmos import *


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
    def __init__(self, memoria : Memoria, estrategia):
        self.memoria = memoria
        self.estrategia = estrategia
        self.tabela_processos = {}

    def aloca(self, id_processo: str, endereco: int, tam: int):
        '''
        Requisicao de alocacao de um processo na memoria, utilizando o algoritmo de alocacao definido.
        '''
        novo_tam = tam
        if tam <= 0 or (tam & (tam - 1)) != 0:
            novo_tam = buddy(tam)
        
        while self.estrategia(self.memoria, novo_tam) is None: # tem que ve se esse self.estrategia funciona
            novo_tam *= 2
            if novo_tam > self.memoria.tam:
                raise Exception("Não há espaço suficiente para alocar o processo.")

        for i in range(endereco, endereco + tam):
            self.memoria.enderecos[i] = id_processo

        self.tabela_processos[id_processo] = (endereco, novo_tam)


    def desaloca(self, id_processo: str):
        '''
        Requisicao de liberacao de um processo na memoria, liberando os enderecos alocados para o processo.
        '''
        for i in range(self.memoria.tam):
            if self.memoria.enderecos[i] == id_processo:
                self.memoria.enderecos[i] = None

    def traduz(self, id_processo: str, endereco_logico: int) -> int:
        '''
        Requisicao de acesso a um endereco logico
        '''
        if id_processo not in self.tabela_processos:
            raise Exception("Processo não encontrado.")
        inicio, tamanho = self.tabela_processos[id_processo]
        if endereco_logico >= tamanho or endereco_logico < 0:
            raise Exception("Endereço lógico fora do limite do processo.")
        endereco_fisico = inicio + endereco_logico
        return self.memoria.enderecos[endereco_fisico]



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
            self.particoes.pop(pid)
            

    def buscar(self, pid):
        return self.particoes[pid]
    

class Memoria:
    def __init__(self):
        self.tam: int = 4096
        self.enderecos = [None] * self.tam

class MMU:
    '''
    representação do componente da MMU para realização das traduções de endereço.
    A implementação lógica de operação da MMU deve seguir o que foi apresentado em sala de aula
    no que tange à tradução de endereços de memória virtual por partições;
    '''
    pass
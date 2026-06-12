from memoria import *
from algoritmos import *

mem = Memoria()

mmu = MMU(mem, first)
mmu.aloca("pid1", 0, 10)
print(mmu.tabela_processos)
print(mmu.traduz("pid1", 5))
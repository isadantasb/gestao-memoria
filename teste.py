from memoria import Memoria
from algoritmos import *

mem = Memoria()

mem.enderecos[0] = "Processo A"
mem.enderecos[1] = "Processo A"
# 2, 3, 4, 5, 6 ficam None (tam 5)
mem.enderecos[7] = "Processo B"
mem.enderecos[8] = "Processo B"
# 9, 10, 11 ficam None (tam 3)
mem.enderecos[12] = "Processo C"

indice_escolhido = best(mem, 2)
print(f"O Best Fit escolheu o índice inicial: {indice_escolhido}")

indice_escolhido = worst(mem, 2)
print(f"O Worst Fit escolheu o índice inicial: {indice_escolhido}")
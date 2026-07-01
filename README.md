# Implementação de Operações de Gestão de Memória para um Sistema Operacional em um Ambiente Computacional Simulado

Trabalho prático desenvolvido para a disciplina 12035 - Sistemas Operacionais da Universidade Estadual de Maringá (UEM).

Este projeto implementa operações de gestão de memória para um Sistema Operacional em um ambiente computacional simulado. A simulação utiliza a técnica de tradução de endereços lógicos para físicos via partições, gerenciando as requisições de alocação, acesso e liberação de memória em Unidades de Armazenamento (UA)

## Integrantes
- Isadora Dantas Bruchmam   | RA: 140870
- Vinicius Taguchi Okada    | RA: 140064

## Tecnologias Utilizadas

### Linguagem
- Python 3.13.3

### Bibliotecas Adicionais
- Collections ABC 

## Funcionalidades implementadas
O simulador realiza a leitura e o processamento de um arquivo em formato de texto (.txt), executando sequencialmente as instruções de alocação, liberação e acesso contidas nele.

### Simulação de componentes
O ambiente emula o comportamento integrado dos seguintes componentes de hardware e do Sistema Operacional:
- Memória
- MMU (Memory Management Unit)
- Tabela de Partições

### Estratégias de Alocação
O sistema gerencia o espaço livre e mitiga a fragmentação através de quatro algoritmos de busca distintos:
- Best-fit
- Worst-fit
- First-fit
- Buddy

## Estrutura do código
- `main.py`: Arquivo principal, responsável por ler o arquivo de teste, processar as requisições e gerar o log de saída.
- `algoritmos.py`: Contém a lógicas das quatro estratégias implementqadas.
- `memoria.py`: Contém as classes dos componentes físicos e lógicos implementados.


## Como executar
A aplicação é executada via terminal, exigindo a passagem de dois parâmetros: A estratégia de alocação; O caminho para o arquivo que contém as instruções de entrada

```bash
python main.py [first|best|worst|buddy] entrada.txt
``` 
-Exemplo:
```bash
python main.py first entrada001.txt
```
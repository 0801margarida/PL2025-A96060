# Analise de Obras

## Autor(a)

Ana Margarida Pires, A96060

## Resumo

Este programa tem como objetivo analisar um ficheiro CSV que contém informação sobre obras musicais. A partir dos dados fornecidos, o programa identifica os compositores únicos, calcula a distribuição de obras por período histórico e organiza os títulos das obras por cada período. Os resultados são apresentados de forma clara no terminal.

## Descrição
O programa realiza as seguintes etapas:

1. Leitura do ficheiro CSV:
Utiliza expressões regulares para extrair o cabeçalho e as linhas de dados do ficheiro. O ficheiro CSV deve estar separado por ponto e vírgula (;), e conter pelo menos as colunas compositor, periodo e nome.

2. Processamento dos dados:
Primeiramente, o programa extrai a lista de compositores únicos. Após isso, conta quantas obras pertencem a cada período histórico. Finalmente, agrupa os nomes das obras por período.

3. Apresentação dos resultados:
Os resultados são impressos no terminal e incluem:
- Lista ordenada de compositores.
- Número de obras por período.
- Lista ordenada de títulos por período.

**NOTA**: O programa é executado via linha de comandos e recebe como argumento o caminho para o ficheiro CSV com os dados.

## Resultados
Ao correr o programa com um ficheiro de entrada válido, o utilizador deverá obter:

- Uma lista de compositores ordenada alfabeticamente.
- Um dicionário com a contagem de obras por período (por exemplo: {"Barroco": 5, "Romântico": 3}).
- Um dicionário com listas de obras agrupadas por período, com os títulos ordenados alfabeticamente.

Exemplo de saída:
```
Lista de Compositores:
['Bach', 'Beethoven', 'Mozart']

Distribuição de Obras por Período:
{'Barroco': 2, 'Clássico': 3, 'Romântico': 1}

Dicionário de Obras por Período:
Barroco: ['Obra 1', 'Obra 2']
Clássico: ['Obra A', 'Obra B', 'Obra C']
Romântico: ['Obra X']
```
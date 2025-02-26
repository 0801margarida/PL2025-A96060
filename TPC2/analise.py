import re
from collections import defaultdict

# Função para analisar o ficheiro CSV usando expressões regulares
def parse_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Dividir o conteúdo em linhas
    lines = content.split('\n')
    
    # Extrair o cabeçalho
    header = lines[0].split(';')
    
    # Extrair as linhas
    rows = []
    for line in lines[1:]:
        if line.strip():
            # Usar regex para dividir por ponto e vírgula, considerando campos entre aspas
            row = re.split(r"(?s)([^;]+);(\".*?\");([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)\n", line)
            if len(row) == len(header):
                rows.append(dict(zip(header, row)))
    
    return rows

# Analisar o ficheiro CSV
obras = parse_csv('obras.csv')

# Verificar o cabeçalho
print("Cabeçalho:", obras[0].keys())

# Gerar compositores.txt
compositores = sorted(set(obra['compositor'] for obra in obras))
with open('compositores.txt', 'w', encoding='utf-8') as file:
    for compositor in compositores:
        file.write(compositor + '\n')

# Gerar obrasPeriodo.txt
periodo_count = defaultdict(int)
for obra in obras:
    periodo_count[obra['periodo']] += 1

with open('obrasPeriodo.txt', 'w', encoding='utf-8') as file:
    for periodo, count in periodo_count.items():
        file.write(f'{periodo}: {count} obras\n')

# Gerar titulosPeriodo.txt
periodo_titulos = defaultdict(list)
for obra in obras:
    periodo_titulos[obra['periodo']].append(obra['nome'])

with open('titulosPeriodo.txt', 'w', encoding='utf-8') as file:
    for periodo, titulos in periodo_titulos.items():
        file.write(f'{periodo}:\n')
        for titulo in sorted(titulos):
            file.write(f'  - {titulo}\n')

print("Ficheiros gerados com sucesso: compositores.txt, obrasPeriodo.txt, titulosPeriodo.txt")
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    # Extrair o cabeçalho
    cabecalho = linhas[0].strip().split(';')
    num_colunas = len(cabecalho)  # Número de colunas esperado
    
    # Processar as linhas de dados
    dados = []
    for linha in linhas[1:]:
        valores = linha.strip().split(';')
        
        # Verificar se o número de valores corresponde ao número de colunas
        if len(valores) != num_colunas:
            print(f"Aviso: Linha ignorada (número incorreto de colunas): {linha}")
            continue  # Ignora esta linha e passa para a próxima
        
        # Criar um dicionário para cada obra
        obra = {}
        for i, coluna in enumerate(cabecalho):
            obra[coluna] = valores[i]
        dados.append(obra)
    
    return dados

def lista_compositores(dados):
    compositores = set()
    for obra in dados:
        if 'compositor' in obra:  # Verifica se a chave 'compositor' existe
            compositores.add(obra['compositor'])
    return sorted(compositores)

def distribuicao_por_periodo(dados):
    distribuicao = {}
    for obra in dados:
        periodo = obra.get('periodo', 'Desconhecido')  # Usa 'Desconhecido' se a chave não existir
        if periodo in distribuicao:
            distribuicao[periodo] += 1
        else:
            distribuicao[periodo] = 1
    return distribuicao

def titulos_por_periodo(dados):
    titulos_por_periodo = {}
    for obra in dados:
        periodo = obra.get('periodo', 'Desconhecido')  # Usa 'Desconhecido' se a chave não existir
        titulo = obra.get('nome', 'Sem título')  # Usa 'Sem título' se a chave não existir
        if periodo in titulos_por_periodo:
            titulos_por_periodo[periodo].append(titulo)
        else:
            titulos_por_periodo[periodo] = [titulo]
    for periodo in titulos_por_periodo:
        titulos_por_periodo[periodo].sort()
    return titulos_por_periodo

def salvar_compositores_ordenados(compositores, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for compositor in compositores:
            arquivo.write(f"{compositor}\n")

def salvar_distribuicao_por_periodo(distribuicao, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for periodo, quantidade in distribuicao.items():
            arquivo.write(f"{periodo}: {quantidade} obras\n")

def salvar_titulos_por_periodo(titulos_por_periodo, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for periodo, titulos in titulos_por_periodo.items():
            arquivo.write(f"{periodo}:\n")
            for titulo in titulos:
                arquivo.write(f"  - {titulo}\n")
            arquivo.write("\n")  # Linha em branco para separar os períodos

def main():
    dados = ler_csv('obras.csv')
    
    # 1. Lista ordenada alfabeticamente dos compositores musicais
    compositores = lista_compositores(dados)
    salvar_compositores_ordenados(compositores, 'compositores_ordenados.txt')
    
    # 2. Distribuição das obras por período
    distribuicao = distribuicao_por_periodo(dados)
    salvar_distribuicao_por_periodo(distribuicao, 'distribuicao_por_periodo.txt')
    
    # 3. Dicionário com listas alfabéticas de títulos por período
    titulos_por_periodo_dict = titulos_por_periodo(dados)
    salvar_titulos_por_periodo(titulos_por_periodo_dict, 'titulos_por_periodo.txt')

    print("Arquivos gerados com sucesso!")

if __name__ == "__main__":
    main()
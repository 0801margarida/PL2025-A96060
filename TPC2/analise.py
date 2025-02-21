import re

def ler_compositores(entrada_arquivo):
    # Expressão regular para capturar as colunas separadas por ";", considerando espaços extras
    padrao = r'([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([^;]+)\s*'
    
    # Abrir o arquivo de entrada
    with open(entrada_arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    
    # Criar um conjunto para armazenar compositores únicos
    compositores = set()
    
    # Iterar sobre cada linha, ignorando a primeira (cabeçalho)
    for linha in linhas[1:]:
        linha = linha.strip()  # Remover espaços em branco ao redor
        
        # Usar regex para encontrar os campos na linha
        correspondencia = re.match(padrao, linha)
        
        if correspondencia:
            compositor = correspondencia.group(5)  # O compositor está no 5º grupo (índice 5)
            compositores.add(compositor)
        else:
            print(f"Linha ignorada: {linha}")  # Imprimir linhas que não foram correspondidas
    
    # Retornar a lista ordenada de compositores
    return sorted(compositores)

def salvar_compositores_saida(compositores, saida_arquivo):
    # Abrir o arquivo de saída para escrever
    with open(saida_arquivo, 'w', encoding='utf-8') as file:
        for compositor in compositores:
            file.write(f"{compositor}\n")  # Escrever cada compositor em uma linha

def main():
    # Defina os caminhos dos arquivos de entrada e saída
    entrada_arquivo = 'obras.csv'  # Caminho para o arquivo de entrada
    saida_arquivo = 'compositores_ordenados.txt'  # Caminho para o arquivo de saída

    # Ler compositores do arquivo CSV
    compositores = ler_compositores(entrada_arquivo)
    
    # Salvar a lista ordenada de compositores em um arquivo
    salvar_compositores_saida(compositores, saida_arquivo)
    
    print(f"Lista de compositores ordenada salva em {saida_arquivo}")

# Executar o programa
if __name__ == "__main__":
    main()

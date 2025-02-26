import re

# Definir tipos de tokens e os seus padrões regex
especificacao_tokens = [
    ('PALAVRA_CHAVE', r'select|where|LIMIT|a'),  # Palavras-chave
    ('IDENTIFICADOR', r'\?\w+|\w+:\w+'),         # Identificadores (variáveis e nomes prefixados)
    ('LITERAL', r'"[^"]+"@\w+'),                 # Literais (strings com tags de idioma)
    ('NUMERO', r'\d+'),                          # Números
    ('PONTUACAO', r'[{}@.]'),                    # Pontuação
    ('OPERADOR', r'='),                          # Operadores
    ('IGNORAR', r'[ \t\n]'),                     # Ignorar espaços, tabs, novas linhas
    ('ERRO', r'.'),                              # Qualquer outro caractere
]

# Construir o padrão regex manualmente (sem f-string)
regex_patterns = []
for token_type, pattern in especificacao_tokens:
    regex_patterns.append(f'(?P<{token_type}>{pattern})')  # Usamos f-string aqui para criar os grupos nomeados

# Juntar todos os padrões com | (alternância)
token_regex = '|'.join(regex_patterns)

# Compilar o regex
lexer_regex = re.compile(token_regex)

def lexer(string_entrada):
    tokens = []
    for match in lexer_regex.finditer(string_entrada):
        tipo = match.lastgroup
        valor = match.group(tipo)
        if tipo == 'IGNORAR':
            continue
        elif tipo == 'ERRO':
            raise RuntimeError(f'Carácter inesperado: {valor}')
        tokens.append((tipo, valor))
    return tokens

# Exemplo de utilização
consulta = '''
select ?home ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?home.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''

tokens = lexer(consulta)
for token in tokens:
    print(token)
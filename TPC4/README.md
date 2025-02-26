# Analisador Léxico

## Autor(a)

Ana Margarida Pires, A96060

## Resumo

Este projeto consiste na implementação de um **analisador léxico** (lexer) para uma linguagem de consulta semelhante a SPARQL. O lexer é desenvolvido em Python e utiliza expressões regulares (regex) para identificar e tokenizar os diferentes elementos da linguagem, como palavras-chave, identificadores, literais, números e símbolos.

## Descrição

O analisador léxico é a primeira fase de um compilador ou interpretador, responsável por ler o código-fonte e dividi-lo em **tokens**, que são as unidades básicas da linguagem. Neste projeto, o lexer foi desenvolvido para processar consultas no seguinte formato:

```sparql
select ?home ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?home.
    ?w dbo:abstract ?desc
} LIMIT 1000
```
# Funcionalidades do Lexer:

- **Identificação de Tokens:**

    Palavras-chave: select, where, LIMIT, a.

    Identificadores: ?s, ?home, dbo:MusicalArtist, foaf:name, etc.

    Literais: "Chuck Berry"@en.

    Números: 1000.

    Pontuação: {, }, ., @.

    Operadores: =.

- **Uso de Expressões Regulares:**

    O lexer utiliza regex para reconhecer os padrões de cada tipo de token.

    Os padrões são definidos numa lista de tuplos, onde cada tuplo contém o nome do token e o respetivo padrão regex.

- **Output:**

    O lexer produz uma lista de tokens, onde cada token é representado por um tuplo contendo o tipo do token e o seu valor.

## Resultados

**Input:**

```
consulta = '''
select ?home ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?home.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''
```

**Output:**

```
[
    ('PALAVRA_CHAVE', 'select'),
    ('IDENTIFICADOR', '?home'),
    ('IDENTIFICADOR', '?desc'),
    ('PALAVRA_CHAVE', 'where'),
    ('PONTUACAO', '{'),
    ('IDENTIFICADOR', '?s'),
    ('PALAVRA_CHAVE', 'a'),
    ('IDENTIFICADOR', 'dbo:MusicalArtist'),
    ('PONTUACAO', '.'),
    ('IDENTIFICADOR', '?s'),
    ('IDENTIFICADOR', 'foaf:name'),
    ('LITERAL', '"Chuck Berry"@en'),
    ('PONTUACAO', '.'),
    ('IDENTIFICADOR', '?w'),
    ('IDENTIFICADOR', 'dbo:artist'),
    ('IDENTIFICADOR', '?s'),
    ('PONTUACAO', '.'),
    ('IDENTIFICADOR', '?w'),
    ('IDENTIFICADOR', 'foaf:name'),
    ('IDENTIFICADOR', '?home'),
    ('PONTUACAO', '.'),
    ('IDENTIFICADOR', '?w'),
    ('IDENTIFICADOR', 'dbo:abstract'),
    ('IDENTIFICADOR', '?desc'),
    ('PONTUACAO', '}'),
    ('PALAVRA_CHAVE', 'LIMIT'),
    ('NUMERO', '1000')
]
```

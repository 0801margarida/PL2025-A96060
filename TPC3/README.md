# Conversor de MarkDown para HTML

## Autor(a)

Ana Margarida Pires, A96060

## Resumo

Este projeto é um conversor de Markdown para HTML em Python. Ele processa texto Markdown e converte-o para a sua correspondente representação HTML, suportando cabeçalhos, negrito, itálico, listas numeradas e links.

## Descrição

O programa percorre linha à linha do texto Markdown e identifica padrões específicos para conversão:
- **Cabeçalhos**: Converte `#`, `##`, e `###` em `<h1>`, `<h2>`, e `<h3>` respetivamente.
- **Negrito e itálico**: Identifica `**texto**` para `<b>texto</b>` e `*texto*` para `<i>texto</i>`.
- **Listas numeradas**: Converte listas numeradas (`1. item`) em elementos `<ol><li></li></ol>`.
- **Links**: Transforma `[texto](url)` em `<a href='url'>texto</a>`.

O código usa expressões regulares para identificar e substituir elementos Markdown por suas versões HTML correspondentes.

## Resultados

O programa recebe um texto Markdown como entrada e gera um HTML formatado como saída. Exemplo:

**Entrada:**
```
# Exemplo
Este é um **exemplo** e um *teste*.
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
```

**Saída:**
```
<h1>Exemplo</h1>
<p>Este é um <b>exemplo</b> e um <i>teste</i>.</p>
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
<p>Como pode ser consultado em <a href='http://www.uc.pt'>página da UC</a></p>
```

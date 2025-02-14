def somador_on_off(nome_ficheiro):
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            texto = f.read().strip()  # Lê o conteúdo e remove espaços extras
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
        return

    ligado = True  # Começa ligado (on)
    soma = 0
    resultado = []
    
    # Divide o texto em palavras separadas por espaços
    palavras = texto.split()

    for item in palavras:
        item_lower = item.lower()  # Para reconhecer as palavras off e on, com maiusculas e/ou minusculas
        
        if item_lower == "off":
            ligado = False
        elif item_lower == "on":
            ligado = True
        elif item == "=":
            resultado.append(str(soma))  # Guarda o valor atual da soma
            soma = 0  # Dá reset da soma, para a próxima conta
        elif item.isdigit() and ligado:
            soma += int(item)

    print("\n".join(resultado))

# Executar o programa
nome_ficheiro = "entrada.txt"
somador_on_off(nome_ficheiro)

# Somador On/Off

## Autor(a)

Ana Margarida Pires, A96060

## Resumo

Este programa em Python processa um ficheiro de entrada que contém números e os comandos "On" e "Off", e realiza a soma dos números com base no estado atual. Esse estado altera conforme os comandos mencionados vão aparecendo.
Quando o estado está "On", os números são somados. Quando está "Off", os números são ignorados. Sempre que aparece o símbolo "=", o programa exibe a soma acumulada até aquele momento e reinicia a contagem.

## Descrição
Primeiramente, o programa abre e lê o ficheiro de entrada especificado.
Após isso, processa cada elemento do ficheiro, verificando se é um número, um comando `"On"/"Off"` ou o símbolo `"="`. 
O valor da soma acumulada é mantido na variável soma, apenas quando o estado está "On".
Por sua vez, quando um `"="` é encontrado, é exibido o valor da soma acumulada e é reiniciado o valor da variável para 0.
No final, os resultados obtidos são impressos no ecrã.

## Resultados

O programa executa corretamente a soma condicional, garantindo que os números só sejam somados quando o estado estiver "On". Isto pode ser verificado pelos resultados que são apresentados no terminal, assim que se corre o programa.
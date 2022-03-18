## Estrutura Sequencial

## 17 - Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

import os

while 1:
    try:
        ano = int(input("Digite um ano no formato 'aaaa': "))
        break
    except: print("\nEntrada inválida!\n")


bissexto = False
if ano % 4 == 0: bissexto = True
if ano % 100 == 0: bissexto = False
if ano % 400 == 0: bissexto = True


if bissexto:
    print("\n\nO ano " + str(ano) + " foi um ano bissexto!")
else:
    print("\n\nO ano " + str(ano) + " NÃO foi um ano bissexto!")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

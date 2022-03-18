## Exercícios com Funções

## 2 - Faça um programa para imprimir:
##     1
##     1 2
##     1 2 3
##     ......
##     1 2 3 ... n
##
## para um n informado pelo usuário. Use uma função que receba um valor inteiro n e imprima até a n-ésima linha.

import os

def escadinha(n):
    for i in range(1, n + 1):
        linha = ""
        for j in range(1, i + 1):
            linha += str(j) + " "
        print(linha)

while 1:
    try:
        n = int(input("Digite um número inteiro e positivo: "))
        if n < 0: raise Exception()
        break
    except: print("\nEntrada inválida!\n\n")

print("\n\n")
escadinha(n)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

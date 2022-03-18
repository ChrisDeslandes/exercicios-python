## Exercícios com Listas

## 4 - Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
##     Imprima as consoantes.

import os

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while 1:
    palavra = input("Digite uma palavra de 10 letras sem espaço: ").replace(" ", "").upper()
    try:
        if len(palavra) != 10: raise Exception()
        for i in palavra:
            if not i in alfabeto: raise Exception()
        break
    except: print("\nEntrada inválida!\n\n")

consoantes = []
for i in palavra:
    if not i in "AEIOU": consoantes.append(i)

print("\n\nNa palavra " + palavra + " existem " + str(len(consoantes)) + " consoantes. São elas:")
print()
print(*consoantes)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

## Estrutura Sequencial

## 4 - Faça um programa que peça 4 notas bimestrais e mostre a média.

import os

while 1:
    try:
        notas = input("Digite as 4 notas bimestrais separadas por espaço: ").replace(",", ".").split()
        for i in range(len(notas)): notas[i] = float(notas[i])
        if len(notas) != 4: raise Exception()
        break
    except: print("\nEntrada inválida!\n")

soma = 0
for i in notas: soma += i

media = round(soma/len(notas), 2)

print("\n\nA média das notas bimestrais é: " + str(media))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

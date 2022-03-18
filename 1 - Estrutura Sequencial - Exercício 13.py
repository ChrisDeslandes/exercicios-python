## Estrutura Sequencial

## 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
##      a) Para homens: (72.7 * h) - 58
##      b) Para mulheres: (62.1 * h) - 44.7

import os

while 1:
    try:
        h = float(input("Digite sua altura: ").replace(",", "."))
        break
    except:
        print("\nEntrada inválida!\n")

pesoHomens = round(72.7 * h - 58, 2)
pesoMulheres = round(62.1 * h - 44.7, 2)

print("\n\nPeso ideal para esta altura:")
print("\tHomens: " + str(pesoHomens))
print("\tMulheres: " + str(pesoMulheres))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

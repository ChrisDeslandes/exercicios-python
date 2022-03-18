## Estrutura Sequencial

## 6 - Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

import os
import math

while 1:
    try:
        raio = float(input("Digite um valor para o raio do círculo: ").replace(",", "."))
        break
    except:
        print("\nEntrada inválida!\n")

area = round(raio**2 * math.pi, 2)

print("\n\nA área do círculo de raio " + str(raio) + " é: " + str(area))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

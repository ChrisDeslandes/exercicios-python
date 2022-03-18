## Estrutura de Repetição

## 15 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,.... Faça um programa capaz de gerar a série até o n-ésimo termo.

import os

while 1:
    try:
        n = int(input("Digite um número inteiro, positivo e não-nulo: "))
        if n < 1: raise Exception()
        break
    except: print("\nEntrada inválida!\n\n")

sequencia = []

for i in range(0, n):
    if i < 2: sequencia.append("1")
    else: sequencia.append(str(int(sequencia[i - 2]) + int(sequencia[i - 1])))

print("\n\nA sequência de Fibonacci até o " + str(n) + "º termo é:")
print(", ".join(sequencia))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

## Exercícios com Listas

## 10 - Faça um programa que leia dois vetores com 10 elementos cada.
##      Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

import os

while 1:
    vetor1 = input("Digite 10 elementos separados por espaço: ").split()
    if len(vetor1) != 10: print("\nEntrada inválida!\n\n")
    else: break
while 1:
    vetor2 = input("Digite 10 elementos separados por espaço: ").split()
    if len(vetor2) != 10: print("\nEntrada inválida!\n\n")
    else: break

vetorFinal = []
for i in range(len(vetor1)):
    vetorFinal.append(vetor1[i])
    vetorFinal.append(vetor2[i])

print("\n\nVetor 1: ")
print(vetor1)
print("\nVetor 2: ")
print(vetor2)
print("\n\nVetor final: ")
print(vetorFinal)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

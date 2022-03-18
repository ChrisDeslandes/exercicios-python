## Exercícios com Listas

## 5 - Faça um programa que leia 20 números inteiros e armazene-os num vetor.
##     Armazene os números pares no vetor PAR e os números ímpares no vetor IMPAR.
##     Imprima os três vetores.

import os

while 1:
    nums = input("Digite 20 números inteiros e positivos separados por espaço: ").split()
    try:
        if len(nums) != 20: raise Exception()
        for i in range(len(nums)): nums[i] = int(nums[i])
        break
    except: print("\nEntrada inválida!\n\n")

pares = []
impares = []
for i in nums:
    if i % 2 == 0: pares.append(i)
    else: impares.append(i)

print("\n\nVetor de entrada: ")
print(nums)
print("\nVetor PAR: ")
print(pares)
print("\n\nVetor IMPAR: ")
print(impares)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

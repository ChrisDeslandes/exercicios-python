## Estrutura Sequencial

## 7 - Faça um programa que leia três números e mostre o maior e o menor deles.

import os

while 1:
    try:
        nums = input("Digite três números separados por espaço: ").replace(",", ".").split()
        if len(nums) != 3: raise Exception()
        for i in range(len(nums)): nums[i] = float(nums[i])
        break
    except: print("\nEntrada inválida!\n")

nums.sort()

print("\n\nO menor número é: " + str(nums[0]))
print("\nO maior número é: " + str(nums[len(nums) - 1]))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

## Exercícios com Funções

## 9 - Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

import os

def reverso(n):
    return n[::-1]

while 1:
    try:
        n = int(input("Digite um número inteiro e positivo para calcular o seu reverso: "))
        if n < 0: raise Exception()
        break
    except: print("\nEntrada inválida!\n\n")

n = str(n)
print("\n\nO reverso do número " + n + " é " + reverso(n) + ".")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

## Exercícios com Strings

## 7 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
##     a) quantos espaços em branco existem na frase.
##     b) quantas vezes aparecem as vogais a, e, i, o, u.

import os

while 1:
    frase = input("Digite uma frase sem acentos: ").upper()
    if len(frase) > 0: break

espacos = 0
aeiou = [0, 0, 0, 0, 0]

for i in frase:
    if i == " ": espacos += 1
    elif i == "A": aeiou[0] += 1
    elif i == "E": aeiou[1] += 1
    elif i == "I": aeiou[2] += 1
    elif i == "O": aeiou[3] += 1
    elif i == "U": aeiou[4] += 1

print("\n\nNúmero de espaços em branco na frase: " + str(espacos))

total = 0
for i, letra in enumerate("AEIOU"):
    print("\nNúmero de vezes em que aparece a letra " + letra + ": " + str(aeiou[i]))
    total += aeiou[i]

print("\nNúmero total de vogais na frase: " + str(total))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

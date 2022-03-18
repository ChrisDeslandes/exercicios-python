## Estrutura de Repetição

## 12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve informar de qual número ele deseja ver a tabuada.

import os

while 1:
    try:
        n = int(input("Digite um valor inteiro de 1 a 10: "))
        if not (1 <= n <= 10): raise Exception()
        break
    except: print("\n\nEntrada inválida!\n\n")

print("\n\nTabuada de " + str(n) + ":\n")

for i in range(1, 11): print(str(n) + " * " + str(i) + " = " + str(n * i))

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

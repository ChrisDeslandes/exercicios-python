## Exercícios com Strings

## 4 e 5 - Nome na vertical em escada e em escada invertida.
##         F
##         FU
##         FUL
##         FULA
##         FULAN
##         FULANO
##         FULAN
##         FULA
##         FUL
##         FU
##         F

import os
while 1:
    frase = input("Digite uma palavra ou frase: ").upper()
    if len(frase) > 0: break

for i in range(len(frase)):
    print(frase[:i])

for i in range(len(frase), 0, -1):
    print(frase[:i])

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

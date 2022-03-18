## Exercícios com Strings

## 9 - Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
##     e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

import os

def calculaDigVerif(cpf):
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    pDig = 11 - (soma % 11)
    if pDig == 10 or pDig == 11:
        pDig = 0
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (11 - i)
    soma += pDig * 2
    sDig = 11 - (soma % 11)
    if sDig == 10 or sDig == 11:
        sDig = 0
    return str(pDig) + str(sDig)


cpf = input("Digite um CPF no formato 'xxx.xxx.xxx-xx': ").strip()

cpfValido = True

if len(cpf) != 14: cpfValido = False
elif cpf[3] != "." or cpf[7] != "." or cpf[11] != "-": cpfValido = False
else:
    cpfLimpo = cpf.replace(".", "").replace("-", "")
    for i in cpfLimpo:
        if not i in "0123456789":
            cpfValido = False
            break
    if calculaDigVerif(cpfLimpo[:9]) != cpfLimpo[9:11]: cpfValido = False

if cpfValido: print("\n\nO CPF informado é válido!")
else: print("\n\nO CPF informado é inválido!")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

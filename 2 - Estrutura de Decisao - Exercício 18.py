## Estrutura Sequencial

## 18 - Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

import os
import datetime

formatoValido = True

data = input("Digite uma data no formato 'dd/mm/aaaa': ").strip()

if len(data) != 10: formatoValido = False
elif data[2] != "/" or data[5] != "/": formatoValido = False
try:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    d = datetime.datetime(ano, mes, dia)
except: formatoValido = False

if formatoValido: print("\n\nA data fornecida é uma data válida!")
else: print("\n\nA data fornecida NÃO é uma data válida!")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

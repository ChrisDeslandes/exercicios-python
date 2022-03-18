## Exercícios com Funções

## 11 - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
##      Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

import os
import datetime

def transformaData(data):
    if not verificaFormato(data): return None
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:10]
    mesPorExtenso = ""
    if mes == "01": mesPorExtenso = "janeiro"
    elif mes == "02": mesPorExtenso = "fevereiro"
    elif mes == "03": mesPorExtenso = "março"
    elif mes == "04": mesPorExtenso = "abril"
    elif mes == "05": mesPorExtenso = "maio"
    elif mes == "06": mesPorExtenso = "junho"
    elif mes == "07": mesPorExtenso = "julho"
    elif mes == "08": mesPorExtenso = "agosto"
    elif mes == "09": mesPorExtenso = "setembro"
    elif mes == "10": mesPorExtenso = "outubro"
    elif mes == "11": mesPorExtenso = "novembro"
    else: mesPorExtenso = "dezembro"
    return dia + " de " + mesPorExtenso + " de " + ano

def verificaFormato(data):
    formatoValido = True
    if len(data) != 10: formatoValido = False
    elif data[2] != "/" or data[5] != "/": formatoValido = False
    try:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])
        d = datetime.datetime(ano, mes, dia)
    except: formatoValido = False
    return formatoValido


data = input("Digite uma data no formato 'dd/mm/aaaa': ").strip()


resultado = transformaData(data)
if resultado:
    print("\n\n" + data + " ==> " + transformaData(data))
else: print("\n\nFormato de data inválido!")


print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")

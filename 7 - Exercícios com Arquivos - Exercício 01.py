## Exercícios com Arquivos

## 1 - Faça um programa que leia um arquivo texto contendo uma lista de endereços IP
##     e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

entrada = "./ips.txt"
saida = "./Resultados - IPs.txt"

fileEntrada = open(entrada, "r")

validos = []
invalidos = []

for linha in fileEntrada:
    valido = True
    campos = linha.split(".")
    if len(campos) != 4:
        valido = False
    else:
        for campo in campos:
            try:
                campo = int(campo)
                if not 0 <= campo <= 255: raise Exception()
            except: valido = False
    if valido: validos.append(linha)
    else: invalidos.append(linha)

fileEntrada.close()

## -----------------------------------------------------

texto = "[Endereços válidos:]\n\n"

for valido in validos:
    texto += valido

texto += "\n\n[Endereços inválidos:]\n\n"

for invalido in invalidos:
    texto += invalido

## -----------------------------------------------------

fileSaida = open(saida, "w")

fileSaida.write(texto)

fileSaida.close()

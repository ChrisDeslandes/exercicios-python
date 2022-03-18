## Exercícios com Arquivos

## 2 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
##     Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
##     e identificar os usuários com maior espaço ocupado.
##     Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

##     alexandre       456123789
##     anderson        1245698456
##     antonio         123456456
##     carlos          91257581
##     cesar           987458
##     rosemary        789456125

##     Neste arquivo, o nome do usuário possui 15 caracteres.
##     A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

##     ACME Inc.   Uso do espaço em disco pelos usuários
##     -------------------------------------------------
##     Nr.  Usuário        Espaço utilizado     % do uso

##     1    alexandre             434,99 MB       16,85%
##     2    anderson             1187,99 MB       46,02%
##     3    antonio               117,73 MB        4,56%
##     4    carlos                 87,03 MB        3,37%
##     5    cesar                   0,94 MB        0,04%
##     6    rosemary              752,88 MB       29,16%

##     Espaço total de memória ocupado: 2581,57 MB
##     Espaço médio ocupado: 430,26 MB

##     O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
##     de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
##     deverá ser feita através de uma função separada, que será chamada pelo programa principal.
##     O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

def conversaoBytesParaMB(nBytes):
    return str(round(nBytes / (1024**2), 2)).replace(".", ",") + " MB"

def percentual(parcial, total):
    return str(round(100 * parcial / total, 2)).replace(".", ",") + "%"

entrada = "./usuarios.txt"
saida = "./relatório.txt"

usuarios = []
memorias = []
fileEntrada = open(entrada, "r")

totalMemoria = 0
for linha in fileEntrada:
    usuarios.append(linha[:15])
    memoria = int(linha[15:])
    totalMemoria += memoria
    memorias.append(memoria)

fileEntrada.close()

## -----------------------------------------------------

texto = "ACME Inc.   Uso do espaço em disco pelos usuários\n"
texto += "-------------------------------------------------\n"
texto += "Nr.  Usuário        Espaço utilizado     % do uso\n\n"

for i in range(len(usuarios)):
    texto += str(i) + (" " * (5 - len(str(i)))) + usuarios[i]
    memoriaMB = conversaoBytesParaMB(memorias[i])
    texto += (" " * (16 - len(memoriaMB))) + memoriaMB
    percentualMemoria = percentual(memorias[i], totalMemoria)
    texto += (" " * (13 - len(percentualMemoria))) + percentualMemoria + "\n"

texto += "\nEspaço total de memória ocupado: " + conversaoBytesParaMB(totalMemoria) + "\n"
texto += "Espaço médio ocupado: " + conversaoBytesParaMB(totalMemoria / len(usuarios))

## -----------------------------------------------------

fileSaida = open(saida, "w")

fileSaida.write(texto)

fileSaida.close()

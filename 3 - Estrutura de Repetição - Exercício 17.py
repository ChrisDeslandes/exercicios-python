## Estrutura de Repetição

## 17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120

def fat(n): return 1 if n < 2 else fat(n - 1) * n

while 1:
    try:
        n = int(input("Digite um número inteiro e positivo para calcular o seu fatorial: "))
        if n < 0: raise Exception()
    except:
        print("\nEntrada inválida!\n\n")
        continue

    string = str(n) + "! = "

    for i in range(n, 1, -1): string += str(i) + " * "
    string += "1 = " + str(fat(n))

    print("\n\n" + string)
    
    print("\n")
    resp = input("Você deseja fazer outra operação? (s para sim) ").lower()
    if resp in ["s", "sim"]: print("\n\n")
    else: break

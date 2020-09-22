"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair

Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"
"""
opcao = ''

while opcao != "S":
    opcao = input("""
    A) Soma
    B) Média
    C) Taboada
    S) Sair
    Selecione a opção: """).upper()

    if opcao == 'A':
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        print(f"A soma é: {n1+n2:.2f}\n")
    elif opcao == 'B':
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        n3 = float(input("Insira o terceiro número: "))
        n4 = float(input("Insira o quarto número: "))
        print(f"A média é: {(n1+n2+n3+n4)/4:.2f}")
    elif opcao == 'C':
        n1 = int(input("Insira um número: "))
        for i in range(11):
            print(f"{n1} X {i}= {n1*i}")
    elif opcao == 'S':
        print("Tchau! Até a proxima :)")
    else:
        print("Opção Inválida")


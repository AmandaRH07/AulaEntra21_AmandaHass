"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um menu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""
opcao = ''

while opcao !='S':
    n1 = float(input("Insira o primeiro número: "))
    n2 = float(input("Insira o segundo número: "))
    opcao = input("""
    1) Soma
    2) Subtração
    3) Multiplicação
    S) Para sair!
    Selecione a opção:  """).upper()
    
    if opcao == '1':
        print(f'A soma é: {n1+n2:.2f}\n')
    elif opcao == '2': 
        print(f'A subtração é: {n1-n2:.2f}\n')
    elif opcao == '3': 
        print(f'A multiplicação é: {n1+n2:.2f} \n')
    elif opcao == "S":
        print("Você escolheu sair\n")
    else:
        print("Operação inválida\n")
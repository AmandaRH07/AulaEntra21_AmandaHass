
"""Execicios 03

Escreva um programa que contenha um menu com 4 opções:
A) soma
B) média
C) divisão
D) Sair

As opções podem ser escolhidas com as letras maiusculas ou minusculas.

Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"
"""

print("""
A) Soma
B) Média
C) Divisão
D) Sair
""")
letra = input("Insira a letra com a operação desejada: ")

if letra == 'A' or letra == 'a':
    n1= int(input("Insira o primeiro número: "))
    n2= int(input("Insira o segundo número: "))
    print(f"A soma de {n1} e {n2} é: ", n1+n2)
elif letra == 'B' or letra == 'b':
    n1= int(input("Insira o primeiro número: "))
    n2= int(input("Insira o segundo número: "))
    n3= int(input("Insira o terceiro número: "))
    n4= int(input("Insira o quarto número: "))
    print(f"A media de {n1}, {n2}, {n3} e {n4} é: ", (n1+n2+n3+n4)/4.0)
elif letra == 'C' or letra == 'c':
    n1= int(input("Insira o primeiro número: "))
    n2= int(input("Insira o segundo número: "))
    if n2 == 0:
        print("Erro! Não pode dividir por ZERO!")
    else:
        print(f"A divisão de {n1} e {n2} é: ", n1/n2)
else:
    print("Muito Obrigada e volte sempre!")
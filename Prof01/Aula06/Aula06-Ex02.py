"""Execicios 02

Escreva um programa que receba 4 notas e calcule a média.
Mostre a seguinte mensagem conforme a media final.

Media Final
de 0 a 5 - Reprovado
de 5 a 6.5 - Recuperação
de 6.5 a 9 - Aprovado
Acima de 9 - Aprovado com louvor
"""

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4.0

if media >= 0 and media <= 5:
    print("Reprovado! Média: ", media)
elif media > 5 and media <= 6.5:
    print("Recuperação! Média: ", media)
elif media > 6.5 and media <= 9:
    print("Aprovado! Média: ", media)
else: 
    print("Aprovado com Louvor! Média: ", media)
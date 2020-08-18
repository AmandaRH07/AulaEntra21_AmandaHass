# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 

n1 = float(input("Insira o n1: "))
n2 = float(input("Insira o n2: "))
n3 = float(input("Insira o n3: "))
n4 = float(input("Insira o n4: "))

media = (n1+n2+n3+n4)/4.0

if media == 10.0:
    print("Aprovado com louvor com média: ", media)
elif media >= 7.0:
    print("Aprovado com média: ", media)
else:
    print("Reprovado com média: ", media)

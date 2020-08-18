# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

num = int(input("Insira o número do dia da semana: "))

if num == 1:
    print("Segunda-Feira")
elif num == 2:
    print("Terça-Feira")
elif num == 3:
    print("Quarta-Feira")
elif num == 4:
    print("Quinta-Feira")
elif num == 5:
    print("Sexta-Feira")
elif num == 6:
    print("Sábado")
elif num == 7:
    print("Domingo")
else:
    print("Dia inválido")
# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

n1 = int(input("Insira o n1: "))
n2 = int(input("Insira o n2: "))
n3 = int(input("Insira o n3: "))

if n1 < n2 and n1 < n3:
    print("Menor: ", n1)
elif n2 < n1 and n2< n3:
    print("Menor: ", n2)
else:
    print("Menor: ", n3)







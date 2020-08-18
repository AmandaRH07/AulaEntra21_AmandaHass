# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
# 
n1 = int(input("Insira o n1: "))
n2 = int(input("Insira o n2: "))
n3 = int(input("Insira o n3: "))

if n1 < n2 and n1 < n3:
    primeiro = n1
elif n2 < n1 and n2 < n3:
    primeiro = n2
else:
    primeiro = n3

if n1 < n2 and n1 > n3:
    segundo = n1
elif n2 > n1 and n2 < n3:
    segundo = n2
else: # n3 > n1 and n3 < n2
    segundo = n3

if n1 > n2 and n1 > n3:
    terceiro = n1
elif n2 > n1 and n2 > n3:
    terceiro = n2
else:
    terceiro = n3

print((primeiro, segundo, terceiro))
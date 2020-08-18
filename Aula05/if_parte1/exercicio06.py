# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

n1 = int(input("Insira o n1: "))
n2 = int(input("Insira o n2: "))

if n1 < n2:
    print((n1, n2))
else: 
    print((n2, n1))
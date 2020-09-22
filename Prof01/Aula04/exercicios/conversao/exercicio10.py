# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

produto1 = input("Insira o produto 1: ")
quantidade1 = int(input("Insira a quantidade do produto 1: "))
preco1 = float(input("Insira o preco do produto 1: "))

produto2 = input("Insira o produto 2: ")
quantidade2 = int(input("Insira a quantidade do produto 2: "))
preco2 = float(input("Insira o preco do produto 2: "))

print(produto1, ", valor total do produto 1 = ", quantidade1*preco1)

print(produto2, ", valor total do produto 2 = ", quantidade2*preco2)
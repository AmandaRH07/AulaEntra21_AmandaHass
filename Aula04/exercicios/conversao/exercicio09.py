
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

nome = input("Insira seu nome: ")
quantidade = int(input("Insira a quantidade: "))
preco = float(input("Insira o preco: "))

print(nome, ", valor total = ", quantidade*preco)
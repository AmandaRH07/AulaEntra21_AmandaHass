# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

num = int(input("Insira o número: "))

if num == 0:
    print("Nulo!")
elif num > 0:
    print("Positivo!")
else: 
    print("Negativo!")

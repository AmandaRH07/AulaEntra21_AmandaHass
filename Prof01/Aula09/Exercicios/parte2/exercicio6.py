
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""

nomes = []
for i in range(11):
    nomes.append(input("Nome: "))

for i in nomes:
    print(i)

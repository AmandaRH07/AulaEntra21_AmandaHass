"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""
nome = []
idade = []
email = []
for i in range(10):
    nome.append(input("Nome: "))
    idade.append(input("Idade: "))
    email.append(input("Email: "))

print("Nomes: ", nome)
print("Idades: ", idade)
print("Emails: ", email)
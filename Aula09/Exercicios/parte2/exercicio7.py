"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""
idades = []
for i in range(4):
    idades.append(int(input("Insira a idade: ")))

for i in idades:
    if i >= 18:
        print(f"{i}, Ingreços da rave liberados!")
    elif i >=16 and i < 18:
        print(f"{i}, Ingreços do cinema liberados!")
    elif i >=13 and i < 16:
        print(f"{i}, Ingreços do fliperama liberados!")
    else: 
        print(f"{i}, Ingreços da piscina de bolinhas liberados!")
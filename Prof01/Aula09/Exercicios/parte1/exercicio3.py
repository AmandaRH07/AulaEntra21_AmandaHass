
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""

notas = []
for n in range(11):
    nota = float(input("Nota: "))
    notas.append(nota)

media = sum(notas)/len(notas)

if media >= 7.0 and media <=10:
    print(f"Aprovado! Média: {media:.2f}")
elif media >= 5.5 and media <7:
    print(f"Recuperação! Média: {media:.2f}")
else:
    print(f"Reprovado! Média: {media:.2f}")

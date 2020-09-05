"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para maiores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""

lista_nome = []
idade = True
nome = True

while idade:
    nome = input("Nome: ")
    lista_nome.append(nome)
    idade = input("Idade: ")
    if nome == "":
        lista_nome.remove(nome)
        while nome == "":
            nome = (input("Nome em branco. Tente novamente: "))
            lista_nome.append(nome)
    if idade == '':
        print("Obrigada pela preferêcia")
        nomes = len(lista_nome)
        for i in range(nomes):
            print(f"{lista_nome[i]}")
    elif idade >= '18':
        print("Entrada permitida.")
    else:
        print("Entrada proibida.")
          
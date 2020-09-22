"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----

Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""

lista_nome = []
lista_idade = []
lista_sexo= []
lista_telefone = []

opcao = ''
while  opcao != 'S':
    opcao = input("""
    A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados:
    C) Ver cadastro pelo nome:
    D) Apagar um cadastro pelo nome:
    S) Sair
    Selecione a opção: """).upper()

    if opcao == 'A':
        lista_nome.append(input("Nome: "))
        lista_idade.append(input("Idade: "))
        lista_sexo.append(input("Sexo: "))
        lista_telefone.append(input("Telefone: "))
    elif opcao == 'B':
        for i in range(len(lista_nome)):
            print(f"{lista_nome[i]}")
    elif opcao == 'C':
        nome = input("Insira um nome para ter acesso ao seu cadastro: ")
        for i in range(len(lista_nome)):
            while nome != lista_nome[i]:
                nome = input("Nome inválido. Por favor, tente novamente:   ")
            if nome == lista_nome[i]:
                print(f"""
                Nome: {lista_nome[i]}
                Idade: {lista_idade[i]}
                Sexo: {lista_sexo[i]}
                Telefone: {lista_telefone[i]}
                """)
    elif opcao == 'D':
        nome = input("Insira um nome para apagar seu cadastro: ")
        for i in range(len(lista_nome)):
            while nome != lista_nome[i]:
                nome = input("Nome inválido. Por favor, tente novamente:   ")
            if nome == lista_nome[i]:
                lista_nome.remove(lista_nome[i])
    else:
        print("Você escolheu sair. Até a próxima!")

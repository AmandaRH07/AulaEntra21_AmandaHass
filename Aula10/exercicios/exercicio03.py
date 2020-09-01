"""Exercício 03

3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

3.2) Depois mostre os dados dos 5 clientes.

3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""

lista_id = []
lista_nome = []
lista_sexo = []
lista_idade = []

print("---------Cadastro do Cliente---------")
for i in range(1,3):
    lista_id.append(i)
    lista_nome.append(input("Digite o nome: "))
    lista_sexo.append(input("Digite o sexo (M ou F): "))
    lista_idade.append(int(input("Digite a idade: ")))
    print()

tamanho = len(lista_id)
for i in range(tamanho):
     print(f"""
    Id: {lista_id[i]}
    Nome: {lista_nome[i]}
    Sexo: {lista_sexo[i]}
    Idade: {lista_idade[i]}
    """)

print("-----------Escolha de um ID-----------")

escolha_Id = int(input("Insira o ID para imprimir a informação dos clientes: "))

for i in range(tamanho):
    if escolha_Id == lista_id[i]:
        print(f"""
        Id: {lista_id[i]}
        Nome: {lista_nome[i]}
        Sexo: {lista_sexo[i]}
        Idade: {lista_idade[i]}
        """)

        if lista_idade[i] >= 18:
            print("Entrada liberada")
        else: 
            print("Entrada proibida")

        if lista_sexo[i] == 'f' or lista_sexo[i] == 'f':
            print("Desconto de 50%")
        else:
            print("Desconto de 5%")

print("-------------------------------")
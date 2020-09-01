"""Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto 
por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

id: 3
Nome: Pedro

ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.

Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""
lista_id = []
lista_nome = []
lista_idade = []
for i in range(4):
    lista_id.append(i+1)
    lista_nome.append(input("Digite o nome: "))
    lista_idade.append(int(input("Digite a idade: ")))
    print()

tamanho = len(lista_nome)
for i in range(tamanho):
    print(f"""
    Id: {lista_id[i]}
    Nome: {lista_nome[i]}
    Idade: {lista_idade[i]}
    """)

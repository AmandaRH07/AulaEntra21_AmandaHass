"""
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:

***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
"""

lista_nome = []
lista_sexo = []
lista_telefone = []

for i in range(5): 
    lista_nome.append(input(f'Digite o nome: '))
    lista_sexo.append(input(f'Digite o sexo: '))
    lista_telefone.append(int(input(f'Digite o telefone: ')))
    print() 

tamanho = len(lista_nome)
for i in range(tamanho):
    print(f""" 
    ***********************************
    Relatório de clientes cadastrados 
    ***********************************
    Nome: {lista_nome[i]}
    Sexo: {lista_sexo[i]}
    Telefone: {lista_telefone[i]} 
    *********************************** 
    """)  

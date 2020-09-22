# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome = input("Insira o nome: ")
idade = int(input("Insira a idade: "))
endereco = input("Insira o endereco: ")
email = input("Insira o email: ")
telefone = input("Insira o telefone: ")

print ("""
1. Dados
2. Endereço
3. Idade
""")

opcao = int(input("Escolha a operação: "))

if opcao == 1:
    print(nome, ",", idade)
elif opcao == 2:
      print(nome, ",", endereco)
else:
      print(nome, ",", email, ",", telefone)


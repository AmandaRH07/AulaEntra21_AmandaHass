#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.


dinheiro_emprestado = float(input("Insira o valor emprestado: "))
taxa_juros = float(input("Insira a taxa de juros: "))
tempo_Emprestimo = int(input("Insira o tempo em meses da duração do empréstimo: "))

valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_Emprestimo

print("O valor a ser recebido é {:.2f}".format(valor_receber))
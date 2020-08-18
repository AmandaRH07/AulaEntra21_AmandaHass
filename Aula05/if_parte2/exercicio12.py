# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

n1 = int(input("Insira o n1: "))
n2 = int(input("Insira o n2: "))

print ("""
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Expoente
""")

operacao = int(input("Escolha a operação: "))

if operacao == 1:
    resultado = n1+n2
elif operacao == 2:
    resultado = n1-n2
elif operacao == 3:
    resultado = n1*n2
elif operacao == 4:
    resultado = n1/n2
else:
    resultado = n1**n2
print(resultado)






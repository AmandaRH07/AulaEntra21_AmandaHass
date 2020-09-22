# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 

litros = int(input("Insira quantos litros: "))

print ("""
1. Álcool
2. Diessel
3. Gasolina
""")

tipo = int(input("Insira o tipo de combustível: "))

if tipo == 1:
    if litros > 20:
        print("Álcool,", litros, ", 20%")
elif tipo == 2:
    if litros < 10:
        print("Diessel,", litros, ", 1.5%")
    else: 
        print("Diessel,", litros, ", 5%")
else:
    if litros < 10:
        print("Gasolina,", litros, ", 5%")
    else: 
        print("Gasolina,", litros, ", 10%")
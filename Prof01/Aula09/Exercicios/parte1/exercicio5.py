"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""

qtdVendas = int(input("Insira a quantidade de vendas do dia: "))

valorTotalLista = []
for i in range(qtdVendas):
    valorTotalLista.append(int(input(f"Valor venda {i+1}: ")))

valorTotal= sum(valorTotalLista)
print(f"""Valor Total: {valorTotal:.2f}
Media: {valorTotal/len(valorTotalLista):.2f}""")
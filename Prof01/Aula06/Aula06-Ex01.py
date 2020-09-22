# -*- coding: utf-8 -*-
"""
Execicios 01

Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

Venda Total
de R$ 0.00 a R$ 30000.00 - 0%
de R$ 30000.01 a R$ 50000.00 - 1.5%
de R$ 50000.01 a R$ 100000.00 - 2.5%
Acima de R$ 100000.00 - 3.5%
"""

valor_venda= float(input("Insira o valor da venda: "))

if valor_venda >= 0.0 and valor_venda <= 30000.00:
    comissao = valor_venda* 0.00
    print("O valor da comissao é de: R$", comissao)
elif valor_venda > 30000.00 and valor_venda <= 50000.00:
    comissao = valor_venda* 0.015
    print("O valor da comissao é de: R$ {:.2f}".format(comissao))
elif valor_venda > 50000.00 and valor_venda <= 100000.00:
    comissao = valor_venda* 0.025
    print("O valor da comissao é de: R$ {:.2f}".format(comissao))
else:
    comissao = valor_venda* 0.035
    print("O valor da comissao é de: R${:.2f}" .format(comissao))


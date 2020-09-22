# 3) Estas 3 listas:
# 
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%
# 

vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]

media_armando = sum(vendas_armando)/ len(vendas_armando)
media_eduardo = sum(vendas_eduardo)/ len(vendas_eduardo)
media_paulo = sum(vendas_paulo)/ len(vendas_paulo)

print(f"""ARMANDO:
Media: {media_armando:.2f} 
Valor total de vendas: {sum(vendas_armando)} 
Quantidade de vendas: {len(vendas_armando)} 
""")
print(f"""EDUARDO:
Media: {media_eduardo:.2f}
Valor total de vendas: {sum(vendas_eduardo)}
Quantidade de vendas: {len(vendas_eduardo)}
""")
print(f"""PAULO:
Media: {media_paulo:.2f}
Valor total de vendas: {sum(vendas_paulo)}
Quantidade de vendas: {len(vendas_paulo)}
""")

comissao_armando = sum(vendas_armando)
comissao_eduardo = sum(vendas_eduardo)
comissao_paulo = sum(vendas_paulo)

if comissao_armando > 0.00 and comissao_armando <= 1000.00:
    comissao_armando *= 0.01
elif comissao_armando > 1000.00 and comissao_armando <= 2500.00:
    comissao_armando *= 0.015
elif comissao_armando > 2500.00 and comissao_armando <= 5000.00:
    comissao_armando *= 0.02
else:
    comissao_armando *= 0.03
print(f"A comissão de Armando é de: R${comissao_armando:.2f}")

if comissao_eduardo > 0.00 and comissao_eduardo <= 1000.00:
    comissao_eduardo *= 0.01
elif comissao_eduardo > 1000.00 and comissao_eduardo <= 2500.00:
    comissao_eduardo *= 0.015
elif comissao_eduardo > 2500.00 and comissao_eduardo <= 5000.00:
    comissao_eduardo *= 0.02
else:
   comissao_eduardo *= 0.03
print(f"A comissão de Eduardo é de: R${comissao_eduardo:.2f}")

if comissao_paulo > 0.00 and comissao_paulo <= 1000.00:
    comissao_paulo *= 0.01
elif comissao_paulo > 1000.00 and comissao_paulo <= 2500.00:
    comissao_paulo *= 0.015
elif comissao_paulo > 2500.00 and comissao_paulo <= 5000.00:
    comissao_paulo *= 0.02
else:
    comissao_paulo *= 0.03
print(f"A comissão de Armando é de: R${comissao_paulo:.2f}")

nome = input()
salario_Fixo = float(input())
vendas = float(input())

total = salario_Fixo + (vendas * 0.15)

print(f'TOTAL = R$ {total:.2f}')
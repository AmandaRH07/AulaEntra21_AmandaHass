salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print("Isento")
elif salario > 2000.00 and salario <= 3000.00:
    imposto = (salario-2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario > 3000.00 and salario <= 4500.00:
    imposto = 1000 * 0.08 + (salario-3000) * 0.18
    print(f"R$ {imposto:.2f}")
elif salario > 4500.00:
    imposto = 1000 * 0.08 + 1500 * 0.18 + (salario-4500) * 0.28
    # 1000 a mais do segundo e 1500 a mais do terceiro
    print(f"R$ {imposto:.2f}")
else:
    pass
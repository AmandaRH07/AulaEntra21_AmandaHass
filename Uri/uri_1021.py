valor = float(input())

notas100 = int(valor / 100)
valor = valor - notas100 * 100
notas50 = int(valor / 50)
valor = valor - notas50 * 50
notas20 = int(valor / 20)
valor = valor - notas20 * 20
notas10 = int(valor / 10)
valor = valor - notas10 * 10
notas5 = int(valor / 5)
valor = valor - notas5 * 5
notas2 = int(valor / 2)
valor = valor - notas2 * 2

moedas1 = int(valor / 1)
valor = valor - moedas1 * 1
moedas050 = int(valor / 0.50)
valor = valor - moedas050 * 0.50
moedas025 = int(valor / 0.25)
valor = valor - moedas025 * 0.25
moedas010 = int(valor / 0.10)
valor = valor - moedas010 * 0.10
moedas005 = int(valor / 0.05)
valor = valor - moedas005 * 0.05
moedas001 = int(valor / 0.01)
valor = valor - moedas001 * 0.01

print("NOTAS")
print(f"{notas100} nota(s) de R$ 100.00")
print(f"{notas50} nota(s) de R$ 50.00")
print(f"{notas20} nota(s) de R$ 20.00")
print(f"{notas10} nota(s) de R$ 10.00")
print(f"{notas5} nota(s) de R$ 5.00")
print(f"{notas2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moedas1} moeda(s) de R$ 1.00")
print(f"{moedas050} moeda(s) de R$ 0.50")
print(f"{moedas025} moeda(s) de R$ 0.25")
print(f"{moedas010} moeda(s) de R$ 0.10")
print(f"{moedas005} moeda(s) de R$ 0.05")
print(f"{moedas001} moeda(s) de R$ 0.01")
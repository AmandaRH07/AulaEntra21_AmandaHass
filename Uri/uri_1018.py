entrada_Inicial = int(input())

cedulas_Restantes = entrada_Inicial

notas100 = int(cedulas_Restantes / 100)
cedulas_Restantes = cedulas_Restantes - notas100 * 100
notas50 = int(cedulas_Restantes / 50)
cedulas_Restantes = cedulas_Restantes - notas50 * 50
notas20 = int(cedulas_Restantes / 20)
cedulas_Restantes = cedulas_Restantes - notas20 * 20
notas10 = int(cedulas_Restantes / 10)
cedulas_Restantes = cedulas_Restantes - notas10 * 10
notas5 = int(cedulas_Restantes / 5)
cedulas_Restantes = cedulas_Restantes - notas5 * 5
notas2 = int(cedulas_Restantes / 2)
cedulas_Restantes = cedulas_Restantes - notas2 * 2
notas1 = int(cedulas_Restantes / 1)
cedulas_Restantes = cedulas_Restantes - notas1 * 1

print(f"{entrada_Inicial}")
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")
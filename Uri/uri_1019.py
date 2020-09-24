entrada_segundos = int(input())

resto = entrada_segundos

horas = int(resto / 3600)
resto = resto - horas * 3600
minutos = int(resto / 60)
segundos = resto

print(f"{horas}:{minutos}:{segundos}")
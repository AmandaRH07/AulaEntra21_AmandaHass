valor_um = float(input())
valor_dois = float(input())
valor_tres = float(input())
valor_quatro = float(input())
valor_cinco = float(input())
valor_seis = float(input())

lista = [valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco, valor_seis]

tamanho = len(lista)
positivos = 0
media = 0
for i in range(tamanho):
    if lista[i] >= 0:
        positivos +=1
        media += lista[i]

print(f"{positivos} valores positivos")
print(f"{(media / positivos):.f}")
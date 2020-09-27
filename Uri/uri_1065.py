valor_um = int(input())
valor_dois = int(input())
valor_tres = int(input())
valor_quatro = int(input())
valor_cinco = int(input())

lista = [valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco]

tamanho = len(lista)
pares = 0
for i in range(tamanho):
    if lista[i] % 2 == 0:
        pares +=1

print(f"{pares} valores pares")

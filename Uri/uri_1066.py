valor_um = int(input())
valor_dois = int(input())
valor_tres = int(input())
valor_quatro = int(input())
valor_cinco = int(input())

lista = [valor_um, valor_dois, valor_tres, valor_quatro, valor_cinco]

tamanho = len(lista)
pares = 0
impares = 0
positivo = 0
negativo = 0 
for i in range(tamanho):
    if lista[i] % 2 == 0:
        pares += 1
    else: 
        impares += 1
    if lista[i] == 0:
        pass
    elif lista[i] > 0:
        positivo += 1
    else: 
        negativo += 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")
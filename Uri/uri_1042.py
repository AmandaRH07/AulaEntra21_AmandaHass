a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

lista = [a, b, c]
lista_aux = [a, b, c]
lista_aux.sort()

for i in range(3):
    print(lista_aux[i])

print()
for i in range(3):
    print(lista[i])

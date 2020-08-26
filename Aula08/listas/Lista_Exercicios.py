# #**LISTAS E METODOS**
# 
#   **Indexação**
#   
#   É a forma usada para recuperar parte da lista usando indices. 
#   
#   lista[ inicio : fim ]
#   
#   Inicio: Inicio da lista, começa com 0
#   Fim: Fin da lista. 
#   Lembrando que pega o valor anterior.

#   Comandos:
#   lista.append() = adicionar na ultima posição
#   lista.insert(index,elemento) = adicionar na posição escolhida
#   ultimo = lista.pop() = retirar o ultimo elemento e retornar
#   lista.remove() = remover o primeiro elemento indexado
#   lista.sort() = ordenar os elementos da lista em order crescente
#   lista.revert() = inverte os elementos da lista

lista = [6,7,8,9,10,11,12,13]
# Pegando o primeiro elemento
print(lista[0])

# Pegando o terceio elemento
print(lista[2])

# Pegando o último elemento
print(lista[-1])

# Pegar todos os números a partir do terceio elemento
print(lista[2:])

# Pegando o número 7 a 10
print(lista[1:5])

# Sabia que isso também funciona com strig!

texto = "Atirei o pau no gato"
print(texto[2])
print(texto[2:10])



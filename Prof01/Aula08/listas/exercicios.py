# **Exercícios**

# Dada a seguinte lista, resolva os seguintes questões:

# EXECUTE ESTE QUADRO PARA PODER USAR A LISTA
lista = [10, 20, 'amor', 'abacaxi', 80, 'Abioluz', 'Cachorro grande é de arrasar']
#        0,   1,   2,      3        4,      5,      6

# 1) Usando a indexação, escreva na tela a palavra abacaxi

print("Abacaxi:", lista[3])

# 2) Usando a indexação, escreva na tela os seguintes dados: 20, amor, abacaxi

print("20, amor, abacaxi:", lista[1:4])

# 3) Usando a indexação, escreva na tela uma lista com dados de 20 até Abioluz

print("Dados de 20 até Abioluz:", lista[1:6])

# 4) Usando a indexação, escreva na tela os seguintes dados:
# 10, amor, 80, Cachorro grande é de arrasar

print("Os dados são: ", lista[0:7:2])

# 5) Usando a indexação escreva na tela os seguintes dados:
# amor - 10 - 10 - abacaxi - Cachorro grande é de arrasar - Abioluz - 10 - 20

print(f"Os dados são: {lista[2]}, {lista[0]}, {lista[0]}, {lista[3]} , {lista[6]}, {lista[5]}, {lista[0]}, {lista[1]}")

# 6) Usando a indexação, escreva na tela uma lista com dados de 10 até 80

print("Dados de 10 até 80:", lista[0:4])

# 7) Usando a indexação, escreva na tela os seguintes dados:
# 10, abacaxi, Cachorro grande é de arrasar

print("10, abacaxi, Cachorro grande é de arrasar: ",lista[::3])

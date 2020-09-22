# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência
# 

import math 

raio = float(input("Insira o raio da circunferência: "))

area = (math.pi) * (raio **2)
print('A área da circunferência é: {:.2f}'.format(area))
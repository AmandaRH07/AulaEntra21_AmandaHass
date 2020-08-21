"""Execicios 04
Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;

Triângulo Isósceles: quaisquer dois lados iguais;

Triângulo Escaleno: três lados diferentes;
"""

print("Insira três lados de um triangulo")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
 
if (c > a+b ) or (b > a+c) or (a > b+c):
    print("Os números inseridos não formam um triangulo")
else:
    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b  == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

  
   

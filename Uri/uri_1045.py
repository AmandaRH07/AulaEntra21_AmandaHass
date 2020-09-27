a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b  
elif b > a and b > c:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a  
else:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a

A = maior
B = meio
C = menor

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else: 
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or A == C != B or B == C != A:
        print("TRIANGULO ISOSCELES")
codigo, quantidade = input().split(' ')

codigo = int(codigo)
quantidade = int (quantidade)

if codigo == 1:
    resultado = 4.00 *quantidade
elif  codigo == 2:
    resultado = 4.50 *quantidade
elif  codigo == 3:
    resultado = 5.00 *quantidade
elif  codigo == 4:
    resultado = 2.00 *quantidade
else:
    resultado = 1.50 *quantidade

print(f"Total: R$ {resultado:.2f}")
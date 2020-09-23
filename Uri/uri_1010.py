codigo_P1, num_P1, valor_P1 = input().split(" ")
codigo_P2, num_P2, valor_P2 = input().split(" ")

codigo_P1 = int(codigo_P1)
num_P1 = int(num_P1)
valor_P1 = float(valor_P1)

codigo_P2 = int(codigo_P2)
num_P2 = int(num_P2)
valor_P2 = float(valor_P2)

valor = (num_P1 * valor_P1) + (num_P2 * valor_P2)

print(f"VALOR A PAGAR: R$ {valor:.2f}")
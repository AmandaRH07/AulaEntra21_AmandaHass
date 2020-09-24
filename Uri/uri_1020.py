idade_Dias = int(input())

ano = int(idade_Dias / 365) 
idade_Dias = idade_Dias - ano * 365
mes = int(idade_Dias / 30)
idade_Dias = idade_Dias - mes * 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{idade_Dias} dia(s)")
hora_Inicial, hora_Final = input().split(" ")

hora_Inicial = int(hora_Inicial)
hora_Final = int(hora_Final)

if hora_Final > hora_Inicial:    
    tempo = hora_Final - hora_Inicial
else:
    tempo = (24 - hora_Inicial) + hora_Final

print(f"O JOGO DUROU {tempo} HORA(S)")
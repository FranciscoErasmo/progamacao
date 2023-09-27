distancia=float(input("Digite a distância: ")) #variável p/ o usuário digitar a distância com ou sem ","
vm=float(input("Digite a velocidade média por hora: ")) #variável p/ o usuário digitar a velocidade média com ou sem ","
tempo=distancia/vm
horas=int(tempo)
minutos=int((tempo-horas)*60)
print(('{}.{} minuto(s)').format( horas, minutos)) #impressão do tempo (em horas) levadas para percorrer a distância e velocidade média digitadas pelo usuário
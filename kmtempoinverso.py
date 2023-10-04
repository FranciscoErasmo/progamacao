distancia=float(input("Digite a distância em quilômetros: ")) #variável p/ o usuário digitar a distância com ou sem ","
minutos=float(input("Digite o tempo que a corrida levará em minutos: ")) #variável p/ o usuário digitar a velocidade média com ou sem ","
horas = distancia/(minutos/60)
print(horas,"km/h")
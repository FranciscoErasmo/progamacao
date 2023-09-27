tamanho=float(input("Digite o tamanho do download em megabit: "))
mgps=float(input("Digite a velocidade de megabytes por segundo: "))
print((tamanho*8)/(mgps*60), "minutos")

peso=float(input("Peso dos peixes em quilos: "))
if peso>50:
    sobra=(peso-50)
    print("Multa: R$",(sobra*4),2)
else:
    print("Sem multa")

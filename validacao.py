while True:
    nota=float(input("Digite um número entre 0 e 10: "))
    if nota>=0 and nota<=10:
        print("valor válido")
        break
    else:
        print("inválido")
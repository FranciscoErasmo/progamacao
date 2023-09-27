num1=int(input("Digite um número"))
num2=int(input("Digite o número do limite"))
b=0
for b in range (num1, num2):
    if b %2 == 0:
        print("par", b)
    else:
        print("ímpar", b)
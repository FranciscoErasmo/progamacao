soma=0 
b=0
num1=int(input("Digite um número"))
num2=int(input("Digite o limite da sua sequência"))
num3=int(input("Digite o tamanho do salto"))

for b in range(num1, num2, num3):
    soma +=b
    print(soma) 

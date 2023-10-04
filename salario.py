num1=float(input("Quantas horas você trabalha por mês?"))
num2=float(input("Quanto você ganha por hora?"))
soma=int(num1*num2) #valor líquido do salário mensal
ir=soma*0.11 #multiplicação do salário vezes o imposto já dividido por 100
inss=soma*0.08
sindicato=soma*0.05
salario_bruto=soma-(ir + inss + sindicato)
print(  "Salário líquido: ", soma, 
        "\n Imposto de Renda:", ir,
        "\n INSS: ", inss,
        "\nSindicato:", sindicato,
        "\n Salário Bruto: ", salario_bruto)
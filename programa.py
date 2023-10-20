nota=float(input("Digite sua nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota+nota2)/2
if media >=9:
    print(nota, ",", nota2,",", media,",", "Nota A, Aprovado")
elif 7.5<=media<9:
    print(nota, ",",nota2,",", media,",", "Nota B, Aprovado")
elif 6<=media<7.5:
    print(nota, ",",nota2,",", media,",", "Nota C, Aprovado")
elif 4<=media<6:
    print(nota,",", nota2,",", media,",", "Nota D, Reprovado")
elif 0<=media<4:
    print(nota,",", nota2,",", media,",", "Nota E, Reprovado")
else:
    print("error")
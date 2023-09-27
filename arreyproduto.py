produtos=("Red-bull", "Coca-Cola", "Guaraná", "Monster")
quantidades=(12,24,32,20)
valores=(10, 11, 8, 7)
for i in range(len(produtos)):
    produto = produtos[i]
    valor = valores[i]
    quantidade = quantidades[i]
    print(f"quantidade: {quantidade}, produto: {produto}, valor de: {valor}")
    print("valor total:", quantidade*valor)
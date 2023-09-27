produtos = ("produto1", "produto2", "produto3")
valorprodutos = (210, 320, 300)
quantidades = ("5, 10, 15")
frete= 50
imposto1 = 12
imposto2 = 6
imposto3 = 3
for i in range (len(produtos))
produto = produtos[i]
valorproduto=valorprodutos[i]
quantidade=quantidades[i]
lucro=60
imposto1 = ((valorproduto * imposto1)/100)
imposto2 = ((valorproduto * imposto2)/100)
imposto3 = ((valorproduto * imposto3)/100)
preco_custo = (valorproduto + imposto1 + imposto2 + imposto3)
margemdelucro=((preco_custo*lucro)/100)
preco_venda= (preco_custo+margemdelucro)
vendaproduto=(preco_venda*quantidade)
precovendacomfrete=(quantidade/frete)
print(f"produto", produto, "custo sem imposto:", round(valorproduto,2), "custo com imposto:", round(preco_custo, 2), "preco de venda", round(preco_venda,2), "quantidade:", round(quantidade), "total de venda", round(vendaproduto,2), "preço de venda com frete", precovendacomfrete,2)

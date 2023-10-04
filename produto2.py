    if menu == 1:
        # Opção 1: Inserir o nome do produto
    def inserir_produto
        nome = str(input("Digite o nome do produto: "))
        quantidade = int(input("Digite a quantidade: "))
        valor = float(input ("Digite o valor para o produto: "))
        frete = float(input ("Digite o valor do frete total da quantidade comprada: "))
        lucro = float(input ("Digite o valor do lucro desejado: "))
        nomes.append(nome)
        quantidades.append(quantidade)
        valores.append(valor)
        fretes.append(frete)
        lucros.append(lucro)/100
        print("Nome, quantidade e valor inseridos com sucesso.")
    elif menu == 2:
    def atualizar_nome
           nome_para_atualizar = input("Digite o nome a ser atualizado: ")
        if nome_para_atualizar in nomes:
            indice = nomes.index(nome_para_atualizar)
            nova_quantidade = input("Digite a nova quantidade: ")
            quantidades[indice] = nova_quantidade
            novo_valor = input("Digite um novo valor para o produto: ")
            valores[indice] = novo_valor
            print("Quantidade e valor atualizados com sucesso.")
            novo_frete = input("Digite um novo valor para o frete: ")
            fretes[indice] = novo_frete
            novo_lucro = input("Digite um novo valor para o lucro: ")
            lucros[indice] = novo_lucro
        else:
            print("Nome não encontrado.")
    elif menu == 3:
        # Opção 3: Imprimir a lista de produtos
    def 
        for i in range(len(nomes)):
            print(f"{nomes[i]}: {quantidades[i]}; valor de {valores[i]}; frete de {fretes[i]}; lucro de {lucros[i]}")
            imposto1 = 12
            imposto2 = 6
            imposto3 = 3
            print("imposto1 = ", ((valor * imposto1)/100))
            print("imposto2 = ", ((valor * imposto2)/100))
            print("imposto3 = ", ((valor * imposto3)/100))
                    freteunitario = (frete/quantidade)
                    preco_custo = (valor + imposto1 + imposto2 + imposto3 + freteunitario)
                    margemdelucro=((preco_custo*lucro)/100)
                    preco_venda= (preco_custo+margemdelucro)
                    vendaproduto=(preco_venda*quantidade)
                    precovendacomfrete=(quantidade/frete)
            print("Preço de custo: ", preço_custo
                  "\n Margem de lucro: ", margemdelucro,"%"
                  "\n Preço de venda: ", preco_venda
                  "\n Preço de venda com frete: ", precovendacomfrete
                  "\n Preço do frete unitário: ", freteunitario
                  "\n Valor total: ", vendaproduto )
    elif menu == 4:
    def deletar produto
    # Loop principal do programa
    while True:
    # Exibe o menu e obtém a escolha do usuário
    menu = float(input(
    "Escolha uma opção para o menu:\n"
            "1 - Inserir\n"
            "2 - Atualizar\n"
            "3 - Imprimir\n"
            "4 - Deletar\n"
            "5 - Sair\n"))
    
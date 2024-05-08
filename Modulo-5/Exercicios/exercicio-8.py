produtos = {"cenoura": [100, 0.99],
            "brócolis": [50, 3.99],
            "batata": [200, 0.49],
            "cebola": [75, 1.10]}
pedido = []

total = 0

produtoDesejado = input("Digite qual produto deseja comprar: ")

if (produtoDesejado in produtos) :
    quantidadePedido = int(input("Digite a quantidade que deseja comprar: "))
    pedido.append({"produto": produtoDesejado, "quantidade": quantidadePedido})

else :
    print("Produto não encontrado!")

for item in pedido :
    produto = item["produto"]
    qtd = item["quantidade"]
    preco = produtos[produto][1]
    valorProd = preco * qtd

    print(f"{produto}: {qtd} x {preco} = {valorProd}")

    produtos[produto][0] -= qtd
    total += valorProd
print(f"Custo total: {total}\n")
print("Estoque:")

for chave,valor in produtos.items() :
    print("Descrição:", chave)
    print("Quantidade:", valor[0])
    print(f"Preço {valor[1]}\n")

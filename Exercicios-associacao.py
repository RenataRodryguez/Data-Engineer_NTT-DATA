produto_selecionado = input("Escreva o produto: ")
cupom10 = ["notebook", "smartphone", "tablet", "headset"]
cupom20 = ["Monitor", "Gabinete", "Caixa de som"]

if produto_selecionado in cupom10:
    print("Voce ganhou cupom de 10% de desconto! Aproveite!")
elif produto_selecionado in cupom20:
    print("Você ganhou 20% de desconto! Aproveite!")
else:
    print("Produto não entra na promoção")

# Use o operador de associação para verificar se o produto está no estoque.

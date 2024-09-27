# Dicionário de produtos e seus respectivos descontos
descontos = {
    "notebook": 10,
    "smartphone": 10,
    "tablet": 10,
    "headset": 10,
    "monitor": 20,
    "gabinete": 20,
    "caixa de som": 20
}

# Solicita o produto ao usuário e padroniza o input para letras minúsculas
produto_selecionado = input("Escreva o nome do produto: ").strip().lower()

# Verifica se o produto está no dicionário de descontos
if produto_selecionado in descontos:
    desconto = descontos[produto_selecionado]
    print(f"Você ganhou um cupom de {desconto}% de desconto! Aproveite!")
else:
    print("Esse produto não está na promoção no momento.")

cliente = input("Digite o banco: ")

lista_clientes_permitidos = ["Santander", "Itaú"]
lista_clientes_proibidos = ["Banco do Brasil", "Caixa"]

if cliente in lista_clientes_permitidos:
    print("Fazer pagamento")
elif cliente in lista_clientes_proibidos:
    print("Não fazer pagamento")
else:
    print("Não fazer pagamento")


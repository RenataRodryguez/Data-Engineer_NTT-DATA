# Se eu digitar o número 10, ele para o programa
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    print(numero, "ok")
else:
    print("Thanks")
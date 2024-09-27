#método uteis da classe string
 # curso = "PythON"
# print(curso.upper())
# print(curso.lower())
# print(curso.title())
# print(curso.strip())
# print(curso.lstrip())
# print(curso.rstrip())
# print(curso.center(10, "A")) numero de caracteres conta o numero dos caracteres existentes + os caratecres que vc quer
# print(".".join(curso))

nome = input("Qual seu nome?")
texto = "Seja bem vindo ao curso de Python"
# print(texto, nome.strip().title())
# print(texto, "-".join(nome).title())
for abaco in nome:
    print(abaco, end="-")
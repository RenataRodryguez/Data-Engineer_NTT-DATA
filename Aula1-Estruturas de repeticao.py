# Receba um número do teclado e exiba os dois números seguintes
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print() #adiciona uma quebra de linha

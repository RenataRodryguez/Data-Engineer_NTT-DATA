# Recebe a entrada e normaliza para letras minúsculas
pasta = input('A pasta está completa?').lower()
assinatura = input('A pasta está assinada pelo contador?').lower()

# Verifica se a pasta está completa e assinada
if pasta == "sim" and assinatura == "sim":
    print("Entregar no condomínio")
    
    # Recebe e valida o nome do condomínio
    condominio = input('Nome do condomínio:').lower()
    if condominio not in ['vila', 'parque', 'edificio']:
        print("Nome de condomínio inválido.")
    else:
        # Recebe e valida o nome da síndica
        sindica = input('Síndica:').lower()
        if sindica not in ['marcio', 'eliana', 'helena']:
            print("Nome de síndica inválido.")
        else:
            # Verifica as condições específicas para o condomínio Poeme
            if condominio == 'vila' and sindica in ['marcio', 'eliana']:
                print('Entregar para síndico assinar')
                
                # Verifica a assinatura do síndico
                assinatura_sindica = input('Tem assinatura do síndico?').lower()
                assinatura_moradores = input('Tem assinatura dos moradores?').lower()
                
                if assinatura_moradores == "sim":
                    print("Pasta completa")
                else:
                    print("Faltam assinaturas dos moradores")
            else:
                print('Não entregar para síndica assinar')
else:
    print('Não entregar no condomínio')

conta_simples = True 
conta_salario = False

saldo = 200
saque = 2500
cheque_especial = 450

if conta_simples >= saque:
    print('saque realizado com sucesso')
elif saque <= (saldo + cheque_especial):
    print('saque realizado com uso do cheque especial!')
elif conta_salario:
    if saldo >= saque:
        print('saque realizado com sucesso')
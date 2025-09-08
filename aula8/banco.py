# Nesse programa, vamos usar o operador and para limitar 
# o saque do cliente.

saldo = 5000.00
limite_saque = 1000.00    # por dia

while True:
    saque = float(input('Digite o valor do seu saque: '))
    if saque <= saldo and saque <= limite_saque:
        print('Saque permitido.')
        saldo -= saque
        print(f'Saldo atual: {saldo:.2f}')
        break
    else:
        print('Valor para saque inválido.')
        print('Tente novamente.')
print('=' * 30)
print('Banco do Povo')
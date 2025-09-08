# Nesse programa vamos usar o operador 'or' para processar 
# o pagamento com cartão de crédito ou PIX

while True:
    print('1 - Cartão de Crédito')
    print('2 - PIX')
    print('3 - Boleto')
    print('4 - Dinheiro')

    metodo_pgto = int(input('Digite o método de pagamento: '))

    if metodo_pgto == 1 or metodo_pgto == 2:
        print('Processando pagamento...')
        # Simulando o acesso ao sistema bancário
        print('Pagamento concluido com sucesso')
        break
    elif metodo_pgto == 3 or metodo_pgto == 4:
        print('Pagamento realizado na entrega ou entrega de boleto.')
        break
    else:
        print('Metodo de pagamento inválido.')

print('=' * 30)
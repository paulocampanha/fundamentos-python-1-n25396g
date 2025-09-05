# As casas Perambulando estão com uma promoção em
# toda linha de eletrodomésticos. Todos os produtos
# podem se parcelados em 10 vezes sem juros.
# Você foi contratado para criar um program que 
# solicita ao vendedor o nome do produto que o cliente 
# está comprado, o preço do produto e o número de parcelas.
# Seu programa deve calcular o valor de cada parcela e 
# imprimir um carnê conforme exemplo abaixo:
# ======================================
# Produto: Notebook
# Valor: 3000.00
# N. de Parcelas: 3
# Parcela 1: 1000.00
# Parcela 2: 1000.00
# Parcela 3: 1000.00
# ======================================
# --- Casas Perambulando S/A --- 

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input('Digite o preço do produto: '))
numero_parcelas = int(input('Digite o número de parcelas: '))
while numero_parcelas > 10:
    print('Número inválido de parcelas. Digite de 1 a 10 parcelas.')
    numero_parcelas = int(input('Digite o número de parcelas: '))

dia_pgto = int(input('Escolha o dia para pagamento 5, 10, 15 ou 25: '))
mes_pgto = 10
ano_pgto = 2025

contador = 1
valor_parcela = preco_produto / numero_parcelas

print('=' * 30)
print(f'Produto: {nome_produto}')
print(f'Valor: R$ {preco_produto:.2f}')
print(f'Nº e Parcelas: {numero_parcelas}')
while contador <= numero_parcelas:
    print(f'Parcela {contador:2d}: {dia_pgto:2d}/{mes_pgto:02d}/{ano_pgto} R$ {valor_parcela:.2f}')
    contador += 1
    mes_pgto += 1
    if mes_pgto > 12:
        mes_pgto = 1
        ano_pgto += 1
print('=' * 30)
print('--- Casas Perambulando S/A ---')
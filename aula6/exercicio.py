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
contador = 1
valor_parcela = preco_produto / numero_parcelas

while contador <= numero_parcelas:
    print(f'Parcela {contador}: R$ {valor_parcela:.2f}')
    contador += 1
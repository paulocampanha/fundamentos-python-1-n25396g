# Nesse programa vamos usar a estrutura de repetição for com
# listas e variaveis do tipo string

frutas = ['maçã', 'pera', 'banana', 'uva', 'melão']

for fruta in frutas:
    print(f'Eu gosto de {fruta}.')

print('=' * 30)

palavra = 'Guarulhos'
for letra in palavra:
    print(letra)

print('=' * 30)

# Usando break para interromper o for
parcelas = 5
for i in range(1, 11):
    print(f'Parcela {i}')
    if i >= parcelas:
        break

print('*' * 30)

# Usando 'continue' para desviar o loop
for i in range(31):
    if i % 3 == 0:
        continue
    print(i)
    print('-' * 30)
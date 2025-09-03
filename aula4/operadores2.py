# Nesse programa vamos estudar os operadores de atribuição
# do Python

nome = 'Gaspar'  # atribuindo a literal 'Gaspar' à variavel 'nome'

valor = 10  # atribuindo a literal '10' à variavel 'valor'

valor += 5  # equivalente à valor = valor + 5
print(valor)
print('-' * 30)

valor -= 7 # equivalente à valor = valor - 7
print(valor)
print('-' * 30)

valor *= 4  # equivalente à valor = valor * 4
print(valor)
print('-' * 30)

valor /= 3  # equivalente à valor = valor / 3
print(valor)
print('-' * 30)

valor **= 2 # equivalente à valor = valor ** 2
print(valor)
print('-' * 30)

valor //= 5 # equivalente à valor = valor // 5
print(valor)
print('-' * 30)


c = 26
cel = str(c)
print('Temp: ', cel + '°')
# Nesse programa vamos estudar o condicional if...else
# Nesse caso será criado dois blocos de código. Se a 
# condicional for falsa, o segundo bloco será executado

sexo = 'M'

if sexo.lower() == 'm':  # lower() - minúsculo e upper() - maiúsculo
    print('Você é do sexo masculino.')
    print('Utilize os banheiros da esquerda.')
else:
    print('Você não é do sexo masculino.')
    print('Utilize os banheiros da direita')
print('-' * 30)
print('Fim do Programa')

nome = 'Gaspar'
print(nome.lower())     # letras minúscula
print(nome.upper())     # letras maiúsculas
print(nome.capitalize())   # primeira letra maiúscula
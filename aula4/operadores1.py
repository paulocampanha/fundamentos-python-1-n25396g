# Nesse programa vamos estudar os operadores aritmético
# do python

num1 = 30
num2 = 3

# Soma (+)
soma = num1 + num2
print('A soma de', num1, 'com', num2, 'e', soma,'.')

# Subtração (-)
sub1 = num1 - num2
sub2 = num2 - num1
print('A subtração de ', num1, 'por', num2, 'é', sub1,'.')
print('A subtração de ', num2, 'por', num1, 'é', sub2,'.')

# Multiplicação (*)
mult = num1 * num2
print('A multiplicação de', num1 ,'por', num2 ,'é', mult ,'.')

# Divisão (/) 
# Obs: A divisão em Python sempre retorno um valor do tipo float
div1 = num1 / num2
div2 = num2 / num1
print('A divisão de', num1, 'por', num2, 'é', div1,'.')
print('A divisão de', num2, 'por', num1, 'é', div2,'.')

# Divisão Inteira (//)
# Obs: A divisão inteira retorna um valor inteiro
div3 = num1 // num2
div4 = num2 // num1
print('A divisão inteira de', num1, 'por', num2, 'é', div3,'.')
print('A divisão inteira de', num2, 'por', num1, 'é', div4,'.')

# Modulo (resto da divisão)
mod1 = num1 % num2
mod2 = num2 % num1
print('O resto da divisão de', num1,'por',num2,'é',mod1,'.')
print('O resto da divisão de', num2,'por',num1,'é',mod2,'.')

# Potencia
potencia = num1 ** num2  
print(num1,'elevado a',num2,'é',potencia,'.')

# Porcentagem
valor = 500
porc = 0.1
desconto = valor * porc  # 500 * 0.1 = 50
valor_desconto = valor - desconto  # 500 - 50
print('Valor com desconto: ', valor_desconto)

salario = 5000
porc_aumento = 0.15
novo_salario = salario + (salario * porc_aumento)
print('Novo salario: ', novo_salario)

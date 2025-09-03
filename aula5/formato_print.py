# Nesse programa vamos explorar algumas das opções
# da função print

# Imprimindo nomes
print('Gaspar','Luiza','Jorge','Anabela')

# Inserindo separadores
print('Gaspar','Luiza','Jorge','Anabela', sep='-')
print('Gaspar','Luiza','Jorge','Anabela', sep='')
print('Gaspar','Luiza','Jorge','Anabela', sep=', ')

# Imprimindo tudo na mesma linha
print('Nome:', end=' ')
print('Gaspar', end=' - ')
print('Idade:', end=' ')
print(15,end='\n')
print('-' * 30)

# Formatação de String
nome = 'Bruce'
idade = 15
sexo = 'masculino'

# Imprimindo da forma antiga
print('O aluno', nome, 'tem', idade,'anos e é do sexo', sexo,'.')

# Imprimindo usando o método .format()
print('O aluno {} tem {} anos e é do sexo {}.'.format(nome, idade,sexo))

# Imprimindo usando f-string
print(f'O aluno {nome} tem {idade} anos e é do sexo {sexo}.')

# Imprimindo casas decimais
indice = 123.4567
print(f'Indice completo {indice}.')
print(f'Índice com duas casas decimais: {indice:.2f}.')
print(f'Índice sem casas decimais: {indice:.0f}.')
print(f'Índice com espaços antes do número: {indice:10.2f}.')

# Arredondamento de casas decimais
print(round(123.4))  #123
print(round(123.6))  #124
print(round(123.456, 2))  #123.46

# Usando f-string em variáveis 
salario = 5540.25
frase = f'Seu salário é R$ {salario}'
print(frase)

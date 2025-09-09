# Nesse programa vamos usar funções com argumentos
# mas sem retorno.


# Definindo uma função com o parâmetro nome
def saudar_usuario(nome):
    print(f'Olá, {nome}')
    print(f'Seja bem-vindo ao nosso sistema.')

# Definindo a função soma para somar dois números
def somar(x, y):
    soma = x + y
    print(f'A soma dos números é {soma}.')

nome_usuario = input('Digite o seu nome: ')
saudar_usuario(nome_usuario)
print('=' * 50)
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
somar(num1, num2)



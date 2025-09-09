# Funções são blocos de código separado do código
# principal que pode ser 'chamado' sempre que for
# preciso. Por exemplo, uma função que imprime uma 
# linhas de separação do código

# Definindo uma função sem argumentos e sem retorno
def linha():
    # imprimindo 50 vezes o sinal de igual
    print('=' * 50)

linha()
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
linha()
escola = input('Digite o nome da sua escola: ')
curso = input('Digite o nome do curso que está fazendo: ')
linha()
linha()
print(f'Seu nome é {nome} e você tem {idade} anos.')
print(f'Você estuda na escola {escola} e faz o curso {curso}.')
linha()
print('--- Sistema Senai ---')
linha()

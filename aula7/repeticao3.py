# Nesse programa vamos estudar a estrutura de repetição
# for. Esse estrutura executa um bloco de código uma vez
# a cada item da sequência. Para gerar essa sequência podemos
# usar uma string, uma lista ou uma faixa de números gerada 
# pela função range()

# Usando o range com 1 argumento
for numero in range(10):   # a sequência inicia em 0 e vai até 9 (10 - 1)
    print(numero)

print('=' * 30)

# Usando o range com 2 argumentos
for numero in range(1, 11):  # a sequencia inicia em 1 e vai até 10 (11-1)
    print(numero)

print('*' * 10)

# Usando o range com 3 argumentos
for numero in range(10, 101, 10):  # a sequencia inicia em 10 e vai até  100 (101 - 1) em intervalos de 10 em 10
    print(numero)

print('+' * 30)
# Desafio: imprima uma contagem regressiva do 10 ate o 1
# usando o for e range()
for numero in range(10, 0, -1):
    print(numero, end='...')
print('F O G O ! ! !')



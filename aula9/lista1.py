# Nesse programa, vamos trabalhar com listas

# Lista de números inteiros
numeros = [10, 23, 15, 56, 32, 48]

# Lista de string (frutas)
frutas = ['maçã', 'banana', 'pera', 'uva', 'melão']

# Lista de números decimais
notas = [8.5, 3.0, 9.4, 10.0, 5.4 ]

# Lista mista
dados_usuario = ['Gaspar', 25, 1.75, True]

# Lista vazia
cursos = []

# Acessando dados da lista
print(numeros[0])  # saída: 10
print(frutas[1])   # saída: banana
print(notas[-1])   # saída: 5.4
print(dados_usuario) # saída: ['Gaspar', 25, 1.75, True]

for dado in dados_usuario:
    print(dado)

soma_notas = 0
contador = 0
for nota in notas:
    soma_notas += nota
    contador += 1

media = soma_notas / contador
print(media)
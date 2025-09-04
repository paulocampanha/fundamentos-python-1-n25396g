# Nesse programa vamos imprimir a tabuada de um número
# fornecido pelo usuário usando a estrutura de repetiçãp
# while

print('=' * 30)
numero = int(input('Digite um número para a tabuada: '))
contador = 1
print(f'\n --- Tabuada do {numero} ---')
print('=' * 30)
while contador <= 10:
    total = numero * contador
    print(f'{numero} X {contador:2d} = {total:3d}')
    contador += 1
print('=' * 30)

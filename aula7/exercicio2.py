# Faça um programa que solicita ao usuário um número 
# inteiro e imprima a tabuada desse número usando a 
# estrutura de repetição for.

numero = int(input('Digite um número inteiro: '))

for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')
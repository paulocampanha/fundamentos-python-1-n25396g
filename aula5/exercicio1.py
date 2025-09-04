"""
Atividade 1: Classificação de Idade
Crie um programa que peça a idade do usuário.
Use estruturas if-elif-else para classificar a idade em:
"Criança" (0 a 12 anos)
"Adolescente" (13 a 17 anos)
"Adulto" (18 a 59 anos)
"Idoso" (60 anos ou mais)
"""

idade = int(input("Digite a idade: "))

print(type(idade))

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')

print('-' * 30)


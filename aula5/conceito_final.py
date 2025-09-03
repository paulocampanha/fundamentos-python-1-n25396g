# Nesse programa vamos solicitar as notas de um aluno
# é imprimir o conceito final do mesmo. 

print('--- Escola Senai ---')
print('=' * 30)
nome_aluno = input('Digite o nome do aluno: ')
nota1 = float(input('A digite a 1ª nota do aluno: '))
nota2 = float(input('A digite a 2ª nota do aluno: '))
nota3 = float(input('A digite a 3ª nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'O aluno {nome_aluno} foi APROVADO com a media {media:.1f}')
elif media >= 4:
    print(f'O aluno {nome_aluno} ficou de RECUPERAÇÃO com a média {media:.1f}.')
else:
    print(f'O aluno {nome_aluno} foi REPROVADO com a média {media:.1f}')

print('=' * 30)
print('Fim do Programa')
# Nesse programa vamos conhecer algumas funções úteis com listas

notas = [5.5, 6.9, 4.8, 9.5, 10.0, 7.8]

# len() retorna o número de itens da lista
print(f'Itens da lista: {len(notas)}') 

# sum() retorna a soma dos itens da lista
print(f'Soma da notas: {sum(notas)}')

# max() retorna o maior elemento da lista
print(f'Nota máxima: {max(notas)}')

# min() retorna o menor elemento da lista
print(f'Nota mínima: {min(notas)}')

# Desafio: calcula a média das notas usando algumas funções acima
media = sum(notas) / len(notas)
print(f'Média: {media:.1f}.')
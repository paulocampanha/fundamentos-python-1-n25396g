# Nesse arquivo vamos inserir e excluior itens da lista

animais = []
# Adicionando itens na lista
animais.append('gato')   # adiciona 'gato' no final da lista
print(animais)
animais.append('cachorro') # adiciona 'cachorro' no fina da lista
print(animais)
animais.append('pássaro')  # adiciona 'pássaro' no final da lista
print(animais)
animais.insert(1, 'rato')  # adiciona 'rato' no indice 1 da lista
print(animais)
animais.insert(0, 'cachorro')
print(animais)

# Removendo itens da lista
animais.remove('cachorro')  # remove a primeira ocorrencia de 'cachorro' na lista
print(animais)
animais.pop()    # remove o último intem da lista
print(animais)
animais.pop(1)   # remove o item na posição 1 da lista
print(animais)
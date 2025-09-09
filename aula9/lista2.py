# Nesse programa vamos continuar trabalhando com listas

nomes = ['Gaspar', 'Luiza', 'Anabela', 'Jorge', 'Bruce']

# Fatiamento da lista
print(nomes[1:3])   # saída: Luiza, Anabela
print(nomes[:3])    # saída: Gaspar, Luiza, Anabela
print(nomes[2:])    # saída: Anabela, Jorge, Bruce
print(nomes[-2:])   # saída: Jorge, Bruce
print(nomes[0::2])  # saída: Gaspar, Anabela, Bruce
print(nomes[::-1])  # saída: Bruce, Jorge, Anabela, Luiza, Gaspar
# Mudando a ordem da lista
nomes.sort()   # Classifica a lista em ordem alfabética
print(nomes)         # saída: Anabela, Bruce, Gaspar, Jorge, Luiza
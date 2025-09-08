# Os operadores lógicos servem para combinar mais de 
# uma condição nos desvios condicionais e estruturas
# de repetição e podem ser usados, também, em 
# expressões simples para retornar verdadeiro ou falso
# Os operadores lógicos do Python são: and(e), or(ou) e not(não)

idade = 25
salario = 2000
tem_carteira = True  

# Verifica se a condição é verdadeira e imprime True ou False
print(idade >= 18)    
print('*' * 30)
# Imprimir True se todas as expressões forem verdadeiras
print(idade >= 18 and salario == 2000 and tem_carteira)
print('=' * 30)
# Imprime True se pelo menos uma expressão for verdadeira
print(idade >= 18 or salario == 2000 or tem_carteira)
print('-' * 30)
# Imprime True se pelo menos duas forem verdadeiras
print(idade >= 18 and salario == 2000 or tem_carteira)
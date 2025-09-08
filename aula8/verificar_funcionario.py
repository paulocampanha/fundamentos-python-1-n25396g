# Nesse programa vamos usar o operador 'not' para verificar
# se o funcionário trabalha no Senai ou não

escola = input('Digite o noma da escola: ')

if not escola.lower() == 'senai':
    print('Utilize o estacionamento externo')
else:
    print('Utilize o estacionamento interno.')
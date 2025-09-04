# Nesse programa vamos verificar a senha digitada
# até que o usuário entre com a senha correta

senha = input('Digite sua senha: ')
contador = 1
print('=' * 30)
while senha != 'senha123':
    if contador > 3:
        print('Você atingiu o limite de tentativas.')
        print('usuário bloqueado.')
        break
    print('Senha incorreta. Tente Novamente')
    senha = input('Digite sua senha: ')
    print('=' * 30)
    contador += 1

if contador <= 3:
    print('Senha correta! Bem-vindo ao sistema.')
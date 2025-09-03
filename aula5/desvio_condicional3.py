# Nesse programa vamos estudar o desvio condicional
# if...elif...else. Nesse estrutura serão criados varios 
# blocos de código. Cada bloco e código com seu teste
# condicional. Se nenhum teste resultar em verdadeiro, o
# bloco final será executado

temperatura = 18

if temperatura <= 0:
    print('O tempo está congelante.')
elif temperatura <= 10:
    print('O tempo ainda está muito frio.')
elif temperatura <= 20:
    print('O tempo ainda está frio.')
elif temperatura <= 30:
    print('O tempo está agradável.')
elif temperatura <= 40:
    print('O tempo está sufocante de quente.')
else:
    print('O tempo está insuportável de quente.')

print('-' * 30)
print('Fim do Programa')
# Nesse programa vamos criar algumas funções com retorno
import math

# Definindo uma função  para calcular a área do retângulo 
# e retornar essa área
def calcular_area(a, l):
    area = a * l
    return area

def calcular_area_circulo(r):
    area = math.pi * r ** 2
    return area

# Desafio: crie uma função para calcular a área de um triângulo
# Fórmula: area = (base * altura) / 2
# Solicite ao usuário para digitar a base e a altura do triângulo
# Calcula e imprima a ára do triângulo

def calcular_area_triangulo(b, a):
    area = (b * a) / 2
    return area



print('=' * 50)
largura = float(input('Digite o lado do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))
area_retangulo = calcular_area(altura, largura)
print(f'A área do retângulo é {area_retangulo}.')

print('=' * 50)
raio = float(input('Digite o raio da circunferência: '))
area_circulo = calcular_area_circulo(raio)
print(f'A área da circunferêcia é {area_circulo}.')

print('=' * 50)
base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
area_triangulo = calcular_area_triangulo(base, altura)
print(f'A área do triângulo é {area_triangulo}.')


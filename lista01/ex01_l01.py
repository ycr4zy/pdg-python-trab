'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

metros_quadrados = float(
    input("Digite quantos m² a area que irá ser pintada: "))
tamanho_lata = 18
valor_lata = 80

litros = math.ceil(metros_quadrados / 3)
qtd_latas = math.ceil(litros/tamanho_lata)

print("Você deverá utilizar %d latas no valor de %.2f" %
      (qtd_latas, (qtd_latas*valor_lata)))

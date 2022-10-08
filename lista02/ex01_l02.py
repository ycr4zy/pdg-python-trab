'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
'''

import math

sexo = int(input("Digite seu Sexo\n1)Para Homem\n2)Para Mulher\n"))
altura_pessoa = float(input("Digite sua altura: "))
valor = ((72.7*altura_pessoa) -
         58) if sexo == 1 else ((62.1*altura_pessoa) - 44.7)
print("%s: %.2f" % ("Homem" if sexo == 1 else "Mulher", valor))
'''
Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar
'''
numero = int(input("Digite um número: "))

print("%s" % ("Par") if numero %2 == 0 else "Impar")
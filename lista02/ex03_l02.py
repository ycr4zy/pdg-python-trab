'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
'''

numero = float(input("Digite um número: "))
print("%s" % ("Inteiro" if numero // 1 == numero else "Decimal"))

'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido
'''

salario_hora = float(
    input("Digite o quanto você recebe por horas trabalhadas: "))
quantidade_horas = int(
    input("Digite a quantidade de horas trabalhadas no mês: "))
ir = 0.11
inss = 0.08
sind = 0.05
salario_bruto = salario_hora * quantidade_horas
ir_total = salario_bruto * ir
inss_total = salario_bruto * inss
sind_total = salario_bruto * sind
salario_liq = salario_bruto - ir_total - inss_total - sind_total
print("Salario Bruto: %.2f\nIR: %.2f\nINSS: %.2f\nSindicato: %.2f\nDescontos Totais: %.2f\nSalario Liquido: %.2f" %
      (salario_bruto, ir_total, inss_total, sind_total, (ir_total + inss_total + sind_total), salario_liq))

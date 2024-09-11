#Faça um algoritmo que leia o valor que um funcionário ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do seu salário
#no referido mês.

horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
ganhosPorHora = float(input("Digite quanto você ganha por hora: "))

salarioTotal = horasTrabalhadas * ganhosPorHora

print("Você recebe R$ " , salarioTotal, " por mês")
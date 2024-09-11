#Desenvolva um algoritmo que receba o salário de um funcionário, calcule e
#mostre seu novo salário com reajuste de 15%.

salario = float(input("Digite seu salário: "))

novoSalario = salario + (salario * 0.15)

print("Seu salario foi reajustado com 15% de bônus.")
print(f"Seu novo salário é R$ {novoSalario}")
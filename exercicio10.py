#Desenvolva um algoritmo que receba o valor de um depósito em poupança,
#calcule e mostre o valor após um mês de aplicação na poupança, sabendo que
#a poupança rende 5% ao mês.

deposito = float(input("Digite quanto você deseja depositar: "))

valorRendimento = deposito + (deposito * 0.15)

print(f"Valor após um mês na poupança: R${valorRendimento}")
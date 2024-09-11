#Com base na altura de uma pessoa, construa um algoritmo que calcule seu
#peso ideal, usando a seguinte fórmula: (72.7 × altura) − 58.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

calculoImc = peso / (altura)**2

print("Seu IMC é: ", calculoImc)
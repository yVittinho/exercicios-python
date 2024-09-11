#Elabore um algoritmo que leia o valor do lado do quadrado e calcule a área. Em
#seguida, calcule o dobro da área. Mostre a área e o dobro.

lado = float(input("Digite o comprimento lateral do quadrado: "))

area = lado**2

areaDobro = area * 2

print("A área mede ", area , " e o dobro da area é " , areaDobro)
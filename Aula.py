lado1 = int(input("digite um lado do triangulo: "))
lado2 = int(input("digite outro lado do triangulo: "))
lado3 = int(input("digite o ultimo lado do triangulo: "))

if lado1 == lado2 == lado3:
    print('o triangulo é equilatero')

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('o triangulo é isoceles')

elif lado1 != lado2 != lado3:
    print('o triandulo é escaleno')

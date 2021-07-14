from fractions import Fraction as f
from decimal import Decimal as d

#given 2 points find the equation
print("Dadas la coordenada de un punto y la pendiente (slope) calcula la ecuación de la recta")
print("el punto se ingresa con el formato (x,y)")
print("por ejemplo: (-3,4) o (13,-24)")
print()
p= eval(input("ingrese el punto: "))
slope= f(input("ingrese la pendiente (slope): "))

if slope==0:
    b= p[1]
    equation = f'y= {b}'
else:
    b= f(p[1] - slope*p[0])
    b= b.limit_denominator(3)

    equation = f'y= {slope}x + {b}' if b >=0 else f'y= {slope}x {b}'
print(equation)
k=input("presione cualquier tecla para salir") 
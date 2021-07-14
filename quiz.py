from fractions import Fraction as f


#given 2 points find the equation
print("Dadas las coordenadas de dos puntos, muestra la respectiva ecuación")
print("los puntos se ingresan con el formato (x,y)")
print("por ejemplo: (-3,4) o (13,-24)")
print()
A= eval(input("ingrese primer punto: "))
B= eval(input("ingrese segundo punto: "))

num= B[1]-A[1]
den= B[0]-A[0]
#m= f((B[1]-A[1])/(B[0]-A[0]))
if num == 0 and den !=0:
    m=0
elif num !=0 and den !=0:
    m= f(num,den)


if den==0:
    equation = f'x= {A[0]}'
else:
    b= f(A[1] - m*A[0])
    equation = f'y= {m}x + {b}' if b >=0 else f'y= {m}x {b}'
print(equation)
k=input("presione cualquier tecla para salir") 


#Escribir una función que, dado el ingreso de 3 variables (a, b, c), retorne las raíces 
# resultantes de una ecuación cuadrática.

import cmath                                         #Llamo a la libreria de matematica que contempla negativos e imaginarios

a = float(input("Ingresar un valor para a: "))       #Pedimos ingresar valores   
b = float(input("Ingresar un valor para b : "))
c = float(input("Ingresar un valor para c: "))

def discriminante (a, b, c):                         # Defino discriminante      
    d= b**2 - 4*a*c
    r1= (-b + cmath.sqrt(d))/(2*a)
    r2= (-b - cmath.sqrt(d))/(2*a)
    return r1, r2


r1, r2 = discriminante (a, b, c)                     # Defino raices
print ("Las raices son: ", r1, r2)


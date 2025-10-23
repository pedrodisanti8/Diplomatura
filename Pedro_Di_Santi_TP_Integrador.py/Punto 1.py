#Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.
# Nro primo un nro natural mayor a 1 y es divisible unicamente por si mismo y 1


def nro_primo(n):                                   # Defino nro natural mayor a 1 
    if n < 2:
        return False 
    for i in range(2, n):                           # Definimos la condicion para nros primos.
        if n % i == 0:
            return False
    return True
    
n = int(input("Por favor, ingresar un número: "))

if nro_primo(n):
    print(f"{n} Es un nro primo!!!!!")
else:
    print(f"{n} No es un nro primo!")

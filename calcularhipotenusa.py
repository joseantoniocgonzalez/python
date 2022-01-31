#escribe un programa que solicite los catetos de un triangulo y calcule la hipotenusa

import math
cateto1=float(input("introduce el primer numero:"))
cateto2=float(input("introduce el segundo numero:"))

sumacatetos= cateto1**2 +cateto2**2
hipotenusa=math.sqrt(sumacatetos)
print("el resultado es: ",hipotenusa)
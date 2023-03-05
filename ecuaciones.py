#Programa para resolver ecuaciones de primer y segundo grado
print("---------------------------------------------------")
print("-------------------Ecuaciones----------------------")
print("---------------------------------------------------")

#Input

import math
x=int(input("¿cuántas ecuaciones quieres que resulva? "))
print("---------------------------------------------------")
z=0

#Processing y output

while z!=x:
    z=z+1
    y=int(input("Dígite 1 para ecuaciones de primer grado o dígite 2 para las de segundo grado: "))
    if y==1:
        a=int(input("Dígite el valor del coeficiente a: "))
        b=int(input("Dígite el valor del coeficiente b: "))
        if a==0:
            print("---------------------------------------------------")
            print("La función es constante y pasa por f(x)="+str(b)+" para todo x")
            print("---------------------------------------------------")
        else:
            w=-b/a
            print("---------------------------------------------------")
            print("La solución de la ecuación es x= "+str(w))
            print("---------------------------------------------------")
    else:
        a=int(input("Dígite el valor del coeficiente a: "))
        b=int(input("Dígite el valor del coeficiente b: "))
        c=int(input("Dígite el valor del coeficiente c: "))
        d=b*b-4*a*c
        if a==0:
            w=-b/c
            print("---------------------------------------------------")
            print("La solución de la ecuación es x= "+str(w))
            print("---------------------------------------------------")
        else:
            if d>0:
                w1=(-b+math.sqrt(d))/2*a
                w2=(-b-math.sqrt(d))/2*a
                print("---------------------------------------------------")
                print("Las soluciones de la ecuación son: x1="+str(w1)+" y x2="+str(w2))
                print("---------------------------------------------------")
            else:
                if d==0:
                    w=-b/2*a
                    print("---------------------------------------------------")
                    print("La solución de la ecuación es x= "+str(w))
                    print("---------------------------------------------------")
                else:
                    print("---------------------------------------------------")
                    print("La ecuación no tiene solución entre los reales")
                    print("---------------------------------------------------")

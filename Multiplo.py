#Escriba un programa que lea dos numeros enteros y que determine e imprima si el primero es multiplo del segundo
#utilice el opereador modulo

print("ingrese el primer numero:")
num1 = int(input())
print("ingrese el segundo numero:")
num2 = int(input())

if num1 % num2 == 0:
    print("El primer numero es multiplo del segundo")
else:
    print("El primer numero no es multiplo del segundo")
    
#Escriba un programa que dado un numero en segundos, lo convierta a minutos y horas

print("ingrese el numero de segundos:")
segundos = int(input())

minutos = segundos / 60
horas = minutos / 60

print("los segundos ingresados son: ", segundos)   
print("los segundos ingresados en minutos son: ", minutos)
print("los segundos ingresados en horas son: ", horas)
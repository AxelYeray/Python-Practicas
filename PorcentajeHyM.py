#Escriba un programa que calcule que porcentaje de hombres y qué porcentaje
# de mujeres hay en un grupo de estudiantes

#Solicitar la cantidad de hombres y de mujeres en el salón
h = int(input("Ingrese el numero de hombres en el salón:"))
m = int(input("Ingrese el numero de mujeres en el salón:"))

#Hace las operaciones para calcular el porcentaje
total = h + m
totalh = (h/total)*100
totalm = (m/total)*100

#Mostrar los resultados
print(f"porcentaje de hombres: {totalh:.2f}%")
print(f"porcentaje de mujeres: {totalm:.2f}%")


#Escriba un programa que calcule la calificación final de un alumno. Dicha calificación
#se compone de tres exámenes parciales cuya ponderación es de 30%,30% y 40%

examen1 = float(input("Ingresa la calificación de matemáticas:"))
examen2 = float(input("Ingresa la calificación de Español:"))
examen3 = float(input("Ingresa la calificación de biología:"))

#Calcular la calificacion final con poderaciones
ponderacion1 = 0.30
ponderacion2 = 0.30
ponderacion3 = 0.40

califacacion_final = (examen1 * ponderacion1) + (examen2 * ponderacion2) + (examen3 * ponderacion3)

print(f"La calificación final del alumno es: {califacacion_final: .2f}")

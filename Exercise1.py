#Exercise 1

#Objetivo: Crear un programa que calcule el Indice de Masa Corporal
#Definicion: IMC se calcula a traves de la formula IMC = peso(kg)/altura(m)**2

print('Bienvenido a tu calculadora de Masa Corporal')

#Solicitud de Datos
peso_kg = float(input('Ingrese su peso (en kilogramos): ' ))
altura_m = float(input('Ingrese su altura (en metros): '))

#Calculo del IMC
Resultado_IMC = peso_kg / (altura_m ** 2)

#Resultado del IMC
#Ubicacion del resultado en su rango
if Resultado_IMC < 18.5:
    print('Tu resultado es: ', round(Resultado_IMC, 2), 'y te encuentras en el rango de Bajo peso')
elif Resultado_IMC >= 18.5 and Resultado_IMC <= 24.99:
    print('Tu resultado es: ', round(Resultado_IMC, 2), 'y te encuentras en el rango Normal')
elif Resultado_IMC >= 25 and Resultado_IMC <= 29.99:
    print('Tu resultado es: ', round(Resultado_IMC, 2), 'y te encuentras en el rango de Sobrepeso')
elif Resultado_IMC >= 30 and Resultado_IMC <= 34.99:
    print('Tu resultado es: ', round(Resultado_IMC, 2), 'y te encuentras en el rango de Obesidad Grado 1')
elif 35 <= Resultado_IMC <= 39.99: #Inclusion de comparacion encadenada
    print('Tu resultado es: ', round(Resultado_IMC, 2), 'y te encuentras en el rango de Obesidad Grado 2')
else:
    print('Tu resultado es: ', round(Resultado_IMC, 2), 'y te encuentras en el rango de Obesidad Grado 3')

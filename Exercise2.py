#Exercise 2

#Objetivo: Conversor de Temperatura
#Definicion: La conversion de temperatura se validara sobre Celsius, Farenheit y Kelvin

print('Bienvenido al Conversor de Temperatura (C/F/K)')

#Solicitud de Datos

#Temperatura Inicial
temperatura_inicial = input('Selecciona la temperatura que quieres convertir, escribiendo: para Celsius > C, Fahrenheit > F, y Kelvin > K.')
if temperatura_inicial == 'C' or temperatura_inicial == 'c':
    valor_temperatura = float(input('Ingresa tu temperatura en escala Celsius: '))
elif temperatura_inicial == 'F' or temperatura_inicial == 'f':
    valor_temperatura = float(input('Ingresa tu temperatura en escala Fahrenheit: '))
elif temperatura_inicial == 'K'or temperatura_inicial == 'k':
    valor_temperatura = float(input('Ingresa tu temperatura en escala Kelvin: '))
else:
    print('No has seleccionado correctamente, vuelve a intentarlo.')

#Temperatura Resultado
temperatura_resultado = input('Selecciona la temperatura destino, escribiendo: para Celsius > C, Fahrenheit > F, y Kelvin > K.')
if temperatura_resultado in ['F', 'f'] and temperatura_inicial in ['C','c']:
    resultado_conver = float((valor_temperatura * (9/5))+32)  
elif temperatura_resultado in ['K', 'k'] and temperatura_inicial in ['C','c']:
    resultado_conver = float(valor_temperatura + 273.15)
elif temperatura_resultado in ['C', 'c'] and temperatura_inicial in ['F','f']:
    resultado_conver = float((valor_temperatura - 32) * (5/9))
elif temperatura_resultado in ['K', 'k'] and temperatura_inicial in ['F','f']:
    resultado_conver = float((valor_temperatura - 32) * (5/9) + 273.15)
elif temperatura_resultado in ['C', 'c'] and temperatura_inicial in ['K','k']:
    resultado_conver = float(valor_temperatura - 273.15)
else:
    resultado_conver = float((valor_temperatura - 273.15) * (9/5) + 32)

print('Los', valor_temperatura, 'grados', temperatura_inicial, 'son', round(resultado_conver,2), 'grados', temperatura_resultado)
#Python Basics

#Message = 'Hello World'

#Entrada y salida de datos

#Salida de informacion
print('Hola Mundo')
print('Tu edad es: ',25)

#Entrada de informacion
nombre = input('Ingrese su nombre: ')
edad1 = int(input('Cual es tu edad?: '))
print(f'Hola {nombre}, tienes {edad1} años')


#Variables
nombre = 'Pedro' #string - texto
edad = 30 #int - numeros enteros
precio = 19.90 #float - numeros decimales
esta_activo = True #boolean - condicion de verdadero o falso
Message = 'Hello World'

print(Message)
print (nombre)
print (edad)
print (precio)
print (esta_activo)
print(f'Hola {nombre}, tienes {edad} años') #f-string es una forma de formatear strings con variables

#Operadores aritmeticos
suma = 10 + 5
resta = 10 + 5
multiplicacion = 10 * 5
division = 10 / 5
division_entera = 10 // 3
modulo = 10 % 5 #residuo de la division por ejemplo 10 / 5 = 2 y residuo 0 pero 10 % 3 = 1 y residuo 1
potencia = 10 ** 2

print (suma)
print (resta)
print (multiplicacion)
print (division)
print (division_entera)
print (modulo)
print (potencia)


#Operadores de comparacion
mayor = 10 > 5
menor = 10 < 5
igual = 10 == 5
diferente = 10 != 5
mayor_igual = 10 >= 5
menor_igual = 10 <= 5

print (mayor)
print (menor)
print (igual)
print (diferente)
print (mayor_igual)
print (menor_igual)

#Operadores logicos

# and devuelve True si ambos valores son True
and_logico1 = True and True #True
and_logico2 = True and False #False
and_logico3 = False and True #False
and_logico4 = False and False #False

# or devuelve True si al menos uno de los valores es True
or_logico1 = True or True #True
or_logico2 = True or False #True
or_logico3 = False or True #True
or_logico4 = False or False #False

# not devuelve el valor contrario del valor booleano
not_logico1 = not True #False
not_logico2 = not False #True

print (and_logico1)
print (and_logico2)
print (and_logico3)
print (and_logico4)
print (or_logico1)
print (or_logico2)
print (or_logico3)
print (or_logico4)
print (not_logico1)
print (not_logico2)


#Estructuras condicionales

#if_basico
edad2 = int(input('Cual es tu edad?: '))
if edad2 >= 18:
    print('Eres mayor de edad')

#if_else
edad3 = int(input('Cual es tu edad?: '))
if edad3 >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

#if_elif_else
nota = int(input('Cual es tu nota?: '))
if nota >= 90:
    print('Excelente')
elif nota >= 80:
    print('Muy Bueno')
elif nota >= 70:
    print('Bueno')
elif nota >= 60:
    print('Regular')
else:
    print('Reprobaste')

#Referencia: Exercise1
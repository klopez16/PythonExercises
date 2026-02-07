#Exercise 3

#Objetivo: Crear un programa que aplique descuentos dependiendo la cantidad
#Definicion: Los descuentos se aplican solo si, la cantidad supera las 10 unidades el 20%
#si superan las 5 unidades el 10%.

print('Bienvenido al Sistema de Descuentos')

#Variables
descuento = 0

#Solicitud de Datos
cantidad_producto = int(input('Ingrese la cantidad: '))
precio = float(input('Ingrese su precio:'))

valor_venta = cantidad_producto * precio

#Calculo de descuentos
if cantidad_producto >= 10:
    descuento = (cantidad_producto * precio) * 0.20
    resultado = (cantidad_producto * precio) * 0.80
elif cantidad_producto >= 5:
    descuento = (cantidad_producto * precio) * 0.10
    resultado = (cantidad_producto * precio) * 0.90
else:
    resultado = cantidad_producto * precio

print('Tu subtotal es de:', round(valor_venta,2))
print('Tu descuento es de:', round(descuento,2))
print('Tu total es de:', round(resultado,2))
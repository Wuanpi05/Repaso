# num1 = int(input( " ingrese el numero uno "));
# num2 = int(input(" ingrese otro numero "));
# suma = (num1 + num2);
# print ("la suma es: " , suma)

# FechaNacimiento = int(input ( " ingrese su fecha de nacimiento "));
# FechaNacimiento = ( 2026 - FechaNacimiento );
# print ( " tu edad es: " , FechaNacimiento);

# num1 = int ( input ( " ingresa un numero "));
# if num1 >= 0 : 
#     print ( " su numero es positivo ");
# else:
#     print ( " el numero es negativo ");

# num1 = int ( input ( " digite un numero ") );
# num2 = int ( input ( " digite otro numero ") );
# divison = ( num1 / num2 );
# print ( " la division es ; " , divison );

# for num in range(10, 0, -1):
#   print ( num )
# print ( "despegue");

# contraseña = "juan0123"
# usuario = input ( " escriba su contraseña: ")
# if usuario == contraseña:
#     print( " acceso permitido ")
# else: 
#     print ( " contraseña incorrecta ")

# nota1 = float ( input ( " escriba su primera nota  ") )
# nota2 = float ( input ( " escriba su segunda nota ") )
# nota3 = float ( input ( " escriba su tercera nota " ) )
# promedio = ( nota1 + nota2 + nota3) / 3 
# print ( " Promedio: " , promedio )

# numero_secreto = 7 
# numero = int ( input( " Adivina el numero " ) )
# if numero == numero_secreto:
#     print ( " ganaste " ) 
# else: 
#     print ( " perdiste " )

# numero = int ( input ( " escriba un numero " ) )
# if numero > 0:
#     print ( " es positivo " )
# elif numero < 0:
#     print ( " es negativo " )
# else:
#     print ( " es cero " ) 

# nombre = input ( " Nombre del estudiante " )
# nota1 = float ( input( " escriba la pirmera nota "))
# nota2 = float ( input ( " escriba su segunda nota "))
# nota3 = float ( input ( " escriba su tercera nota "))
# promedio = ( nota1 + nota2 + nota3 ) / 3
# print ( " \n- - - RESULTADOS - - - " )
# print ( " estudiante " , nombre )
# print ( " promedio " , promedio )
# if promedio >= 3:
#     print ( " estado: APROBO" )
# else:
#     print ( " estado: REPROBO " )

# saldo = 10000
# print ( " Bienvenido al cajero " )
# print ( " Tu saldo es " , saldo )
# retirar = int ( input( " Cuanto dinero quieres retirar? "))
# if retirar <= saldo:
#     saldo = saldo - retirar 
#     print ( " retiro exitoso " )
#     print ( " nuevo saldo " , saldo)
# else: 
#     print ( " fondos insuficientes " )

# print ( " === CALCULADORA === " )

# print ( " 1. suma ")
# print ( " 2. resta ")
# print ( " 3. multipiclar ")
# print ( " 4. dividir ")
 
# opcion = input ( " escoge una opcion " )

# num1 = float ( input ( " Primer numero " ) )
# num2 = float ( input ( " segundo numero " ) )

# if opcion == " 1 ":
#     resultado = num1 + num2 
#     print ( " Resultado " , resultado )

# elif opcion == " 2 ":
#     resultado = num1 - num2 
#     print ( " Resultado " , resultado )

# elif opcion == " 3 ":
#     resultado = num1 * num2 
#     print ( " Resultado " , resultado )

# elif opcion == " 4 ":
#     resultado = num1 / num2 
#     print ( " Resultado " , resultado )

# else: 
#     print ( " Opcion invalida " )

# usuario_correcto =  "juan"
# contraseña_correcta =  "123"

# usuario = input ( " Usuario: " )
# contraseña = input ( " Contraseña: " )

# if usuario == usuario_correcto and contraseña == contraseña_correcta :
#     print ( " Bienvenido " , usuario )
# else: 
#     print ( " Datos incorrectos " )

# print ( " === TIENDA === " )

# producto = input ( " Nombre del producto " )
# precio = float ( input ( " Precio del producto " ) )
# cantidad = int ( input ( " Cantidad: " ) )

# total = precio * cantidad 

# print ( "\n --- FACTURA ---" )
# print ( " Producto: " , producto )
# print ( " Cantidad: " , cantidad ) 
# print ( " Total a pagar: " , total )

numero_secreto = 8 
intentos = 3 

# while intentos > 0: 

#     numero = int ( input ( " Adivina el numero: " ) )

#     if numero == numero_secreto:
#         print ( " Ganaste " )
#         break
#     else:
#         intentos = intentos - 1
#         print ( " Incorrecto " )
#         print ( " Intentos restantes: " , intentos )

#     if intentos == 0:
#         print ( " Perdiste " )

# pesos = float ( input ( " Pesos colombianos " ) )

# dolar = 4100
# euro = 4500

# usd = pesos / dolar
# eur = pesos / euro

# print ( " Dolares: " , usd )
# print ( " Euros: " , eur )

# precio = float ( input ( " Precio del producto " ) )

# if precio >= 100000:

#     descuento = precio * 0.10
#     total = precio - descuento

#     print ( " Tienes descuento " )
#     print ( " Descuento: " , descuento )
#     print ( " Total a pagar: " )

# else: 
#     print ( " No tienes descuento " )
#     print ( " Toltal: " , precio )

# def saludar ( nombre ):
    
#     print ( " Hola",nombre )

# saludar ( "Juan " )
# saludar ( "Carlos " )


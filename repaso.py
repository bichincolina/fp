# print ("por favor ingrese su nombre ")
# nombre_usuario=input()
# print ("por favor ingrese su apellido")
# apellido=input()

# print("ingrese un numero")
# num=int(input())
# print("por favor, ingrese otro numero:")
# num2=int(input())
# print("por favor, ingrese otro numero:")
# num3=int(input())

# if num>num2 and num>num3:
#     print("el "+ str(num)+" es mayor que todos" )
# elif num2>num3:
#     print("el "+ str(num2)+" es mayor que todos ")
# else:
#     print("el"+str(num3)+" es mayor que todos")

# num=7

# if num!=0:
#     print("el numero es distinto a 0")
# else:
#     print ("el numero es igual a 0")


# print("por favor ingrese su numero de ticket")
# numero_ticket=int(input())





def validar_ticket(precio, ubicacion):
    if precio >= 100 and precio <= 750:
        if ubicacion() == "galeria":
            return "El ticket es válido y es para la galería."
        elif ubicacion() == "cancha":
            return "El ticket es válido pero es para la cancha."
        else:
            return "Ubicación no válida. Por favor ingrese 'cancha' o 'galeria'."
    else:
        return "El precio del ticket está fuera del rango válido (100-750 pesos)."

#Ejemplo de uso
precio_ticket = 500
ubicacion_ticket = "galeria"
resultado = validar_ticket(precio_ticket, ubicacion_ticket)
print(resultado)










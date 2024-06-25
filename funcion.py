# # Solicitar al usuario que ingrese su nombre
# nombre = input("Por favor, ingresa tu nombre: ")

# # Imprimir un saludo personalizado
# print("Hola,", nombre, "! Bienvenido a Python.")

# print("ingrese el area del circulo")
# pi=3,14
# num1=int(input())
# def calculaareacirc(num):
#     area=(num*num)*3.14
#     return area

# print("ingrese el numero")
# radio=int(input())
# print(calculaareacirc(radio))


# def calcularperimetrocuadrado():
#     perimetro=num*4
#     return perimetro

# #      0   1 2  3 4  5
# lista=[41,73,4,55,77,89]
# lista.append("paola tiene"+str(lista(5))+"años") #indice 6
# lista.append(True) #indice 7 
# if lista[7]:
#     lista.append(2.6) #indice 8
# for elemento in lista:  
#     print(elemento)


  #    0   1 2  3 4  5
# lista=[41,73,4,55,77,89]
#      -6 -5 -4 -3 -2 -1
##lista.insert(3,"vicente")
##lista.append("jesenia")

# lista.remove(55)
# lista.sort()
# lista.reverse()
# for elemento in lista:  
#     print(elemento)

# matriz_sencila=[[1,2,3][4,5,6]]
# array=         [    1     2     ]
# print(matriz_sencila[0][1])
# for elemento in matriz_sencila:  
#     print(elemento)


# lista_nombre=[num1=input(),num2=input(),num3=input()]

# nombre=input()
# nombre2=input()
# nombre3=input()
# lista=[nombre,nombre2,nombre3]

# for nom in lista:
#       print(len(nom))
      
#       print("el nombre con mayor caracteres es:", nom)


# import random
# bingo=[]

# for j in range(6):
#     num=random.randint(1,99)
#     bingo.append(num)
#     print(num)
# import random 
# # num1=random
# # num2=random
# # num3=random

# lista=["benja","vicente","david"] 
# edades=[]
# for j in range(len(lista)):
#   num=random.randint(1,99)
#   edades.append(num)
#   print(lista[0],edades)

# for e in range(len(lista)):
#   print("su nombres es", lista(e),"y su edad es", str(edades(j)))

# for i in range(3):
#         num=random.randint(1,100)
#         print(lista,num)
#         print(num)

# ingresa="si"
# nombres=[]
# while ingresa!="no":
#     nom=input("ingrese un nombre nuevo")
#     nombres.append(nom)
#     print("desea agregar otro nombre=")
#     respt=input()
#     if respt.lower()=="no":
#         break
# print(min(nombres,key=len))
# nombres.remove(min(nombres,key=len))
# print(nombres)


# def funcion_sencilla():
#     print("hol, soy una funcion sencilla.")

# funcion_sencilla()

# def muetraporpantalla(palabra):
#     print(palabra)

# palabra=input()
# muetraporpantalla(palabra)    


#value error


    # try:
    # numero=float(input(numero_entrada))
    # return numero 
    # except ValueError:



# def rec_lista(lista):
#     rec_lista[1,2,3]
#     print ("la lista es", rec_lista)

# rec_lista()


# def separar_numeros_pares_impares(lista):
#     pares = [i for i in lista if i % 2 == 0]
#     impares = [i for i in lista if i % 2 != 0]
#     return pares, impares

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
# pares, impares = separar_numeros_pares_impares(numeros)
# print("Números pares:", pares)
# print("Números impares:", impares)
  





# def buscar_valor_en_diccionario(dicc, clave):
#     if clave in dicc:
#         return dicc[clave]
#     else:
#         return None

# # Ejemplo de uso
# mi_diccionario = {
#     "nombre": "Juan",
#     "edad": 30,
#     "ciudad": "Madrid"
# }

# valor_buscado = "nombre"
# resultado = buscar_valor_en_diccionario(mi_diccionario, valor_buscado)
# print(f"El valor de la clave '{valor_buscado}' es: {resultado}")

# valor_buscado = "telefono"
# resultado = buscar_valor_en_diccionario(mi_diccionario, valor_buscado)
# print(f"El valor de la clave '{valor_buscado}' es: {resultado}")




# def buscar_valor(diccionario,key):
#     if key in diccionario:
#         return diccionario(key)
#     else:
#         return f"la clave'{key}'no existe en el diccionario."
# mi_diccionario={'a':1,'b':2,'c':3}
# clave_buscada=str(input("ingrese numero indice:"))
# resultado=buscar_valor(mi_diccionario,clave_buscada)
# print(resultado)

from funCalculadora import*

sumar(9,9)
restar(9,9)
multiplicar(9,9)
dividir(9,9)

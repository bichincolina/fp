# mi_tupla=[1, "dos",3]
# mi_lista=(1,2,3)



# print(type())


# diccionario={"nombre":"cesar huispe",
#              "fonos":[
#                  9898174919,
#                  8913749814,
#                  5786753734],
#                  "email":"email@example.com",
#                  "activo":True}
# print(diccionario)
# for h in diccionario:
#     valor=diccionario[h]
#     print(h, valor)
# print(diccionario["email"])

# # conjunto={3,1,4,1,5,2,4}
# # conj={"milo","saga","shura","aldebaran","saga","aldebaran","shaka"}
# # lista=[3,1,4,1,5,2,4]

# # print("conjunto")
# # print(conjunto)
# # print("lista")
# # print(lista)

# yari=input("que valor desea?")
# print(diccionario[yari].lower())

# divisas={"euro":"€","dolar":"$", "yen":"¥"}



# lista_productos={
#     "frutas":{
#         "uvas":1800, "manzana":2100
#         }, 
#         "verduras":{
#             "apio":900, "lechuga":1300
#         },
#         "cereales":{
#             "chocapic":4800, "zucaritas":5200
#         },
#         "carnes":{
#             "puerco":8990, "vacuno":13000
#         },
#         "snacks":{
#             "papas fritas":2000, "doritos":1990
#         }
#     }

# print(lista_productos["cereales"]["zucaritas"])

# print("zucaritas",lista_productos["cereales"]["zucaritas"])


# for key  in lista_productos:
#     print(key, ",", lista_productos[key])
#     for ll in lista_productos[key]:
#         print(ll,":", lista_productos[key][ll])


# lista=[1,2,3]
# lista.append(9)
# lista.append(19)

# while True:
#     op=int(input())
#     match op:
#         case 1:
#             for g in lista:
#                 print(g) 



# frutas={
#     'uvas': 1800, 'manzana':2100

# }
# frutas["sandias"]=5490
# frutas["pera"]=1800
# frutas["frutilla"]=2000

# print(frutas)



# from isreal_solu import busca_valor

# def creadiccionario():
#     dic_vacio={}
#     while True:
#         key=input("ingrese una key")
#         if key=="shazam":
#             print(dic_vacio)
#             break
#         else:
#             value=input("ingrese el valor de la key anterior")
#             dic_vacio[f"{key}"]=value
#     preg=input("ingrese la key a buscar") 
#     print(busca_valor(dic_vacio,preg))       

# creadiccionario()


# avion = [
#     [[], [], [], [], [], [], ],#1 0
#     [[], [], [], [], [], [], ],#2 1
#     [[], [], [], [], [], [], ],#3 2
#     [[], [], [], [], [], [], ],#4 3
#     [[], [], [], [], [], [], ],#5 4
#     [[], [], [], [], [], [], ],#6 5
#     [[], [], [], [], [], [], ],#7 6
#     [[], [], [], [], [], [], ],#8 7
#     [[], [], [], [], [], [], ],#9 8
#     [[], [], [], [], [], [], ],#10 9
#     [[], [], [], [], [], [], ],#11 10
#     [[], [], [], [], [], [], ],#12 11
#     [[], [], [], [], [], [], ],#13 12
#     [[], [], [], [], [], [], ],#14 13
#     [[], [], [], [], [], [], ],#15 14
#     [[], [], [], [], [], [], ],#16 15
# ]
# while True:
#     print("En que piso se va  alaojar?")
#     piso=int(input())
#     print("En que habitacion se va  alaojar?")
#     hab=int(input())
#     if avion[piso-1][hab-1]:
#         print("la habitacion esta usada\n")
#     else:
#         pasa=input("Ingrese el nombre del pasajero")
#         avion[piso-1][hab-1]={"nombre": pasa}
    
    
    
#     for i in avion:
#         print(i)

# from datetime import datetime
# import datetime

# parking= [
#     [[], [], [], [], [], [],[], [], [], [], [], [],[], [], [], [], [], [],[],[]],#1 0
#     [[], [], [], [], [], [],[], [], [], [], [], [],[], [], [], [], [], [],[],[]],#2 1
#     [[], [], [], [], [], [],[], [], [], [], [], [],[], [], [], [], [], [],[],[]],#3 2
#     [[], [], [], [], [], [],[], [], [], [], [], [],[], [], [], [], [], [],[],[]],#4 3
#     [[], [], [], [], [], [],[], [], [], [], [], [],[], [], [], [], [], [],[],[]],#5 4
#     [[], [], [], [], [], [],[], [], [], [], [], [],[], [], [], [], [], [],[],[]],#6 5
# ]

# entra=datetime.datetime.now()

# fue=datetime.datetime(2024, 6, 27, 19, 00)
# minutos=entra-fue
# # print(minutos.strftime("%H:%M"))
# print(minutos)

# entra=datetime.now()
# parking[2][2]={"placa":"cvvk29","fecga": entra}
# diferencia= datetime.now() - parking[0][0]["fecha"]
# print(diferencia)

# print(parking[2][2]["fecha"].strftime("%H:%M"))

# def calcula_tiempo(piso,sitio,placa):
#     diferencia=datetime.now() - parking[piso-1][sitio-1]["fecha"]
#     return diferencia
# def ingresa(piso,sitio,placa):
#     entra=datetime.now
#     parking[piso-1][sitio-1]={"placa":placa, "fecha": entra }




# import datetime

# class Espacio:
#     def __init__(self):
#         self.ocupado = False
#         self.patente = None
#         self.hora_llegada = None

# class Estacionamiento:
#     def __init__(self, pisos, espacios_por_piso):
#         self.pisos = pisos
#         self.espacios_por_piso = espacios_por_piso
#         self.espacios = [[Espacio() for _ in range(espacios_por_piso)] for _ in range(pisos)]

#     def ingresar_vehiculo(self):
#         patente = input("Ingrese la patente del vehículo: ")
#         for piso in self.espacios:
#             for espacio in piso:
#                 if not espacio.ocupado:
#                     espacio.ocupado = True
#                     espacio.patente = patente
#                     espacio.hora_llegada = datetime.datetime.now()
#                     print(f"Vehículo con patente {patente} ingresó al estacionamiento.")
#                     return
#         print("No hay espacios disponibles.")

#     def salir_vehiculo(self):
#         patente = input("Ingrese la patente del vehículo que sale: ")
#         for piso in self.espacios:
#             for espacio in piso:
#                 if espacio.ocupado and espacio.patente == patente:
#                     hora_salida = datetime.datetime.now()
#                     tiempo_estadia = (hora_salida - espacio.hora_llegada).total_seconds() // 60
#                     costo_total = tiempo_estadia * 15
#                     print(f"Vehículo con patente {patente} salió del estacionamiento.")
#                     print(f"Tiempo de estadía: {int(tiempo_estadia)} minutos")
#                     print(f"Costo total: {costo_total} pesos")
#                     self.generar_boleta(patente, espacio.hora_llegada, hora_salida, costo_total)
#                     espacio.ocupado = False
#                     espacio.patente = None
#                     espacio.hora_llegada = None
#                     return
#         print(f"No se encontró el vehículo con patente {patente}.")

#     def generar_boleta(self, patente, hora_llegada, hora_salida, costo_total):
#         with open(f"{patente}.txt", "w") as archivo:
#             archivo.write(f"Hora de llegada: {hora_llegada.strftime('%Y-%m-%d %H:%M:%S')}\n")
#             archivo.write(f"Hora de salida: {hora_salida.strftime('%Y-%m-%d %H:%M:%S')}\n")
#             archivo.write(f"Patente: {patente}\n")
#             archivo.write(f"Costo total: {costo_total} pesos\n")

# # # Ejemplo de uso
# estacionamiento = Estacionamiento(5, 30)
# estacionamiento.ingresar_vehiculo()
# estacionamiento.ingresar_vehiculo()
# estacionamiento.salir_vehiculo()

# import datetime

# class Espacio:
#     def __init__(self):
#         self.ocupado = False
#         self.patente = None
#         self.hora_llegada = None

# class Estacionamiento:
#     def __init__(self, pisos, espacios_por_piso):
#         self.pisos = pisos
#         self.espacios_por_piso = espacios_por_piso
#         self.espacios = [[Espacio() for _ in range(espacios_por_piso)] for _ in range(pisos)]

#     def ingresar_vehiculo(self):
#         patente = input("Ingrese la patente del vehículo: ")
#         for piso in self.espacios:
#             for espacio in piso:
#                 if not espacio.ocupado:
#                     espacio.ocupado = True
#                     espacio.patente = patente
#                     espacio.hora_llegada = datetime.datetime.now()
#                     print(f"Vehículo con patente {patente} ingresó al estacionamiento.")
#                     return
#         print("No hay espacios disponibles.")

#     def salir_vehiculo(self):
#         salir = input("¿Desea sacar un vehículo? (s/n): ")
#         if salir.lower() == "s":
#             patente = input("Ingrese la patente del vehículo que sale: ")
#             for piso in self.espacios:
#                 for espacio in piso:
#                     if espacio.ocupado and espacio.patente == patente:
#                         hora_salida = datetime.datetime.now()
#                         tiempo_estadia = (hora_salida - espacio.hora_llegada).total_seconds() // 60
#                         costo_total = tiempo_estadia * 15
#                         print(f"Vehículo con patente {patente} salió del estacionamiento.")
#                         print(f"Tiempo de estadía: {int(tiempo_estadia)} minutos")
#                         print(f"Costo total: {costo_total} pesos")
#                         self.generar_boleta(patente, espacio.hora_llegada, hora_salida, costo_total)
#                         espacio.ocupado = False
#                         espacio.patente = None
#                         espacio.hora_llegada = None
#                         return
#             print(f"No se encontró el vehículo con patente {patente}.")
#         else:
#             print("Saliendo del estacionamiento.")

#     def generar_boleta(self, patente, hora_llegada, hora_salida, costo_total):
#         with open(f"{patente}.txt", "w") as archivo:
#             archivo.write(f"Hora de llegada: {hora_llegada.strftime('%Y-%m-%d %H:%M:%S')}\n")
#             archivo.write(f"Hora de salida: {hora_salida.strftime('%Y-%m-%d %H:%M:%S')}\n")
#             archivo.write(f"Patente: {patente}\n")
#             archivo.write(f"Costo total: {costo_total} pesos\n")

# # Ejemplo de uso
# estacionamiento = Estacionamiento(5, 30)
# estacionamiento.ingresar_vehiculo()
# estacionamiento.salir_vehiculo()




# from datetime import datetime
# parking=[
#     [[],[],[],[],[],[],[],[],[],[],[],[],[],
#     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], #piso 1
#     [[],[],[],[],[],[],[],[],[],[],[],[],[],
#     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], #piso 2
#     [[],[],[],[],[],[],[],[],[],[],[],[],[],
#     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], #piso 3
# ]
# entra=datetime.now()
# parking[0][0]={"placa":"placa", "fecha": entra}

# print(parking[0][0]["fecha"].strftime("%H:%M"))

# def calcula_tiempo(piso, sitio, placa):
#     diferencia = datetime.now() - parking[piso-1][sitio-1]["fecha"]
#     return diferencia
# def ingresa(piso, sitio, placa):
#     entra=datetime.now()
#     parking[piso-1][sitio-1]={"placa":placa, "fecha": entra}


# while True:
#     print("Bienvenido ")
#     print("""
#  //Que desea hacer?//
#     1)Ingresar un vehiculo
#     2)Verificar el tiempo de un vehiculo
#     3)Cobrar servicio
#     4)Guardar en un Archivo
#     5)Salir
#     """)
#     op=int(input("SELECCIONE UNA OPCION\n"))
#     match op:
#         case 1:
#             piso=int(input("Ingrese un piso\n"))
#             piso=int(input("Ingrese un piso\n"))



# hotel = [
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
#     [[], [], [], [], [], [], ],
# ]
# while True:
#     print("Bienvenido al hotel duocuc")
#     print("""
#  // ¿Qué desea hacer? //
# 1. Reservar una habitación.
# 2. Check out de una habitación.
# 3. Ver todas las habitaciones.
# 4. Guardar en un archivo
# 5. Salir.
#     """)
#     op = int(input("Seleccione una opción: "))
#     match op:
#         case 1:
#             print("En que piso se va  alaojar?")
#             piso=int(input())
#             while piso<1 or piso>10:
#                 print("Opcion invalida")
#                 print("En que piso se va  alaojar?")
#                 piso=int(input())


#             print("En que habitacion se va  alaojar?")
#             hab=int(input())
#             while hab<0 or hab>5:
#                 print("Opcion invalida")
#                 print("En que habitacion se va  alaojar?")
#                 hab=int(input())
#             if hotel[piso-1][hab-1]:
#                 print("La habitacion está usada")
#             else:
#                 nom=input("Ingrese un nombre\n")
#                 hotel[piso-1][hab-1]={"nombre":nom}
#         case 2:
#             print("Que piso va a actualizar?")
#             piso=int(input())
#             print("Que habitacion va a actualizar?")
#             hab=int(input())
#             hotel[piso-1][hab-1]=[]

#         case 3:
#                 for i in hotel:
#                     print(i)
#         case 4:
#             f = open("outfile.txt","w")
#             for piso in hotel:
#                 for hab in piso:
#                     f.write(str(hab))
#                 f.write('\n')
#             f.close()
#         case 5:
#               break
#         case _:
#               print("Opcion invalida")



#lista
lista= [29,True, 3.1415,"el numero de avogadro si que mola "]
#cambiar elementos de la funcion

lista[2]= [3,2,1]

print(lista)
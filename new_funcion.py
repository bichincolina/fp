# def area_circulo (radio):
#     return 3.14*radio*radio

# def volumen_cilindro(radio,alt):
#     return area_circulo(radio)*alt


# print("ingrese el valor de radio")
# int(input())
# print("ingrese el valor de altura")
# int(input())

# print(area_circulo)



# def area_cuadrado (lado):
#     return lado*lado

# def area_cuadrado(alt):
#     return area_cuadrado(lado)*alt


# print("ingrese el valor de radio")
# int(input())
# print("ingrese el valor de altura")
# int(input())

# print(area_cuadrado)



# def cuadrados(lista):
#     hook=[]
#     cont=0
#     for i in lista:
#         hook.append(i*i)
#     with open (f'cuadrados.text','w') as file:
#             for num in hook:
#                  cont=cont+1
#                  file.write(f"{cont} {num} ")   
#     return hook
# oo=[2,6,4,5,8,14,3]
# print(cuadrados(oo))



# import csv 
# from datetime import datetime
# bitacora=[]
# def agregar_evento(evento):
#     fecha_hora_actual = datatime.now().strftime("%D-%M-%Y %H:%M:%S")
#     fecha_evento =f"{fecha_hora_actual} - {evento}"
#     bitacora.append(fecha_evento)
#     print(f"evento '{evento}' registrado en la bitacora del auto")
#     return(f"evento '{fecha_evento}'registrado en la bitacora del auto.")

# evento="viaje a la cancha"


# with open ("bitacora.txt",mode='a', newline='') as escri: 
#     escri.write()

# print(agregar_evento())

# print("el hotel tiene 10 pisos y cada piso tiene 6 habitaciones")

# hotel = [
#     [False, False, False, False, False, False],  #1
#     [False, False, False, False, False, False],  #2
#     [False, False, False, False, False, False],  #3
#     [False, False, False, False, False, False],  #4
#     [False, False, False, False, False, False],  #5
#     [False, False, False, False, False, False],  #6
#     [False, False, False, False, False, False],  #7
#     [False, False, False, False, False, False],  #8
#     [False, False, False, False, False, False],  #9
#     [False, False, False, False, False, False]   #10
# ]
# def registrar_pasajero(piso, habitacion):
#     if hotel[piso][habitacion] == False:
#         hotel[piso][habitacion] = True
#         print(f"Pasajero registrado en la habitación {piso+1}-{habitacion+1}")
#     else:
#         print(f"La habitación {piso+1}-{habitacion+1} ya está ocupada")
# def generar_reporte():
#     ocupadas = 0
#     for piso in hotel:
#         for habitacion in piso:
#             if habitacion:
#                 ocupadas += ocupadas+1
#     print(f"Reporte de habitaciones ocupadas: {ocupadas} de 60 habitaciones")
#     return ocupadas
# def guardar_reporte(ocupadas):
#     with open("reporte_habitaciones.txt", "w") as archivo:
#         archivo.write(f"Reporte de habitaciones ocupadas: {ocupadas} de 60 habitaciones")
#     print("Reporte guardado en 'reporte_habitaciones.txt'")

# registrar_pasajero(0, 2)
# registrar_pasajero(3, 4)
# registrar_pasajero(7, 1)
# ocupadas = generar_reporte()
# guardar_reporte(ocupadas)



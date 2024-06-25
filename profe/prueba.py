# import csv
# datos = """Este es un archivo de texto simple que no tiene 
# ningún formato en particular, lo podemos utilizar
# para guardar todo tipo de texto. 
# """
# with open('archivo_vicente.csv', 'w') as archivo_csv:
#     escritor_csv= csv.writer (archivo_csv)

#     # Escribir una fila en el archivo CSV
#     escritor_csv.writerow(['Nombre', 'Edad', 'Comuna'])
    
#     # Escribir múltiples filas en el archivo CSV
#     escritor_csv.writerows([
#         ['Esteban', 25, 'Santiago'],
#         ['María', 30, 'Valparaíso'],
#         ['Carlos', 22, 'Osorno'],
#         ['Sigrid', 25, 'Santiago'],
#         ['Daniela', 30, 'La Cisterna'],
#         ['Aylen', 22, 'La florida']
#     ])

# import csv
# # Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# # Modo común: 'r' (lectura)
# with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
#     lector_csv = csv.reader(archivo_csv)
    
#     for fila in lector_csv:
#         print(fila)

from datetime import datatime
now=datatime.now()
import random
tiempo=now.strftime("%Y%M%D_$H%M%S")
bingo=[]
for i in range (6):
    bingo.append(random.randint(1,99))
num=1
lista="los numeros del bingo son", str(bingo)

with open ("lista_vicente.txt(tiempo)",'w') as archivo:
    archivo.write(print(lista))
    
    
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



from isreal_solu import busca_valor

def creadiccionario():
    dic_vacio={}
    while True:
        key=input("ingrese una key")
        if key=="shazam":
            print(dic_vacio)
            break
        else:
            value=input("ingrese el valor de la key anterior")
            dic_vacio[f"{key}"]=value
    preg=input("ingrese la key a buscar") 
    print(busca_valor(dic_vacio,preg))       

creadiccionario()
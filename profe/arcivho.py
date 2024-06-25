with open('datos.txt','r') as archivo:
    contenido= archivo.read()
print(contenido)

num=int(input())
for i in range(1,11):
    archivo.write(str(num), "x",str(i) , "=",str(num*i)),'\n'
# print(num, "x", i , "=",num*i)



n=int(input('introducde un numero entero entre 1 y 10:  '))
nombre_fichero='tabla-'+ str(n) +'text'
with open(nombre_fichero,'w') as f:
    for i in range (1,11):
        f.write(str(n)+'x'+str(i),+'='+str(n*1)+'\n')


n=int(input('introduce un numero entero:'))
n2=int(input('introduce un numero entero:'))
nombre_fichero='tabla-'+ str (n)+'+str(n2)+''txt'
with open(nombre_fichero,'w') as f:
    f.write(str(n)+'+'+str(n2)+'='+str(n+n2))

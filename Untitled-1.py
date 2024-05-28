
def multiPorDos():

    print("Ingrese un numero")
    num=int(input())
    print(num*2)

def resta5():
    print("Ingrese un numero")
    num=int(input())
    print(num-5)

def validaFolio():
    ticket_valido=False
    folio_valido=123
    print("Ingrese el numero de folio")
    n_folio=int(input())

    if n_folio==folio_valido:
        ticket_valido=True

def suma(num1, num2):
    resul=num1+num2
    return resul
def resta(num1, num2):
    resul=num1-num2
    return resul
def multi(num1, num2):
    resul=num1*num2
    return resul
def divi(num1, num2):
    resul=num1/num2
    return resul 
def perimetrocuadrado(num1):
    result=num1*4
    return result
def calculaareacirc(num):
    area=(num*num)*3.14
    return area
def pi_valor(num):
    result=(num*3.14)
    return result

    

while True:
    print("Seleccione una opcion")
    print("1.- -Suma")
    print("2.- -Resta")
    print("3.- -Multiplicacion")
    print("4.- -Division")
    print("5.- -perimetro del cuadrado")
    print("6.- -area del cirlculo")
    print("7.- -salir")
    op=int(input())

    match op:
        case 1:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",suma(num1,num2))
        case 2:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",resta(num1,num2))
        case 3:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",multi(num1,num2))
        case 4:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",divi(num1,num2))
        case 5:
            print("Ingrese un numeros")
            num1=int(input())
            print("Su resultado es ",perimetrocuadrado(num1))
        case 6:
            print("Ingrese un numeros")
            num1=int(input())
            print("Su resultado es ",calculaareacirc(num1))
            
        case 7: 
            print("Ingrese un numeros")
            num=int(input())
            print("Su resultado es ",pi_valor(num))
    


        






            





            
            


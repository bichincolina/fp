def suma_(num1,num2):
    result=(num1+num2)
    print("el resultado de su suma es:", result)
def resta_(num1,num2):
    result=(num1-num2)
    print("el resultado de su resta es:", result)
def multiplacion_(num1,num2):
    result=(num1*num2)
    print("el resultado de la multiplicacion", result)
def division(num1,num2):
    result=(num1/num2)
    print("el resultado de la division es", result )


while suma_:
    print("n°1 suma")
    print("n°2 resta")
    print("n°3 multiplicacion")
    print("n°4 division")
    op=int(input())



    match op:
        case 1:
            print("ingrese los numeros ")
            num1=int(input())
            num2=int(input())
            print("la suma es ",suma_(num1,num2))
        case 2:
            print("ingrese los numeros ")
            num1=int(input())
            num2=int(input())
            print("el resultado de su resta es:",resta_(num1,num2))
        case 3:
            print("ingrese los numeros ")
            num1=int(input())
            num2=int(input())
            print("el resultado de la multiplicacion es:", multiplacion_(num1,num2))
        case 4:
            print("ingrese numeros")
            num1=int(input())
            num2=int(input())
            print("el resultado de su divisio es", division(num1,num2))



        



    


    
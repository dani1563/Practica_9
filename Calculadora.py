"""
 ------COMENTARIOS---------
#vamos a hacer la funcion 
#los espacios y tabuladores son muy importantes
#debemos seguir la dependencia de funciones

def es para definir la funcion
sumar,restar, etc los nombres de nuestras funciones 
y los dos puntos es como abrir llaves 
(a,b) los argumentos de nuestra funcion

 el switch no existe en python, tampoco el do while
    var = True
    var = False
variables booleanas de forma natiava
            # && || < > >= <= !=
            # and or
----------------------------
"""
def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a - b
     

def multiplicar(a,b):
    c = a * b
    return c

def div_entera(a,b):
    if b == 0:
        print("error división sobre cero")
        return
    c = a//b
    return c

def division(a,b):
    if b == 0:
        print("error división sobre cero")
        return
    return a/b

def modulo(a,b):
    if b == 0:
        print("error división sobre cero")
        return
    c = a%b
    return c

def potencia(a,b):
    return a**b

while True:
    print("\n Selecciona la opcion que deseas ocupar\n")
    print(" 1.sumar\n 2.restar\n 3.división entera\n 4.división")
    print(" 5.módulo\n 6.potencia\n 7.multiplicar\n 8.salir\n ")
    op = int(input())
    if op <= 7 :
        print("Ingresa dos valores\n")
        x = int(input())
        y = int(input())
        if op == 1:
            print(" Tu resultado es = ", sumar(x,y))
        elif op == 2:
            print(" Tu resultado es = ", restar(x,y))
        elif op == 3:
            print(" Tu resultado es = ", div_entera(x,y))
        elif op == 4:
            print(" Tu resultado es = ", division(x,y))
        elif op == 5:
            print(" Tu resultado es = ", modulo(x,y))
        elif op == 6:
            print(" Tu resultado es = ", potencia(x,y))
        elif op == 7:
            print(" Tu resultado es = ", multiplicar(x,y))
    elif op == 8 :
        print("Saliste\n")
        break
    else:
        print("OPCION NO VALIDA\n INGRESA UNA OPCION NUEVAMENTE")

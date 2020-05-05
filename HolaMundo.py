#este es un comentario de una linea

"""
Esto es un comentario de varias
lineas
"""

print("HOLA MUNDO")

"""
las variables en python no se declaran
aqui solamente le asignamos a x un valor
"""
x = 10  # no utilizamos el punto y coma
print(type(x)) #imprime el tipo
print(x)
x = y = z = 2.3
print( x, y, z)
print(type(x)) #puede cambiar el tipo
x = "cadena"
print(x)
print(type(x))

#concatedamos cadenas, unirlas
#aparentemente las sumamos, pero solo unimos
c1 = "Hola"
c2= "Daniela"
saludo = c1+ " "+c2
print(saludo)

#las llaves representan que las llaves se van a sustituir
#por un valor
saludo2 = "{} {} {}".format(c1, c2, 3)
print(saludo2)

saludo3 = "Cambio de orden {1} {2} {0}". format(c1, c2, 3)
print(saludo3)



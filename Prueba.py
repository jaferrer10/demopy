#Funciones

temperatura=4
def miFuncion(nombre):
     print(f"Hola como estás, {nombre}")
     for i in range(1, 11):
          print(i)
          print("Temperatura: ", temperatura)

def suma(a=1,b=0,c=0):
     print(f"El resultado de la suma es: {a+b+c}")
     print("Primer parametro: ",a)
     print("Primer parametro: ",b)
     print("Primer parametro: ",c)
     
def sumaNumeros(*args):
     suma=0
     for i in args:
          suma += i
     print("Total", suma)


def miDiccionario(**kwargs):
     for key, value in kwargs.items():
          print(key,"=",value)


def operaciones (a,b):
     return a+b, a-b, a*b, a/b

miFuncion("Julian")

suma(a=10,b=10,c=1)

#envía a la función n cantidad de parametros
sumaNumeros(1,2,3,4,5,9,10,11,20,50)

miDiccionario(vivienda="piso",auto='rojo')


# funcion con multiples resultados
suma, resta, multi, divi = operaciones(20,10)
print('Función con multiples resultados')
print(suma)
print(resta)
print(multi)
print(divi)




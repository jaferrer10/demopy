
"""
palabras=['pato','carro','pelota','anillo']

for i in palabras:
     print(i)

 
print(f'La lista termina en la palabra {i}')

"""
num=1

while num <= 10:
     num += 1 
     if num % 2 == 0:
          print (f"El número {num} es par...")
          continue

print('Fin del bucle')

lista=['1','2','3','u','f']

for i in lista:
     print('Elemento ', i, 'de la lista...')
     
long=len(lista)
print('La lista tiene ', long, ' items....')
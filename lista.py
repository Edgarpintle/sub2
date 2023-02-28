lista01 = ['uvas','peras','Manzanas','Mangos']
print(lista01)
print(lista01[2])                 # Imprime el elemento de la lista 
for fruta in lista01:             # for donde el ciclo es fruta  en lista
    print(fruta)
hayfruta ="kiwi" in lista01       # Busca "x" en la lista
print(hayfruta)


lista01.append("kiwi")           # Agrega un elemento al final de la lista 
print(lista01)
print(len(lista01))
lista01.insert(0, "sandia")      # Agrega un elemento en la posicion de "x"
print(lista01)
lista01[2] = "Piña"              # Remplaza un elemento 2 por "X"
print(lista01)


lista01.remove("kiwi")           # Borra el elemento "x"
print(lista01)
lista01.pop()                    # Elimina el ultimo elemento de la lista 
print (lista01)
lista01.pop()
print(lista01)
lista01.sort()                   # Ordena los elementop de la lista 

lista02 = lista01.copy()         # Copia una estructura de otra
lista02.reverse()                #coloca los elementos de la lista inversa

print(lista01)
print(lista02)

lista01.clear()

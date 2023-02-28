# cadenas o string
nombre = "edgar"
paterno ="cirio"

#concatenar
NomCompleto=nombre+""+paterno
print(NomCompleto)

#concatenar con f-string
NomCompleto=f"{nombre}{paterno}"
print(NomCompleto)

#cadenas
miTexto="algo que voy a FROMATEAR con string"
print(miTexto.upper()) #MAYUSCULA
print(miTexto.lower()) #minuscula
print(miTexto.title()) #titulo

edad=17
NomCompleto=f"{nombre}{paterno}{edad}"
NomCompleto= nombre+""+paterno+""+str(edad)
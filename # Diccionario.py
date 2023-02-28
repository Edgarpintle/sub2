# Diccionario
# son estructuras de clave:Valor


persona = {
    'Daniel' : 'Daniel Pintle',
    'Edgar'  : 'Edgar cirio',
    'Kimberly' : 'Kimberly Reyes'
}

print(persona)
print(persona['Edgar'])

cuantaspersonas = len(persona)
print(cuantaspersonas)

print('Kimberly' in persona)

esta='karla'
print(persona.get(esta))


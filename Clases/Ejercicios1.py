# qué es una clase? - clase = molde , nota: las clases siempre deben ir en singular

curso = "Python" # esto es una calse tipo str
class Persona:
    pass

#Objeto
diego = Persona()

print(diego)
print(type(curso))

# Cree una clase llamada personaje y a continuación cree un objeto a 
# partir de ella,por ejemplo : harry potter
class Personaje:
    pass

harry_potter = Personaje()
print(harry_potter)

# cree una clase llamada Dinosaurio y tres instancias a partir de ella 
# velociraptor,tiranosaurio_rex y braquiosaurio.

class Dinosaurio:
    pass

# NOTA: instancia y objeto es lo mismo
velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()

print(f'1:{velociraptor}, 2: {tiranosaurio_rex}, 3: {braquiosaurio}')



# Cree una clase llamada platafromaStreaming y crea los siguientes objetos a partir de ella:
# netflix,hbo_max, amazon_prime_video

class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

print(netflix)
print(hbo_max)
print(amazon_prime_video)

# Elaborar un algoritmo que saque las notas del curso de python, el cual cuenta con tres cortes
# 1 corte es del 30%, 30%, 40%

#Ejemplo:
'''Diego marin (25% , 25%, 35%)
Kelly Rincon (26%, 26%, 34%)
Liam Marrin (26%, 26%, 38%)'''

class Estudiante:
    pass 

diego = Estudiante()
kelly = Estudiante()
liam = Estudiante()

print(diego)
print(kelly)
print(liam)


'''Los atributos son variables que pertenecen a la clase.Existen
atributos de clase (compartidos por todas las instancias de la clase)
y de instancia (que son distintos en cada instancia de la clase)'''

# Atributos -> caracteristicas del objeto

#Ejemplo
class Persona:
    
    # ATRIBUTOS
    nombre = ' '
    cedula = ' '
    color = ' '
    edad = ' '
    
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        
# Objeto 
diego = Persona('Diego', '10245854')
print(diego)

# Ejercicios:

'''1. Crea una clase llamada casa y asignale atributos: color , cantidad_pisos.
Crea una instancia de Casa, llamada casa_blanca de color "blanco" y cantidad de pisos
igual a 4.'''

class Casa:
    color = ''
    cantidad_pisos = 0 # en este caso dejo el cero , porque me refiero a un tipo de dato int
    def __init__(self,color, cantidad):
        self.color = color
        self.cantidad_pisos = cantidad
        
    
casa_blanca = Casa('Blanco', 4 )
print(casa_blanca)


# 2. Crear una clase llamada cubo y asignarle el atributo de clase:
#     caras = 6
#     y el atributo de instancia :
#         color
#    crea una instancia cubo_rojo, de dicho color. 

class Cubo:
    caras = 6
    color = ' '
    def __init__(self, color):
        self.color = color
        
cubo_rojo = Cubo('Rojo')
print(cubo_rojo)


'''3. Crea una clase llamada Personaje y asignale el siguiente atributo de clase:
real = False 
Crea una instancia llamada harry_potter con los siguientes atributos de instancia :
especie = "Humano"
magico = True
edad = 17'''

class Personaje:
    real = False
    especie = ''
    magico = ''
    edad = 0
    def __init__(self, e, m, age): # aqui dentro del metodo constructo no es necesario llamar las variables de forma igual al nombre de los atributos
        self.especie = e
        self.magico = m
        self.edad = age
        
harry_potter = ('Humano', True, 17)
print(harry_potter)


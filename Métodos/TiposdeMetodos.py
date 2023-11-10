class Persona:
    nombre = ""
    apellido = ""
    edad = 0
    
    def __init__(self, _nombre, _apellido,_edad):
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
    
    
    
    def saludar(self):
        print(f"Hola {self.nombre}")
        
#Se crea el objeto
liam = Persona('Daniel', 'Marin', 1)
liam.saludar()

#Ejercicio

'''class Person:
    def __init__(self, edad , nombre):
        self.edad =  edad
        self.name = nombre
        
    def cumplir_anios(self):
        self.edad +=1
        
'''
# ATRIBUTOS CON VALORES POR DEFECTO 

'''class Person:
    def __init__(self,edad, nombre):
        self.age = edad
        self.name = nombre
        
    def cumplir_anios(self):
        self.edad +=1'''
        
# Ejercicio1
'''En este ejemplo crearemos un nuevo tipo llamado NumeroComplejo. Este tipo tiene un 
atributo x para la coordenada en x e y para la coordenada en  y. Representa un numero complejo
de la forma (x,y)'''

# class NumeroComplejo:
#     def __init__(self, _x, _y):
#         self.x = _x
#         self.y = _y
        
# punto1 = NumeroComplejo(1,2)
# punto2 = NumeroComplejo(3,6)

#En este caso accederemos a x del punto1

# print(punto1.x)

#En este caso accederemos a y del punto2

# print(punto2.y)


#EJERCICIO2
'''Definir una clase llamada NumeroComplejo un método que permita imprimir una instancia de
la clase.Recordemos que al intentar imprimir u tipo definido por nosotros, se imprime la 
dirección de memoria'''

# class NumeroComplejo:
#     def __init__(self, _x, _y):
#         self.x = _x
#         self.y = _y
        
#     def imprimir(self):
#         print(f"Punto ({self.x},{self.y}) ")
        
#punto1 = NumeroComplejo(1,2)
#print(punto1) # este print nos imprime el espacio en memoria
#punto1.imprimir() #en este caso nos imprime el valor de los puntos

#EJERCICIO3 
'''En este ejemplo una función que compara dos números complejos, ya que si dos objetos
distintos tienen sus atributos iguales, no se  consideran iguales
'''
class NumeroComplejo:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        
    def comparar(self, objeto2):
        if self.x == objeto2.x and self.y == objeto2.y:
            print('Los oibjetos son iguales')
        else:
            print('Los objetos no son iguales')
            
punto1 = NumeroComplejo(4,6)
punto2 = NumeroComplejo(4,3)

punto1.comparar(punto2)
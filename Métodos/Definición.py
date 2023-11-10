'''Los métodos son funciones que pertenenecen al objeto'''
# Ejm:
class Persona:
    especie = "huamno"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        
    def saludar(self):
        print(f'Hola mi nombre es:{self.nombre}')
        
    def cumplir_anios(self,estado_humor):
        print(f'Cumplir {self.edad + 1} años me pone en estado de humor {estado_humor}')
        
        
#objetos
diego = Persona('diego', 28)
diego.saludar()
diego.cumplir_anios("feliz")

# EJERCICIOS
'''Crea una clase Perro. Dicho perro debe poder ladrar .
Crea el método ladrar() y ejecutalo en una instancia de perro
cada vez que ladre, debe mostrarse en pantalla "GUAU"'''

class Perro:
    nombre = ''
    def __init__(self,name):
        self.nombre = name
        
    def ladrar(self):
        print(f" El perro con el nombre {self.nombre} esta ladrando y hace GUAU!")
        
objeto = Perro('Sasha')
objeto.ladrar()

'''Crea una clase llamada Mago  y crea un metodo llamado lanzar_hechizo()
debera imprimir ¡Abracadabra!. Crea una instancia de mago en el objeto merlin
y haz lance un hechizo'''


class Mago:
    def __init__(self): #generalmente cuando utilizamos atributos, inicializamos el metodo constructor.
        pass
      
    def lanzar_hechizo(self):
        print("¡ABRACADABRA!")
          
merlin = Mago() 
merlin.lanzar_hechizo()

'''Crear una instancia de la clase Alarma que tenga un método llamado postergar(cantidad_minutos)
El metodo debe imprimir en pantalla el mensaje 
"La alarma ha sido pospuesta {cantidad_minutos} minutos"'''

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
         
alarma1 = Alarma()
alarma1.postergar(10)
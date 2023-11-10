# Herencia: nos permite heredar atributos: caracteristicas y métodos: comportamientos de una clase

# La  clase abstracta, me va a permitir inicializar los atributos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
      
# en este caso la clase empleado es hijo de persona
# y va a tener un nuevo atributo que en este caso se llama sueldo
       
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        
        # super es un método de herencia
        super().__init__(nombre, edad)
        self.sueldo = sueldo 
        
    
empleado1 = Empleado('Diego', 34, 2500000)
print(f"El nombre es:{empleado1.nombre} ")
print(f"La edad es:{empleado1.edad} años ")
print(f"El sueldo es de :${empleado1.sueldo} ")
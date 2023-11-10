# Hallar el area de un ractángulo , pidiendo los datoas por teclado.

class Rectangulo:

# Crear métdodo constructor que me permita inicializar base y altura 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura 
        
    def calcularArea(self):
        return self.base * self.altura
    
base = int(input('Digite la base: '))
altura = int(input('Digite la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f"Área rectángulo 1: {rectangulo1.calcularArea()}")

base = int(input('Digite la base: '))
altura = int(input('Digite la altura: '))

rectangulo2 = Rectangulo(base, altura)
print(f"Área rectángulo 2: {rectangulo2.calcularArea()}")
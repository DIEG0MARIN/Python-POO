class Cubo:
    def __init__(self, alto, ancho, profundo):
        self.alto  = alto
        self.ancho = ancho
        self.profundo = profundo
        
    def calcularVolumen(self):
        return self.ancho * self.alto *self.profundo
        
ancho = int(input('Digite el ancho: '))
alto = int(input('Digite el alto: '))
profundo = int(input('Digite el profundo: '))

#El objeto es cubo1
cubo1 = Cubo(ancho,alto,profundo)
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')

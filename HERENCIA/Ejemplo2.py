#  Definir una clase padre llamada vehiculoy dos clases hijhas llamadas coche y bicicleta, las cuales heredan 
#  las cuales heredan la clase padre vehiculo. La clase padre debe tener los siguientes 
#  atributos y métodos:

class Vehiculo:
    def __init__(self, color , ruedas):
        self.color = color
        self.ruedas = ruedas
        
        
    def __str__(self):
        return 'color : ' + self.color + ' sus ruedas: ' + str(self.ruedas)
        
    
class Coche(Vehiculo):
      def __init__(self, color , ruedas, velocidad ):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    
      def __str__(self):
          return super().__str__() + ' su velocidad en km/h ' + str(self.velocidad)
      
      
class Bicicleta(Vehiculo):
      def __init__(self, color , ruedas, tipo ):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    
      def __str__(self):
          return super().__str__() + 'su tipo es' + self.tipo
      
vehiculo1 = Vehiculo('Negro', 5)
print("VEHICULO: ", vehiculo1)

coche1 = Coche('Negro', 5, 240)
print("COCHE: ", coche1)

bicicleta1 = Bicicleta('Negro', 4, 'URBANO')
print("BICICLETA: " ,bicicleta1)

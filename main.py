# qué es una clase? - clase = molde , nota: las clases siempre deben ir en singular

class Coche:
    
    
     # Atributos -> propiedades o características 
     
    color = 'rojo'
    marca = 'Hyundai'
    Kmh = 220
     
     # Métodos -> acciones o comportamientos.
     
     # EJEMPLO MÉTODOS
    def acelerar(self):
         self.Kmh += 10 # esn este caso estamos instanciando Kmh
    def frenar (self):
         self.Kmh -= 10
         
    def setColor(self, color):
        
    # lo que esta dentro del parentesis en el método el primer termino es un parametro y el segundo es un atributo.
    # y se diferencian del color, los atributos me sirven para imrprimir
    # los parametros reciben literal de informacion y se lo asignan a atributo
    #NOTA: que nos permite recibir literal de información? los parametros.

       
    #  método get -> sacar u obtener 
    #  método set -> establecer
  
        
     def Kmh(self):
        return self.Kmh
    
    # fin 
    
    # vamos a instanciar 
    # Siempre debemos instanciar con el nombre del objeto.
    #No debemos instanciar con el nombre de la clase.
    #Por eso para este caso llamamos al objeto Coche1
Coche1 = Coche()
print(Coche1.color,  Coche1.marca, Coche1.Kmh) # para este caso se estan instanciando los atributos

print(f"Velocidad en km/h es: {Coche1.Kmh}")

#instanciamos el método frenar  
Coche1.frenar()
Coche1.frenar()
Coche1.frenar()
print(f"Velocidad en km/h es: {Coche1.Kmh}")

#instanciamos el método acelerar
Coche1.acelerar()
print(f"Velocidad en km/h es: {Coche1.Kmh}")

class Aritmetica:
    
    # El método init, tiene toda la figura de un método constructor y me permite inicializar los atributos

    def __init__(self, numero1, numero2):
       self.numero1 = numero1 # recibe los parametros e inicializa los atributos
       self.numero2 = numero2
    
    def getSumar(self): # me permite obtener la información (get)
            return self.numero1 + self.numero2
    
    def getRestar(self):
        return self.numero1 - self.numero2
    
    def getMultiplicar(self):
        return self.numero1 * self.numero2
    
    def getDividir(self):
        return self.numero1 / self.numero2
    
# Lo que me permite instanciar la clase es el objeto
aritmetica1 = Aritmetica(10,4)

print(f"La suma es: {aritmetica1.getSumar()}  ")
# por ejemplo el objeto aritmetica1 esta instanciando el metodo sumar
# primero llama al objeto aritmetica1 y luego con el get se trae la funcion sumar
 
print(f"La suma es: {aritmetica1.getRestar()}  ")
print(f"La suma es: {aritmetica1.getMultiplicar()}  ")
print(f"La suma es: {aritmetica1.getDividir()}  ")




from pickle import *


class Vehiculo:
            
    def __init__(self, puertas, color, motor):
        self.puertas = puertas
        self.color = color 
        self.motor=motor
                
        def __str__(self):
         return self.puertas + " " + self.color + " " + self.motor
            

stepway = Vehiculo('4', 'Azul', '1.6')
print(str(stepway))

archivo = open("vehiculo_objeto", 'w+b')
dump(stepway, archivo)

archivo.seek(0)
stepway2 = load(archivo)

print(str(stepway2))
archivo.close()





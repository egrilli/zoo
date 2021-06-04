class Animal:
    
    def __init__ (self,nombre,anio):
        self.name=nombre
        self.age=anio
        self.happy=0
        self.health=0
    
    def display_info(self):
        print(f"Nombre:{self.name}\n Edad:{self.age}\n Felicidad:{self.happy}\n Salud:{self.health}" )
        return self

    def alimentar(self):
        self.happy+=10
        self.health+=10
        return self


class Leon(Animal):
    pass

'''
class Pinguino(Animal):
    pass
class Mono(Animal):
    pass
'''


animal1=Leon('Mufasa',25)
animal1.display_info().alimentar().alimentar().display_info()

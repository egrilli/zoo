class Animal():
    def __init__(self,nombre,edad):
        self.name=nombre
        self.age=edad
        self.health=70
        self.happy=70

    def display_info(self):
        return print(f"Nombre: {self.name} \n Edad: {self.age} \n Salud: {self.health} \n Felicidad: {self.happy}")

    def alimentar(self):
        self.health+=10
        self.happy+=10
        return print(f"Por alimentar a los {self.name} Su Salud y Felicidad aumentaraon +10 !! Su nueva estadisitica es:"),self.display_info()


class Leon(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.health=70
        self.happy=70
    def alimentar(self):
        self.health+=30
        self.happy+=30
        return print(f"Por alimentar a los {self.name} Su Salud y Felicidad aumentaraon +10 !! Su nueva estadisitica es:"),self.display_info()

class Pinguino(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.health=20
        self.happy=20
    def alimentar(self):
        self.health+=80
        self.happy+=80
        return print(f"Por alimentar a los {self.name} Su Salud y Felicidad aumentaraon +10 !! Su nueva estadisitica es:"),self.display_info()
    

class Mono(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.health=90
        self.happy=90
        self.pelaje=1
    
    def display_info(self):
        return print(f"Nombre: {self.name} \n Edad: {self.age} \n Salud: {self.health} \n Felicidad: {self.happy} \n Pelaje:{self.pelaje}")

    def alimentar(self):
        self.health+=10
        self.happy+=10
        self.pelaje+=2
        return print(f"Por alimentar a los {self.name} Su Salud y Felicidad aumentaraon +10, el pelaje crecio 2 cm Su nueva estadisitica es:"),self.display_info()
    
class Zoo(Animal):
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_leon(self, name,edad):
        self.animals.append( Leon(name,edad) )
    def add_pinguino(self, name,edad):
        self.animals.append( Pinguino(name,edad) )
    def add_mono(self, name,edad):
        self.animals.append( Mono(name,edad) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def alimentar(self):
        super().alimentar()
    


leon1=Leon("mufasa",20)
leon1.display_info()
leon1.alimentar()
pinguino1=Pinguino("pin",5)
pinguino1.display_info()
pinguino1.alimentar()
mono1=Mono("donky",5)
mono1.display_info()
mono1.alimentar()
animal1=Animal("Blacky",22)
animal1.display_info()
animal1.alimentar()

zoo1 = Zoo("Grill's Zoo")
zoo1.print_all_info()




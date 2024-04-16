from Producto import *
class Antibiotico(Producto):
    def __init__(self, nombre, dosis, tipo_animal, precio):
        super().__init__(None, nombre, None, precio)
        self.dosis = dosis
        self.tipo_animal = tipo_animal

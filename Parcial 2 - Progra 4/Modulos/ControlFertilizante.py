from Producto import *
class ProductoControlFertilizantes(Producto):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
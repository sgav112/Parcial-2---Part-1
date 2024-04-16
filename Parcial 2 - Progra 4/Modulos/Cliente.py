class Cliente:
  def __init__(self, nombre, cedula):
    self.__nombre = nombre
    self.cedula = cedula
    self.facturas = []
  
  def setNombre(self,nombre):
    self.__nombre=nombre
    
  def getNombre(self):
    return self.__nombre


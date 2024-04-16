class Factura:
    def __init__(self, cliente, fecha, productos):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = productos
        self.valor_total = self.calcular_valor_total()

        def calcular_valor_total(self):
            valor_total = 0
            for producto in self.productos:
                valor_total += producto.valor
            return valor_total
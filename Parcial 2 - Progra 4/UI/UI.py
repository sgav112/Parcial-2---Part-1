import Modulos 

def crear_producto_control_plagas(registro_ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
    return ProductoControlPlagas(registro_ica, nombre, frecuencia_aplicacion, valor, periodo_carencia)

def crear_producto_control_fertilizantes(registro_ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
    return ProductoControlFertilizantes(registro_ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion)

def crear_antibiotico(nombre, dosis, tipo_animal, precio):
    return Antibiotico(nombre, dosis, tipo_animal, precio)

def crear_cliente(nombre, cedula):
    return Cliente(nombre, cedula)

def crear_factura(cliente, fecha, productos):
    return Factura(cliente, fecha, productos)

def agregar_producto_a_factura(factura, producto):
    factura.productos.append(producto)

def consultar_historial_compras_cliente(cliente):
    return cliente.facturas

def generar_informe_ventas(facturas, filtro_fecha=None, filtro_cliente=None, filtro_producto=None):
    ventas_filtradas = []
    for factura in facturas:
        if filtro_fecha is None or factura.fecha >= filtro_fecha:
            if filtro_cliente is None or factura.cliente == filtro_cliente:
                if filtro_producto is None or any(producto in factura.productos for producto in filtro_producto):
                    ventas_filtradas.append(factura)
    valor_total_ventas = 0
    for factura in ventas_filtradas:
        valor_total_ventas += factura.valor_total
    print(f"Informe de ventas:")
    print(f"Fecha de filtro: {filtro_fecha}")
    print(f"Cliente de filtro: {filtro_cliente}")
    print(f"Producto de filtro: {filtro_producto}")
    print(f"Ventas filtradas: {ventas_filtradas}")
    print(f"Valor total de ventas: {valor_total_ventas}")
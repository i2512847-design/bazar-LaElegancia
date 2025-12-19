from capaDatos.dProductos import obtener_productos, agregar_producto

def listar_productos():
    return obtener_productos()

def crear_producto(codigo, nombre, precio, stock):
    data = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    return agregar_producto(data)
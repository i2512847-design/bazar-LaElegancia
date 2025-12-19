import streamlit as st
from capaLogica.lProductos import listar_productos, crear_producto

st.title("Gestión de Productos")

menu = st.sidebar.selectbox("Menú", ["Listar", "Agregar"])

if menu == "Listar":
    productos = listar_productos()
    st.table(productos)

elif menu == "Agregar":
    codigo = st.text_input("Código")
    nombre = st.text_input("Nombre")
    precio = st.number_input("Precio", min_value=0.0)
    stock = st.number_input("Stock", min_value=0)
    if st.button("Guardar"):
        crear_producto(codigo, nombre, precio, stock)
        st.success("Producto agregado correctamente")
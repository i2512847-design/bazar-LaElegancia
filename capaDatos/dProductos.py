from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_productos():
    response = supabase.table("productos").select("*").execute()
    return response.data

def agregar_producto(codigo, nombre, precio, stock):
    data = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    response = supabase.table("productos").insert(data).execute()
    return response.data
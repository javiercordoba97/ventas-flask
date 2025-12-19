import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "Libertad.636",   # poné tu contraseña real
    "database": "proyecto_python"
}

def mostrar_ventas():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ventas")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()

    print("=== Ventas registradas ===")
    for venta in resultados:
        print(f"ID: {venta['id']} | Fecha: {venta['fecha']} | Producto: {venta['producto']} | Cantidad: {venta['cantidad']} | Precio: {venta['precio']}")

if __name__ == "__main__":
    mostrar_ventas()
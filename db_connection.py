import pandas as pd
import mysql.connector

def cargar_csv_a_mysql():
    # Leer CSV
    df = pd.read_csv("data/ventas.csv")

    # Conectar a MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Libertad.636",
        database="proyecto_python"
    )
    cursor = conn.cursor()

    # Insertar filas
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO ventas (fecha, producto, cantidad, precio) VALUES (%s, %s, %s, %s)",
            (row['fecha'], row['producto'], int(row['cantidad']), float(row['precio']))
        )

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    cargar_csv_a_mysql()
    print("Datos cargados en la base de datos")
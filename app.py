import mysql.connector
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

config = {
    "host": "localhost",
    "user": "root",
    "password": "Libertad.636",   # reemplaza con tu contraseña real
    "database": "proyecto_python"
}

CSV_FILE = "data/ventas.csv"   # ruta a tu archivo CSV

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ventas", methods=["GET", "POST"])
def ventas():
    if request.method == "POST":
        # Insertar nueva venta en MySQL
        datos = request.form
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ventas (fecha, producto, cantidad, precio) VALUES (%s, %s, %s, %s)",
            (datos["fecha"], datos["producto"], datos["cantidad"], datos["precio"])
        )
        conn.commit()
        cursor.close()
        conn.close()

        # Guardar también en el CSV
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datos["fecha"], datos["producto"], datos["cantidad"], datos["precio"]])

        return redirect("/ventas")

    # Mostrar listado de ventas desde MySQL
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ventas")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("ventas.html", ventas=resultados)

if __name__ == "__main__":
    app.run(debug=True)
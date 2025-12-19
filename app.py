import csv
from flask import Flask, render_template, request, redirect
from services.mysql_service import execute_query, fetch_all
from services.dataframe_service import ventas_por_producto

app = Flask(__name__)

CSV_FILE = "data/ventas.csv"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ventas", methods=["GET", "POST"])
def ventas():
    if request.method == "POST":
        datos = request.form

        # Insertar en MySQL
        execute_query(
            "INSERT INTO ventas (fecha, producto, cantidad, precio) VALUES (%s, %s, %s, %s)",
            (datos["fecha"], datos["producto"], datos["cantidad"], datos["precio"])
        )

        # Guardar en CSV
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datos["fecha"], datos["producto"], datos["cantidad"], datos["precio"]])

        return redirect("/ventas")

    # Obtener ventas desde MySQL
    ventas = fetch_all("SELECT * FROM ventas")

    # Análisis con pandas
    totales = ventas_por_producto()

    return render_template("ventas.html", ventas=ventas, totales=totales)

if __name__ == "__main__":
    app.run(debug=True)
import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer el archivo CSV
df = pd.read_csv("data/ventas.csv")

# 2. Crear una columna 'total'
df["total"] = df["cantidad"] * df["precio"]

# 3. Ventas totales
ventas_totales = df["total"].sum()

# 4. Ventas por producto
ventas_por_producto = df.groupby("producto")["total"].sum()

# 5. Promedio de venta
promedio_venta = df["total"].mean()

# 6. Mostrar resultados
print("Ventas totales:", ventas_totales)
print("\nVentas por producto:")
print(ventas_por_producto)
print("\nPromedio de venta:", promedio_venta)

# 7. Gráfico
ventas_por_producto.plot(kind="bar")
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Total vendido")
plt.show()

# 8. Exportar a Excel
ventas_por_producto_df = ventas_por_producto.reset_index()
ventas_por_producto_df.to_excel("ventas_por_producto.xlsx", index=False)

print("Archivo ventas_por_producto.xlsx generado")

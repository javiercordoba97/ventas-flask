import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ventas.csv")

df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()
ventas_por_producto = df.groupby("producto")["total"].sum()
promedio_venta = df["total"].mean()

print("Ventas totales:", ventas_totales)
print("\nVentas por producto:")
print(ventas_por_producto)
print("\nPromedio de venta:", promedio_venta)

ventas_por_producto.plot(kind="bar")
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Total vendido")
plt.show()

ventas_por_producto_df = ventas_por_producto.reset_index()
ventas_por_producto_df.to_excel("ventas_por_producto.xlsx", index=False)

print("Archivo ventas_por_producto.xlsx generado")
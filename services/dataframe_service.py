import pandas as pd
from services.mysql_service import fetch_all

def get_dataframe():
    query = "SELECT * FROM ventas"
    data = fetch_all(query)
    df = pd.DataFrame(data)

    # Asegurar tipos correctos
    df["cantidad"] = df["cantidad"].astype(int)
    df["precio"] = df["precio"].astype(float)
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Columna calculada
    df["total"] = df["cantidad"] * df["precio"]

    return df

def ventas_por_producto():
    df = get_dataframe()
    return df.groupby("producto")["total"].sum().to_dict()

def ventas_totales():
    df = get_dataframe()
    return df["total"].sum()

def promedio_venta():
    df = get_dataframe()
    return df["total"].mean()
import matplotlib.pyplot as plt
#Cargo El Dataset
df = pd.read_csv("datos/ventas.csv")
#convertimos la columna de fecha a tipo datetime
df["sales_date"] = pd.to.datetime(df["sales_date"])
#Calculamos imdicadores principales
total_ventas = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
max_ventas = df["sales_amount"].max()
min_ventas = df["sales_amount"].min()
print (f"Ventas Totales: {total_ventas}")
print (f"Promedio Diario: {promedio_ventas:.2f}")
#Agrupamos por mes
df ["mes"] = df ["sales_date"].dt.to_period("M")
venta_mes = df.groupby("mes") ["sales_amount"].sum()
print ("\nVentas por Mes:")

#Generamos de Evolucion de ventas
plt.figure(figsize="bar",color="steelblue")
plt.title("Evolución de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto de Ventas")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado en resultados/")



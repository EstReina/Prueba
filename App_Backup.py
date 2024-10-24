from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# Cambiar el backend para evitar usar Tkinter
matplotlib.use('Agg')

app = Flask(__name__)

# Leer el archivo CSV
df = pd.read_csv('datos.csv')  # Asegúrate de que el archivo CSV esté en la misma carpeta que tu script.

@app.route('/')
def show_charts():
    return render_template('Estadisticas.html')


# Seleccionar datos de ejemplo para graficar (modificar según lo que necesites)
ciudades = df['Ciudad'].value_counts().head(5)  # Top 5 ciudades con más registros
productos = df['Producto'].value_counts().head(5)  # Top 5 productos más vendidos
genero = df['Género'].value_counts()  # Distribución de género
fechas = df['Fecha'].value_counts().sort_index().head(10)  # Actividad por fecha (ordenada)

# Gráfico de Barras (para distribución de género)

fig1, ax1 = plt.subplots()
ax1.bar(genero.index, genero.values, color='blue')
ax1.set_xlabel('Género')
ax1.set_ylabel('Cantidad')
plt.savefig('static/img/barras.png')
plt.close(fig1)

#Gráfico de Torta (para ciudades con más registros)

fig2, ax2 = plt.subplots()
ax2.pie(ciudades.values, labels=ciudades.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.savefig('static/img/torta.png')
plt.close(fig2)

# Gráfico de Líneas (para actividad por fecha)

fig3, ax3 = plt.subplots()
ax3.plot(fechas.index, fechas.values, marker='o', color='purple')
plt.xticks(rotation=45)
plt.savefig('static/img/lineas.png')
plt.close(fig3)


# Gráfico de Área (para productos más vendidos)
fig4, ax4 = plt.subplots()
ax4.fill_between(productos.index, productos.values, color="green", alpha=0.6)
plt.xticks(rotation=45)
plt.savefig('static/img/area.png')
plt.close(fig4)


if __name__ == '__main__':
    app.run(debug=True)

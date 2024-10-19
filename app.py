from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import pandas as pd
import io
import matplotlib

# Cambiar el backend para evitar usar Tkinter
matplotlib.use('Agg')

app = Flask(__name__)

# Leer el archivo CSV
df = pd.read_csv('datos.csv')  # Asegúrate de que el archivo CSV esté en la misma carpeta que tu script.

@app.route('/graficos.png')
def crear_graficos():
    # Seleccionar datos de ejemplo para graficar (modificar según lo que necesites)
    ciudades = df['Ciudad'].value_counts().head(5)  # Top 5 ciudades con más registros
    productos = df['Producto'].value_counts().head(5)  # Top 5 productos más vendidos
    genero = df['Género'].value_counts()  # Distribución de género
    fechas = df['Fecha'].value_counts().sort_index().head(10)  # Actividad por fecha (ordenada)

    # Crear los gráficos

    # Gráfico de Barras (para distribución de género)
    plt.subplot(2, 2, 1)
    plt.bar(genero.index, genero.values, color='blue')
    plt.title('Distribución por Género')

    # Gráfico de Torta (para ciudades con más registros)
    plt.subplot(2, 2, 2)
    plt.pie(ciudades.values, labels=ciudades.index, autopct='%1.1f%%', startangle=90)
    plt.title('Ciudades con más registros')
    plt.axis('equal')

    # Gráfico de Área (para productos más vendidos)
    plt.subplot(2, 2, 3)
    plt.fill_between(productos.index, productos.values, color="green", alpha=0.6)
    plt.title('Productos más Vendidos')
    plt.xticks(rotation=45)

    # Gráfico de Líneas (para actividad por fecha)
    plt.subplot(2, 2, 4)
    plt.plot(fechas.index, fechas.values, marker='o', color='purple')
    plt.title('Actividad por Fecha')
    plt.xticks(rotation=45)

    # Ajustar el espacio entre subplots
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('Estadisticas.html')

if __name__ == '__main__':
    app.run(debug=True)

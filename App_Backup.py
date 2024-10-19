from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io
import matplotlib


# Cambiar el backend para evitar usar Tkinter
matplotlib.use('Agg')

app = Flask(__name__)

@app.route('/graficos.png')
def crear_graficos():
    x = [1, 2, 3, 4, 5]
    y1 = [1, 4, 10, 15, 25]
    y2 = [2, 8, 12, 18, 24]
    y3 = [3, 6, 9, 12, 15]
    y4 = [4, 5, 7, 8, 10]

    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [10, 20, 30, 40, 50]

    #Crear el primer gráfico (2 fila, 2 columna, 1 grafico)
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, color='red')
    plt.title('Gráfico de lineas')

    #Crear el segundo gráfico (2 fila, 2 columna, 2 grafico)
    plt.subplot(2, 2, 2)
    plt.bar(x, y2, color='green')
    plt.title('Gráfico de barras')

    #Crear el primer gráfico (2 fila, 2 columna, 3 grafico)
    plt.subplot(2, 2, 3)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Gráfico de torta')

    #Crear el segundo gráfico (2 fila, 2 columna, 4 grafico)
    plt.subplot(2, 2, 4)
    plt.plot(x, y1, label='Serie 1')
    plt.plot(x, y2, label='Serie 2')
    plt.fill_between(x, y1, y2, alpha=0.2)
    plt.legend()
    plt.title('Gráfico de lineas')

    #Ajustar el espacio entre subplots
    plt.tight_layout()
    
    img=io.BytesIO() 
    plt.savefig(img, format='png')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('Estadisticas.html')


if __name__ == '__main__':
    app.run(debug=True)

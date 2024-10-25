from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Ruta para cargar la página de contacto
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

# Ruta para manejar el envío del formulario
@app.route('/submit', methods=['POST'])
def submit_form():
    # Procesar el formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    pais = request.form['pais']
    ciudad = request.form.get('city', '')  # Obtener ciudad de manera segura

    # Crear un diccionario con los datos del formulario
    nuevo_dato = {
        'Nombre': [nombre],
        'Apellido': [apellido],
        'Email': [email],
        'Telefono': [telefono],
        'Pais': [pais],
        'Ciudad': [ciudad]
    }

    df_nuevo = pd.DataFrame(nuevo_dato)

    # Guardar los datos en un archivo CSV
    try:
        df_existente = pd.read_csv('data.csv')
        df_total = pd.concat([df_existente, df_nuevo])
        df_total.to_csv('data.csv', index=False)
    except FileNotFoundError:
        df_nuevo.to_csv('data.csv', index=False)

    # Redirigir de vuelta a la página de contacto después de enviar el formulario
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

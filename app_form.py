from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/')

def formulario():
    return render_template('Contacto.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    email=request.form['email']
    telefono=request.form['telefono']
    pais=request.form['pais']
    ciudad=request.form['city']
    
    #Crear un diccionario
    
    nuevo_dato={
        'Nombre':[nombre],
        'Apellido':[apellido],
        'Email':[email],
        'Telefono':[telefono],
        'Pais':[pais],
        'Ciudad':[ciudad]
    }
    
    df_nuevo=pd.DataFrame(nuevo_dato)
    
    #Guardar datos en un archivo CSV
    try:
        df_existente=pd.read_csv('data.csv')
        df_total=pd.concat([df_existente, df_nuevo])
        df_total.to_csv('data.csv', index=False)
    except FileNotFoundError:
        df_nuevo.to_csv('data.csv', index=False)    
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
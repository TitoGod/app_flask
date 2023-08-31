# app.py
import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de la clave de API
api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
if not api_key:
    raise ValueError("No se encontró la clave de API de OpenWeatherMap. "
                     "Asegúrate de configurar la variable de entorno 'OPENWEATHERMAP_API_KEY'.")

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


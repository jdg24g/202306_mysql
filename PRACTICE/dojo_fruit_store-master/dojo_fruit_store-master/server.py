from flask import Flask, render_template, request, redirect

import os
from datetime import datetime

def listar_archivos_png(carpeta):
    png_files = [file for file in os.listdir(carpeta) if file.lower().endswith('.png')]
    return png_files

if __name__ == '__main__':
    carpeta = './static/img'
    png_files = listar_archivos_png(carpeta)



app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])         
def checkout():
    lista = request.form
    total = int(lista['strawberry'])+int(lista['raspberry']) + int(lista['apple'])
     # Obtener la fecha y hora actual
    now = datetime.now()
    date_string = now.strftime('%B %d, %Y %I:%M:%S %p')
    print(f'Cobrando a {lista["first_name"]} {lista["last_name"]} por {total} frutas')
    return render_template('checkout.html',lista=lista,date_string=date_string,total=total)

@app.route('/fruits')         
def fruits():
    return render_template('fruits.html',file_name=png_files)

if __name__=='__main__':   
    app.run(debug=True, host='0.0.0.0',port=5000 )
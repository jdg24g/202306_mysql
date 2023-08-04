from flask import Flask, render_template, request, redirect,flash

import os
from datetime import datetime

def listar_archivos_png(carpeta):
    png_files = [file for file in os.listdir(carpeta) if file.lower().endswith('.png')]
    return png_files

if __name__ == '__main__':
    carpeta = './static/img'
    png_files = listar_archivos_png(carpeta)



app = Flask(__name__) 

app.secret_key = 'XXXXXXXXXXXXXXXX'

lista = []
@app.route('/')         
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])         
def checkout():
    lista.append(request.form)
    return redirect('/show')

@app.route('/show')
def show():
    try:
        form_data = lista[-1]  # Obtener el último elemento de la lista, que es el ImmutableMultiDict
        print(form_data)
        total = int(form_data['strawberry']) + int(form_data['raspberry']) + int(form_data['apple'])
        # Obtener la fecha y hora actual
        now = datetime.now()
        date_string = now.strftime('%B %d, %Y %I:%M:%S %p')
        print(f'Cobrando a {form_data["first_name"]} {form_data["last_name"]} por {total} frutas')
        return render_template('checkout.html', lista=form_data, date_string=date_string, total=total)
    except:
        print('Error')
        return redirect('/')


@app.route('/fruits')         
def fruits():
    return render_template('fruits.html',file_name=png_files)



if __name__=='__main__':   
    app.run(debug=True, host='0.0.0.0',port=5000 )
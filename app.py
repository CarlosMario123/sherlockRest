from flask import Flask, request, jsonify
from sherlock import searchUser

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def handle_post_request():
    if request.method == 'POST':
        # Obtener los datos JSON del cuerpo de la solicitud sin verificar el encabezado Content-Type
        data = request.json

        # Verificar si se proporcionó el nombre en los datos recibidos
        if data and 'name' in data:
            nombre = data['name']
             
            resultado = searchUser(nombre)
            
            response = {'resultados': resultado}

            # Devolver una respuesta al cliente en formato JSON
            return jsonify(response)
        else:
            return jsonify({'error': 'No se proporcionó un nombre válido en la solicitud'})
    else:
        return jsonify({'error': 'Se esperaba una solicitud POST'})

if __name__ == '__main__':
    app.run()

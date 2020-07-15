from flask import Flask, jsonify, request
import json



app = Flask(__name__)

desenvoldores = [
    {   'id': '0',
        'nome':'DEV DEVILSON SILVISON',
        'habilidades':['python','flask']
    },
    {
        'id': '1',
        'nome':'DEV DVANEIO',
        'habilidades':['sql','oracle']
    }
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvoldores[id]
            return jsonify(response)
        except IndexError:
            response = {'status':'erro','mensagem':'id {} de desenvolvedor inexistente'.format(id)}
        except Exception:
            response = {'status':'erro','mensagem':'Erro desconhecido, procure o administrador da API'}


    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvoldores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluído com sucesso'})

# lista todos e inser
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados - json.loads(request.data)
        posicao = len(desenvoldores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'Registro inserido com sucesso'})
    
    elif request.method == 'GET':
        return jsnify(desenvolvedores)

    
    

if __name__ == '__main__':
    app.run(debug=True)
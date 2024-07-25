from controllers.word_controller import api as wordControllerApi
from flask import Flask, request, jsonify
from flask_restx import Api
from werkzeug.exceptions import InternalServerError, BadRequest

app = Flask(__name__)
api = Api(app, title='Teste Pilar', version='1.0', description='Teste para vaga de Backend', doc='/api')
api.add_namespace(wordControllerApi)

if __name__ == '__main__':
    app.run(debug=False)

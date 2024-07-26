from controllers.word_controller import api as wordApi
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, title='Teste Pilar', version='1.0', description='Teste para vaga de Backend', doc='/api')
api.add_namespace(wordApi)

if __name__ == '__main__':
    app.run(debug=False)

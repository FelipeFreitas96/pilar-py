"""
MIT License

PilarPY - Backend
Author: Felipe Freitas
"""

from flask import Flask
from flask_restx import Api
from controllers.word_controller import api as wordApi

app = Flask(__name__)
api = Api(
    app,
    title='Pilar PY',
    version='1.0',
    description='Teste Backend',
    doc='/api'
)
api.add_namespace(wordApi)

if __name__ == '__main__':
    app.run()

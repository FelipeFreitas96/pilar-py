from flask import jsonify
from flask import request
from flask_restx import Resource, Namespace, fields
from services.word_service import WordService
from werkzeug.exceptions import InternalServerError, BadRequest

api = Namespace('WordController', description='Controlador de palavras', path='/')
models = {
    'Request': api.model('GetVowalsRequest', {
        'words': fields.List(fields.String, required=True, description='Lista de palavras a serem contadas as vogais')
    }),
    'Response': api.model('GetVowalsResponse', {
        'key': fields.Integer,
    })
}

@api.route('/vowel_count')
class WordController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_service = WordService()

    @api.expect(models['Request'])
    @api.response(200, 'Success', models['Response'])
    def post(self):
        return self.word_service.getVowalsFromArray(
            words=request.get_json()['words']
        )
        
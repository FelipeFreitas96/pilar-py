"""
MIT License

PilarPY - Backend
Author: Felipe Freitas
"""

from flask import request
from flask_restx import Resource, Namespace, fields
from services.word_service import WordService

word_service = WordService()
api = Namespace(
    'WordController',
    description='Controlador de palavras',
    path='/'
)

vowals_count_model = {
    'Request': api.model('GetVowalsRequest', {
        'words': fields.List(
            fields.String,
            required=True,
            description='Lista de palavras a serem contadas as vogais'
        )
    }),
    'Response': api.model('GetVowalsResponse', {
        'key': fields.Integer,
    })
}

sort_model = {
    'Request': api.model('SortRequest', {
        'words': fields.List(fields.String,
            required=True,
            description='Lista de palavras a serem contadas as vogais'
        ),
        'order': fields.String(
            required=True,
            description='Ordenação da lista'
        )
    }),
    'Response': fields.List(fields.String)
}

error_model = api.model('ErrorResponse', {
    'message': fields.String(
        required=True,
        description='Mensagem de erro'
    )
})

@api.route('/sort')
@api.doc(params={'order': 'asc|desc'})
class SortResource(Resource):
    @api.expect(sort_model['Request'], validate=True)
    @api.response(200, 'Success', sort_model['Response'])
    @api.response(400, 'Bad Request', error_model)
    def post(self):
        body = request.get_json()
        words = body['words']
        order = body['order'].lower()

        if order not in ['asc', 'desc']:
            return {
                'message': "Invalid order (try 'asc' or 'desc')"
            }, 400
        
        if len(words) == 0:
            return {
                'message': "Empty list"
            }, 400

        return word_service.sort_words_from_array(
            words,
            order,
        )
@api.route('/vowel_count')
class VowelCountResource(Resource):
    @api.expect(vowals_count_model['Request'], validate=True)
    @api.response(200, 'Success', vowals_count_model['Response'])
    @api.response(400, 'Bad Request', error_model)
    def post(self):
        body = request.get_json()
        words = body['words']

        if len(words) == 0:
            return {
                'message': "Empty list"
            }, 400

        return word_service.get_vowals_from_array(words)

api.add_resource(SortResource, '/sort')
api.add_resource(VowelCountResource, '/vowel_count')

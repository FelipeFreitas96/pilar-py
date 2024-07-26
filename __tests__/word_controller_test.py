import json
import pytest
from flask import Flask
from flask_restx import Api
from controllers.word_controller import api as wordApi

@pytest.fixture
def client():
    app = Flask(__name__)
    api_app = Api(app)
    api_app.add_namespace(wordApi)
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_sort_words(client):
    ## Testando a ordenação crescente
    response = client.post('/sort',
                           data=json.dumps({"words": ["batman", "robin", "coringa"], "order": "asc"}),
                           content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data) == ["batman", "coringa", "robin"]
    
    ## Testando a ordenação decrescente
    response = client.post('/sort',
                        data = json.dumps({"words": ["batman", "robin", "coringa"], "order": "desc"}),
                        content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data) == ["robin", "coringa", "batman"]
    
    ## Testando a ordenação errada
    response = client.post('/sort', 
                           data=json.dumps({"words": ["batman", "robin", "coringa"], 'order': 'wrong'}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'message': "Invalid order (try 'asc' or 'desc')"}

    ## Testando a ordenação com lista vazia
    response = client.post('/sort', 
                           data=json.dumps({'words': [], 'order': 'asc'}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'message': "Empty list"}
    
    ## Testando sem o parametro words
    response = client.post('/sort', 
                           data=json.dumps({'order': 'asc'}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'errors': {'words': "'words' is a required property"}, 'message': 'Input payload validation failed'}

    ## Testando sem o parametro order
    response = client.post('/sort', 
                           data=json.dumps({'words': ["batman", "robin", "coringa"]}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'errors': {'order': "'order' is a required property"}, 'message': 'Input payload validation failed'}

    ## Testando sem parametros
    response = client.post('/sort', 
                           data=json.dumps({}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'errors': {'words': "'words' is a required property", 'order': "'order' is a required property"}, 'message': 'Input payload validation failed'}

def test_vowel_count(client):
    ## Testando a contagem de vogais
    response = client.post('/vowel_count', 
                           data=json.dumps({'words': ["batman", "robin", "coringa"]}),
                           content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data) == {'batman': 2, 'robin': 2, 'coringa': 3}
    
    ## Testando com a lista vazia
    response = client.post('/vowel_count', 
                           data=json.dumps({'words': []}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'message': "Empty list"}
    
    ## Testando sem o parametro words
    response = client.post('/vowel_count', 
                           data=json.dumps({}),
                           content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'errors': {'words': "'words' is a required property"}, 'message': 'Input payload validation failed'}

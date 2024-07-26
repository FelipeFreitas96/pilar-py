# Pilar PY

Este repositório contém o código para o teste de Software Engineer Backend. A tarefa envolve a criação de uma API usando Python com duas rotas: uma para contar vogais em palavras e outra para ordenar palavras. O projeto também inclui um pipeline de CI/CD usando GitHub Actions que executa as etapas de lint, testes e deploy.

# Endpoints da API
## [POST] /vowel_count
Conta o número de vogais em cada palavra fornecida.

### Requisição:

```json
{
  "words": ["batman", "robin", "coringa"]
}
```
### Resposta:

```json
{
  "batman": 2,
  "robin": 2,
  "coringa": 3
}
```
## [POST] /sort

Ordena o array de palavras em ordem ascendente ou descendente.

### Requisição (ordem ascendente):

```json
{
  "words": ["batman", "robin", "coringa"],
  "order": "asc"
}
```

### Resposta:

```json
[
  "batman",
  "coringa",
  "robin"
]
```
### Requisição (ordem descendente):
```json
{
  "words": ["batman", "robin", "coringa"],
  "order": "desc"
}
```

### Resposta:

```json
[
  "robin",
  "coringa",
  "batman"
]
```

### Tratamento de Erros

A API retornará códigos de status HTTP apropriados para requisições inválidas:

- Método não permitido (se não for POST)
- Rota não encontrada (se a rota não existir)
- Tipo de mídia não suportado (se Content-Type não for application/json)

## Como Começar
### Pré-requisitos
- Python 3.x
- pip (gerenciador de pacotes do Python)

### Instalação
#### Clone o repositório:

```bash
git clone https://github.com/FelipeFreitas96/pilar-py.git
cd pilar-py
```

#### Crie um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Instale as dependências:

```bash
pip install -r requirements.txt
```

#### Executando a API

```bash
python main.py
```

A API estará acessível em http://127.0.0.1:5000.

## Testes
Para rodar os testes, use:
```bash
set PYTHONPATH=%cd%
pytest
```

## Licença
Este projeto está licenciado sob a [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
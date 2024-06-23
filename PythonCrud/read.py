import requests
from requests.auth import HTTPBasicAuth

# Configurações básicas
BASE_URL = 'http://localhost:5984'
DB_NAME = 'meubanco'  # Substitua pelo nome do seu banco de dados
AUTH = HTTPBasicAuth('admin', 'admin')  # Substitua pelos seus dados de usuário e senha

def read_document(doc_id):
    """ Lê um documento pelo ID com autenticação. """
    response = requests.get(f'{BASE_URL}/{DB_NAME}/{doc_id}', auth=AUTH)
    return response.json()

    # ID do documento criado (substitua isso pelo ID real obtido na criação)
doc_id = 'e1b131ce6258b88b8b119e1b28011f85'

    # Ler um documento
print('Documento lido:', read_document(doc_id))

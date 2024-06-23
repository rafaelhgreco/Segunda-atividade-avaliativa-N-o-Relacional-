import requests
from requests.auth import HTTPBasicAuth

# Configurações básicas
BASE_URL = 'http://localhost:5984'
DB_NAME = 'meubanco'  # Substitua pelo nome do seu banco de dados
AUTH = HTTPBasicAuth('admin', 'admin')  # Substitua pelos seus dados de usuário e senha
doc_id = 'e1b131ce6258b88b8b119e1b28011f85'

def read_document(doc_id):
    """ Lê um documento pelo ID com autenticação. """
    response = requests.get(f'{BASE_URL}/{DB_NAME}/{doc_id}', auth=AUTH)
    return response.json()
def delete_document(doc_id):
    """ Deleta um documento pelo ID com autenticação. """
    doc = read_document(doc_id)
    if 'error' in doc:
        return doc  # Retorna o erro se o documento não puder ser lido
    response = requests.delete(f'{BASE_URL}/{DB_NAME}/{doc_id}', params={'rev': doc['_rev']}, auth=AUTH)
    return response.json()
print('Documento deletado:', delete_document(doc_id))
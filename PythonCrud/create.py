import requests
from requests.auth import HTTPBasicAuth

# Configurações básicas
BASE_URL = 'http://localhost:5984'
DB_NAME = 'meubanco'  # Substitua pelo nome do seu banco de dados
AUTH = HTTPBasicAuth('admin', 'admin')  # Substitua pelos seus dados de usuário e senha

def create_document(doc_data):
    """ Cria um novo documento no banco de dados com autenticação. """
    response = requests.post(f'{BASE_URL}/{DB_NAME}', auth=AUTH, json=doc_data)
    return response.json()

# Exemplos de uso
if __name__ == '__main__':
    # Criar um documento
    new_doc = {
        'nome': 'João Silva',
        'idade': 30,
        'cidade': 'São Paulo'
    }
    print('Criando documento:', create_document(new_doc))
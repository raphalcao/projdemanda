USO DO DOCKER

Para fazer uma imagem a partir dos dados: docker-compose build
Para efetuar um clone, abra a plataforma do docker e digite o comando: docker push raphalcao/projdemanda:tagname, onde
tagname é de sua escolha.

Para executar essa API, deve executar os seguintes comandos:

makemigrations -> python manage.py makemigrations
migrations -> python manage.py migrate

A base de dados é local, em SQLite.

Após executar a migration, deve criar um superusuario através do comando: python manage.py createsuperuser
Com o superusuario logado, gere um token que será utilizado para o consumo da API.


PARA USO DOS ENDPOINTS

Link para uso dos endpoints da API:
Os endpoints deverão ser executados e autenticados pelo insomnia ou postman.

Classe Demanda:
GET: http://localhost:8000/api/demandas/
GET: http://localhost:8000/api/demandas/<id>
POST: http://localhost:8000/api/demandas/
PUT: http://localhost:8000/api/demandas/<id>
DELETE: http://localhost:8000/api/demandas/<id>

Classe Users:
GET: http://localhost:8000/api/users/
GET: http://localhost:8000/api/users/<id>
POST: http://localhost:8000/api/users/
PUT: http://localhost:8000/api/users/<id>
DELETE: http://localhost:8000/api/users/<id>

Classe Enderecos:
GET: http://localhost:8000/api/enderecos/
GET: http://localhost:8000/api/enderecos/<id>
POST: http://localhost:8000/api/enderecos/
PUT: http://localhost:8000/api/enderecos/<id>
DELETE: http://localhost:8000/api/enderecos/<id>

EXECUTANDO OS TESTES

Para executar os testes, deixe o servidor ligado e com outro terminal, abra o diretório de testes.
Execute os comandos:

Teste de Demanda -> pytest teste_demandas_pytest.py
Teste de Endereco -> pytest teste_endereco_pytest.py
Teste de Users -> pytest teste_users_pytest.py
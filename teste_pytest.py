import requests


class TestDemandas:
    headers = {'Authorization': 'Token de4cb62936c4eaeee1addf29bf38ec7cd26fbd0b'}
    url_base_demandas = 'http://localhost:8000/api/demandas/'


    def test_get_demandas(self):
        demandas = requests.get(url=self.url_base_demandas,  verify=False, headers=self.headers)
        assert demandas.status_code == 200


    def test_get_demanda(self):
        demanda = requests.get(url=f'{self.url_base_demandas}1/', headers=self.headers)
        assert demanda.status_code == 200


    def test_post_demanda(self):
        novo = {
            "descricao": "Refrigerante em lata",
            "endereco": 2,
            "anunciante": 2
        }

        resposta = requests.post(url=self.url_base_demandas, headers=self.headers, data=novo)
        assert resposta.status_code == 201

    def test_put_curso(self):
        atualizado = {
            "descricao": "Coca Cola",
            "endereco": 1,
            "anunciante": 2

        }
        resposta = requests.put(url=f'{self.url_base_demandas}1/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200


    def test_delete_demanda(self):
        resposta = requests.delete(url=f'{self.url_base_demandas}1/', headers=self.headers)
        assert resposta.status_code == 204
import requests


class TestEnderecos:
    headers = {'Authorization': 'Token de4cb62936c4eaeee1addf29bf38ec7cd26fbd0b'}
    url_base_enderecos = 'http://localhost:8000/api/enderecos/'


    def test_get_enderecos(self):
        enderecos = requests.get(url=self.url_base_enderecos,  verify=False, headers=self.headers)
        assert enderecos.status_code == 200


    def test_get_user(self):
        endereco = requests.get(url=f'{self.url_base_enderecos}4/', headers=self.headers)
        assert endereco.status_code == 200


    def test_post_endereco(self):
        novo = {
            "cep": "20241150",
            "endereco": "Rua A",
            "numero": 159,
            "complemento": "Casa 2",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "usuario": 3
        }

        resposta = requests.post(url=self.url_base_enderecos, headers=self.headers, data=novo)
        assert resposta.status_code == 201

    def test_put_endereco(self):
        atualizado = {
            "cep": "20241150",
            "endereco": "Rua A",
            "numero": 159,
            "complemento": "Casa 2",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "usuario": 3

        }
        resposta = requests.put(url=f'{self.url_base_enderecos}3/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 404

    def test_delete_endereco(self):
        resposta = requests.delete(url=f'{self.url_base_enderecos}1/', headers=self.headers)
        assert resposta.status_code == 404
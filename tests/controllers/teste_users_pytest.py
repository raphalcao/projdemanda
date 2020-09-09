import requests


class TestUsers:
    headers = {'Authorization': 'Token de4cb62936c4eaeee1addf29bf38ec7cd26fbd0b'}
    url_base_users = 'http://localhost:8000/api/users/'


    def test_get_users(self):
        users = requests.get(url=self.url_base_users,  verify=False, headers=self.headers)
        assert users.status_code == 200


    def test_get_user(self):
        user = requests.get(url=f'{self.url_base_users}3/', headers=self.headers)
        assert user.status_code == 200


    def test_post_user(self):
        novo = {
            "password": "R@phael1234",
            "last_login": "2020-09-08T15:33:11Z",
            "email": "raphalcao@gmail.com",
            "nomeCompleto": "Leonardo Falcao",
            "telefone": "21988487213"
        }

        resposta = requests.post(url=self.url_base_users, headers=self.headers, data=novo)
        assert resposta.status_code == 400

    def test_put_user(self):
        atualizado = {
            "password": "123456",
            "last_login": "2020-09-08T15:33:11Z",
            "email": "raphalcao@gmail.com",
            "nomeCompleto": "Leonardo Falcao",
            "telefone": "21988487213"

        }
        resposta = requests.put(url=f'{self.url_base_users}3/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200

    def test_delete_user(self):
        resposta = requests.delete(url=f'{self.url_base_users}1/', headers=self.headers)
        assert resposta.status_code == 404
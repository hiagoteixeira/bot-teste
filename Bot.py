import requests

class Bot:

    def login_view(self):
        try:
            print("Tentando acessar URL")
            result = requests.get("https://estoque.micron.com.br/login")
            return result.text
        except Exception as e:
            print("Erro ao acessar URL")

    def authenticate(self):
        url = "https://estoque.micron.com.br/api/login"
        print("Definindo url: ", url)
        params = {"login": "", "senha": ""}
        try:
            session = requests.Session()
            result = session.post(url, data=params, json={}, timeout=20)
            if result.json()['status'] == "success":
                print("Autenticado com sucesso!")
            else:
                print("Erro na autenticação!")
            
            session.close()
            result.close()
            
        except Exception as e:
            print("Error during execution")
            print(e)

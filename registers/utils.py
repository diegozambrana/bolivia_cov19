import requests
URL_API = "https://boliviasegura.gob.bo/wp-content/json/api.php"


def get_data():
    response = requests.get(URL_API)
    return response.json()

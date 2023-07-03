import requests
# import your unique api key ERLI
from config import api_key_erli

def get_erli_product_by_id(id):
    url = f'https://erli.pl/svc/shop-api/products/{id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key_erli}"}
    response = requests.get(url, headers=headers)
    return response.json()


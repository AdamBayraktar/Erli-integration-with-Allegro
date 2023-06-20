import requests
# import your unique api key ERLI
from config import api_key_erli


# request url data
url = 'https://erli.pl/svc/shop-api/me'
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key_erli}"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Connection established")
else:
    raise Exception("Api key", "Check your api key")

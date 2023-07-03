import requests
# import your unique api key ERLI
from config import api_key_erli

# You can use this main function to check if it works
def main():
    example = get_erli_product_by_id("12585141381")
    print(example)

def get_erli_product_by_id(id):
    url = f'https://erli.pl/svc/shop-api/products/{id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key_erli}"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    main()
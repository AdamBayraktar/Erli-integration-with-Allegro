import requests
import json
from get_access_token_allegro import get_token

requests.packages.urllib3.disable_warnings()

# get all user's products
def main():
    access_token = get_token()
    example = all_products_id(access_token)
    print(example)
    


def get_all_products(access_token, lower_price=0, upper_price=1000, limit=1000):
    url = "https://api.allegro.pl/sale/offers"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        "limit": limit,
        'sellingMode.price.amount.gte': lower_price,
        'sellingMode.price.amount.lte': upper_price,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()["offers"]


def save_file_as_json(file, file_name):
    json_object = json.dumps(file, indent=4)
    with open(file_name, "w") as outfile:
        outfile.write(json_object)

# gets all user's products and return list of products id
def all_products_id(access_token):
    all_products = []
    # max limit products per request is 1000 therefore divide by price to several requests to get all products
    all_products.extend(get_all_products(access_token, upper_price=10))
    all_products.extend(get_all_products(access_token, lower_price=10.01, upper_price=18))
    all_products.extend(get_all_products(access_token, lower_price=18.01))
    return [product["id"] for product in all_products]
    

if __name__ == "__main__":
    main()
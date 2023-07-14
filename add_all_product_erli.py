from new_erli_product import NewErliProduct
from get_all_allegro_products_detailed_info import all_product_detail
from get_access_token_allegro import get_token
import requests
# import your unique api key ERLI
from config import api_key_erli
import json

# main code that is responsible for adding all products from allegro to erli
def main():
    access_token = get_token()
    all_products, all_id = all_product_detail(access_token)
    erli_product = []
    # export list of product id's as a text fie. You can use it later to update products by id because it also sets it as unique ID in Erli platform. Use this id as title post_product funtion when you are sure that it won't fail otherwise use some random IDs. I am not sure if once created title and then archieved can be used again.
    with open(f'list_of_product_id.txt', "w") as f:
        for id in all_id:
            f.write(str(id) + "\n")
    global failed_number_products
    failed_number_products = 0
    for product in all_products:
        erli_product.append(NewErliProduct(product))
    for product in erli_product:
        post_product(product.data, product.id)


def post_product(data, title):
    url = f'https://erli.pl/svc/shop-api/products/{title}'
    headers = {
        "accept": "*/*",
        "Authorization": f"Bearer {api_key_erli}",
        "Content-Type": "application/json"
        }
    response = requests.post(url, json=data, headers=headers)
    # write all relavant information, when products fail to be created
    if response.status_code != 202:
        global failed_number_products
        with open(f'fialed_to_create_{failed_number_products}.txt', "w") as f:
            failed_number_products += 1
            f.write(json.dumps(data) + "\n")
            f.write(str(title) + "\n")
            f.write(str(response.status_code) + "\n")
            f.write(json.dumps(response.text) + "\n")

    
if __name__ == "__main__":
    main()
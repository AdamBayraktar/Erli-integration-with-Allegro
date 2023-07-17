from new_erli_product import NewErliProduct
from get_all_allegro_products_detailed_info import get_product_details
from get_access_token_allegro import get_token
from convert_txt_to_list import convert_text_file_to_list
import requests
# import your unique api key ERLI
from config import api_key_erli
import json

# code that is responsible for adding new products from allegro to erli
def main():
    access_token = get_token()
    # add text file with new products IDs
    new_id_list = convert_text_file_to_list("new_products.txt")
    new_products_allegro = []
    for id in new_id_list:
        new_products_allegro.append(get_product_details(access_token, id))
    # Update list of existing product IDs
    # list of IDs that you update
    with open(f'list_of_product_id.txt', "a") as f:
        for id in new_id_list:
            f.write(str(id) + "\n")
    global failed_number_products
    failed_number_products = 0
    erli_product = []
    for product in new_products_allegro:
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
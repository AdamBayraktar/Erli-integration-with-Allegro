import requests
import json
from get_access_token_allegro import get_token
from get_offer_by_id_allegro import get_offer_by_id_allegro
from updated_erli_product_class import UpdatedErliProduct
from convert_txt_to_list import convert_text_file_to_list
# import your unique api key ERLI
from config import api_key_erli

def main():
    access_token = get_token()
    # enter the name of text file that contains all products ID
    ID_LIST = convert_text_file_to_list("list_of_product_id.txt")
    list_of_updated_products_info = []
    list_failed_id = []
    # get from allegro all recent information about products
    for id in ID_LIST:
        # if there is not allegro product with the id then it returns empty list
        allegro_product = get_offer_by_id_allegro(access_token, id)
        if allegro_product:
            updated_product = UpdatedErliProduct(allegro_product[0])
            list_of_updated_products_info.append(updated_product)
        else:
            list_failed_id.append(id)
    # send recent information to erli
    for updated_product in list_of_updated_products_info:
        response = patch_product(updated_product)
        if response.status_code != 202:
            list_failed_id.append(id)
    # if there is any product failed to update
    if list_failed_id:
        create_txt(list_failed_id)
            
        
        

def patch_product(UpdatedProduct):
    url = f'https://erli.pl/svc/shop-api/products/{UpdatedProduct.id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key_erli}"}
    data = {
        "price": UpdatedProduct.price,
        "status": UpdatedProduct.status,
        "stock": UpdatedProduct.stock
    }
    response = requests.patch(url, headers=headers, json=data)
    return response

def create_txt(list_failed_ids, file_name="failed_ids.txt"):
    with open(file_name, "w") as f:
        f.writelines(list_failed_ids)


if __name__ == "__main__":
    main()
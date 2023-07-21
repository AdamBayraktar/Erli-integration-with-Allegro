from convert_txt_to_list import convert_text_file_to_list
import requests
# import your unique api key ERLI
from config import api_key_erli
import json

# code that is responsible for deleting products that are archived in Allegro
def main():
    # convert text file of terminated and actual IDs to the list
    archived_id_list = convert_text_file_to_list("terminated_products.txt")
    # list of IDs that you use to update existing products on ERLI
    actual_ids = convert_text_file_to_list("list_of_product_id.txt")
    # counter of failed to terminated products
    global failed_number_products
    failed_number_products = 0
    for id in archived_id_list:
        archive_product({"archived": True}, id)
    # Update list of existing product IDs, removes terminated IDs from actual ID list
    update_file("list_of_product_id.txt", actual_ids, archived_id_list)


def archive_product(data, id):
    url = f'https://erli.pl/svc/shop-api/products/{id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key_erli}"
        }
    response = requests.patch(url, json=data, headers=headers)
    # write all relavant information, when products fail to be created
    if response.status_code != 202:
        global failed_number_products
        with open(f'failed_to_archive_{failed_number_products}.txt', "w") as f:
            failed_number_products += 1
            f.write(json.dumps(data) + "\n")
            f.write(str(id) + "\n")
            f.write(str(response.status_code) + "\n")
            f.write(json.dumps(response.text) + "\n")

 
def update_file(file_name, old_id_list, terminated_id_list):
    with open(file_name, "w") as f:
        for id in old_id_list:
            if id in terminated_id_list:
                terminated_id_list.remove(id)
            else:
                f.write(id + "\n")
    if terminated_id_list:
        print(f"Something went wrong with this IDs {terminated_id_list}" )
    else:
        print("Successly removed terminated IDs from actual list")
    
if __name__ == "__main__":
    main()
from get_access_token_allegro import get_token
from get_all_allegro_products_main_info import all_products_id
from convert_txt_to_list import convert_text_file_to_list

def main():
    token = get_token()
    all_allegro_id = all_products_id(token)
    erli_products_id = convert_text_file_to_list("list_of_product_id.txt")
    # new products
    new_products = []
    for allegro_id in all_allegro_id:
        if allegro_id not in erli_products_id:
            new_products.append(allegro_id)
    create_txt("new_products.txt", new_products, msg="There isn't any new products")
    # terminated products
    terminated_products = []
    for erli_id in erli_products_id:
        if erli_id not in all_allegro_id:
            terminated_products.append(erli_id)
    create_txt("terminated_products.txt", terminated_products, msg="There isn't any terminated products")
    
    
def create_txt(file_name, id_list, msg="nothing new"):
    with open(file_name, "w") as file:
        if id_list:
            for id in id_list:
                file.write(id + '\n')
        else:
            file.write("Nothing new")
            print(msg)
    
if __name__ == "__main__":
    main()
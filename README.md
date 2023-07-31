# Transfering auctions from Allegro to Erli

***

In this repository you can find all requests that are needed in order to take your offers from ALLEGRO to another e-commerce platform which is ERLI. 

***
You have to define unique ID for each new ERLI product. I suggest using the same ID as ALLEGRO product ID. After creating products in ERLI, the next step is to keep prices and quantities up to date. If you use the same ID as I suggested then with one ID you can get actual information about the product in ALLEGRO and then PATCH it to ERLI with the same ID.

***
You can GET maximum 1000 products per request in Allegro. In my case, my store has about 2200 products. I divided all products into 3 requests by price. 
```
    all_products.extend(get_all_products(access_token, upper_price=10))
    all_products.extend(get_all_products(access_token, lower_price=10.01, upper_price=18))
    all_products.extend(get_all_products(access_token, lower_price=18.01))
```

***
What you need:

- unique erli api key for authorization 
- Allegro CLIENT ID
- Allegro CLIENT SECRET


***
Step by step instruction:

1. Create config.py
2. In the file define variables:
    - api_key_erli
        private API key - you must generate it in integration methods tab
    - client_id_allegro
        client ID - in order to get these 2 allegro keys, you must create application in Allegro API and select type: device
    - client_secret_id_allegro
        client Secret
3. Run check_connection_allegro.py and check_connection_erli.py - if tests passed then you may proceed to next step
4. Open get_all_allegro_products_main_info.py
    - remember that you can get maximum 1000 offers per one request
    - adjust lower and upper prices in all_products_id function that you will get all your products
    - if needed add another get_all_products function inside it
    - for test purpose you can run this file and check output
5. Run get_all_allegro_products_detailed_info.py for test purpose
6. Adding products from Allegro to Erli for THE FIRST TIME
    - open add_all_product_erli.py
    - For test purpose: add any letters before "title" variable in post product function. Example below:
    ```
    def post_product(data, title):
        url = f'https://erli.pl/svc/shop-api/products/anyLetter{title}'
    ```
    - check the output in the console and also examine if offers were correctly added in the erli website
    - if there is any error, examine the error message and then change the unique word/letter before "title" variable
    - if offers were correctly, then archieve all offers from website, remove the unique word/letter before "title" variable, and finally run again add_all_product_erli.py
    - IMPORTANT: make backup file of list_of_product_id.txt - you will use it to update existing offers
7.
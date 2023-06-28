# Transfering auctions from Allegro to Erli

***

In this repository you can find all request that are need in order to take your offers from ALLEGRO to another e-commerce platform which is ERLI. 

***
You have to add unique ID for each new ERLI product. I suggest using the same ID as ALLEGRO product ID. After creating products in ERLI, the next step is to keep prices and quantities up to date. If you use the same ID as I suggested then with one ID you can get actual information about the product in ALLEGRO and then PATCH it to ERLI with the same ID.

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
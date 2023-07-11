import requests
from get_access_token_allegro import get_token

requests.packages.urllib3.disable_warnings()

# get list of products by ID
def main():
    access_token = get_token()
    ID = "PRODUCT ID - you can test it manually here"
    example = get_offer_by_id_allegro(access_token, ID)
    print(example)



def get_offer_by_id_allegro(access_token, id):
    url = "https://api.allegro.pl/sale/offers"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        "offer.id": id,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()["offers"]



if __name__ == "__main__":
    main()
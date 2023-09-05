# creates ready to import Erli product by passing allegro product with detailed information
class NewErliProduct:
    def __init__(self, allegro_product) -> None:
            self.id = allegro_product['id']
            self.name = allegro_product['name']
            self.description = self.__add_description(allegro_product["description"])
            self.ean = self.__set_parameter(allegro_product, "EAN (GTIN)")
            self.sku = self.__set_parameter(allegro_product, "Kod producenta")
            self.externalReferences = [{ "id": self.id, "kind": "allegro" }]
            self.externalCategories = [{"source": "allegro", "breadcrumb": [{"id": allegro_product['category']['id']}]}]
            self.externalAttributes = self.add_allegro_params(allegro_product["productSet"][0]["product"]["parameters"])
            self.images = [{"url": image} for image in allegro_product['images']]
            self.price = self.__get_price_in_grosze(allegro_product["sellingMode"]["price"]["amount"])
            self.stock = int(allegro_product["stock"]["available"])
            self.status = allegro_product['publication']["status"]
            self.data = {
                "name": self.name,
                "description": self.description,
                "ean": self.ean,
                "sku": self.sku,
                "externalReferences": self.externalReferences,
                "externalCategories": self.externalCategories,
                "externalAttributes": self.externalAttributes,
                "images": self.images,
                "price": self.price,
                "stock": self.stock,
                "dispatchTime": {"period": 1},
                "weight": 50, 
                "deliveryPriceList": "SMART",
                "status": "active" if self.status.lower() == "active" else "inactive"
            }
    
    def __set_parameter(self, product, name):
        parameters = product["productSet"][0]["product"]["parameters"]
        for param in parameters:
            if param.get("name") == name:
                return param["values"][0]
            
    
    def add_allegro_params(self, parameters):
        data = []
        for param in parameters:
            if param["name"] in ["EAN (GTIN)"]:
                continue
            data.append({
                "source": "allegro",
                "id": param["id"],
                "name": param["name"],
                "type": "string",
                "values": param["values"],
            })
        data.append({
            "source": "allegro",
            "id": "11323",
            "name": "Stan",
            "type": "string",
            "values": ["Nowy"],
        })
        return data

    def __get_price_in_grosze(self, price_zl: int | float) -> int:
        price_zl = float(price_zl)
        price_gr = int(price_zl * 100)
        return price_gr
            
    def __add_description(self, allegro_description: dict) -> str:
        erli_description = {"sections": allegro_description["sections"]}
        return erli_description
    

    
    
            

    

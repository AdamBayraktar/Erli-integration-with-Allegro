# this is class that creates object from allegro product with updated core information like price, stock and the status
class UpdatedErliProduct:
    def __init__(self, allegro_product) -> None:
            self.id = allegro_product['id']
            self.price = self.__change_to_grosze(allegro_product['sellingMode']['price']['amount'])
            self.stock = int(allegro_product["stock"]["available"])
            self.status = "active" if allegro_product['publication']['status'] == "ACTIVE" else "inactive"
    
    def __change_to_grosze(self, zloty):
        grosze = int(float(zloty) * 100)
        return grosze
    

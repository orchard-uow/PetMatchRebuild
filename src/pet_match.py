from src.pet_store import PetStore


class PetMatch:
    def __init__(self):
        self.petstore = PetStore()
        
        
    def add_pet_breed(self, pet):
        return self.petstore.add_pet_breed(pet)
        
    def search_pet_breed(self, id="", breed=""):
        return self.petstore.search_pet_breed(id=id, breed=breed)
    
    def delete_pet_breed(self, id):
        return self.petstore.delete_pet_breed(id)
        
    def edit_pet_breed(self, id, pet):
        return self.petstore.edit_pet_breed(id, pet)

    def show_all_pet_breeds(self):
        return self.petstore.show_all_pet_breeds()

    def get_pet_breed(self, id=""):
        return self.petstore.get_pet_breed(id=id)
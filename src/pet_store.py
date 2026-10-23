class PetStore:

    def __init__(self):
        self.pet_store = []

    def add_pet_breed(self, petbreed):
        self.pet_store.append(petbreed)

    def search_pet_breed(self, id="", name=""):
        result = []
        for pet in self.pet_store:
            if id:
                if pet.id == id:
                    result.append(pet)
            if name:
                if pet.name == name:
                    result.append(pet)
        return result
    
    def delete_pet_breed(self, id):
        for pet in self.pet_store:
            if pet.id == id:
                self.pet_store.remove(pet)
        

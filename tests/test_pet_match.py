import unittest

from src.pet_breed import PetBreed
from src.pet_match import PetMatch
from src.dog_breed import DogBreed


class PetMatchTests(unittest.TestCase):

    def setUp(self):
        PetBreed.next_pet_id = 1
        self.petmatch = PetMatch()

    def create_test_dog(self):
        return DogBreed(
            "Border Collie",
            "medium",
            "5",
            "21.3 kg",
            "medium",
            "high",
            "loving",
            "12-15 years",
            "running",
        )

    def test_petmatch_has_pet_store(self):
        self.assertIsNotNone(self.petmatch.petstore)
        
    def test_add_pet_breed_via_petmatch(self):
        dog = self.create_test_dog()
        self.petmatch.add_pet_breed(dog)
        self.assertEqual(len(self.petmatch.petstore.pet_store),1)
        result = self.petmatch.search_pet_breed(id = dog.id)
        self.assertEqual(result, [dog])
        
    def test_delete_pet_breed_via_petmatch(self):
        dog = self.create_test_dog()
        self.petmatch.add_pet_breed(dog)
        self.assertEqual(len(self.petmatch.petstore.pet_store),1)
        self.petmatch.delete_pet_breed(dog.id)
        result = self.petmatch.search_pet_breed(id = dog.id)
        self.assertEqual(result, [])
        
    def test_edit_pet_breed_via_petmatch(self):
        dog = self.create_test_dog()
        self.petmatch.add_pet_breed(dog)
        updated_dog = self.create_test_dog()
        updated_dog.id = dog.id
        updated_dog.name = "Gentle Orchard"
        self.petmatch.edit_pet_breed(dog.id, updated_dog)
        result = self.petmatch.search_pet_breed(id=dog.id)
        self.assertEqual(len(result), 1)
        self.assertEqual(self.petmatch.petstore.pet_store[0].name, "Gentle Orchard")
        self.assertIs(result[0], updated_dog)
        
        

import unittest

from src.pet_breed import PetBreed
from src.pet_store import PetStore
from src.dog_breed import DogBreed


class PetStoreTests(unittest.TestCase):

    def setUp(self):
        PetBreed.next_pet_id = 1
        self.store = PetStore()

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
        
    def test_petstore_initially_is_empty(self):
        self.assertEqual(self.store.pet_store, [])
        
    def test_add_pet_breed_to_pet_store(self):
        dog = self.create_test_dog()
        self.store.add_pet_breed(dog)
        self.assertEqual(len(self.store.pet_store), 1)
        self.assertIn(dog, self.store.pet_store)
        
    def test_search_pet_breed_by_id(self):
        dog = self.create_test_dog()
        self.store.add_pet_breed(dog)
        result = self.store.search_pet_breed(id = dog.id)
        self.assertIn(dog, result )
        self.assertListEqual(result, [dog])
        
    def test_search_pet_breed_by_name(self):
        dog = self.create_test_dog()
        self.store.add_pet_breed(dog)
        result = self.store.search_pet_breed(name = dog.name)
        self.assertIn(dog, result)
        self.assertListEqual(result, [dog])
        
    def test_delete_pet_breed(self):
        dog = self.create_test_dog()
        self.store.add_pet_breed(dog)
        self.assertEqual(len(self.store.pet_store), 1)
        self.store.delete_pet_breed(dog.id)
        self.assertEqual(len(self.store.pet_store), 0)
        
    def test_delete_removes_selected_pet_only(self):
        dog = self.create_test_dog()
        dog2 = self.create_test_dog()
        self.store.add_pet_breed(dog)        
        self.store.add_pet_breed(dog2)
        self.store.delete_pet_breed(dog2.id)
        self.assertEqual(len(self.store.pet_store), 1)
        self.assertEqual(self.store.pet_store[0].id, "PET-0001")
                
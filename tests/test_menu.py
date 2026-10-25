import unittest

from src.pet_match import PetMatch
from src.menu import Menu
from src.dog_breed import DogBreed


class MenuTests(unittest.TestCase):

    def setUp(self):
        self.petmatch = PetMatch()
        self.menu = Menu(self.petmatch)
        
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
            "running" 
        )

    def test_menu_uses_petmatch(self):
        '''test the connection between Menu and PetMatch'''
        self.assertIs(self.menu.petmatch, self.petmatch)
        
        
    def test_menu_add_pet_breed_via_petmatch(self):
        dog = self.create_test_dog()
        def get_test_breed():
            return dog
        self.menu.breed_input.get_pet_breed_values = get_test_breed
        self.menu.add_pet_breed()
        self.assertEqual(len(self.petmatch.petstore.pet_store),1)

    def test_menu_search_pet_breed_by_id_via_petmatch(self):
        dog = self.create_test_dog()
        def get_test_breed():
            return dog
        self.menu.breed_input.get_pet_breed_values = get_test_breed
        self.menu.add_pet_breed()
        result = self.menu.search_pet_breed(id=dog.id)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], dog)

    def test_menu_search_pet_breed_by_full_name_via_petmatch(self):
        dog = self.create_test_dog()
        def get_test_breed():
            return dog
        self.menu.breed_input.get_pet_breed_values = get_test_breed
        self.menu.add_pet_breed()
        result = self.menu.search_pet_breed(name="Border Collie")
        self.assertEqual(len(result),1)

    def test_menu_search_pet_breed_by_part_name_via_petmatch(self):
        dog = self.create_test_dog()
        def get_test_breed():
            return dog
        self.menu.breed_input.get_pet_breed_values = get_test_breed
        self.menu.add_pet_breed()
        result = self.menu.search_pet_breed(name="Collie")
        self.assertEqual(len(result),1)
        self.assertIs(result[0], dog)


if __name__ == "__main__":
    unittest.main()
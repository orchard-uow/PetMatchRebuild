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
        
        
    # def test_menu_add_pet_breed_via_petmatch(self):
    #     dog = self.create_test_dog()
    #     self.menu.petmatch.add_pet_breed(dog)
    #     result = self.menu.petmatch.search_pet_breed(id=dog.id)
    #     self.assertEqual(len(result), 1)
    #     self.assertIs(result[0], dog)
        
    def test_menu_add_pet_breed_via_petmatch(self):
        dog = self.create_test_dog()
        def get_test_breed():
            return dog
        self.menu.breed_input.get_pet_breed_values = get_test_breed
        self.menu.add_pet_breed()
        result = self.petmatch.search_pet_breed(id=dog.id)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], dog)
        # print(result[0].name)

if __name__ == "__main__":
    unittest.main()
import unittest
from src.pet_match import PetMatch
from src.get_pets_from_text_file import load_pets_from_text_file


class PetTextToJSONToObjectsTests(unittest.TestCase):
    def setUp(self):
        self.petmatch =PetMatch()
        self.file = "src/Pet.txt"

    def test_load_pet_text_file(self):
        load_pets_from_text_file(self.petmatch, self.file)
        pets = self.petmatch.show_all_pet_breeds()
        self.assertEqual(len(pets),12)
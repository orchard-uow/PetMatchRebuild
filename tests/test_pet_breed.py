# A breed receives a unique, incrementing ID.
# A breed name cannot be blank.
# The breed name is capitalised as required by our design.
# PetBreed cannot be instantiated directly because it is abstract.

import unittest

from src.pet_breed import PetBreed

class TestPetBreed(PetBreed):
    def display_breed_info(self):
        pass

class PetBreedTests(unittest.TestCase):

    def setUp(self):
        PetBreed.next_pet_id = 1

    def create_test_pet(self, name="Border Collie", age="5", weight="21.3 kg"):
        return TestPetBreed(
            "dog", name, "medium", age, weight
        )

    # ID tests
    def test_breed_id_format(self):
        ''' test breed format'''
        pet = self.create_test_pet()
        self.assertRegex(pet.id, r"^PET-\d{4}$")

    def test_pet_id(self):
        ''' test breed id exists'''
        pet = self.create_test_pet()
        self.assertEqual(pet.id, 'PET-0001')

    def test_pet_ids_increment(self):
        ''' test breed id's increment'''
        pet = self.create_test_pet()
        pet2 = self.create_test_pet()
        self.assertEqual(pet.id, 'PET-0001')
        self.assertEqual(pet2.id, 'PET-0002')

    def test_id_is_a_atring(self):
        pet = self.create_test_pet()
        self.assertIsInstance(pet.id, str)


    # Age tests
    def test_valid_age_0(self):
        '''test age lowest valid value'''
        pet = self.create_test_pet(age=0)
        self.assertEqual(pet.age, 0)
    
    def test_valid_age_22(self):
        '''test age highest valid value'''
        pet = self.create_test_pet(age=22)
        self.assertEqual(pet.age, 22)

    def test_valid_age_float(self):
        '''test age valid float value'''
        pet = self.create_test_pet(age=18.3)
        self.assertEqual(pet.age, 18.3)

    def test_invalid_age_through_error(self):
        '''test invalid ages'''
        invalid_ages = ["3.55", "3.", "-1", "xyz"]
        for i_age in invalid_ages:
            with self.subTest(age=i_age):
                with self.assertRaises(ValueError):
                    self.create_test_pet(age=i_age)

    def test_age_above_22_throws_error(self):
        '''test age invalid above 22'''
        with self.assertRaises(ValueError):
            self.create_test_pet(age="24")


    # Weight tests
    def test_valid_weight_float(self):
        '''test weight valid float value'''
        pet = self.create_test_pet(weight="18.3 kg")
        self.assertEqual(pet.weight, 18.3)
        self.assertIsInstance(pet.weight, float)

    def test_invalid_weight_throws_error(self):
        '''test invalid weight raises error'''
        invalid_weights = ["18.30 kg", "18.3kg", "18.3 KG"]
        for i_weight in invalid_weights:
            with self.subTest(weight = i_weight):
                with self.assertRaises(ValueError):
                    self.create_test_pet(weight=i_weight)


    # Test PetBreed is abstract
    def test_pet_breed_is_abstract(self):
        with self.assertRaises(TypeError):
            PetBreed('dog', 'Border Collie', 'medium', '5', '18.3 kg')


if __name__ == "__main__":
    unittest.main()
import unittest

from src.pet_breed import PetBreed
from src.dog_breed import DogBreed

class DogBreedTests(unittest.TestCase):

    def setUp(self):
        PetBreed.next_pet_id = 1

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
        
    def test_dog_is_instance_of_petbreed(self):
        dog = self.create_test_dog()
        self.assertIsInstance(dog, PetBreed)
        
    def test_dog_id(self):
        dog = self.create_test_dog()
        self.assertEqual(dog.id, 'PET-0001')
        
    def test_dog_ids_increment(self):
        dog = self.create_test_dog()
        dog2 = self.create_test_dog()
        self.assertEqual(dog.id, 'PET-0001')
        self.assertEqual(dog2.id, 'PET-0002')
        
    def test_dog_attributes(self):
        dog = self.create_test_dog()
        self.assertEqual(dog.type, 'dog')
        self.assertEqual(dog.name, 'Border Collie')
        self.assertEqual(dog.size, 'medium')
        self.assertEqual(dog.age, 5)
        self.assertEqual(dog.weight, 21.3)
        self.assertEqual(dog.coat, 'medium')
        self.assertEqual(dog.energy, 'high')
        self.assertEqual(dog.temperament, 'loving')
        self.assertEqual(dog.lifespan, '12-15 years')
        self.assertEqual(dog.activities, 'running')
        


if __name__ == "__main__":
    unittest.main()
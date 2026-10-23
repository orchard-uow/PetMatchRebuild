import unittest

from src.pet_breed import PetBreed
from src.cat_breed import CatBreed


class CatBreedTests(unittest.TestCase):

    def setUp(self):
        PetBreed.next_pet_id = 1

    def create_test_cat(self):
        return CatBreed(
            "Persian",
            "medium",
            "3",
            "5.1 kg",
            "medium",
            "high",
            "loving",
            "8-12 years",
            "grey, blue",
        )

    def test_cat_is_instance_of_petbreed(self):
        cat = self.create_test_cat()
        self.assertIsInstance(cat, PetBreed)

    def test_cat_id(self):
        cat = self.create_test_cat()
        self.assertEqual(cat.id, "PET-0001")

    def test_cat_ids_increment(self):
        cat = self.create_test_cat()
        cat2 = self.create_test_cat()
        self.assertEqual(cat.id, "PET-0001")
        self.assertEqual(cat2.id, "PET-0002")

    def test_cat_attributes(self):
        cat = self.create_test_cat()
        self.assertEqual(cat.type, "cat")
        self.assertEqual(cat.name, "Persian")
        self.assertEqual(cat.size, "medium")
        self.assertEqual(cat.age, 3)
        self.assertEqual(cat.weight, 5.1)
        self.assertEqual(cat.coat, "medium")
        self.assertEqual(cat.energy, "high")
        self.assertEqual(cat.temperament, "loving")
        self.assertEqual(cat.lifespan, "8-12 years")
        self.assertEqual(cat.colours, "grey, blue")


if __name__ == "__main__":
    unittest.main()

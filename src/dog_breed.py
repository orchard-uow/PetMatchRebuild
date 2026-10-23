from src.pet_breed import PetBreed


class DogBreed(PetBreed):

    def __init__(
        self,
        name,
        size,
        age,
        weight,
        coat="",
        energy="",
        temperament="",
        lifespan="",
        activities="",
    ):
        super().__init__("dog", name, size, age, weight)
        self.coat = coat
        self.energy = energy
        self.temperament = temperament
        self.lifespan = lifespan
        self.activities = activities

    def display_breed_info(self):
        pass

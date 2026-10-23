from src.pet_breed import PetBreed


class CatBreed(PetBreed):
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
        colours=""
    ):
        super().__init__("cat", name, size, age, weight)
        self.coat = coat
        self.energy = energy
        self.temperament = temperament
        self.lifespan = lifespan
        self.colours = colours

    def display_breed_info(self):
        pass
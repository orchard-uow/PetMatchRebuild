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
        colours="",
        breed="",
        pet_id=None
    ):
        super().__init__(type="cat",name=name, size=size, age=age, weight=weight, coat=coat, energy=energy, temperament=temperament, lifespan=lifespan, colours=colours, breed=breed, pet_id=pet_id)

        

    def display_breed_info(self):
        print(f"ID: {self.id}")
        print(f"Breed: {self.breed}")
        print(f"Name: {self.name}")
        print(f"Colours: {self.colours}")
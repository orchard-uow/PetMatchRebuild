from src.dog_breed import DogBreed

class BorderCollie(DogBreed):

    default_prefs = {
        "type": "dog",
        "size": "medium",
        "coat": "medium"
    }

    def __init__(self):
        super().__init__(
            name="Border Collie",
            size="medium",
            age="4",
            weight="16.1 kg",
            coat="",
            energy="medium",
            temperament="loving",
            lifespan="12-15 years",
            activities="Conformation, Herding, Obedience,",
            colours="black, white",
            breed="BorderCollie",
        )
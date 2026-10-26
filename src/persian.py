from src.cat_breed import CatBreed

class Persian(CatBreed):

    def __init__(self):
        super().__init__(
            name="Persian",
            size="medium",
            age="2",
            weight="4.1 kg",
            coat="long",
            energy="medium",
            temperament="gentle",
            lifespan="12-17 years",
            colours="grey, blue",
            breed="Persian",
        )
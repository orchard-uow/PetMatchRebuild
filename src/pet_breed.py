import re
from abc import ABC, abstractmethod

class PetBreed(ABC):

    next_pet_id = 1

    def __init__(self, type, name, size, age, weight):

        ## validate attributes ##
        # validate name
        if not name.strip():
            raise ValueError('Breed cannot be empty')
        
        # validate age format
        if not re.fullmatch(r"[0-9]+(?:\.[0-9])?", str(age)):
            raise ValueError('Age can be a whole number or have 1 decimal place')

        # convert age to float
        age_value = float(age)
        # test range of age
        if not 0 <= age_value <=22:
            raise ValueError('Age must be between 0 -22')

        # validate weight format
        if not re.fullmatch(r"[0-9]+(?:\.[0-9])? kg", weight):
            raise ValueError("Weight can be a whole number or have 1 decimal place")

        # get weight number
        weight_value = float(weight[:-3]) # remove last 3 chars -> ' kg' or 'lbs'

        # assign unique auto gen ID
        self.id = f"PET-{PetBreed.next_pet_id:04d}"
        PetBreed.next_pet_id += 1

        self.type = type
        self.name = name.strip().title()
        self.size = size
        self.age = age_value
        self.weight = weight_value

    @abstractmethod
    def display_breed_info(self):
        # Display info about pet breed.
        # Use inheritance and ploymorphism for sub classes
        pass

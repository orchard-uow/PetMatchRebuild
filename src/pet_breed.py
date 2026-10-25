import re
from abc import ABC, abstractmethod

class PetBreed(ABC):

    # class variables
    next_pet_id = 1
    valid_types = ['cat', 'dog']
    sizes = ['small', 'medium', 'large']
    coats = ['hairless', 'short', 'medium', 'long']
    
        # constructor

    def __init__(self, type, name, size, age, weight, 
                 coat="", energy="", temperament="",
                   lifespan="", colours="", breed="", pet_id=None):

        ## validate attributes ##
        # validate type
        if type not in PetBreed.valid_types:
            raise ValueError("Type must be cat or dog")
        
        # validate size
        if size not in PetBreed.sizes:
            raise ValueError("Invaild size")
        
        # validate coats
        if coat and coat not in PetBreed.coats:
            raise ValueError("Invaild coat")
        
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
        if pet_id is None:
            self.id = f"PET-{PetBreed.next_pet_id:04d}"
            PetBreed.next_pet_id += 1
        else:
            if not re.fullmatch(r"PET-\d{4}", pet_id):
                raise ValueError("Invalid pet ID")
            self.id = pet_id

        self.type = type
        self.name = name.strip().title()
        self.breed = breed
        self.size = size
        self.age = age_value
        self.weight = weight_value
        self.coat = coat
        self.energy = energy
        self.temperament = temperament
        self.lifespan = lifespan
        self.colours = colours

    @abstractmethod
    def display_breed_info(self):
        # Display info about pet breed.
        # Use inheritance and ploymorphism for sub classes
        pass

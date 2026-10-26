from src.cat_breed import CatBreed
from src.dog_breed import DogBreed

from src.persian import Persian
from src.border_collie import BorderCollie

from src.exceptions import InvalidBreedError, InvalidSizeError, InvalidCoatError

class PetBreedInput:

    def get_pet_breed_values(self):

        cat_attributes = [
            'breed', 'name', 'size', 'age', 'weight', 'coat',
            'energy', 'temperament', 'lifespan', 'colours'
        ]
        
        dog_attributes = [
            'breed', 'name', 'size', 'age', 'weight', 'coat',
            'energy', 'temperament', 'lifespan', 'activities'
        ]

        breed_values = {}
        breed = None
        concrete_breed = False

        while True:
            pet_type = input('Enter pet type (Cat, Dog): ')

            try:
                if pet_type.lower() not in ['cat', 'dog']:
                    raise InvalidBreedError('Please enter Cat or Dog.')

                if pet_type.lower() == 'cat':
                    breed_name = input("Enter breed name (Eg: Persian or press enter): ")
                    if breed_name.lower() == 'persian':
                        breed = Persian
                        concrete_breed = True
                    else:
                        breed = CatBreed
                        attributes = cat_attributes
                else:
                    breed_name = input("Enter breed name (Eg: BorderCollie or press enter): ")
                    if breed_name.lower() == 'bordercollie':
                        breed = BorderCollie
                        concrete_breed = True
                    else:
                        breed = DogBreed
                        attributes = dog_attributes

                # breed_values['type'] = pet_type.capitalize()
                break

            except InvalidBreedError as e:
                print(e)

        # return concrete breeds immediately
        if concrete_breed:
            return breed()

        # Get values to set attributes
        for prop in attributes:

            while True:
                if prop == 'size':
                    value = input(f'Enter {prop}({breed.sizes}): ')
                elif prop == 'coat':
                    value = input(f'Enter {prop}({breed.coats}): ')
                else:
                    # default non validated attribute values
                    # can be left empty
                    value = input(f'Enter {prop}: ')

                try:
                    if prop == 'size':
                        if value.lower() not in breed.sizes:
                            raise InvalidSizeError(
                                f'Size must be one of {breed.sizes}'
                            )

                    if prop == 'age':
                        try:
                            breed_values[prop] = float(value)
                        except ValueError:
                            raise ValueError('Age must be a number')

                    if prop == 'coat':
                        if value.lower() not in breed.coats:
                            raise InvalidCoatError(
                                f'Coat must be one of {breed.coats}'
                            )

                    if prop == 'weight':
                        if value == '':
                            raise ValueError(
                                'A pet must weigh something.'
                            )

                    if prop == 'weight':
                        breed_values[prop] = value + ' kg'
                    elif prop == 'lifespan':
                        breed_values[prop] = value + ' yrs'
                    # elif prop == 'age':
                    #     breed_values[prop] = float(value)
                    else:
                        breed_values[prop] = value
                    break

                except (InvalidSizeError, InvalidCoatError, ValueError) as e:
                    print(e)
                    
        # ** unpack dict & pass each k:v pairs
        try:
            return breed(**breed_values)
            
        except ValueError as e:
            print("Validation error:", e)
            return self.get_pet_breed_values()
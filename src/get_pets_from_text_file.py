import json
from src.cat_breed import CatBreed
from src.dog_breed import DogBreed
from src.pet_breed import PetBreed

def load_pets_from_text_file(petmatch, file):

    data = []

    with open(file, "r") as file:

        for line in file:
            attributes = line.strip().split(',')
            pet = {
                "type": attributes[0],
                "breed": attributes[1],
                "pet_id": attributes[2],
                "name": attributes[3],
                "age": attributes[4],
                "colours": attributes[5],
                "weight": attributes[6]
            }
            data.append(pet)

        # convert to JSON and back to dictionaries
        # serialize data
        json_data = json.dumps(data)
        # deserialise data
        pets_data = json.loads(json_data)

        # create pet objects and save to pet store
        for pet in data:
            weight = pet['weight'] + ' kg'

            if pet['type'] == 'dog':
                pet = DogBreed(
                    name = pet['name'],
                    size =  "medium",
                    age =  pet['age'],
                    weight = weight,
                    colours = pet['colours'],
                    breed = pet['breed'],
                    pet_id = pet['pet_id'] 
                )

            elif pet['type'] == 'cat':
                pet = CatBreed(
                    name = pet['name'],
                    size =  "small",
                    age =  pet['age'],
                    weight = weight,
                    colours = pet['colours'],
                    breed = pet['breed'],
                    pet_id = pet['pet_id'] 
                )

            else:
                raise ValueError("Data error: " + pet.type)

            # add pet through PetMatch facade
            petmatch.add_pet_breed(pet)

        PetBreed.next_pet_id = len(petmatch.show_all_pet_breeds()) + 1

        # print(pets_data)
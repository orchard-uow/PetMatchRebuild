import json

def save_pets_to_json(petmatch, filename):
        pets = petmatch.show_all_pet_breeds()
        pets_data = []

        for pet in pets:
            pet_data = {
                "id": pet.id,
                "type": pet.type,
                "breed": pet.breed,
                "name": pet.name,
                "size": pet.size,
                "age": pet.age,
                "weight": pet.weight,
                "coat=": pet.coat,
                "energy": pet.energy,
                "temperament": pet.temperament,
                "lifespan": pet.lifespan,
                "colours": pet.colours,          
            }

            if pet.type == "dog":
                pet_data["activities"] = pet.activities

            pets_data.append(pet_data)

        with open(filename, "w") as file:
            json.dump(pets_data, file, indent=4)

        print(f"Pet data saved to {filename}")

from src.pet_breed_input import PetBreedInput
from src.save_pets_to_json import save_pets_to_json

class Menu():
    
    '''menu to display and react to user input'''
    
    def __init__(self, petmatch):
        self.petmatch = petmatch
        self.breed_input = PetBreedInput()

    def petmatch_menu(self):
        '''display menu for users to choose'''
        print()
        print("PetMatch Menu")
        print("1. Add Pet Breed")
        print("2. Search Pet Breeds")
        print("3. Show all Pet Breeds")
        print("4. Show a Pet Breed")
        print("5. Edit Pet Breed")
        print("6. Delete Pet Breed")
        print("7. Save all pet breeds to a JSON file")
        print("8. Quit")
        print()

    def petmatch_menu_interface(self):
        '''user interface for menu display.
        user to enter an option number'''
        while True:
            self.petmatch_menu()

            # option exception handling
            try:
                p_m_option = int(input('Enter an option number: '))
                
                if p_m_option < 1 or p_m_option > 8:
                    raise ValueError('Option must be between 1 and 8')
                
            except ValueError as e:
                if str(e) != 'Option must be between 1 and 8':
                    print("Please enter a number.")
                else:
                    print(e)
            else:
                match p_m_option:
                    case 1:
                        print("1. Add Pet Breed")
                        self.add_pet_breed()
                    case 2:
                        print("2. Search Pet Breeds")
                        self.search_pet_breed()
                    case 3:
                        print("3. Show all Pet Breeds")
                        self.show_all_pet_breeds()
                    case 4:
                        print("4. Show a Pet Breed")
                        self.get_pet_breed()
                    case 5:
                        print("5. Edit Pet Breed")
                        self.edit_pet_breed()
                    case 6:
                        print("6. Delete Pet Breed")
                        self.delete_pet_breed()
                    case 7:
                        print("7. Save all Pet Breeds to a JSON file")
                        self.save_pet_breeds()
                    case 8:
                        print("Thanks for visiting PetMatch")
                        # rewrite PetBreed file
                        # self.create_pet_breed_file()
                        break

    def add_pet_breed(self):
        # refactored pet input sequence into PetBreedInput class
        pet = self.breed_input.get_pet_breed_values()

        # append pet to self.petmatch.pet_store
        self.petmatch.add_pet_breed(pet)
        print(f"\n{pet.breed} {pet.type} added to pet store")

    def search_pet_breed(self, id="", breed=""):
        if not id:
            id = input("Enter pet ID or press enter to search by breed: ").strip()
        if not id and not breed:
            breed = input("Enter pet breed or press enter to return to menu: ").strip()
        if id:
            result = self.petmatch.search_pet_breed(id=id)
        elif breed:
            result = self.petmatch.search_pet_breed(breed=breed)
        else:
            return

        if result:
            for pet in result:
                self.display_pet_breed_details(pet)
        else:
            print("Pet breed not found.")

        return result

    def delete_pet_breed(self, id=""):
        if not id:
            id = input("Enter pet ID: ").strip()
        
        if not id:
            print("No pet id entered")

        result = self.petmatch.delete_pet_breed(id)

        if result == True:
            print(f"Pet breed with {id} has been deleted from your pet store")
        else:
            print(f"Pet {id} not found.")

        return result

    def edit_pet_breed(self, id="", updatedPet=None):
        if not id:
            id = input("Enter pet ID: ").strip()

        # search for pet ID
        result = self.petmatch.search_pet_breed(id=id)

        if not result:
            print("Pet breed not found")
            return False

        # display rearch result
        pet = result[0]
        self.display_pet_breed_details(pet)

        # get updated pet data
        updatedPet = self.breed_input.get_pet_breed_values()

        # keep id of pet
        updatedPet.id = pet.id

        # save changes via petmatch
        self.petmatch.edit_pet_breed(id, updatedPet)

        # display changes made
        self.get_pet_breed(updatedPet.id)

    def show_all_pet_breeds(self):
        result = self.petmatch.show_all_pet_breeds()
        for pet in result:
            self.display_pet_breed_details(pet)

    def get_pet_breed(self, id=""):
        if not id:
            id = input("Enter pet ID: ")
        if id:
            result = self.petmatch.get_pet_breed(id=id)
        if result == False:
            print("There were no matches for your search")
            return
        else:
            self.display_pet_breed_details(result)

    def display_pet_breed_details(self, pet):
        print()
        print(f"{'Id: ':<5}{pet.id}")
        print(f"{'Type: ':<5}{pet.type}")
        print(f"{'Breed: ':<5}{pet.breed}")
        print(f"{'Name: ':<5}{pet.name}")
        print(f"{'Size: ':<5}{pet.size}")
        print(f"{'Age: ':<5}{pet.age} yrs")
        print(f"{'Weight: ':<5}{pet.weight} kg")
        print(f"{'Coat: ':<5}{pet.coat}")
        print(f"{'Energy: ':<5}{pet.energy}")
        print(f"{'Temperament: ':<5}{pet.temperament}")
        print(f"{'Lifespan: ':<5}{pet.lifespan}")
        print(f"{'Colours: ':<5}{pet.colours}")
        if pet.type == 'dog':
            print(f"{'Activities: ':<5}{pet.activities}")

    def save_pet_breeds(self):
        save_pets_to_json(self.petmatch, "src/PetBreed.json")
        
            
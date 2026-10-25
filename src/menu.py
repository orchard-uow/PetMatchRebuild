
from src.pet_breed_input import PetBreedInput

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
        print("7. Quit")
        print()

    def petmatch_menu_interface(self):
        '''user interface for menu display.
        user to enter an option number'''
        while True:
            self.petmatch_menu()

            # option exception handling
            try:
                p_m_option = int(input('Enter an option number: '))
                
                if p_m_option < 1 or p_m_option > 7:
                    raise ValueError('Option must be between 1 and 7')
                
            except ValueError as e:
                if str(e) != 'Option must be between 1 and 7':
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
                        self.search_pet_breeds()
                    case 3:
                        print("3. Show all Pet Breeds")
                        # self.show_all_pet_breeds()
                    case 4:
                        print("4. Show a Pet Breed")
                        # self.get_pet_breed()
                    case 5:
                        print("5. Edit Pet Breed")
                        # self.edit_pet_breed()
                    case 6:
                        print("6. Delete Pet Breed")
                        self.delete_pet_breed()
                    case 7:
                        print("Thanks for visiting PetMatch")
                        # rewrite PetBreed file
                        # self.create_pet_breed_file()
                        break

    def add_pet_breed(self):
        # refactored pet input sequence into PetBreedInput class
        pet = self.breed_input.get_pet_breed_values()

        # append pet to self.petmatch.pet_store
        self.petmatch.add_pet_breed(pet)
        # print(f"\n{pet.name} {pet.type} added to pet store")

    def search_pet_breed(self, id="", name=""):
        if id:
            return self.petmatch.search_pet_breed(id=id)

        if name:
            return self.petmatch.search_pet_breed(name=name)

    def delete_pet_breed(self, petId):
        self.petmatch.delete_pet_breed(petId)

    def edit_pet_breed(self, id, updatedPet):
        self.petmatch.edit_pet_breed(id, updatedPet)
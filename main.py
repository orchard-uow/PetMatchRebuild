from src.pet_match import PetMatch
from src.menu import Menu
from src.get_pets_from_text_file import load_pets_from_text_file

if __name__ == "__main__":
    petmatch = PetMatch()

    # load pets from text files
    load_pets_from_text_file(petmatch, "src/Pet.txt")
    load_pets_from_text_file(petmatch, "src/PetBreed.txt")

    # start menu
    menu = Menu(petmatch)
    menu.petmatch_menu_interface()
from src.pet_match import PetMatch
from src.menu import Menu

if __name__ == "__main__":
    petmatch = PetMatch()
    menu = Menu(petmatch)
    menu.petmatch_menu_interface()
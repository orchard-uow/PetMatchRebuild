from src.persian import Persian
from src.border_collie import BorderCollie

def match_pet_breeds():
    breed_classes = [Persian, BorderCollie]
    valid_prefs = ['size', 'coat']

    # select pet type
    while True: 
        pet_type = input("Choose pet type (Dog or Cat): ").strip().lower()

        if pet_type in ['dog', 'cat']:
            break
        print("Please enter Dog or Cat.")

    # select prefs
    prefs = {}

    while len(prefs) < 2:
        pref = input("Choose a preference (size or coat): ").strip().lower()

        if pref not in valid_prefs:
            print("Invalid preference")
            continue

        value = input(f"Enter preferred {pref}: ").strip().lower()

        if not value:
            print("Preference cannot be empty.")

        prefs[pref] = value

    # compare prefs
    matches = []

    for breed in breed_classes:
        defaults = breed.default_prefs

        if defaults['type'] != pet_type:
            continue

        match = True
        for pref in prefs:
            if defaults[pref] != prefs[pref]:
                match = False

        if match:
            matches.append(breed)

    # Prepare the report
    report = [
        "PetMatch Breed Matching Report",
        "==============================",
        f"Pet type: {pet_type.title()}",
        "Selected preferences:"
    ]

    for pref in prefs:
        report.append(
            f"{pref.title()}: {prefs[pref]}"
        )

    if matches:
        report.append("\nMatching breeds:")

        for breed_class in matches:
            defaults = breed_class.default_prefs
            report.append(f"\nBreed: {breed_class.__name__}")

            for attribute in defaults:
                report.append(
                    f"{attribute.title()}: {defaults[attribute]}"
                )

        print("\n".join(report))

    else:
        message = "No breeds matched your selected preferences."
        print(message)
        report.append("\n" + message)

    # Save both successful and unsuccessful searches
    with open("PetMatch_report.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(report) + "\n")

    print("Report saved to PetMatch_report.txt")
import matplotlib.pyplot as plt
import numpy as np

def show_statistics(pets):

    # initial check for any data passed via pets arg
    if len(pets) == 0:
        print("No pet data available")
        return

    # create sub-plots
    # ================
    fig, ax = plt.subplots(1,3, figsize=(10,5))

    # pie chart showing the distribution of dogs and cats
    # ===================================================
    # set zero count totals for dog and cat
    dog_count = 0
    cat_count = 0
    # count pet type totals
    for pet in pets:
        if pet.type.lower() == 'dog':
            dog_count += 1
        elif pet.type.lower() == 'cat':
            cat_count += 1

    # build chart
    pet_counts = [dog_count, cat_count]
    pc_labels = ["Dog", "Cat"]
    ax[0].pie(pet_counts, labels = pc_labels, autopct="%1.0f%%")
    ax[0].set_title("Pet Distribution Dogs vs. Cats")
    # ax[0].legend(title="Pet Type Counts", loc="lower left")


    # bar chart showing the number of individual pets by breed
    # ========================================================
    # count breeds and store in dictionary
    breed_counts = {}
    # count breed totals
    for pet in pets:
        breed_name = pet.breed

        if breed_name in breed_counts:
            breed_counts[breed_name] += 1
        else:
            breed_counts[breed_name] = 1

    # build chart
    ax[1].bar(breed_counts.keys(), breed_counts.values())
    ax[1].set_title("Pet Breed Totals")
    ax[1].set_xlabel("Breed")
    ax[1].tick_params(axis="x", labelrotation=80)
    ax[1].set_ylabel("Pet Total")


    # histogram showing the distribution pet weights
    # ==============================================
    # set empty weights list
    weights = []
    # get and store all pet weights
    for pet in pets:
        weights.append(pet.weight)

    # build chart
    ax[2].hist(weights, bins=10, facecolor='g', alpha=0.75)
    ax[2].set_title("Histogram of Pet Weights")
    ax[2].set_xlabel("Weight (kg)")
    ax[2].set_ylabel("Number of Pets")

    # display all three charts
    # spacing
    plt.tight_layout()

    # save as png
    plt.savefig("PetStatistics.png", transparent=False, dpi=80, bbox_inches="tight")

    # dislpay charts
    plt.show()
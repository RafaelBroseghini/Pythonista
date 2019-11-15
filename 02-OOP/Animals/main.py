from animals import Parrot, Penguin, Dog, HouseCat, BobCat

if __name__ == "__main__":
    animal_classes = [Parrot, Penguin, Dog, HouseCat, BobCat]
    colors = ["White", "Black", "Red", "Green", "Blue", "Striped"]
    habitats = ["Land", "Sea", "Air", "Tree", "Campus"]
    random_true_false = [True, False]
    zoo = []
    zoo_size = 10
    for _ in range(zoo_size):
        spec = animal_classes[random.randint(0, 4)]
        age = random.randint(1, 10)
        color = random.choice(colors)
        habitat = random.choice(habitats)
        if spec == Parrot:
            new_animal = Parrot(age, color, random.choice(random_true_false))
        elif spec == Penguin:
            new_animal = Penguin(age, color)
        elif spec == Dog:
            new_animal = Dog(age, color)
        elif spec == HouseCat:
            new_animal = HouseCat(age, color)
        else:
            # BobCat
            try:
                new_animal = BobCat(age, color, habitat)
            except ValueError as value_error:
                print(habitat + " is " + str(value_error))
                continue
        zoo.append(new_animal)
    print("There are {} animals in the zoo".format(len(zoo)))
    for animal in zoo:
        print("{} says {}".format(str(animal), animal.sound()))

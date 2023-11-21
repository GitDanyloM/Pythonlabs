from enum import Enum


class Kind(Enum):
    DOG = 1
    CAT = 2
    BIRD = 3


class Pet:
    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    def is_polite(self):
        if "Hello" in self.greeting:
            return True
        else:
            return False


class Home:
    def __init__(self):
        self.pets = []

    def add(self, pet):
        self.pets.append(pet)

    def are_friends(self, pet):
        friends = []
        for other_pet in self.pets:
            if abs(pet.age - other_pet.age) < 2:
                friends.append(other_pet)
        return friends

    def friends_of_pet(self, others_pet):
        friends_of_pet = self.are_friends(others_pet)
        if friends_of_pet:
            friends_names = [friend.name for friend in friends_of_pet if friend.name != others_pet.name]
            if friends_names:
                return f"Friends of {others_pet.name}: {', '.join(friends_names)}"
            else:
                return f"{others_pet.name} has no friends"
        else:
            return f"{others_pet.name} has no friends"

    def sort_pets_by_age(self):
        self.pets.sort(key=lambda x: x.age)

import random

races_list = [
    {"raza": "Humano" ,
    "HP": 2},
    {"raza": "Elfo",
     "HP": 1},
    {"raza": "Enano",
     "HP": 3}
    ]

profession_list = [
    {"clase": "Picaro" ,
    "HP": 2},
    {"clase": "Mago",
     "HP": 1},
    {"clase": "Guerrero",
     "HP": 3}
    ]


class Character:
    def __init__(self,):
        self.race = "bla"
        self.hp = 0
        self.profession = "bla"

    def stats(self):
        random_race = random.choice(races_list)
        self.race = random_race["raza"]
        self.hp += int(random_race["HP"])

        random_profession = random.choice(profession_list)
        self.profession = random_profession["clase"]
        self.hp += int(random_profession["HP"])


name = Character()
name.stats()

print (name.race)
print (name.profession)
print (name.hp)
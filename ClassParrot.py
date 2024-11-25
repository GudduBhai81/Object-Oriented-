class Parrot:



    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Mithu = Parrot("Mithu", 10)
Carrot = Parrot("Carrot", 15)

print("Mithu is a {}".format(Mithu.species))
print("Carrot is a {}".format(Carrot.species))

print("{} is {} years old".format( Mithu.name, Mithu.age))
print("{} is {} years old".format( Carrot.name, Carrot.age))
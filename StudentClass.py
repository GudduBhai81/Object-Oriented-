class student:
    grade = 7
    def __init__(self,name ,age):
        self.name = name
        self.age = age




ob1 = student("Abdullah", "13")
ob2 = student("Hasnain", "9")
ob3 = student("Lone", "12")
ob4 = student("Umair", "13")
print(ob1.name,ob1.age,ob1.grade)
print(ob2.name,ob2.age,ob2.grade)
print(ob3.name,ob3.age,ob3.grade)
print(ob4.name,ob4.age,ob4.grade)
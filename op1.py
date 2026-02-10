class Dog:

    def __init__(self,name,breed,hasFur,):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur


    def bark (self):
        print("woof!! woof")


    def locomote (self):
         print("walking")

dog1 = Dog("jj","bulldog",True)
print(dog1.name,dog1.breed,dog1.hasFur)

dog2 = Dog("tony",  "German shepherd", True)
print(dog2.name,dog2.breed,dog2.hasFur)


dog3 = Dog("jim","siberian husky",True)
print(dog3.name,dog3.breed,dog3.hasFur)


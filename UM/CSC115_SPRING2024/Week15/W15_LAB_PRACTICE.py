class Car:
    def __init__(self, theBrand, theModel, theYear):
        self.brand = theBrand
        self.model = theModel
        self.year = theYear
        self.speed = 0
        
    def __str__(self):
        return (
            f"********************************************\n"
            f"CAR INFORMATION: \n"
            f"Name: {self.brand}\n"
            f"Model : {self.model}\n"
            f"Year: {self.year}\n"
            f"Speed: {self.speed}\n"
            f"********************************************\n"
        )
    
    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
    
    def getCarSpeed(self):
        return self.speed


# ----------------------------------------------------------
class Pet:
    def __init__(self, theName, theBreed, theAge):
        self.name = theName
        self.breed = theBreed
        self.age = theAge

    def __str__(self):
        return (
            f"********************************************\n"
            f"Pet name = {self.name}, Breed = {self.breed}, Age = {self.age}\n"
            f"********************************************\n"
        )

    def getPetName(self):
        return self.name

    def setPetName(self, newName):
        self.name = newName

    def getPetBreed(self):
        return self.breed

    def setPetBreed(self, newBreed):
        self.breed = newBreed

    def getPetAge(self):
        return self.age

    def setPetAge(self, newAge):
        self.age = newAge


# ----------------------------------------------------------
def main():
    print(f"WEEK 15 LAB - PREACTICE ABOUT CLASSES & OBJECTS")
    
    myCar = Car("Tesla", "Model Y", 2021)

    print(myCar)
    
    print("Accelerating........")
    for _ in range(5):
        myCar.accelerate()
        print(myCar.getCarSpeed())
        
    print(myCar)
    
    print("Braking........")
    for _ in range(5):
        myCar.brake()
        print(myCar.getCarSpeed())
    
    print(myCar)

    # myPet = Pet("Dole", "Chihuahua", 16)
    # print(myPet)

    # myPet.setPetName("Zen")
    # myPet.setPetBreed("Jack Russel")
    # myPet.setPetAge(6)

    # print(myPet)
    
    


if __name__ == "__main__":
    main()

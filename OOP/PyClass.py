class Vaccine:
    def __init__(self, name, made_in, intrvl) -> None:
        self.name = name
        self.made_in = made_in
        self.intrvl = intrvl
        

class Person:
    def __init__(self, pname, age, type = "General Citizen") -> None:
        self.pname = pname
        self.age = age
        self.type = type
        self.vec = ""
        self.firstdose = False
        self.seconddose = False
        
    def pushVaccine(self, veccine, dose = "1st dose"):
        if dose == "1st dose":
            if self.age >= 25 or self.type == "Student":
                self.vec = veccine
                self.firstdose = True
                print("1st dose done for", self.pname,"\n")
                
            else:
                print("Sorry", self.pname,", Minimum age for taking vaccine is 25 years now.\n")
                
        else:
            if self.vec.name != veccine.name:
                print("Sorry", self.pname,", you can't take 2 different vaccines.\n")
                
            else:
                print("2nd dose done for", self.pname,"\n")
                self.seconddose = True
                
                
    def showDetail(self):
        print(f"\nName: {self.pname}\n Age: {self.age}\n  Type: {self.type}")
        if self.firstdose == True and self.seconddose == True:
            print(f"Vaccine name: {self.vec.name}")
            print("1st dose: Given")
            print("2nd dose: Given\n\n")
            
        elif self.firstdose == True:
            print(f"Vaccine name: {self.vec.name}")
            print("1st dose: Given")
            print(f"2nd dose: Please come after {self.vec.intrvl} days.\n\n")
            
        else:
            print("Vaccine name: None")
            if self.age >= 25 or self.type == "Student":
                print("Please take a vaccine imidietly..\n\n")
            else:
                print("Sorry you are not old enough to take vaccine\n\n")
            
            
            
astra = Vaccine("AstraZeneca", "UK", 60)
sin = Vaccine("Sinopharm", "China", 30)
modr = Vaccine("Moderna", "UK", 30)

P1 = Person("Tohubar", 21, "Student")
P2 = Person("Abdullah", 24, "Actor")
P3 = Person("Khairul", 34)

P1.showDetail()
P1.pushVaccine(astra)
P1.showDetail()
P1.pushVaccine(sin, "2nd dose")
P1.pushVaccine(astra, "2nd dose")
P1.showDetail()

P2.pushVaccine(sin)
P2.showDetail()

P3.pushVaccine(modr)
P3.showDetail()
P3.pushVaccine(modr, "2nd dose")
P3.showDetail()
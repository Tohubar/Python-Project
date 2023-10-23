class Student:
    var = "BUET"
    def __init__(self, name, id) -> None:
        self.name = name
        self.__id = id
        
    def show(self):
        print(f"{self.name}'s id is {self.__id}. He/She study in {Student.var}")
        

class Arman(Student):
    def __init__(self, name, id, age) -> None:
        super().__init__(name, id)
        self.age = age
        
    def show(self):
        super().show()
        print(f"Age is : {self.age}")
        
class Munni(Student):
    def __init__(self, name, id, age, fav_color) -> None:
        super().__init__(name, id)
        self.age = age
        self.color = fav_color
        
    
    def show(self):
        super().show()
        print(f"Age: {self.age} and Favourite color: {self.color}")   
        
     
        
arman = Arman("Arman", 345, 20)
arman.show()
munni = Munni("munni", 346, 21, "Yellow")
munni.show()
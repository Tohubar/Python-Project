class Vecotor:
    
    def __init__(self, x, y, z) -> None:
        self.x = x;
        self.y = y
        self.z = z
        
    def showVector(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")
        
    def __add__(self, vec):
        x = self.x + vec.x
        y = self.y + vec.y
        z = self.z + vec.z
        new_vec = Vecotor(x, y, z)
        
        return new_vec
        
    
A = Vecotor(3, 5, 7)
B = Vecotor(-4, 2, 10)

C = A + B
C.showVector()

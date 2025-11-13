class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Make :{self.make}")
        print(f"Model :{self.model}")
        print(f"Num_doors :{self.num_doors}")
    
a = Car("Toyota","Shift",4)
a.display_info()
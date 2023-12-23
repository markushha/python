class Car:
    
   

    def __init__(self, make, model, year, color):
      self.make = make
      self.model = model
      self.year = year
      self.color = color

    def drive(self):
        print(f"{self.make} {self.model} in {self.color} color is driving")
    
    def stop(self):
      print(f"{self.make} {self.model} in {self.color} color has stopped")
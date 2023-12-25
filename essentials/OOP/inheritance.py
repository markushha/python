class Animal:
    alive = True
    
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def jump(self):
        print("Rabbit is jumping")

rabbit = Rabbit()

print(rabbit.alive)
rabbit.jump()
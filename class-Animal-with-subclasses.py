class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f" {self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)

        self.breed = breed

    def bark(self):
        print(f"{self.name} breed of {self.breed} barks")


class Cat(Animal):
    def meow(self):
        print(f"Cat {self.name} says meow")


class Frog(Animal):
    def EatInsects(self):
        print(f"Frog {self.name} eats insects")


dog = Dog("Boby", "Pitbull")
cat = Cat("Tom")
frog = Frog("Crazy")

dog.eat()
dog.bark()
cat.eat()
frog.eat()

cat.meow()
frog.EatInsects()

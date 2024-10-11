# Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Derived class Cat inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Creating objects of the derived classes
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Rex barks.
print(cat.speak())  # Output: Whiskers meows.

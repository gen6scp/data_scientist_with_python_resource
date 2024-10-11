# Defining a class called Dog
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute

    # Method to display the dog's info
    def display_info(self):
        return f"{self.name} is a {self.breed}"

# Creating an object of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.display_info())  # Output: Buddy is a Golden Retriever

# Defining a class called Dog
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute
        
    # Method to display the dog's info
    def display_info(self):
        return f"{self.name} is a {self.breed}"
                                            

# Creating two objects of the Dog class
dog1 = Dog("Max", "Bulldog")
dog2 = Dog("Bella", "Poodle")

print(dog1.display_info())  # Output: Max is a Bulldog
print(dog2.display_info())  # Output: Bella is a Poodle

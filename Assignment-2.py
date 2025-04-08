# Base class representing a generic entity
class Entity:
    def move(self):
        # This method is meant to be overridden by subclasses
        raise NotImplementedError("Subclasses must implement this method")

# Subclass representing an animal
class Animal(Entity):
    def move(self):
        return "walking on the ground 🐾"

# Subclass representing a bird
class Bird(Entity):
    def move(self):
        return "flying in the sky 🕊️"

# Subclass representing a fish
class Fish(Entity):
    def move(self):
        return "swimming in the water 🐟"

# Subclass representing a car
class Car(Entity):
    def move(self):
        return "driving on the road 🚗"

# Subclass representing a plane
class Plane(Entity):
    def move(self):
        return "soaring through the clouds ✈️"

# Subclass representing a boat
class Boat(Entity):
    def move(self):
        return "sailing across the sea 🚢"

# Function to demonstrate how different entities move
def demonstrate_movement(entities):
    for entity in entities:
        print(f"The {entity.__class__.__name__.lower()} is {entity.move()}.")

# Create a list of different entities
entities = [
    Animal(),
    Bird(),
    Fish(),
    Car(),
    Plane(),
    Boat(),
]

# Display how each entity moves
demonstrate_movement(entities)

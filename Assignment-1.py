# Defining a base class for superheroes
class Superhero:
    def __init__(self, name, alias, superpower, strength_level):
        # Initialize the superhero's basic attributes
        self.name = name                  # Their real name
        self.alias = alias                # Their superhero identity
        self.superpower = superpower      # Their unique ability or power
        self.strength_level = strength_level  # Strength level (1-100 scale)

    # Introduce the superhero
    def introduce(self):
        return f"I am {self.alias}! My superpower is {self.superpower}."

    # Show the superhero's strength level
    def show_strength(self):
        return f"My strength level is {self.strength_level}."

# A specialized superhero class for heroes who can fly
class FlyingHero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, flight_speed):
        # Initialize the base class attributes and add flight-specific details
        super().__init__(name, alias, superpower, strength_level)
        self.flight_speed = flight_speed  # How fast they can fly (in km/h)

    # A unique method for flying heroes
    def fly(self):
        return f"{self.alias} soars through the skies at {self.flight_speed} km/h!"

    # Override the show_strength method to include flight speed
    def show_strength(self):
        return f"As a FlyingHero, my strength level is {self.strength_level}, and I can fly at {self.flight_speed} km/h!"

# A specialized superhero class for heroes who excel underwater
class AquaticHero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, swim_speed):
        # Initialize the base class attributes and add swimming-specific details
        super().__init__(name, alias, superpower, strength_level)
        self.swim_speed = swim_speed  # How fast they can swim (in knots)

    # A unique method for aquatic heroes
    def swim(self):
        return f"{self.alias} glides through the water at {self.swim_speed} knots!"

    # Override the introduce method to add a sea-themed flair
    def introduce(self):
        return f"I am {self.alias}, ruler of the seas! My superpower is {self.superpower}."

# Let's create some superhero objects and see them in action
hero1 = Superhero("Clark Kent", "Superman", "Super Strength", 95)
hero2 = FlyingHero("Bruce Wayne", "Batman", "Genius Intellect", 85, 120)
hero3 = AquaticHero("Arthur Curry", "Aquaman", "Marine Telepathy", 80, 40)

# Testing the functionality of each superhero
print(hero1.introduce())
print(hero1.show_strength())

print(hero2.introduce())
print(hero2.fly())
print(hero2.show_strength())

print(hero3.introduce())
print(hero3.swim())
print(hero3.show_strength())

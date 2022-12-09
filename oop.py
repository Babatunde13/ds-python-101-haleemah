import datetime

class Mammal:
    """
    A mammal class

    """
    animalName = ''
    gender = ''
    age = 0
    weight = 0 # weight in kg
    numberOfLegs = 2

    def walk(self):
        print('I am walking')
    
    def __doc__(self):
        print('This is a mammal')
    
class BushAnimal:
    def run(self):
        """
        The way I run is implemented here
        @param self: The object itself
        @param distance: The distance I am running
        @return: void
        @author: Babatunde
        """
        print('I am running')
    
    def walk(self):
        print('I am walking like a bush animal')

class Lion(BushAnimal, Mammal):
    def walk(self):
        super().walk()
        print('like a lion')

lion1 = Lion()
lion1.animalName = 'Simba'
print(lion1.animalName)
print(lion1.numberOfLegs)
lion1.walk()

class Human(Mammal):
    age = 0
    name = ''
    gender = ''
    height = 0 # heighgt in cm
    current_year = datetime.datetime.now().year

    def __init__(self, nameOfChild, genderOfChild) -> None:
        if genderOfChild.lower() not in ['male', 'female']:
            raise Exception('Gender should be male or female')
        self.age = 0
        self.name = nameOfChild
        self.gender = genderOfChild
        self.height = 30

    def __howToGrow(self):
        print('I am a private method')

    def get_current_year():
        return Human.current_year

    def grow(self):
        self.__howToGrow()
        print(Human.name)
        print(self.name)
        self.height += 1
        self.age += 1

    def speak(self, word):
        print(f'{self.name} said {word}')

    def year_orBirth(self):
        return Human.current_year - self.age

    @staticmethod
    def get_year():
        return Human.current_year

haleemah = Human('Haleemah', 'female')
babatunde = Human('Babatunde', 'male')
haleemah.grow()
print(Human.get_year())
print(haleemah.year_orBirth())

haleemah.name = 'Haleemah Daramola'

mammal = Mammal()
print(mammal)

print(isinstance(haleemah, Human))
print(isinstance(haleemah, Mammal))
print()

print(isinstance(mammal, Human))
print(isinstance(mammal, Mammal))

get_year_from_now = lambda year, age, name: (
    datetime.datetime.now().year - year
)

print(get_year_from_now(1990, 20, 'B'))
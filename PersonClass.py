from datetime import datetime
from SessionClass import Session
from BACClass import BAC
import enum

class Person:

    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.session = Session()

    def get_combined_gram(self):
        for b in self.session.beverages:
            alc_gram += b.gram_of_alcohol
        return alc_gram

    def get_combined_oz(self):
        for b in self.session.beverages:
            alc_oz += b.oz_of_alc
        return alc_oz

    def get_simple_BAC(self):
        return BAC.simple_BAC_calc(self)

    def get_advanced_BAC(self):
        return BAC.advanced_BAC_calc(self)

class Gender(enum.Enum):
    male = 1
    female = 2
    other = 3

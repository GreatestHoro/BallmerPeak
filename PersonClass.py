from datetime import datetime
from SessionClass import Session
import enum

class Person:
    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.session = Session()

class Gender(enum.Enum):
    male = 1
    female = 2
    other = 3

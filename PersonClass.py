from datetime import datetime
from SessionClass import Session

class Person:
    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.session = Session
    def get_name(self):
        return self.name

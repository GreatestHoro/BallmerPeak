from datetime import datetime
from SessionClass import Session

class Person():
    def __init__(self, _name, _gender, _age, _weight, _height):
        self.name = _name
        self.gender = _gender
        self.age = _age
        self.weight = _weight
        self.height = _height
        self.session = Session
    def get_name(self):
        return self.name

from PersonClass import Person
from BACClass import BAC

print("yeet")
name = "John Doe"
age = 42
weight = 100
height = 180
gender = "male"

p = Person(name, gender, age, weight, height)
print(BAC.calc_body_water(p))
print(p.name)

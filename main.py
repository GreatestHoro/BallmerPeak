import PersonClass as ps
from BACClass import BAC
from BeverageClass import Beverage

bac = BAC()
name = "John Doe"
age = 42
weight = 100
height = 180
gender = ps.Gender.male

b = Beverage(33, 4.5)
p = ps.Person(name, gender.name, age, weight, height)

print(bac.calc_body_water(p), "Calc body water")
print(bac.female_body_blood(p), "Female body blood")
print(p.name, "is a", p.gender)

print(b.gram_of_alcohol, "gram of alcohol in a beverage consisting of", b.amount, "ml and ", b.percent_alcohol, "percent alcohol")
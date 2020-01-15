import PersonClass as ps
from BACClass import BAC
import time
from BeverageClass import Beverage
from GraphDisplayer import GraphDisplayer as GDisplay

dict = {1:"one",2:"two",3:"three"} #dictionary
print(dict.get(1))

bac = BAC()
name = "John Doe"
age = 42
weight = 100
height = 180
gender = ps.Gender.male

#b = Beverage()
p = ps.Person(name, gender.name, age, weight, height)

print(bac.calc_body_water(p), "Calc body water")
print(bac.female_body_blood(p), "Female body blood")
print(p.name, "is a", p.gender)

#b = Beverage(33, 4.5)
print(len(p.session.beverages))
#p.session.add_beverage(b)
print(len(p.session.beverages))
time.sleep(1)
print(p.session.duration_sec)

GDisplay(p)
#print(b.gram_of_alcohol, "gram of alcohol in a beverage consisting of", b.amount, "ml and ", b.percent_alcohol, "percent alcohol")

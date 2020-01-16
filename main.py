import PersonAttributes.PersonClass as ps
from STML. BACClass import BAC
import time
from PersonAttributes.BeverageClass import Beverage
from Graph.GraphDisplayer import GraphDisplayer as GDisplay
from datetime import datetime

dict = {1:"one",2:"two",3:"three"} #dictionary
print(dict.get(1))

bac = BAC()
name = "John Doe"
age = 42
weight = 100
height = 180
gender = ps.Gender.male

b = Beverage(330, 100, "beer", "IPA", "Tuborg")
p = ps.Person(name, gender.name, age, weight, height)

p.start_session()
p.session[-1].add_beverage(b)
p.update_bac_values(-1)
print(p.get_combined_gram(0), "Combined gram alc")
print(p.current_bac, "BAC")

p.session[-1].register_piss()
time.sleep(1)
p.session[-1].register_piss()
time.sleep(2)
p.session[-1].register_piss()
time.sleep(3)
p.session[-1].register_piss()

p.session[-1].set_avg_piss()
print(str(p.session[-1].avg_piss) , "minutes AVG time between pisses")




#print(bac.calc_body_water(p), "Calc body water")
#print(bac.female_body_blood(p), "Female body blood")
#print(p.name, "is a", p.gender)

#print(len(p.session.beverages))
#p.session.add_beverage(b)
#print(len(p.session.beverages))
#time.sleep(10)
#print(p.session.duration_sec)

#GDisplay(p)
#print(b.gram_of_alcohol, "gram of alcohol in a beverage consisting of", b.amount, "ml and ", b.percent_alcohol, "percent alcohol")

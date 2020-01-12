import PersonClass

class BAC:
    def __init__(self):
        print("yeet")
    def male_body_water(cls, person):
        return 2.447 + 0.3362 * person.weight + 10.74 * person.height - 0.09516 * person.age

    def female_body_water(cls, person):
        return 2.097 + 0.2466 * person.weight + 10.69 * person.height

    def male_body_blood(cls, person):
        return (0.3669*person.height**3) + (0.03219 * person.weight) + 0.6041

    def female_body_blood(cls, person):
        return (0.3561 * person.height**3) + (0.03308 * person.weight) +0.1833
    
    def calc_body_water(cls, person):
        if person.gender == "male":
            return cls.male_body_water(person)
        elif person.gender == "female":
            return cls.female_body_water(person)
        else:
            raise ValueError("invalid gender you dumb queer fuck, go die pls")
    
    def calc_body_blood(person):
        if person.gender == "male":
            return cls.male_body_blood(person)
        elif person.gender == "female":
            return cls.female_body_blood(person)
        else:
            raise ValueError("invalid gender you dumb queer fuck, go die pls")
    
    def blood_to_water(cls,person):
        return cls.calc_body_blood(person)/0.92

    def simple_BAC_calc(cls,person):
        return (person.session.beverages[-1].alc_qunc*5.14/person.weight* 0.73 if person.gender == male else 0.6)-0.15*person.session.duration
    
    def advanced_BAC_calc(cls,person):
        return ((person.session.Consumed*cls.blood_to_water(person))/cls.calc_body_water(person))*person.session.beverages[-1].unit
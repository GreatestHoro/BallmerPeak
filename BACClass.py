import PersonClass as ps

class BAC:

    @staticmethod
    def male_body_water(person):
        return 2.447 + 0.3362 * person.weight + 10.74 * person.height - 0.09516 * person.age

    @staticmethod
    def female_body_water(person):
        return 2.097 + 0.2466 * person.weight + 10.69 * person.height

    @staticmethod
    def male_body_blood(person):
        return (0.3669*person.height**3) + (0.03219 * person.weight) + 0.6041

    @staticmethod
    def female_body_blood(person):
        return (0.3561 * person.height**3) + (0.03308 * person.weight) +0.1833

    @staticmethod
    def calc_body_water(person):
        if person.gender == ps.Gender.male.name:
            return BAC.male_body_water(person)
        elif person.gender == ps.Gender.female.name:
            return BAC.female_body_water(person)
        else:
            raise ValueError("invalid gender you dumb queer fuck, go die pls")
    
    @staticmethod
    def calc_body_blood(person):
        if person.gender == ps.Gender.male.name:
            return BAC.male_body_blood(person)
        elif person.gender == ps.Gender.female.name:
            return BAC.female_body_blood(person)
        else:
            raise ValueError("invalid gender you dumb queer fuck, go die pls")
    
    @staticmethod
    def blood_to_water(person):
        return BAC.calc_body_blood(person)/0.92

    @staticmethod
    def simple_BAC_calc(person):
        return (person.get_combined_oz*5.14/person.weight* 0.73 if person.gender == ps.Gender.male.name else 0.6)-0.15*person.session.duration
    
    @staticmethod
    def advanced_BAC_calc(person):
        return ((person.session.Consumed*BAC.blood_to_water(person))/BAC.calc_body_water(person))*person.session.beverages[-1].unit
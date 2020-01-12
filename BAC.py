import person

class BAC:

    @staticmethod
    def male_body_water(person):
        return 2.447 + 0.3362 * person.weight + 10.74 * person.height - 0.09516 * person.age

    @staticmethod
    def female_body_water(person):
        return 2.097 + 0.2466 * person.weight + 10.69 * person.height
    
    @staticmethod
    def calc_body_water(person):
        if person.gender == "male":
            return male_body_water(person)
        elif person.gender == "female":
            return female_body_water(person)
        else:
            raise ValueError("invalid gender you dumb queer fuck, go die pls")
from CalcAlcoholClass import CalcAlcohol

class Beverage():
    def __init__(self, _amount, _percent_alcohol):
        self.amount = _amount
        self.percent_alcohol = _percent_alcohol
        self.gram_of_alcohol = CalcAlcohol.get_gram_of_alcohol(self.amount, self.percent_alcohol)
        self.oz_of_alc = CalcAlcohol.get_oz_of_alcohol(self.amount, self.percent_alcohol)

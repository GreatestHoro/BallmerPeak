from CalcAlcoholClass import CalcAlcohol

class Beverage():
    def __init__(self, amount, percent_alcohol, category, style, brand):
        self.brand = brand
        self.style = style
        self.category = category
        self.amount = amount
        self.percent_alcohol = percent_alcohol
        self.gram_of_alcohol = CalcAlcohol.get_gram_of_alcohol(self.amount, self.percent_alcohol)
        self.oz_of_alc = CalcAlcohol.get_oz_of_alcohol(self.gram_of_alcohol)
        self.miligram_alc_pr_hundred_ml = CalcAlcohol.miligram_alc_pr_hundred_ml(self.gram_of_alcohol)

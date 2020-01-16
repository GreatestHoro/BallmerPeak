
class CalcAlcohol:
    """
    Is used by the beverage class.
    Calculates the amount of alcohol in a beverage in different in different units.
    """

    @staticmethod
    def gram_to_oz(gram):
        """Converts grams go ounces"""
        return gram * 0.035274
        
    @staticmethod
    def gram_to_miligram(gram):
        """Converts gram to miligram"""
        return gram / 1000

    @staticmethod
    def ml_to_oz(ml):
        """Converts milliliter to ounces"""
        return ml * 0.033814

    @staticmethod
    def get_gram_of_alcohol(amount, percent_alcohol):
        """Finds how many gram of alcohol there is in beverage based on amount in cl and percent alcohol"""
        return CalcAlcohol.ml_to_oz(amount) * 29.5735 * (percent_alcohol / 100) * 0.789

    @staticmethod
    def get_oz_of_alcohol(gram_of_alc):
        """Calculates ounces of alcohol based on a beverage based on amount in cl and percent of alcohol"""
        return CalcAlcohol.gram_to_oz(gram_of_alc)
        
    @staticmethod
    def miligram_alc_pr_hundred_ml(gram_of_alc):
        """Calculates miligram of alcohol pr hundred milliliter in a beverage based on amount in cl and percent of alcohol"""
        return CalcAlcohol.gram_to_miligram(gram_of_alc)

class CalcAlcohol:
    @staticmethod
    def gram_to_oz(gram):
        return gram * 0.035274
        
    @staticmethod
    def gram_to_miligram(gram):
        return gram / 1000

    @staticmethod
    def ml_to_oz(amount):
        return amount * 0.033814

    @staticmethod
    def get_gram_of_alcohol(amount, percent_alcohol):
        return CalcAlcohol.ml_to_oz(amount) * 29.5735 * (percent_alcohol / 100) * 0.789

    @staticmethod
    def get_oz_of_alcohol(amount, percent_alcohol):
        result = CalcAlcohol.get_gram_of_alcohol(amount, percent_alcohol)
        return CalcAlcohol.gram_to_oz(result)
        
    @staticmethod
    def miligram_alc_pr_hundred_ml(amount, percent_alcohol):
        result = CalcAlcohol.get_gram_of_alcohol(amount, percent_alcohol)
        return CalcAlcohol.gram_to_miligram(result)
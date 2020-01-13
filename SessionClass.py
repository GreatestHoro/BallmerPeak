from datetime import datetime
from BeverageClass import Beverage

class Session():
    beverages = []
    beverage_time = {}
    duration = 0

    def __init__(self):
        self.start = datetime.now()
    
    def add_beverage(cls,beverage):
        cls.beverages.append(beverage)
        cls.beverage_time[beverage] = datetime.now()
        cls.End = datetime.now()

    @property
    def duration(cls):
        dif = datetime.now() - cls.start
        return round(((dif.total_seconds()/60)/60),5) 

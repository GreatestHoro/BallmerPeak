from datetime import datetime
from PersonAttributes.BeverageClass import Beverage

class Session():
    beverages = []
    beverage_time = {}
    duration_hour = 0
    duration_minut = 0
    duration_sec = 0
    time_since_last_drink = 0


    def __init__(self):
        self.start = datetime.now()

    def add_beverage(cls,beverage):
        cls.beverages.append(beverage)
        cls.beverage_time[beverage] = datetime.now()
        cls.End = datetime.now()
    
    @property
    def time_since_last_drink(cls):
       dif = datetime.now() - cls.beverage_time[cls.beverages[-1]]
       return dif.total_seconds()/60/60


    @property
    def duration_hour(cls):
        return round((cls.duration_minut/60),5)

    @property
    def duration_minut(cls):
        return int(round(cls.duration_sec/60,0))
        
    @property
    def duration_sec(cls):
        dif = datetime.now() - cls.start
        return int(round(dif.total_seconds(),0))
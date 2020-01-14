from datetime import datetime
from BeverageClass import Beverage

class Session():
    beverages = []
    beverage_time = {}
    duration_hour = 0
    duration_minut = 0
    duration_sec = 0


    def __init__(self):
        self.start = datetime.now()

    def add_beverage(cls,beverage):
        cls.beverages.append(beverage)
        cls.beverage_time[beverage] = datetime.now()
        cls.End = datetime.now()
    

    @property
    def duration_hour(cls):
        dif = datetime.now() - cls.start
        return round((cls.duration_minut/60),5)

    @property
    def duration_minut(cls):
        dif = datetime.now() - cls.start
        return int(round(cls.duration_sec/60,0))
        
    @property
    def duration_sec(cls):
        dif = datetime.now() - cls.start
        return int(round(dif.total_seconds(),0))
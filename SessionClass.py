from datetime import datetime
from BeverageClass import Beverage

class Session():
    beverages = []
    beverage_time = {}

    def __init__(self):
        self.start = datetime.now()
    
    def add_beverage(self, beverage):
        self.beverages.append(beverage)

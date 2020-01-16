from datetime import datetime
from SessionClass import Session
from BACClass import BAC
import enum

class Person:
    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.session = []
        self.prev_bac = 0
        self.current_bac = 0

    def start_session(self):
        self.session.append(Session())

    def get_combined_gram(self, ses_num):
        """Goes through a all beverages in a given sesstion, and returns the combined gram of alcohol comsumed"""
        alc_gram = 0
        for b in self.session[ses_num].beverages:
            alc_gram += b.gram_of_alcohol
        return alc_gram

    def get_combined_oz(self, ses_num):
        """Goes through a all beverages in a given sesstion, and returns the combined oz of alcohol comsumed"""
        alc_oz = 0
        for b in self.session[ses_num].beverages:
            alc_oz += b.oz_of_alc
        return alc_oz

    def get_simple_BAC(self, ses_num):
        return BAC.simple_BAC_calc(self, ses_num)

    def get_advanced_BAC(self):
        return BAC.advanced_BAC_calc(self)

    def __set_bac(self, ses_num):
        """Updates the BAC value. Do not use this method, use update_bac_values instead"""
        new_val = self.get_simple_BAC(ses_num)
        if new_val < 0:
            return 0
        return new_val

    def __set_pre_bac(self, new_val):
        """Updates the prev_BAC value. Do not use this method, use update_bac_values instead"""
        if new_val < 0:
            return 0
        return new_val

    def update_bac_values(self, ses_num):
        """Updates both BAC valuese"""
        self.prev_bac = self.__set_pre_bac(self.current_bac)
        self.current_bac = self.__set_bac(ses_num)

class Gender(enum.Enum):
    male = 1
    female = 2
    other = 3

import plotly.graph_objects as go
import PersonAttributes.PersonClass as ps
from matplotlib import pyplot as plt
import numpy as np
import math  # needed for definition of pi

class GraphDisplayer:
    Ballmer_x = []
    Ballmer_y = []
    def __init__(self, person : ps.Person) -> ps.Person:
        self.person = person
        self.ballmer_peak_plot_generator()

        x = np.arange(0, math.pi * 2, 0.05)
        y = np.tan(x)
        plt.plot(x, y)
        plt.xlabel("Blood Alcohol Cocentration(BAC)")
        plt.ylabel("Alcohol powers level")
        plt.title("Ballmerpeak")
        plt.savefig(r"C:\Users\jeppe\OneDrive\Skrivebord\DEB eksam\yeet.png")
        #plt.show()

    def balmer_func(cls,x):
        return (4**(-x**2/(0.1)**29 + 9**(-(x-0.13)**2/(0.00001))))

    def ballmer_peak_plot_generator(cls):
        for x in range(100):
            cls.Ballmer_x.append(x)
            cls.Ballmer_y.append(cls.balmer_func(x))



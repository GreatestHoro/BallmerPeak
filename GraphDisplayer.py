import plotly.graph_objects as go
import PersonClass as ps
from matplotlib import pyplot as plt
import numpy as np
import math  # needed for definition of pi

class GraphDisplayer:
    Ballmer_x = []
    Ballmer_y = []
    def __init__(self, person : ps.Person) -> ps.Person:
        self.person = person
        self.ballmer_peak_plot_generator()
        """fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=self.Ballmer_x,
                y=self.Ballmer_y
            ))

        fig.add_trace(
            go.scatter(
                x=[0, 1, 2, 3, 4, 5],
                y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
            ))
        fig.show()"""

        x = np.arange(0, math.pi * 2, 0.05)
        y = np.tan(x)
        plt.plot(x, y)
        plt.xlabel("angle")
        plt.ylabel("Tan value")
        plt.title('Tan wave')
        plt.savefig(r"C:\Users\jeppe\OneDrive\Skrivebord\DEB eksam\yeet.png")
        #plt.show()

    def ballmer_peak_plot_generator(cls):
        for x in range(100):
            cls.Ballmer_x.append(x)
            cls.Ballmer_y.append(cls.balmer_func(x))

    def balmer_func(cls,x:int) -> int:
        pass

    #def calc
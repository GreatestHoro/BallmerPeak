import plotly.express as px
import PersonClass as ps

class GraphDisplayer:
    def __init__(self,person):
        self.person = person
        fig = px.scatter(x = self.generate_x_axis(), y=[0, 1, 4, 9, 16])
        fig.show()
    
    def generate_x_axis(cls):
        killMe = [*range(0,cls.person.session.duration_sec,1)]
        return killMe[:5]
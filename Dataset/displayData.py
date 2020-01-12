import pandas as p

Dataset = "open_units.csv"

d=p.read_csv("../BallmerPeak/Dataset/Data/" + Dataset, index_col="Product")
print(d)
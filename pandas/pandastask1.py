import pandas as pd

data = pd.read_csv("./ipl.csv")
data["runs"] = [100,120,45,70,76,115,45,100]
data["matches"] = [1000,900,100,70,70,1000,50,1000]

#print(data)

filter1 = data["Team"] =="mi"
filter2 = data["type"] == "batsman"
filter3 = data["runs"] >50

data.where(filter1 & filter2 & filter3 , inplace=True)
print(data)
# with open("weather_data.csv", "r") as file:
#      data = file.readlines()
#      print(data)

# csv

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = [int(row[1]) for row in data if row[1]!='temp']

#     print(temp)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"].mean())
print(data["temp"].max())

print(data[data["day"]=="Monday"])

print(data[data.temp == data.temp.max()])
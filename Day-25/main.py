import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

def counter(lst):
    """
    :param lst: A list of colors
    :return: A dictionary of Fur Color and Count
    """

    counts = []
    for color in lst:
        counts.append(len(data[data["Primary Fur Color"]==color]))

    dict_data = {"Fur Color": lst,
                 "Count": counts,
                }
    return dict_data


colors = ["Cinnamon", "Black", "Gray",]

data_dict = counter(colors)

csv = pd.DataFrame(data_dict).to_csv()
print(csv)



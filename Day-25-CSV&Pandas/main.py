# csv : comma separated values

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         # print(row)
#         # print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# pandas is a python data analysis library

"""
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
print(data["temp"])
print(type(data["temp"]))

# table : dataframe
# column : series

data_dist = data.to_dict()
print(data_dist)

data_list = data["temp"].to_list()
print(data_list)
print(len(data_list))

average = sum(data_list) / len(data_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)

# print data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32

print(monday_temp_F)

# create a dataframe from scratch

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 65, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
"""

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

print(df)
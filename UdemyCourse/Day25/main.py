import csv
import pandas as pd
# with open(r"UdemyCourse\Day25\weather_data.csv",mode='r') as file:
#     data = csv.reader(file,)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

data = pd.read_csv(r"UdemyCourse\Day25\weather_data.csv")
# data_dict = data.to_dict
# temp = list(data['temp'])
# print(temp)
# average = sum(temp)/len(temp)
# print(average)
print(data.day[data.temp == data['temp'].max()])
# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)

# import csv
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if not row[1] == 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(f"max temp is : {data['temp'].max()}")
# print(data.temp)

# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# for items in monday.temp:
#     print(items)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
red_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
black_squirrels = data[data['Primary Fur Color'] == 'Black']
print(len(gray_squirrels))
print(len(red_squirrels))
print(len(black_squirrels))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(red_squirrels), len(black_squirrels)],
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')

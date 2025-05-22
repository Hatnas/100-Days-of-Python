
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")



# Mi solucion
# GRAY = 0
# BLACK= 0
# CINNAMON = 0
#
#squirrel_color = data["Primary Fur Color"]
#
# for color in squirrel_color:
#     if color == "Gray":
#         GRAY += 1
#     elif color == "Cinnamon":
#         CINNAMON += 1
#     elif color == "Black":
#         BLACK += 1
#
# sq_colors = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [GRAY, CINNAMON, BLACK],
# }
#
# sq_frame = pandas.DataFrame(sq_colors)
# sq_frame.to_csv("squirrel_count.cvs")
#

gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

sq_colors = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq_count, cinnamon_sq_count, black_sq_count],
}

sq_frame = pandas.DataFrame(sq_colors)
sq_frame.to_csv("squirrel_count.cvs")


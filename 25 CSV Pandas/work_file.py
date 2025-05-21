
import pandas

data = pandas.read_csv("weather_data.csv")

dataframe_dict = {
    "students": ["Amy", "James", "Angelo"],
    "score": [76, 56, 65]
}

data_frame = pandas.DataFrame(dataframe_dict)
print (data_frame)
data_frame.to_csv("new_data.csv")
